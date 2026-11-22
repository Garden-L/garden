# Completed module example: speed signal

This is an illustrative local Python model, not deployable vehicle software. It demonstrates how a module's source, SRS, STS, issue decision, bounded work, code, test results, and final handoff connect. The [module index](docs/modules/speed-signal/README.md) is the final entry point.

Run the example from this directory:

```sh
python3 -m unittest discover -s tests -v
python3 ../../scripts/report-module-coverage.py docs/modules/speed-signal
python3 ../../scripts/validate-module-delivery.py docs/modules/speed-signal
```

The example's required verification environment is this local Python model. ECU, HIL, vehicle, safety, and release claims are outside its scope. The documents name those limits explicitly.

The [skill-to-output audit](skill-audit.md) maps each applied skill to this example's artifacts and names the gates that were not exercised.
