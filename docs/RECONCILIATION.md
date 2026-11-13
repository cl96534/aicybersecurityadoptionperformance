# Reconciliation: dissertation text vs. this dataset

This file compares `src/analysis.py` run on `data/organizations.csv` (Dissertation Table C3, "Analytical Data set Values Used for Chapters 4 and 5") against the final dissertation file (`Dissertation_lyonsFinal1.docx`, third revision). **Nothing in the dissertation was altered by this repository.**

## What reproduces

| Dissertation item | Reported | Reproduced |
|---|---|---|
| Table 3: AI adoption M, SD | 2.03, 1.34 | yes |
| Table 3: performance and employees | 85.38 (3.72); 282,583.43 (415,088.13) | yes |
| Table 4 / Abstract: Spearman | rho = .101, p = .564 | yes |
| Table 4 / Abstract: Pearson | r = .055, p = .753 | yes |
| Table 5: all coefficients, SEs, p-values | e.g. AI B = 0.471, p = .363 | yes (to rounding, see below) |
| Table 5 and Chapter 4/5 text: model fit | R² = .455, adj. R² = .258, F(9,25) = 2.316, p = .047 | yes |

## What still needs a fix in the dissertation

| Location | Printed | Should be (Table 5 / this dataset) |
|---|---|---|
| Abstract: AI adoption coefficient | B = 0.471, **p = 0.471** | B = 0.471, p = .363 |
| Abstract and Appendix C narrative: F | F(9, 25) = **2.3167** | 2.316 (Table 5 prints 2.316; the exact value is 2.3164) |

The regression R² (.455), adjusted R² (.258) and model p (.047) now agree everywhere. Appendix C also gives AI adoption p = .363, which agrees with Table 5. The abstract's p = 0.471 appears to be left over from an earlier model run.

## Other inconsistencies

1. **Appendix A is an earlier version of the data.** It differs from Table C3 in 18 AI-adoption scores and in several employee counts (for example CVS 300,000+ vs 219,000; FedEx 452,000 vs 530,000). It also lists Apple as Level 2, while Chapter 4's coding example and Table C2 give Level 1. This repo treats Table C3 as authoritative because it matches Table 5 and is labelled as the analytic dataset. `data/appendix_a_version.csv` is kept for transparency.
2. **Rounding.** The published tables appear to use performance scores already rounded to two decimals. `analysis.py` uses unrounded `UpGuard / 950 * 100`, causing differences of up to about 0.005 in some coefficients (e.g. AI B = 0.472 vs 0.471). Tests allow a 0.01 tolerance.
3. **Date of UpGuard observations.** Table 3's note says 33 of 35 UpGuard observations are dated after July 2026, but no observation dates are stored in the dataset and no dated screenshot was retained.
4. **Placeholders.** Chapter 3 and Appendix D contain `[INSERT VERIFIED PUBLIC GITHUB REPOSITORY URL]` and need the final repository URL.
