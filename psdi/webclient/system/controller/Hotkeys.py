IDX_KEYCODE = "int  0"
IDX_CTRL = "int  1"
IDX_ALT = "int  2"
IDX_TARGET = "int  3"
IDX_EVENT = "int  4"
IDX_CHAR = "int  5"
def Hotkeys():
'''public Hotkeys()
'''
pass
def reset():
'''public void reset()
'''
pass
def addHotkey():
'''public String addHotkey(final WebClientSession wcs, String hotkey, final String target, final String eventname)
'''
pass
def localize():
'''public String localize(final WebClientSession wcs, String hotkey)
'''
pass
def getKeycodes():
'''public Set<Integer> getKeycodes()
'''
pass
def getHotkeysForKeycode():
'''public List<List<Object>> getHotkeysForKeycode(final int keycode)
'''
pass
def getCtrlState():
'''public boolean getCtrlState(final String hotkey)
'''
pass
def getAltState():
'''public boolean getAltState(final String hotkey)
'''
pass
def getAccessKey():
'''public char getAccessKey(final String hotkey)
'''
pass
