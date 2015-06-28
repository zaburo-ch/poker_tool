from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from AppKit import NSApplication, NSApp, NSWorkspace ,NSRunningApplication
import time

def print_window_list():
  options = kCGWindowListOptionOnScreenOnly
  windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)

  for window in windowList:
    print
    print window.isActive()
    for key in window:
      print key,window[key]
def print_active_app():
  workspace = NSWorkspace.sharedWorkspace()
  activeApps = workspace.runningApplications()
  activeApp = None
  for app in activeApps:
    if app.isActive():
      activeApp = app
      break
  print activeApp.localizedName(),activeApp.isActive()

