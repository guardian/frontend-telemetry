# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
from telemetry.page import page as page_module
from telemetry.page import page_set as page_set_module


class GuPage(page_module.Page):

  def __init__(self, url, page_set, run_no_page_interactions):
    super(GuPage, self).__init__(url=url, page_set=page_set)
    self.user_agent_type = 'desktop'
    self.archive_data_file = 'data/gu.json'
    self._run_no_page_interactions = run_no_page_interactions

  def RunPageInteractions(self, action_runner):
    if self._run_no_page_interactions:
      return
    interaction = action_runner.BeginGestureInteraction(
        'ScrollAction', is_smooth=True)
    action_runner.ScrollPage()
    interaction.End()

class GuContentPageSet(page_set_module.PageSet):

  """ Pages designed to represent the median, not highly optimized web """

  def __init__(self, make_pages_with_no_interactions=False):
    super(GuContentPageSet, self).__init__(
      user_agent_type='desktop',
      archive_data_file='data/gu.json',
      bucket=page_set_module.PARTNER_BUCKET)

    urls_list = [
      'http://www.theguardian.com/business/2015/feb/09/margaret-hodge-accuses-ex-chairman-lord-stephen-green-over-hsbc-files',
      'http://www.theguardian.com/news/live/2015/feb/09/hsbc-files-global-reaction',
      'http://www.theguardian.com/news/video/2015/feb/09/lord-stephen-green-hsbc-files-video'
    ]

    for url in urls_list:
      self.AddUserStory(
        GuPage(url, self, make_pages_with_no_interactions))



class GuFrontsPageSet(page_set_module.PageSet):

  """ Pages designed to represent the median, not highly optimized web """

  def __init__(self, make_pages_with_no_interactions=False):
    super(GuFrontsPageSet, self).__init__(
      user_agent_type='desktop',
      archive_data_file='data/gu.json',
      bucket=page_set_module.PARTNER_BUCKET)

    urls_list = [
      'http://www.theguardian.com/uk'
      #'http://www.theguardian.com/video'
    ]

    for url in urls_list:
      self.AddUserStory(
        GuPage(url, self, make_pages_with_no_interactions))
