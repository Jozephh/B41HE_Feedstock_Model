FIFE NGL FEEDSTOCK MODEL - ASSUMPTION REGISTER
UPDATED PRODUCT-SPLIT VERSION

=======
PURPOSE
=======
Estimate potential ethane, propane, butane and natural-gasoline output
from the Fife NGL plant over the project period.

=====
FILES
=====
assumptions.py
    All source-derived inputs and user-editable modelling assumptions.

model.py
    Calculation logic only.

run_model.py
    Runs the model, prints yearly results, exports the project-period CSV,
    and plots product availability.

=====================
SOURCE-DERIVED INPUTS
=====================

1. FIFE NGL THROUGHPUT
2024 anchor = 2,237 kt/y.
Basis: reported Fife Council Shell FNGL processing data.

2. 2025 ST FERGUS THROUGHPUT
SEGAL = 7.5 bcm/y
FUKA  = 4.7 bcm/y
SAGE  = 3.7 bcm/y
Basis: OEUK / Westwood, February 2026.

3. NORWEGIAN CONTRIBUTION (https://www.sodir.no/en/whats-new/publications/reports/the-shelf/the-shelf-in-2025/summary/)
Reconstructed from OEUK / Westwood 2025 field shares:
SEGAL = 54% Norway (Gjoa 45% + Statfjord 9%)
FUKA  = 31% Norway (Martin Linge 31%)
SAGE  = 38% Norway (Alvheim 21% + Eiga 17%)

4. UK GAS PRODUCTION, 2026-2050 
Read directly from the supplied NSTA February 2026 production-projection
workbook.

================================
FIFE NGL PRODUCT COMPOSITION
================================

Representative Fife NGL product mass fractions are derived from historical
Shell Fife NGL operating data reported to SEPA.

The 2018 and 2020 operating years are used as the representative basis.

2019 is excluded because SEPA reports prolonged ethane flaring during that
year due to an FEP shutdown.

2021 is excluded because SEPA reports an FEP shutdown which resulted in part
of the ethane production being exported to Grangemouth rather than following
the usual FEP route.

SOURCE DATA
-----------

SEPA reports the following product exports from Fife NGL.

2018:

Ethane:
    932,980.53 t/y

Propane:
    Ships         = 917,382.20 t/y
    Road tankers  =  96,953.40 t/y
    FEP           =  12,478.20 t/y

    Total propane = 1,026,813.80 t/y

Butane:
    Ships         = 639,464.20 t/y
    Road tankers  =  84,127.20 t/y

    Total butane  = 723,591.40 t/y

Natural gasoline:
    526,721.90 t/y


2020:

Ethane:
    695,319.23 t/y

Propane:
    Ships         = 720,700.60 t/y
    Road tankers  = 103,286.20 t/y
    FEP           =   5,342.83 t/y

    Total propane = 829,329.63 t/y

Butane:
    Ships         = 517,693.70 t/y
    Road tankers  =  82,695.80 t/y

    Total butane  = 600,389.50 t/y

Natural gasoline:
    430,810.80 t/y


REPRESENTATIVE PRODUCT SPLIT
----------------------------

The 2018 and 2020 product quantities are combined to provide a representative
two-year product distribution.

Ethane:
    932,980.53 + 695,319.23
    = 1,628,299.76 t

Propane:
    1,026,813.80 + 829,329.63
    = 1,856,143.43 t

Butane:
    723,591.40 + 600,389.50
    = 1,323,980.90 t

Natural gasoline:
    526,721.90 + 430,810.80
    = 957,532.70 t


Total represented product:

    1,628,299.76
  + 1,856,143.43
  + 1,323,980.90
  +   957,532.70
  = 5,765,956.79 t


The representative mass fraction of each product is therefore calculated as:

    Product mass fraction
        = Combined product quantity / Combined total product quantity


Ethane:

    1,628,299.76 / 5,765,956.79
    = 0.28240
    = 28.24 wt%


Propane:

    1,856,143.43 / 5,765,956.79
    = 0.32191
    = 32.19 wt%


Butane:

    1,323,980.90 / 5,765,956.79
    = 0.22962
    = 22.96 wt%


Natural gasoline:

    957,532.70 / 5,765,956.79
    = 0.16607
    = 16.61 wt%


MODEL PRODUCT FRACTIONS
-----------------------

ETHANE_MASS_SHARE   = 0.2824
PROPANE_MASS_SHARE  = 0.3219
BUTANE_MASS_SHARE   = 0.2296
GASOLINE_MASS_SHARE = 0.1661

Total = 1.0000 (100.00 wt%)

These fractions represent the historical distribution of the four principal
saleable Fife NGL products during the selected 2018 and 2020 operating years.

The model assumes that this representative product distribution remains
constant throughout the forecast period. This is a screening assumption:
future NGL composition may change as the mix of UK and Norwegian producing
fields changes.

=================
MODEL ASSUMPTIONS
=================

UK ST FERGUS SHARE
32% of NSTA UK gross gas is assigned to the northern / St Fergus systems.
This is a screening approximation and future routing may differ.

NORWAY
Relevant Norwegian St Fergus supply is held constant through 2029 and then
declined by 4.5% per year. This remains a screening approximation rather than
a field-by-field Norwegian forecast.

UK AFTER 2050
NSTA ends in 2050. From 2051 to 2063 the annual UK decline is sampled between
9% and 13%. Random seed 45 makes the result reproducible.

FIFE NGL SCALING
Future total Fife NGL throughput is calculated as:

    Fife NGL = 2,237 kt/y
               x future relevant St Fergus gas
               / 2025 relevant St Fergus gas

This assumes average NGL yield/richness and routing remain sufficiently similar
for throughput scaling to be useful as a screening model.

=====================
IMPORTANT LIMITATIONS
=====================

The outputs are potential product/feedstock availability, not guaranteed
commercial availability for a new Mossmorran project.

Actual quantities may differ because of:
- changing field composition and NGL richness
- routing between Fife and other facilities
- commercial contracts
- alternative Norwegian export routes
- plant availability and shutdowns
- changes in NGL recovery/fractionation
- new UK or Norwegian developments
- imports or other future infrastructure changes

The historical FNGL product split is held constant through the forecast.
This is an explicit modelling assumption and should be sensitivity-tested
if product composition becomes important to plant sizing.

==============
PROJECT PERIOD
==============
Project start = 2028
Model end     = 2063

2028 to 2063 is a 35-year difference. Including both endpoints produces
36 annual table entries.
