# ============================================================
# FIFE NGL FEEDSTOCK MODEL - ASSUMPTIONS
# ============================================================

START_YEAR = 2025
PROJECT_START_YEAR = 2028
END_YEAR = 2063

# Fife NGL baseline
FIFE_NGL_KTPA = 2237.0

# 2025 St Fergus gas throughput
SEGAL_BCM = 7.5
FUKA_BCM = 4.7
SAGE_BCM = 3.7

SEGAL_NORWAY_SHARE = 0.54
FUKA_NORWAY_SHARE = 0.31
SAGE_NORWAY_SHARE = 0.38

UK_ST_FERGUS_SHARE = 0.32

# Fife NGL product mass fractions
ETHANE_MASS_SHARE = 0.2824
PROPANE_MASS_SHARE = 0.3219
BUTANE_MASS_SHARE = 0.2296
GASOLINE_MASS_SHARE = 0.1661

# Norwegian national sales-gas profile, bcm/y.
# 2025 is the NOD 40 MJ-normalised reported value.
# 2026-2035 are rounded readings from the NOD chart
# "Expected volumes of sales gas from Norwegian fields, 1995-2035".
# These values are used only as an index to scale the 2025
# Norwegian contribution relevant to St Fergus.
NORWAY_SALES_GAS_BCM = {
    2025: 120.5,
    2026: 122.0,
    2027: 122.0,
    2028: 119.0,
    2029: 114.0,
    2030: 108.0,
    2031: 102.0,
    2032: 97.0,
    2033: 93.0,
    2034: 89.0,
    2035: 85.0,
}

# After 2035, continue the CAGR implied by the 2030-2035
# Norwegian gas-production profile.
NORWAY_DECLINE_START_YEAR = 2030
NORWAY_FORECAST_END_YEAR = 2035

# UK post-2050 decline
UK_RANDOM_DECLINE_MIN = 0.09
UK_RANDOM_DECLINE_MAX = 0.13
RANDOM_SEED = 45
