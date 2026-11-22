# Package scripts

Scripts in this directory must be deterministic, safe to rerun, and scoped to the package. They should validate or produce an auditable artifact rather than hide workflow decisions in shell code.

The structural validator is `validate-structure.sh`.
The completed-module link and ID checker is `validate-module-delivery.py <docs/modules/module>`; it does not judge requirement meaning or code behavior.
The derived requirement/test/work summary is `report-module-coverage.py <docs/modules/module>`; review the generated `05-verification/completion-report.md` against actual verification evidence before using its counts.
