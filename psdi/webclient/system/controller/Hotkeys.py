IDX_KEYCODE = "int  0"
IDX_CTRL = "int  1"
IDX_ALT = "int  2"
IDX_TARGET = "int  3"
IDX_EVENT = "int  4"
IDX_CHAR = "int  5"
def ():
    '''returns Hotkeys\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def addHotkey():
    '''returns String\n\n
    addHotkey(final WebClientSession wcs, String hotkey, final String target, final String eventname)\n
    '''
def localize():
    '''returns String\n\n
    localize(final WebClientSession wcs, String hotkey)\n
    '''
def getKeycodes():
    '''returns Set<Integer>\n\n
    getKeycodes()\n
    '''
def getHotkeysForKeycode():
    '''returns List<List<Object>>\n\n
    getHotkeysForKeycode(final int keycode)\n
    '''
def getCtrlState():
    '''returns boolean\n\n
    getCtrlState(final String hotkey)\n
    '''
def getAltState():
    '''returns boolean\n\n
    getAltState(final String hotkey)\n
    '''
def getAccessKey():
    '''returns char\n\n
    getAccessKey(final String hotkey)\n
    '''
