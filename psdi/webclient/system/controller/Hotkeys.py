IDX_KEYCODE = "int  0"
IDX_CTRL = "int  1"
IDX_ALT = "int  2"
IDX_TARGET = "int  3"
IDX_EVENT = "int  4"
IDX_CHAR = "int  5"
def Hotkeys():
    '''    public Hotkeys()
    '''
def reset():
    '''    public void reset()
    '''
def addHotkey():
    '''    public String addHotkey(final WebClientSession wcs, String hotkey, final String target, final String eventname)
    '''
def localize():
    '''    public String localize(final WebClientSession wcs, String hotkey)
    '''
def getKeycodes():
    '''    public Set<Integer> getKeycodes()
    '''
def getHotkeysForKeycode():
    '''    public List<List<Object>> getHotkeysForKeycode(final int keycode)
    '''
def getCtrlState():
    '''    public boolean getCtrlState(final String hotkey)
    '''
def getAltState():
    '''    public boolean getAltState(final String hotkey)
    '''
def getAccessKey():
    '''    public char getAccessKey(final String hotkey)
    '''
