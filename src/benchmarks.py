# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from core import perf_benchmark

from measurements import smoothness
from .pagesets import TheGuardianSmoothPageSet


class SmoothnessTheGuardian(perf_benchmark.PerfBenchmark):
  """Measures rendering statistics while scrolling down theguardian.com.

  http://www.chromium.org/developers/design-documents/rendering-benchmarks
  """
  test = smoothness.Smoothness
  page_set = TheGuardianSmoothPageSet

  @classmethod
  def Name(cls):
    return 'smoothness.the_guardian'

