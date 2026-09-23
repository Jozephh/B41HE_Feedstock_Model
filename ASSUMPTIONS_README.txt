FIFE NGL FEEDSTOCK MODEL - ASSUMPTION REGISTER
===============================================

PURPOSE
-------
Estimate potential long-term Fife NGL product/feedstock availability.
Baseline model products are ethane, propane, butane and natural gasoline.
Scenario outputs use ethane, propane and butane.

SOURCE-DERIVED INPUTS
---------------------

FIFE NGL THROUGHPUT [1]
2024 processed NGL = approximately 2,237 kt/y, based on reported monthly
Fife NGL processing data.

2025 ST FERGUS GAS [2]
SEGAL = 7.5 bcm/y
FUKA  = 4.7 bcm/y
SAGE  = 3.7 bcm/y
Total = 15.9 bcm/y

Norwegian shares reconstructed from source field contributions:
SEGAL = 54%, FUKA = 31%, SAGE = 38%.
Derived 2025 split: Norway = 6.913 bcm/y; UK = 8.987 bcm/y.

UK GAS PRODUCTION, 2026-2050 [3,4]
Annual UK gross-gas production is read from the NSTA February 2026
production-projection workbook.

NORWEGIAN GAS PRODUCTION, 2025-2035 [5,6]
The 2025 Norwegian sales-gas value is 120.5 bcm on a 40 MJ-normalised basis.
The 2026-2035 values below are rounded readings from the Norwegian Offshore
Directorate chart "Expected volumes of sales gas from Norwegian fields,
1995-2035", updated April 2026:

2025  120.5 bcm/y
2026  122
2027  122
2028  119
2029  114
2030  108
2031  102
2032   97
2033   93
2034   89
2035   85

These national values are used only as an index to scale the 2025 Norwegian
gas contribution relevant to St Fergus.

FIFE NGL PRODUCT SPLIT [7,8]
Representative mass fractions use Shell Fife NGL export data reported to SEPA
for 2018 and 2020:

ETHANE_MASS_SHARE   = 0.2824
PROPANE_MASS_SHARE  = 0.3219
BUTANE_MASS_SHARE   = 0.2296
GASOLINE_MASS_SHARE = 0.1661

2019 and 2021 are excluded because FEP shutdowns made the normal ethane route
unrepresentative.

MODEL ASSUMPTIONS
-----------------

UK TO ST FERGUS
32% of NSTA total UK gross gas is allocated to the St Fergus/northern system.
This is a central screening assumption, not a fixed routing share.

NORWAY AFTER 2035
The gas-specific NOD outlook ends in 2035. From 2036-2063 the model continues
the compound annual decline implied by the 2030-2035 gas profile:

decline = 1 - (85 / 108)^(1/5) = approximately 4.7%/y

This is a model extrapolation, not an NOD forecast.

UK AFTER 2050
NSTA ends in 2050. From 2051-2063, annual UK decline is sampled between
9% and 13%. RANDOM_SEED = 45 makes the result reproducible.
The 9-13% range is a model assumption.

FIFE NGL SCALING
Fife NGL(t) = 2237 x [Relevant gas(t) / Relevant gas(2025)]  kt/y

This assumes average NGL richness, recovery and routing remain sufficiently
similar for proportional scaling to be useful.

PRODUCT SPLIT
The representative 2018/2020 product fractions are held constant through the
forecast. Future changes in gas composition/NGL richness are not modelled.

PROJECT PERIOD
--------------
2028-2063 inclusive.

KEY LIMITATIONS
---------------
- Results represent potential technical availability, not guaranteed supply.
- Norwegian national production is used as a proxy for decline in the specific
  Norwegian fields feeding the relevant St Fergus systems.
- The 2026-2035 Norwegian annual values are rounded readings from an official
  published chart rather than a machine-readable annual table.
- Gas composition, routing, contracts and plant availability may change output.
- Constant NGL yield and product split are screening assumptions.

SOURCES
-------
[1] Fife Council, Shell Fife NGL Annual Operations Report 2024, Appendix C:
https://www.fife.gov.uk/__data/assets/pdf_file/0029/675452/Agenda-and-Papers-Environment,-Transportation-and-Climate-Change-Scrutiny-Committee-of-27-May-2025.pdf

[2] OEUK / Westwood, UK Produced Gas and its Role in Future Security of Supply,
February 2026:
https://oeuk.org.uk/product/uk-produced-gas-and-its-role-in-future-security-of-supply/

[3] NSTA, February 2026 Production and Expenditure Projections:
https://www.nstauthority.co.uk/data-and-insights/insights-and-analysis/production-and-expenditure-projections/

[4] NSTA, Process for Producing NSTA Production Projections, February 2026:
https://www.nstauthority.co.uk/media/vr0ij4ki/process-for-producing-nsta-production-projections-february-2026.pdf

[5] Norwegian Petroleum / Norwegian Offshore Directorate, Production Forecasts:
https://www.norskpetroleum.no/en/production-and-exports/production-forecasts/

[6] Norwegian Petroleum / Norwegian Offshore Directorate, Exports of Oil and Gas,
including "Expected volumes of sales gas from Norwegian fields, 1995-2035":
https://www.norskpetroleum.no/en/production-and-exports/exports-of-oil-and-gas/

[7] SEPA, Shell Fife NGL Plant - Resource Utilisation Systematic Assessment:
https://www.sepa.org.uk/media/594397/fngl-2_5_2-resource_utilisation_redacted.pdf

[8] SEPA, Shell Fife NGL Plant - Plans 2021:
https://www.sepa.org.uk/media/594396/fngl-2_4_7-plans_2021_redacted.pdf
