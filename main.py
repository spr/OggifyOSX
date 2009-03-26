#
#  main.py
#  OggifyOSX
#
#  Created by Scott Robertson on 3/24/09.
#  Copyright __MyCompanyName__ 2009. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import OggifyOSXAppDelegate
import mutagen
import tag_wrapper
import oggify

# pass control to AppKit
AppHelper.runEventLoop()
