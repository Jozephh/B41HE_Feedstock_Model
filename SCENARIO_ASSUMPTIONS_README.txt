FIFE NGL FEEDSTOCK MODEL - ASSUMPTIONS
=======================================

Scope
-----
Scenario-specific assumptions only. Baseline Fife NGL throughput, product split,
Norwegian supply and other baseline inputs are documented separately.

Scenarios
---------
1. NSTA Reference
2. Rosebank + Jackdaw
3. Max Drilling (OEUK Upside)

All scenarios are identical through 2026 and diverge from 2027.
Project outputs are assessed over 2028-2063.

1. NSTA Reference
-----------------
Uses the baseline NSTA February 2026 UK gas-production projection with no
additional scenario uplift.

2. Rosebank + Jackdaw
---------------------
Published field gas-production profiles are added to the NSTA Reference.

Jackdaw:
- Published P50 profile: 2024-2032, kSm3/day.
- Model shift: +3 years -> contribution from 2027-2035.
- Conversion: bcm/y = kSm3/day x 365 / 1,000,000.

Rosebank:
- Published profile: 2026-2051, MMSm3/day.
- Model shift: +1 year -> contribution from 2027-2052.
- Conversion: bcm/y = MMSm3/day x 365 / 1,000.
- No production is extrapolated beyond the shifted published profile.

The timing shifts are model assumptions used to preserve the common 2026 start.
Named-field production is treated as relevant to the St Fergus/Fife supply chain.

3. Max Drilling (OEUK Upside)
-----------------------------
Based on OEUK/Westwood's published "Upside Potential" case for total UK gas production.

Source inputs:
- 2030 OEUK Upside = 26.588 bcm/y.
- 2035 OEUK Upside = 26.180 bcm/y.
- 2025-2050 cumulative OEUK Upside = 456 bcm.

Because a complete annual OEUK series is not published, the model uses:
- 2025-2026: same as NSTA.
- 2027-2030: linear interpolation to 26.588 bcm/y.
- 2031-2035: linear interpolation to 26.180 bcm/y.
- 2036-2050: exponential decline fitted so 2025-2050 totals 456 bcm.
- 2051-2063: continuation of the calculated decline.

OEUK values are total UK production. The baseline UK-to-St-Fergus allocation
(32%) is applied before adding the baseline Norwegian contribution.

Max Drilling is the upper development sensitivity:
    G_Max,t = max(G_OEUK_case,t, G_Rosebank+Jackdaw,t)

This ordering rule is a model assumption. Rosebank and Jackdaw are not added
separately to OEUK Upside, avoiding potential double counting.

Sources
-------
[1] NSTA, February 2026 Production and Expenditure Projections:
https://www.nstauthority.co.uk/data-and-insights/insights-and-analysis/production-and-expenditure-projections/

[2] NSTA, Process for Producing NSTA Production Projections (February 2026):
https://www.nstauthority.co.uk/media/vr0ij4ki/process-for-producing-nsta-production-projections-february-2026.pdf

[3] OEUK / Westwood Global Energy Group, "UK Produced Gas and its Role in
Future Security of Supply", February 2026:
https://oeuk.org.uk/wp-content/uploads/woocommerce_uploads/2026/02/OEUK-UK-Produced-gas-and-its-role-in-security-of-energy-supply-February-2026-yfdscn.pdf

[4] UK Government / OPRED, Jackdaw Field Development:
https://www.gov.uk/government/publications/jackdaw-field-development

[5] Jackdaw Field Development Environmental Statement:
https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/983810/Jackdaw_Project_Environmental_Statement_D.4260.2021.pdf

[6] UK Government / OPRED, Rosebank Field Development:
https://www.gov.uk/government/publications/rosebank-field-development

[7] Rosebank Environmental Statement:
https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1097880/Rosebank_Environmental_Statement_-_Final_for_Submission_To_OPRED_Equinor_3rd_August_2022.pdf