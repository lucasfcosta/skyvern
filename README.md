<h1 align="center">
 <a href="https://www.skyvern.com">
 <picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/skyvern_logo.png">
  <img height="120" src="images/skyvern_logo.png">
 </picture>
 </a>
 <br />
</h1>
<p align="center">
🐉 Automate browser-based workflows using LLMS and computer vision 🐉
</p>
<p align="center">
  <a href="https://www.skyvern.com/"><img src="https://img.shields.io/badge/Website-blue?logo=googlechrome&logoColor=black"></a>
  <a href="https://docs.skyvern.com/"><img src="https://img.shields.io/badge/Docs-yellow?logo=gitbook&logoColor=black"></a>
  <a href="https://discord.gg/fG2XXEuQX3"><img src="https://img.shields.io/discord/1212486326352617534?logo=discord&label=discord"></a>
  <!-- <a href="https://pepy.tech/project/skyvern" target="_blank"><img src="https://static.pepy.tech/badge/skyvern" alt="Total Downloads"/></a> -->
  <a href="https://github.com/skyvern-ai/skyvern"><img src="https://img.shields.io/github/stars/skyvern-ai/skyvern" /></a>
  <a href="https://www.linkedin.com/company/95726232"><img src="https://img.shields.io/github/license/skyvern-ai/skyvern"></a>
  <a href="https://twitter.com/skyvernai"><img src="https://img.shields.io/twitter/follow/skyvernai?style=social"></a>
  <a href="https://www.linkedin.com/company/95726232"><img src="https://img.shields.io/badge/Follow%20 on%20LinkedIn-8A2BE2?logo=linkedin"></a>
</p>

[Skyvern](https://www.skyvern.com) automates browser-based workflows using LLMs and computer vision. It provides a simple API endpoint to automate workflows and replace unreliable automation solutions. 

<p align="center">
  <img src="images/geico_shu_recording_cropped.gif">
</p>

## Getting started

To use Skyvern, download XYZ, import the library, and call `myFunction` to scrape the website.

```
add code as early as possible
people need something actionable
to copy and paste ASAP
```

Add more details at the bottom of the code so people can get started quickly.


## How it works

Technical people tend to be skeptical when they read "AI", so I'd add a section here to get rid of the "magic".

![add an image to aid your explanation - people perceive READMES with more visual resources as higher quality]()

Do _not_ make your explanation too extensive, and take advantage of good formatting for `code` and other things so it looks **slick**.

![two diagrams here are probably enough - see my notes on slack about how to make good images]()

Three to four paragraphs total in this section. Make sure to export the diagrams both for dark and light mode. Excalidraw has that feature when you're exporting stuff. Then do the same kind of `prefers-color-scheme` attributes you've used in the logo.


## Documentation

Add a brief overview here explaining the high-level constructs and methods. Two to three paragraphs is fine.

Only send people to external links once you've teased them with enough valuable content. That's because they're unlikely to click otherwise.

![if that makes sense or there's some interesting and helpful diagram, add one here]()

Visit our [documentation website](https://docs.skyvern.ai) for more extensive documentation.


## Examples

Either:

1. Link examples in another repo or folder here using a list
2. Add small `h3` sections with descriptions and snippets.

I like both options, but I think the second is slightly better.

Don't worry too much about the length. Higher length is also perceived as higher quality and people probably wouldn't click links anyway.

If you show them it took you effort to write, people will star more.



## Frequently Asked Questions (FAQs)

### What gets us excited about Skyvern?

<<< do not use click to expand, see my note above about length >>>

<details>
<summary> Click to expand </summary>
Our focus is bringing stability to browser-based workflows. We leverage LLMs to create an AI Agent capable of interacting with websites like you or I would — all via a simple API call.

Traditional approaches required writing custom scripts for websites, often relying on DOM parsing and XPath-based interactions which would break whenever the website layouts changed.

Skyvern operates like a human — increasing reliability by not relying on fragile scripts, instead relying on computer vision to parse items in the viewport and interact with them the way a human would.

This approach gives us a few advantages:

1. Skyvern can operate on websites it’s never seen before, as it’s able to map visual elements to actions necessary to complete a workflow, without any customized code
1. Skyvern is resistant to website layout changes, as there are no pre-determined XPaths or other selectors our system is looking for while trying to navigate
1. We’re able to circumvent or navigate through many bot detection methods as many of them rely on allowing people to access the websites
1. We rely on LLMs to reason through interactions to ensure we can cover complex situations. Examples include:
1. If you wanted to get an auto insurance quote from Geico, the answer to a common question “Were you eligible to drive at 18?” could be inferred from the driver receiving their license at age 16
1. If you were doing competitor analysis, it’s understanding that an Arnold Palmer 22 oz can at 7/11 is almost definitely the same product as a 23 oz can at Gopuff (even though the sizes are slightly different, which could be a rounding error!)

</details>


## Roadmap

This is our planned roadmap for the next few months.

- [x] **Open Source** - Open Source Skyvern's core codebase
- [x] **[BETA] Workflow support** - Allow support to chain multiple Skyvern calls together
- [ ] **Improved context** - Improve Skyvern's ability to understand content around interactable elements by introducing feeding relevant label context through the text prompt
- [ ] **Cost Savings** - Improve Skyvern's stability and reduce the cost of running Skyvern by optimizing the context tree passed into Skyvern
- [ ] **Self-serve UI** - Deprecate the Streamlit UI in favour of a React-based UI component that allows users to kick off new jobs in Skyvern
- [ ] **Prompt Caching** - Introduce a caching layer to the LLM calls to dramatically reduce the cost of running Skyvern (memorize past actions and repeat them!)
- [ ] **Chrome Viewport streaming** - Introduce a way to live-stream the Chrome viewport to the user's browser (as a part of the self-serve UI)
- [ ] **Past Runs UI** - Deprecate the Streamlit UI in favour of a React-based UI that allows you to visualize past runs and their results
- [ ] **Integrate LLM Observability tools** - Integrate LLM Observability tools to allow back-testing prompt changes with specific data sets + visualize the performance of Skyvern over time
- [ ] **Integrate public datasets** - Integrate Skyvern with public benchmark tests to track the quality our models over time
- [ ] **Workflow UI Builder** - Introduce a UI to allow users to build and analyze workflows visually

## Contributing

We welcome PRs and suggestions! Don't hesitate to open a PR/issue or to reach out to us [via email](mailto:founders@skyvern.com) or [discord](https://discord.gg/fG2XXEuQX3).
Please have a look at our [contribution guide](CONTRIBUTING.md) and
["Help Wanted" issues](https://github.com/skyvern-ai/skyvern/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) to get started!

## Usage and Feedback

<< you linked your email and discord in many places. just leave this one to avoid annoying people >>

We are delighted to work with the community to help shape the roadmap of our product. Please don't hesitate to reach out via [via email](mailto:founders@skyvern.com) or [discord](https://discord.gg/fG2XXEuQX3) if you have any product suggestions or feedback.

### Privacy

By Default, Skyvern collects basic usage statistics to help us understand how Skyvern is being used. If you would like to opt-out of telemetry, please set the `SKYVERN_TELEMETRY` environment variable to `false`.

## License

<< I'd explicitly mention which parts are OSS >>

The majority of Skyvern is open source. The current license can be found in the  [LICENSE](LICENSE) file. If there are any questions or concerns around licensing, please [contact us](mailto:founders@skyvern.com) and we would be happy to help.

<see my notes about moving the examples that were here to a section above>
