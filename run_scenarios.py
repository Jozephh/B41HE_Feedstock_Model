import os

import matplotlib.pyplot as plt
import pandas as pd

import assumptions as A
from model import run_model
from scenarios import (
    SCENARIOS,
    build_oeuk_production,
    scenario_gas,
)


WORKBOOK = (
    "nsta-february-2026-production-projections-plus-"
    "ccc-and-desnz-demand-projections.xlsx"
)

OUTPUT_FOLDER = "scenario_outputs"
GRAPH_START_YEAR = 2026

FEEDSTOCKS = {
    "ethane": A.ETHANE_MASS_SHARE,
    "propane": A.PROPANE_MASS_SHARE,
    "butane": A.BUTANE_MASS_SHARE,
}

SCENARIO_SHEETS = {
    "NSTA Reference": "NSTA Reference",
    "Rosebank + Jackdaw": "Rosebank + Jackdaw",
    "Max Drilling (OEUK Upside)": "Max Drilling",
}

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ------------------------------------------------------------
# Baseline
# ------------------------------------------------------------

baseline = run_model(WORKBOOK)

baseline_2025_gas = (
    A.SEGAL_BCM
    + A.FUKA_BCM
    + A.SAGE_BCM
)

# Convert St Fergus allocated UK gas back to total UK production
nsta_uk = {
    int(row.year):
    row.uk_bcm / A.UK_ST_FERGUS_SHARE
    for row in baseline.itertuples()
}

oeuk = build_oeuk_production(nsta_uk)


# ------------------------------------------------------------
# Run scenarios
# ------------------------------------------------------------

rows = []

for scenario in SCENARIOS:
    for base in baseline.itertuples():

        year = int(base.year)

        total_gas = scenario_gas(
            year=year,
            scenario=scenario,
            baseline_uk=base.uk_bcm,
            baseline_norway=base.norway_bcm,
            oeuk_production=oeuk,
            st_fergus_share=A.UK_ST_FERGUS_SHARE,
        )

        total_ngl = (
            A.FIFE_NGL_KTPA
            * total_gas
            / baseline_2025_gas
        )

        row = {
            "scenario": scenario,
            "year": year,
        }

        for feedstock, share in FEEDSTOCKS.items():
            row[f"{feedstock}_ktpa"] = (
                total_ngl * share
            )

        rows.append(row)


results = pd.DataFrame(rows)

columns = [
    f"{feedstock}_ktpa"
    for feedstock in FEEDSTOCKS
]

project = results[
    results["year"].between(
        A.PROJECT_START_YEAR,
        A.END_YEAR,
    )
].copy()

plot_data = results[
    results["year"].between(
        GRAPH_START_YEAR,
        A.END_YEAR,
    )
].copy()


# ------------------------------------------------------------
# Validation
# ------------------------------------------------------------

if project.empty:
    raise ValueError(
        "No results exist within the project period."
    )

if project[columns].isna().any().any():
    raise ValueError(
        "NaN values detected."
    )

if (project[columns] < 0).any().any():
    raise ValueError(
        "Negative feedstock availability detected."
    )

start = plot_data[
    plot_data["year"] == GRAPH_START_YEAR
]

for column in columns:
    if start[column].round(10).nunique() != 1:
        raise ValueError(
            f"Scenarios are not identical in "
            f"{GRAPH_START_YEAR}: {column}"
        )

for column in columns:
    comparison = plot_data.pivot(
        index="year",
        columns="scenario",
        values=column,
    )

    if (
        comparison["Max Drilling (OEUK Upside)"]
        < comparison["Rosebank + Jackdaw"]
    ).any():
        raise ValueError(
            f"Max Drilling falls below "
            f"Rosebank + Jackdaw: {column}"
        )


# ------------------------------------------------------------
# Export scenario workbook
# ------------------------------------------------------------

with pd.ExcelWriter(
    os.path.join(
        OUTPUT_FOLDER,
        "feedstock_scenarios.xlsx",
    ),
    engine="openpyxl",
) as writer:

    project.to_excel(
        writer,
        sheet_name="All Scenarios",
        index=False,
    )

    for scenario in SCENARIOS:
        data = project[
            project["scenario"] == scenario
        ][["year"] + columns]

        data.to_excel(
            writer,
            sheet_name=SCENARIO_SHEETS[scenario],
            index=False,
        )


# ------------------------------------------------------------
# Export comparison workbook
# ------------------------------------------------------------

with pd.ExcelWriter(
    os.path.join(
        OUTPUT_FOLDER,
        "feedstock_comparisons.xlsx",
    ),
    engine="openpyxl",
) as writer:

    for feedstock in FEEDSTOCKS:
        comparison = project.pivot(
            index="year",
            columns="scenario",
            values=f"{feedstock}_ktpa",
        )

        comparison.to_excel(
            writer,
            sheet_name=feedstock.capitalize(),
        )


# ------------------------------------------------------------
# Plots
# ------------------------------------------------------------

for feedstock in FEEDSTOCKS:

    column = f"{feedstock}_ktpa"

    plt.figure(figsize=(11, 6))

    for scenario in SCENARIOS:
        data = plot_data[
            plot_data["scenario"] == scenario
        ]

        plt.plot(
            data["year"],
            data[column],
            label=scenario,
        )

    label = feedstock.capitalize()

    plt.xlabel("Year")
    plt.ylabel(
        f"Potential {label} availability (kt/y)"
    )
    plt.title(
        f"Projected Fife NGL {label} Availability"
    )

    plt.xlim(
        GRAPH_START_YEAR,
        A.END_YEAR,
    )

    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()