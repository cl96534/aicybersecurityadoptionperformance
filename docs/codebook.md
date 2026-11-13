# Codebook

## `data/organizations.csv`

| Column | Type | Description |
|---|---|---|
| `org_id` | string | Identifier `O01`-`O35`, in the order of Dissertation Table C3 |
| `organization` | string | Organization name |
| `industry` | categorical | Aerospace & Defense, Automotive, Financial Services, Healthcare, Retail, Technology, Telecommunications, Transportation & Logistics. Aerospace & Defense is the reference category in the regression |
| `ai_adoption_1_to_5` | ordinal 1-5 | Organizational AI-Related Cybersecurity Adoption Scale (see `rubric.md`). Audited score |
| `employees` | integer | Most recent publicly reported employee count |
| `upguard_rating_0_to_950` | integer | UpGuard security rating on its native scale |
| `cybersecurity_performance_0_to_100` | float | `(upguard_rating / 950) * 100`, rounded to 2 decimals as published. `analysis.py` recomputes it unrounded |

## `data/coding_audit_trail.csv`

| Column | Description |
|---|---|
| `org_id`, `organization` | Link to `organizations.csv` |
| `prior_score` | Score before the re-audit (Table C2 "Prior score") |
| `audited_score` | Score after applying the rubric; equals `ai_adoption_1_to_5` |
| `evidence_excerpt` | Quoted evidence supporting the score |
| `primary_source_url` | Source of the excerpt |
| `additional_evidence` | Further source or audit observation, where present |
| `coding_rationale` | Why the assigned level was chosen over the next level |

## `data/appendix_a_version.csv`

The earlier table printed in Dissertation Appendix A (employee counts as reported, including values such as `390,000+`). It differs from the final dataset in 18 AI scores and several employee counts; see `RECONCILIATION.md`. It is not used by `analysis.py`.
