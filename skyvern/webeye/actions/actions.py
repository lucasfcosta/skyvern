import abc
from enum import StrEnum
from typing import Any, Dict, List

import structlog
from pydantic import BaseModel

from skyvern.forge.sdk.schemas.tasks import Task

LOG = structlog.get_logger()


class ActionType(StrEnum):
    CLICK = "click"
    INPUT_TEXT = "input_text"
    UPLOAD_FILE = "upload_file"
    SELECT_OPTION = "select_option"
    CHECKBOX = "checkbox"
    WAIT = "wait"
    NULL_ACTION = "null_action"
    SOLVE_CAPTCHA = "solve_captcha"
    TERMINATE = "terminate"
    COMPLETE = "complete"
    # Note: Remember to update ActionTypeUnion with new actions


class Action(BaseModel):
    action_type: ActionType
    description: str | None = None
    reasoning: str | None = None


class WebAction(Action, abc.ABC):
    element_id: int


class ClickAction(WebAction):
    action_type: ActionType = ActionType.CLICK
    file_url: str | None = None

    def __repr__(self) -> str:
        return f"ClickAction(element_id={self.element_id}, file_url={self.file_url})"


class InputTextAction(WebAction):
    action_type: ActionType = ActionType.INPUT_TEXT
    text: str

    def __repr__(self) -> str:
        return f"InputTextAction(element_id={self.element_id}, text={self.text})"


class UploadFileAction(WebAction):
    action_type: ActionType = ActionType.UPLOAD_FILE
    file_url: str
    is_upload_file_tag: bool = True

    def __repr__(self) -> str:
        return f"UploadFileAction(element_id={self.element_id}, file={self.file_url}, is_upload_file_tag={self.is_upload_file_tag})"


class NullAction(Action):
    action_type: ActionType = ActionType.NULL_ACTION


class SolveCaptchaAction(Action):
    action_type: ActionType = ActionType.SOLVE_CAPTCHA


class SelectOption(BaseModel):
    label: str | None
    value: str | None
    index: int | None

    def __repr__(self) -> str:
        return f"SelectOption(label={self.label}, value={self.value}, index={self.index})"


class SelectOptionAction(WebAction):
    action_type: ActionType = ActionType.SELECT_OPTION
    option: SelectOption

    def __repr__(self) -> str:
        return f"SelectOptionAction(element_id={self.element_id}, option={self.option})"


###
# This action causes more harm than it does good.
# It frequently mis-behaves, or gets stuck in click loops.
# Treating checkbox actions as click actions seem to perform way more reliably
# Developers who tried this and failed: 2 (Suchintan and Shu 😂)
###
class CheckboxAction(WebAction):
    action_type: ActionType = ActionType.CHECKBOX
    is_checked: bool

    def __repr__(self) -> str:
        return f"CheckboxAction(element_id={self.element_id}, is_checked={self.is_checked})"


class WaitAction(Action):
    action_type: ActionType = ActionType.WAIT


class TerminateAction(Action):
    action_type: ActionType = ActionType.TERMINATE


class CompleteAction(Action):
    action_type: ActionType = ActionType.COMPLETE
    data_extraction_goal: str | None = None


def parse_actions(task: Task, json_response: List[Dict[str, Any]]) -> List[Action]:
    actions = []
    for action in json_response:
        element_id = action["id"]
        reasoning = action["reasoning"] if "reasoning" in action else None
        if "action_type" not in action or action["action_type"] is None:
            actions.append(NullAction(reasoning=reasoning))
            continue
        # `.upper()` handles the case where the LLM returns a lowercase action type (e.g. "click" instead of "CLICK")
        action_type = ActionType[action["action_type"].upper()]
        if action_type == ActionType.TERMINATE:
            LOG.warning(
                "Agent decided to terminate",
                task_id=task.task_id,
                llm_response=json_response,
                reasoning=reasoning,
                actions=actions,
            )
            actions.append(TerminateAction(reasoning=reasoning))
        elif action_type == ActionType.CLICK:
            file_url = action["file_url"] if "file_url" in action else None
            actions.append(ClickAction(element_id=element_id, reasoning=reasoning, file_url=file_url))
        elif action_type == ActionType.INPUT_TEXT:
            actions.append(InputTextAction(element_id=element_id, text=action["text"], reasoning=reasoning))
        elif action_type == ActionType.UPLOAD_FILE:
            # TODO: see if the element is a file input element. if it's not, convert this action into a click action

            actions.append(UploadFileAction(element_id=element_id, file_url=action["file_url"], reasoning=reasoning))
        elif action_type == ActionType.SELECT_OPTION:
            actions.append(
                SelectOptionAction(
                    element_id=element_id,
                    option=SelectOption(
                        label=action["option"]["label"],
                        value=action["option"]["value"],
                        index=action["option"]["index"],
                    ),
                    reasoning=reasoning,
                )
            )
        elif action_type == ActionType.CHECKBOX:
            actions.append(CheckboxAction(element_id=element_id, is_checked=action["is_checked"], reasoning=reasoning))
        elif action_type == ActionType.WAIT:
            actions.append(WaitAction(reasoning=reasoning))
        elif action_type == ActionType.COMPLETE:
            if actions:
                LOG.info(
                    "Navigation goal achieved, creating complete action and discarding all other actions except "
                    "complete action",
                    task_id=task.task_id,
                    nav_goal=task.navigation_goal,
                    actions=actions,
                    llm_response=json_response,
                )
            return [CompleteAction(reasoning=reasoning, data_extraction_goal=task.data_extraction_goal)]
        elif action_type == "null":
            actions.append(NullAction(reasoning=reasoning))
        elif action_type == ActionType.SOLVE_CAPTCHA:
            actions.append(SolveCaptchaAction(reasoning=reasoning))
        else:
            LOG.error(
                "Unsupported action type when parsing actions",
                task_id=task.task_id,
                action_type=action_type,
                raw_action=action,
            )
    return actions


class ScrapeResult(BaseModel):
    """
    Scraped response from a webpage, including:
    1. JSON representation of what the user is seeing
    """

    scraped_data: dict[str, Any] | list[dict[str, Any]]


# https://blog.devgenius.io/deserialize-child-classes-with-pydantic-that-gonna-work-784230e1cf83
ActionTypeUnion = (
    ClickAction
    | InputTextAction
    | UploadFileAction
    | SelectOptionAction
    | CheckboxAction
    | WaitAction
    | NullAction
    | SolveCaptchaAction
    | TerminateAction
    | CompleteAction
)
