#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright Š 2010 alexliyu email:alexliyu2012@gmail.com
# This file is part of CDM SYSTEM.
#
# CDM SYSTEM is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 0.3 of the License, or (at your option) any later
# version. WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# CDM SYSTEM. If not, see <http://www.gnu.org/licenses/>.
#  Copyright Š 2010 alexliyu email:alexliyu2012@gmail.com

from cdm_plugin import *
from model import *
from google.appengine.api import urlfetch
from app import htmllib
from app.htmllib import HTMLStripper
from datetime import datetime, timedelta
from google.appengine.ext import webapp
from google.appengine.api.urlfetch_errors import DownloadError
from feedmodel import FeedList, FeedsList, AddmemFeed, Tempimages
import feedparser
from google.appengine.runtime import DeadlineExceededError
from time import sleep
from base import *
from app.htmllib import getImageInfo

class FetchImages(BaseRequestHandler):

		def __init__(self):
				BaseRequestHandler.__init__(self)
				self.current = "fetchimages"


		
