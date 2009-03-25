#
#  OggifyOSXAppDelegate.py
#  OggifyOSX
#
#  Created by Scott Robertson on 3/24/09.
#  Copyright __MyCompanyName__ 2009. All rights reserved.
#

from Foundation import *
from AppKit import *

class OggifyOSXAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
