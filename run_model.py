import matplotlib.pyplot as plt
import assumptions as A
from model import run_model


# ============================================================
# NSTA WORKBOOK
# ============================================================

WORKBOOK = (
    "nsta-february-2026-production-projections-plus-ccc-and-desnz-demand-projections.xlsx"
)


# ============================================================
# RUN MODEL
# ============================================================

df = run_model(WORKBOOK)


# ============================================================
# PRINT FULL RESULTS
# ============================================================

print("\nFIFE NGL FEEDSTOCK PROJECTION\n")
print(df.round(2).to_string(index=False))


# ============================================================
# PROJECT PERIOD: 2028-2063
# ============================================================

project = df[
    df["year"].between(
        A.PROJECT_START_YEAR,
        A.END_YEAR
    )
]


# ============================================================
# SAVE RESULTS
# ============================================================

project.to_csv(
    "fife_feedstock_projection_2028_2063.csv",
    index=False
)


# ============================================================
# PLOT
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    project["year"],
    project["ethane_ktpa"],
    label="Ethane"
)

plt.plot(
    project["year"],
    project["propane_ktpa"],
    label="Propane"
)

plt.plot(
    project["year"],
    project["butane_ktpa"],
    label="Butane"
)

plt.xlabel("Year")
plt.ylabel("Potential feedstock from Fife NGL (kt/y)")
plt.title("Projected Fife NGL Product Availability")

plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()