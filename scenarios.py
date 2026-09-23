"""
UKCS development scenarios for the Fife NGL feedstock model.

IMPORTANT
---------
These scenarios are engineering sensitivities, not forecasts of future
government policy or predictions that particular fields will be developed.

The NSTA Reference scenario remains the official February 2026 projection.

Additional field profiles are explicit modelling assumptions used to test
the sensitivity of future Fife NGL feedstock availability to additional
UKCS development.
"""


# ============================================================
# SCENARIO DEFINITIONS
# ============================================================

SCENARIOS = {

    "NSTA Reference": {
        "include_jackdaw": False,
        "include_rosebank": False,
        "future_fields": [],
    },

    "Jackdaw + Rosebank": {
        "include_jackdaw": True,
        "include_rosebank": True,
        "future_fields": [],
    },

    "Continued Development": {
        "include_jackdaw": True,
        "include_rosebank": True,
        "future_fields": [
            2033,
            2038,
            2043,
            2048,
        ],
    },

    "High Development": {
        "include_jackdaw": True,
        "include_rosebank": True,
        "future_fields": [
            2031,
            2034,
            2037,
            2040,
            2043,
            2046,
            2049,
            2052,
        ],
    },
}


# ============================================================
# FIELD PROFILE ASSUMPTIONS
# ============================================================

# These are placeholders for the scenario framework.
#
# Do NOT treat these as sourced Rosebank/Jackdaw production data.
# We will replace them with source-derived values after reviewing
# the field development documents.

JACKDAW = {
    "start_year": 2027,
    "plateau_bcm": None,
    "plateau_years": 3,
    "decline_rate": 0.12,
    "st_fergus_fraction": 1.0,
}

ROSEBANK = {
    "start_year": 2027,
    "plateau_bcm": None,
    "plateau_years": 3,
    "decline_rate": 0.12,
    "st_fergus_fraction": None,
}


# ============================================================
# GENERIC FUTURE FIELD
# ============================================================

# Once Jackdaw and Rosebank gas profiles are established,
# this value can be calculated from their representative scale.

FUTURE_FIELD = {
    "plateau_bcm": None,
    "plateau_years": 3,
    "decline_rate": 0.12,

    # Generic future UKCS development.
    # In the absence of a known export route, use the baseline
    # northern/St Fergus allocation assumption.
    "st_fergus_fraction": 0.32,
}

def field_production(
    year,
    start_year,
    plateau_bcm,
    plateau_years,
    decline_rate,
):
    """
    Calculate annual gas production for one modelled development.

    Production profile:
        before start year -> zero
        plateau period    -> constant plateau production
        after plateau     -> exponential decline
    """

    if plateau_bcm is None:
        return 0.0

    if year < start_year:
        return 0.0

    plateau_end = start_year + plateau_years - 1

    if year <= plateau_end:
        return plateau_bcm

    years_declining = year - plateau_end

    return (
        plateau_bcm
        * (1 - decline_rate) ** years_declining
    )

def calculate_field_contribution(year, field):
    """
    Calculate gas from a field that reaches the relevant
    St Fergus/Fife supply system.
    """

    production = field_production(
        year=year,
        start_year=field["start_year"],
        plateau_bcm=field["plateau_bcm"],
        plateau_years=field["plateau_years"],
        decline_rate=field["decline_rate"],
    )

    routing_fraction = field["st_fergus_fraction"]

    if routing_fraction is None:
        return 0.0

    return production * routing_fraction

def calculate_future_field(
    year,
    start_year,
):
    """
    Calculate relevant gas contribution from one hypothetical
    future UKCS field-equivalent.
    """

    field = {
        "start_year": start_year,
        "plateau_bcm": FUTURE_FIELD["plateau_bcm"],
        "plateau_years": FUTURE_FIELD["plateau_years"],
        "decline_rate": FUTURE_FIELD["decline_rate"],
        "st_fergus_fraction": FUTURE_FIELD["st_fergus_fraction"],
    }

    return calculate_field_contribution(year, field)

def scenario_uplift(year, scenario_name):
    """
    Return additional relevant St Fergus gas for a scenario
    relative to the NSTA Reference case.
    """

    scenario = SCENARIOS[scenario_name]

    uplift = 0.0

    # Jackdaw
    if scenario["include_jackdaw"]:
        uplift += calculate_field_contribution(
            year,
            JACKDAW,
        )

    # Rosebank
    if scenario["include_rosebank"]:
        uplift += calculate_field_contribution(
            year,
            ROSEBANK,
        )

    # Hypothetical future developments
    for start_year in scenario["future_fields"]:
        uplift += calculate_future_field(
            year,
            start_year,
        )

    return uplift