# ============================================================
# FIFE NGL FEEDSTOCK MODEL - ASSUMPTIONS
# ============================================================

# Model period
START_YEAR = 2025
PROJECT_START_YEAR = 2028
END_YEAR = 2063


# ============================================================
# FIFE NGL THROUGHPUT
# ============================================================

# Actual Fife NGL throughput anchor, 2024
# Source: Fife Council reported Shell FNGL processing data
FIFE_NGL_KTPA = 2237.0


# ============================================================
# ST FERGUS GAS THROUGHPUT
# ============================================================

# 2025 throughput
# Source: OEUK / Westwood, February 2026
SEGAL_BCM = 7.5
FUKA_BCM = 4.7
SAGE_BCM = 3.7


# ============================================================
# NORWEGIAN SHARE OF EACH SYSTEM
# ============================================================

# Derived from OEUK / Westwood 2025 field shares:
# SEGAL: Gjoa 45% + Statfjord 9% = 54%
# FUKA: Martin Linge = 31%
# SAGE: Alvheim 21% + Eiga 17% = 38%
SEGAL_NORWAY_SHARE = 0.54
FUKA_NORWAY_SHARE = 0.31
SAGE_NORWAY_SHARE = 0.38


# ============================================================
# UK GAS ROUTING
# ============================================================

# Screening assumption: fraction of NSTA UK gross gas assigned
# to the northern / St Fergus systems
UK_ST_FERGUS_SHARE = 0.32


# ============================================================
# FIFE NGL PRODUCT MASS SPLIT
# ============================================================

# Estimated representative FNGL product mass split based on
# Shell/SEPA operating material-balance data for 2018 and 2020.
#
# These replace the previous assumed wet-gas molar composition,
# molecular-weight conversion and 99% recovery calculation.
#
# The four reported product shares total about 99.8%; the small
# balance is left unallocated rather than artificially normalised.

ETHANE_MASS_SHARE = 0.2824
PROPANE_MASS_SHARE = 0.3219
BUTANE_MASS_SHARE = 0.2296
GASOLINE_MASS_SHARE = 0.1661


# ============================================================
# NORWEGIAN PRODUCTION ASSUMPTIONS
# ============================================================

# Norwegian St Fergus supply held flat through 2029,
# then declined by 4.5% per year.
NORWAY_FLAT_TO_YEAR = 2029
NORWAY_DECLINE = 0.045


# ============================================================
# UK POST-2050 ASSUMPTIONS
# ============================================================

# NSTA projection ends in 2050.
# Thereafter annual decline is sampled between 9% and 13%.
UK_RANDOM_DECLINE_MIN = 0.09
UK_RANDOM_DECLINE_MAX = 0.13

# Fixed seed makes the post-2050 projection reproducible.
RANDOM_SEED = 45
