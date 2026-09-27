import os

import matplotlib.pyplot as plt
import pandas as pd

from simple_model import run_simple_model


# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------

OUTPUT_FOLDER = "simple_model_outputs"
PROJECT_START_YEAR = 2028

PLOT_PRODUCTS = {
    "Ethane": "ethane_ktpa",
    "Propane": "propane_ktpa",
    "Butane": "butane_ktpa",
}

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True,
)


# ------------------------------------------------------------
# Run model
# ------------------------------------------------------------

results = run_simple_model()

project = results[
    results["year"] >= PROJECT_START_YEAR
].copy()


# ------------------------------------------------------------
# Export Excel workbook
# ------------------------------------------------------------

output_file = os.path.join(
    OUTPUT_FOLDER,
    "simple_feedstock_model.xlsx",
)

with pd.ExcelWriter(
    output_file,
    engine="openpyxl",
) as writer:

    results.to_excel(
        writer,
        sheet_name="All Years",
        index=False,
    )

    project.to_excel(
        writer,
        sheet_name="Project Period",
        index=False,
    )


# ------------------------------------------------------------
# Plot ethane, propane and butane
# ------------------------------------------------------------

for name, column in PLOT_PRODUCTS.items():

    plt.figure(
        figsize=(11, 6)
    )

    plt.plot(
        results["year"],
        results[column],
    )

    plt.xlabel("Year")

    plt.ylabel(
        f"Potential {name} availability (kt/y)"
    )

    plt.title(
        f"Simple Model - Fife NGL {name} Availability"
    )

    plt.xlim(
        results["year"].min(),
        results["year"].max(),
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()
    plt.show()