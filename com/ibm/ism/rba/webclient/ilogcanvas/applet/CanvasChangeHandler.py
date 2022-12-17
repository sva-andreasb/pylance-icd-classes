WF_NOOP = "int  0"
WF_MVNODE = "int  1"
WF_DELLINK = "int  2"
WF_ADDNODE = "int  5"
WF_ADDLINK = "int  8"
WF_DELNODE = "int  18"
WF_MVLINK = "int  10"
def ():
    '''returns CanvasChangeHandler\n\n
    (final ILOGCanvasApplet applet)\n
    '''
def contentsChanged():
    '''returns None\n\n
    contentsChanged(final ManagerContentChangedEvent event)\n
    '''
def commitChangeToServer():
    '''returns None\n\n
    commitChangeToServer()\n
    '''
def sendStructureChangeEvent():
    '''returns String\n\n
    sendStructureChangeEvent(final String eventType, final Hashtable<String, String> values)\n
    '''
def getMoveNodeCount():
    '''returns int\n\n
    getMoveNodeCount()\n
    '''
