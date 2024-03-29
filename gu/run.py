#!/usr/bin/env python
# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'telemetry/src/tools/telemetry'))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'telemetry/src/tools/perf'))

from telemetry import benchmark_runner
from telemetry.core import environment

if __name__ == '__main__':
  base_dir = os.path.dirname(os.path.realpath(__file__))
  benchmark_runner.config = environment.Environment([base_dir])
  sys.exit(benchmark_runner.main())
