import pandas as pd
import matplotlib.pyplot as plt

import assumptions as A
from model import run_model
from scenarios import SCENARIOS, scenario_uplift


WORKBOOK = (
    "nsta-february-2026-production-projections-plus-ccc-and-desnz-demand-projections.xlsx"
)


# ============================================================
# RUN BASELINE MODEL
# ============================================================

baseline = run_model(WORKBOOK)


# ============================================================
# RUN SCENARIOS
# ============================================================

scenario_results = []

for scenario_name in SCENARIOS:

    for _, row in baseline.iterrows():

        year = int(row["year"])

        baseline_relevant_gas = row["total_gas_bcm"]

        additional_gas = scenario_uplift(
            year,
            scenario_name,
        )

        scenario_gas = (
            baseline_relevant_gas
            + additional_gas
        )

        # Scale scenario gas to Fife NGL throughput
        total_ngl = (
            A.FIFE_NGL_KTPA
            * scenario_gas
            / (
                A.SEGAL_BCM
                + A.FUKA_BCM
                + A.SAGE_BCM
            )
        )

        ethane = (
            total_ngl
            * A.ETHANE_MASS_SHARE
        )

        propane = (
            total_ngl
            * A.PROPANE_MASS_SHARE
        )

        butane = (
            total_ngl
            * A.BUTANE_MASS_SHARE
        )

        gasoline = (
            total_ngl
            * A.GASOLINE_MASS_SHARE
        )

        scenario_results.append({
            "scenario": scenario_name,
            "year": year,
            "baseline_gas_bcm": baseline_relevant_gas,
            "additional_gas_bcm": additional_gas,
            "scenario_gas_bcm": scenario_gas,
            "total_ngl_ktpa": total_ngl,
            "ethane_ktpa": ethane,
            "propane_ktpa": propane,
            "butane_ktpa": butane,
            "gasoline_ktpa": gasoline,
        })


results = pd.DataFrame(scenario_results)


# ============================================================
# PROJECT PERIOD ONLY
# ============================================================

project = results[
    results["year"].between(
        A.PROJECT_START_YEAR,
        A.END_YEAR,
    )
].copy()


# ============================================================
# EXPORT
# ============================================================

project.to_csv(
    "fife_feedstock_scenarios_2028_2063.csv",
    index=False,
)


# ============================================================
# PLOT ETHANE
# ============================================================

plt.figure(figsize=(11, 6))

for scenario_name in SCENARIOS:

    data = project[
        project["scenario"] == scenario_name
    ]

    plt.plot(
        data["year"],
        data["ethane_ktpa"],
        label=scenario_name,
    )

plt.xlabel("Year")
plt.ylabel("Potential ethane availability (kt/y)")
plt.title("Fife NGL Ethane Availability - UKCS Scenarios")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()


# ============================================================
# PLOT TOTAL NGL
# ============================================================

plt.figure(figsize=(11, 6))

for scenario_name in SCENARIOS:

    data = project[
        project["scenario"] == scenario_name
    ]

    plt.plot(
        data["year"],
        data["total_ngl_ktpa"],
        label=scenario_name,
    )

plt.xlabel("Year")
plt.ylabel("Potential Fife NGL throughput (kt/y)")
plt.title("Fife NGL Feedstock Availability - UKCS Scenarios")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()