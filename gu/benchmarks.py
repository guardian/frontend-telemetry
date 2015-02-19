# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import pagesets
from measurements import guperf
from telemetry import benchmark

class FrontsAll(benchmark.Benchmark):
  test = guperf.All
  page_set = pagesets.GuFrontsPageSet

  @classmethod
  def Name(cls):
    return 'gu.FrontsAll'

class ContentAll(benchmark.Benchmark):
  test = guperf.All
  page_set = pagesets.GuContentPageSet

  @classmethod
  def Name(cls):
    return 'gu.ContentAll'
