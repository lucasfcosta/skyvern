import json


def get_sample_url() -> str:
    return "https://www.geico.com"


def get_sample_navigation_goal() -> str:
    return "Navigate through the website until you generate an auto insurance quote. Do not generate a home insurance quote. If this page contains an auto insurance quote, consider the goal achieved"


def get_sample_data_extraction_goal() -> str:
    return "Extract all quote information in JSON format including the premium amount, the timeframe for the quote."


def get_sample_navigation_payload() -> str:
    navigation_payload = {
        "licensed_at_age": 19,
        "education_level": "HIGH_SCHOOL",
        "phone_number": "8042221111",
        "full_name": "Chris P. Bacon",
        "past_claim": [],
        "has_claims": False,
        "spouse_occupation": "Florist",
        "auto_current_carrier": "None",
        "home_commercial_uses": None,
        "spouse_full_name": "Amy Stake",
        "auto_commercial_uses": None,
        "requires_sr22": False,
        "previous_address_move_date": None,
        "line_of_work": None,
        "spouse_age": "1987-12-12",
        "auto_insurance_deadline": None,
        "email": "chris.p.bacon@abc.com",
        "net_worth_numeric": 1000000,
        "spouse_gender": "F",
        "marital_status": "married",
        "spouse_licensed_at_age": 20,
        "license_number": "AAAAAAA090AA",
        "spouse_license_number": "AAAAAAA080AA",
        "how_much_can_you_lose": 25000,
        "vehicles": [
            {
                "annual_mileage": 10000,
                "commute_mileage": 4000,
                "existing_coverages": None,
                "ideal_coverages": {
                    "bodily_injury_per_incident_limit": 50000,
                    "bodily_injury_per_person_limit": 25000,
                    "collision_deductible": 1000,
                    "comprehensive_deductible": 1000,
                    "personal_injury_protection": None,
                    "property_damage_per_incident_limit": None,
                    "property_damage_per_person_limit": 25000,
                    "rental_reimbursement_per_incident_limit": None,
                    "rental_reimbursement_per_person_limit": None,
                    "roadside_assistance_limit": None,
                    "underinsured_motorist_bodily_injury_per_incident_limit": 50000,
                    "underinsured_motorist_bodily_injury_per_person_limit": 25000,
                    "underinsured_motorist_property_limit": None,
                },
                "ownership": "Owned",
                "parked": "Garage",
                "purpose": "commute",
                "vehicle": {
                    "style": "AWD 3.0 quattro TDI 4dr Sedan",
                    "model": "A8 L",
                    "price_estimate": 29084,
                    "year": 2015,
                    "make": "Audi",
                },
                "vehicle_id": None,
                "vin": None,
            }
        ],
        "additional_drivers": [],
        "home": [
            {
                "home_ownership": "owned",
            }
        ],
        "spouse_line_of_work": "Agriculture, Forestry and Fishing",
        "occupation": "Customer Service Representative",
        "id": None,
        "gender": "M",
        "credit_check_authorized": False,
        "age": "1987-11-11",
        "license_state": "Washington",
        "cash_on_hand": "$10000–14999",
        "address": {
            "city": "HOUSTON",
            "country": "US",
            "state": "TX",
            "street": "9625 GARFIELD AVE.",
            "zip": "77082",
        },
        "spouse_education_level": "MASTERS",
        "spouse_email": "amy.stake@abc.com",
        "spouse_added_to_auto_policy": True,
    }

    return json.dumps(navigation_payload)


def get_sample_extracted_information_schema() -> str:
    extracted_information_schema = {
        "additionalProperties": False,
        "properties": {
            "quotes": {
                "items": {
                    "additionalProperties": False,
                    "properties": {
                        "coverages": {
                            "items": {
                                "additionalProperties": False,
                                "properties": {
                                    "amount": {
                                        "description": "The coverage amount in USD, which can be a single value or a range (e.g., '$300,000' or '$300,000/$300,000').",
                                        "type": "string",
                                    },
                                    "included": {
                                        "description": "Indicates whether the coverage is included in the policy (true or False).",
                                        "type": "boolean",
                                    },
                                    "type": {
                                        "description": "The limit of the coverage (e.g., 'bodily_injury_limit', 'property_damage_limit', 'underinsured_motorist_bodily_injury_limit').\nTranslate the english name of the coverage to snake case values in the following list:\n  * bodily_injury_limit\n  * property_damage_limit\n  * underinsured_motorist_bodily_injury_limit\n  * personal_injury_protection\n  * accidental_death\n  * work_loss_exclusion\n",
                                        "type": "string",
                                    },
                                },
                                "type": "object",
                            },
                            "type": "array",
                        },
                        "premium_amount": {
                            "description": "The total premium amount for the whole quote timeframe in USD, formatted as a string (e.g., '$321.57').",
                            "type": "string",
                        },
                        "quote_number": {
                            "description": "The quote number generated by the carrier that identifies this quote",
                            "type": "string",
                        },
                        "timeframe": {
                            "description": "The duration of the coverage, typically expressed in months or years.",
                            "type": "string",
                        },
                        "vehicle_coverages": {
                            "items": {
                                "additionalProperties": False,
                                "properties": {
                                    "collision_deductible": {
                                        "description": "The collision deductible amount in USD, which is a single value (e.g., '$500') or null if it is not included",
                                        "type": "string",
                                    },
                                    "comprehensive_deductible": {
                                        "description": "The collision deductible amount in USD, which is a single value (e.g., '$500') or null if it is not included",
                                        "type": "string",
                                    },
                                    "for_vehicle": {
                                        "additionalProperties": False,
                                        "description": "The vehicle that the collision and comprehensive coverage is for",
                                        "properties": {
                                            "make": {"description": "The make of the vehicle", "type": "string"},
                                            "model": {"description": "The model of the vehicle", "type": "string"},
                                            "year": {"description": "The year of the vehicle", "type": "string"},
                                        },
                                        "type": "object",
                                    },
                                    "underinsured_property_damage": {
                                        "description": "The underinsured property damage limit for this vehicle, which is a limit and a deductible (e.g., '$25,000/$250 deductible') or null if it is not included",
                                        "type": "string",
                                    },
                                },
                                "type": "object",
                            },
                            "type": "array",
                        },
                    },
                    "type": "object",
                },
                "type": "array",
            }
        },
        "type": "object",
    }
    return json.dumps(extracted_information_schema)
