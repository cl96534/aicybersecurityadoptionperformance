# AI-Related Cybersecurity Adoption Rubric

Researcher-developed, based on concepts from the NIST Cybersecurity Framework 2.0 (Pascoe et al., 2024) and the NIST AI Risk Management Framework (Tabassi, 2023). One score (1-5) is assigned per organization from publicly available evidence.

| Level | Classification | Decision rule |
|---|---|---|
| 1 | No Adoption | No publicly available evidence that AI or machine learning is used for cybersecurity purposes. |
| 2 | Emerging Adoption | AI-related cybersecurity is discussed, planned, evaluated, governed or considered, but operational implementation is not clearly documented. |
| 3 | Moderate Adoption | AI/ML is operationally implemented in one or more specific cybersecurity functions (e.g., threat or anomaly detection, monitoring, alert prioritization, threat intelligence, incident-response support). |
| 4 | Advanced Adoption | AI/ML is integrated into multiple core cybersecurity functions or an organizational cybersecurity-AI capability. |
| 5 | Integrated Adoption | AI/ML is extensively integrated across multiple cybersecurity functions, with broad operational use and/or governance, measured outcomes, assurance or comparable enterprise evidence. |

## Coding rules

1. Assign the **lower fully supported level** when evidence does not establish the next level.
2. Planning or discussion alone is not operational deployment.
3. One documented use case is not integration across multiple functions.
4. Customer-facing product marketing, security *of* AI workloads, general AI governance, and AI-related cyber-risk disclosures are **not** evidence of internal AI-*for*-cybersecurity use.
5. Record the source, the specific evidence, the criterion satisfied and the rationale for every score (`data/coding_audit_trail.csv`).
6. Coding was done by one researcher; replication should use at least two independent raters and report an agreement statistic (e.g., Cohen's kappa).

## Data-collection instrument (Appendix B)

For each organization record: ID, name, industry, employee count, collection date; AI-adoption score with evidence; UpGuard rating (0-950) and converted 0-100 score; source citation/URL, access date and verification notes; verification status; missing or ambiguous information.
