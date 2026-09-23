import pandas as pd
import numpy as np
import assumptions as A


def run_model(workbook):

    # ========================================================
    # 2025 GAS BASELINE
    # ========================================================

    total_2025 = A.SEGAL_BCM + A.FUKA_BCM + A.SAGE_BCM

    norway_2025 = (
        A.SEGAL_BCM * A.SEGAL_NORWAY_SHARE
        + A.FUKA_BCM * A.FUKA_NORWAY_SHARE
        + A.SAGE_BCM * A.SAGE_NORWAY_SHARE
    )

    uk_2025 = total_2025 - norway_2025


    # ========================================================
    # READ NSTA UK GAS FORECAST
    # ========================================================

    gas = pd.read_excel(
        workbook,
        sheet_name="Projections",
        usecols="H,J",
        header=None,
        names=["year", "uk_gas"]
    )

    gas["year"] = pd.to_numeric(gas["year"], errors="coerce")
    gas["uk_gas"] = pd.to_numeric(gas["uk_gas"], errors="coerce")

    gas = gas.dropna()
    gas = gas[gas["year"].between(2026, 2050)]
    gas["year"] = gas["year"].astype(int)

    nsta = dict(zip(gas["year"], gas["uk_gas"]))


    # ========================================================
    # UK GAS PROJECTION
    # ========================================================

    uk = {2025: uk_2025}

    for year in range(2026, 2051):
        uk[year] = A.UK_ST_FERGUS_SHARE * nsta[year]


    # ========================================================
    # UK AFTER 2050
    # ========================================================

    rng = np.random.default_rng(A.RANDOM_SEED)

    for year in range(2051, A.END_YEAR + 1):
        decline = rng.uniform(
            A.UK_RANDOM_DECLINE_MIN,
            A.UK_RANDOM_DECLINE_MAX
        )
        uk[year] = uk[year - 1] * (1 - decline)


    # ========================================================
    # NORWEGIAN GAS PROJECTION
    # ========================================================

    norway = {}

    for year in range(A.START_YEAR, A.END_YEAR + 1):

        if year <= A.NORWAY_FLAT_TO_YEAR:
            norway[year] = norway_2025

        else:
            norway[year] = (
                norway_2025
                * (1 - A.NORWAY_DECLINE)
                ** (year - A.NORWAY_FLAT_TO_YEAR)
            )


    # ========================================================
    # FIFE NGL AND PRODUCT OUTPUT
    # ========================================================

    rows = []

    for year in range(A.START_YEAR, A.END_YEAR + 1):

        total_gas = uk[year] + norway[year]

        # Scale the actual Fife NGL throughput anchor in direct
        # proportion to relevant St Fergus gas throughput.
        total_ngl = (
            A.FIFE_NGL_KTPA
            * total_gas
            / total_2025
        )

        # Product quantities use representative FNGL mass shares
        # derived from Shell/SEPA operating material balances.
        ethane = total_ngl * A.ETHANE_MASS_SHARE
        propane = total_ngl * A.PROPANE_MASS_SHARE
        butane = total_ngl * A.BUTANE_MASS_SHARE

        rows.append([
            year,
            uk[year],
            norway[year],
            total_gas,
            total_ngl,
            ethane,
            propane,
            butane
        ])


    # ========================================================
    # DATAFRAME
    # ========================================================

    df = pd.DataFrame(
        rows,
        columns=[
            "year",
            "uk_bcm",
            "norway_bcm",
            "total_gas_bcm",
            "total_ngl_ktpa",
            "ethane_ktpa",
            "propane_ktpa",
            "butane_ktpa"
        ]
    )


    # ========================================================
    # YEARLY DECLINE
    # ========================================================

    df["uk_decline_percent"] = -df["uk_bcm"].pct_change() * 100
    df["norway_decline_percent"] = -df["norway_bcm"].pct_change() * 100
    df["ngl_decline_percent"] = -df["total_ngl_ktpa"].pct_change() * 100

    return df
