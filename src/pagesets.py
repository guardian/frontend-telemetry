# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
from telemetry.page import page as page_module
from telemetry.page import shared_page_state
from telemetry import story

from page_sets import top_pages


def _IssueMarkerAndScroll(action_runner):
  with action_runner.CreateGestureInteraction('ScrollAction'):
    action_runner.ScrollPage()


class SmoothPage(page_module.Page):

  def __init__(self, url, page_set, name='', credentials=None):
    super(SmoothPage, self).__init__(
        url=url, page_set=page_set, name=name,
        shared_page_state_class=shared_page_state.SharedDesktopPageState)
    self.credentials = credentials

  def RunPageInteractions(self, action_runner):
    _IssueMarkerAndScroll(action_runner)


class TheGuardianSmoothPageSet(story.StorySet):
  def __init__(self):
    super(TheGuardianSmoothPageSet, self).__init__()

    desktop_state_class = shared_page_state.SharedDesktopPageState

    self.AddStory(SmoothPage('http://theguardian.com', self))
