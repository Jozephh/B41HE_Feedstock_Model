"""
UKCS development scenarios for the Fife NGL feedstock model.

Scenarios:
1. NSTA Reference
2. Rosebank + Jackdaw
3. Max Drilling (OEUK Upside)

All scenarios are identical through 2026.
Scenario divergence begins in 2027.
"""

import numpy as np


DAYS_PER_YEAR = 365
SCENARIO_START_YEAR = 2027

SCENARIOS = [
    "NSTA Reference",
    "Rosebank + Jackdaw",
    "Max Drilling (OEUK Upside)",
]


# Jackdaw P50 gas profile, kSm3/day
JACKDAW = {
    2024: 1163,
    2025: 4853,
    2026: 4688,
    2027: 3852,
    2028: 3108,
    2029: 2026,
    2030: 1619,
    2031: 1089,
    2032: 504,
}

# Rosebank gas profile, MMSm3/day
ROSEBANK = {
    2026: 0.47,
    2027: 1.62,
    2028: 1.67,
    2029: 1.72,
    2030: 1.72,
    2031: 1.72,
    2032: 1.66,
    2033: 1.58,
    2034: 1.47,
    2035: 1.39,
    2036: 1.33,
    2037: 1.39,
    2038: 1.35,
    2039: 1.27,
    2040: 1.26,
    2041: 1.21,
    2042: 1.05,
    2043: 0.98,
    2044: 0.84,
    2045: 0.72,
    2046: 0.61,
    2047: 0.52,
    2048: 0.48,
    2049: 0.45,
    2050: 0.40,
    2051: 0.37,
}

JACKDAW_SHIFT = 3
ROSEBANK_SHIFT = 1


def named_field_uplift(year):
    """Return Rosebank + Jackdaw contribution in bcm/y."""

    jackdaw = (
        JACKDAW.get(year - JACKDAW_SHIFT, 0)
        * DAYS_PER_YEAR
        / 1_000_000
    )

    rosebank = (
        ROSEBANK.get(year - ROSEBANK_SHIFT, 0)
        * DAYS_PER_YEAR
        / 1000
    )

    return jackdaw + rosebank


# OEUK Upside Potential inputs
OEUK_2030 = 26.588
OEUK_2035 = 26.180
OEUK_TOTAL_2025_2050 = 456.0


def build_oeuk_production(nsta_uk):
    """
    Construct the OEUK Upside trajectory.

    2025-2026: NSTA
    2027-2030: interpolate to OEUK 2030
    2031-2035: interpolate to OEUK 2035
    2036-2063: exponential decline fitted to 456 bcm by 2050
    """

    production = {
        2025: nsta_uk[2025],
        2026: nsta_uk[2026],
    }

    for year in range(2027, 2031):
        production[year] = np.interp(
            year,
            [2026, 2030],
            [nsta_uk[2026], OEUK_2030],
        )

    for year in range(2031, 2036):
        production[year] = np.interp(
            year,
            [2030, 2035],
            [OEUK_2030, OEUK_2035],
        )

    remaining = (
        OEUK_TOTAL_2025_2050
        - sum(production.values())
    )

    low, high = 0.0, 1.0

    for _ in range(60):
        factor = (low + high) / 2

        total = sum(
            OEUK_2035 * factor ** age
            for age in range(1, 16)
        )

        if total < remaining:
            low = factor
        else:
            high = factor

    factor = (low + high) / 2

    for year in range(2036, 2064):
        production[year] = (
            OEUK_2035
            * factor ** (year - 2035)
        )

    return production


def scenario_gas(
    year,
    scenario,
    baseline_uk,
    baseline_norway,
    oeuk_production,
    st_fergus_share,
):
    """Return gas relevant to Fife NGL in bcm/y."""

    reference = baseline_uk + baseline_norway

    if year < SCENARIO_START_YEAR:
        return reference

    rosebank_jackdaw = (
        reference
        + named_field_uplift(year)
    )

    if scenario == "NSTA Reference":
        return reference

    if scenario == "Rosebank + Jackdaw":
        return rosebank_jackdaw

    if scenario == "Max Drilling (OEUK Upside)":
        oeuk_case = (
            oeuk_production[year]
            * st_fergus_share
            + baseline_norway
        )

        return max(
            oeuk_case,
            rosebank_jackdaw,
        )

    raise ValueError(
        f"Unknown scenario: {scenario}"
    )