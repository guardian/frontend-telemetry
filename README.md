1. Download Telemetry from https://www.chromium.org/developers/telemetry/run_locally
2. Unzip and copy the `telemetry` directory to this directory

```
./run_benchmark --browser=canary smoothness.the_guardian --output-format=json --output-dir=./results
```

For more info:

```
./run_benchmark help run
```

General info about smoothness benchmarks: https://www.chromium.org/developers/design-documents/rendering-benchmarks
