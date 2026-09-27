import numpy as np
import pandas as pd


# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------

START_YEAR = 2025
END_YEAR = 2063

DECLINE_MIN = 0.09
DECLINE_MAX = 0.13
RANDOM_SEED = 45


# ------------------------------------------------------------
# SEPA 2020 Fife NGL material balance
# kt/y
# ------------------------------------------------------------

# 2020 values are used as the starting reference balance.
# The model labels this reference point as 2025 so that
# decline begins from 2026.

BASE_PRODUCTS = {
    "ethane_ktpa": 695.31923,
    "propane_ktpa": 829.32963,
    "butane_ktpa": 600.38950,
    "gasoline_ktpa": 430.81080,
}


def run_simple_model():
    """
    Simple Fife NGL decline model.

    Uses the SEPA 2020 material balance as the starting
    reference production balance.

    From 2026 onwards, total production declines by a
    randomly selected 9-13% each year.

    The same annual decline is applied to every product,
    preserving the original material balance.
    """

    rng = np.random.default_rng(
        RANDOM_SEED
    )

    current = BASE_PRODUCTS.copy()

    rows = []

    # 2025 reference point
    rows.append({
        "year": START_YEAR,
        "decline_percent": 0.0,
        **current,
    })

    # 2026-2063
    for year in range(
        START_YEAR + 1,
        END_YEAR + 1,
    ):
        decline = rng.uniform(
            DECLINE_MIN,
            DECLINE_MAX,
        )

        for product in current:
            current[product] *= (
                1 - decline
            )

        rows.append({
            "year": year,
            "decline_percent": decline * 100,
            **current,
        })

    df = pd.DataFrame(rows)

    df["total_ngl_ktpa"] = (
        df["ethane_ktpa"]
        + df["propane_ktpa"]
        + df["butane_ktpa"]
        + df["gasoline_ktpa"]
    )

    return df