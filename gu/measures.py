# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from metrics import power
from metrics import cpu
from metrics import media
from metrics import memory
from measurements import smoothness_controller
from telemetry.page import page_test


class All(page_test.PageTest):
  def __init__(self):
    super(All, self).__init__('RunPageInteractions')
    self._smoothness_controller = None

    self._power_metric = None
    self._cpu_metric = None
    self._memory_metric = None

  @classmethod
  def CustomizeBrowserOptions(cls, options):
    options.AppendExtraBrowserArgs('--enable-gpu-benchmarking')
    options.AppendExtraBrowserArgs('--touch-events=enabled')
    options.AppendExtraBrowserArgs('--running-performance-benchmark')
    options.AppendExtraBrowserArgs('--memory-metrics')
    power.PowerMetric.CustomizeBrowserOptions(options)
    memory.MemoryMetric.CustomizeBrowserOptions(options)

  def WillStartBrowser(self, platform):
    self._power_metric = power.PowerMetric(platform)

  def DidStartBrowser(self, browser):
    self._memory_metric = memory.MemoryMetric(browser)


  def WillNavigateToPage(self, page, tab):
    self._power_metric.Start(page, tab)
    self._memory_metric.Start(page, tab)

    self._smoothness_controller = smoothness_controller.SmoothnessController()
    self._smoothness_controller.SetUp(page, tab)

    self._cpu_metric = cpu.CpuMetric(tab.browser)
    self._cpu_metric.Start(page, tab)

  def WillRunActions(self, page, tab):
    self._smoothness_controller.Start(tab)

  def DidRunActions(self, page, tab):
    self._power_metric.Stop(page, tab)
    self._cpu_metric.Stop(page, tab)
    self._memory_metric.Stop(page, tab)
    self._smoothness_controller.Stop(tab)

  def ValidateAndMeasurePage(self, page, tab, results):
    self._power_metric.AddResults(tab, results)
    self._smoothness_controller.AddResults(tab, results)
    self._cpu_metric.AddResults(tab, results)
    self._memory_metric.AddResults(tab, results)

  def CleanUpAfterPage(self, page, tab):
    if self._power_metric:          self._power_metric.Stop(page, tab)
    if self._smoothness_controller: self._smoothness_controller.CleanUp(tab)
