DOCKING_FIRST = "int  100"
DOCKABLE_PANE_ACTIVATED = "int  100"
DOCKABLE_PANE_DEACTIVATED = "int  101"
DOCKABLE_PANE_HIDDEN = "int  102"
DOCKABLE_PANE_SHOWN = "int  103"
DOCKABLE_PANE_DOCKED = "int  104"
DOCKABLE_PANE_UNDOCKED = "int  105"
DOCKABLE_PANE_MOVED = "int  106"
WORKSPACE_ADDED = "int  107"
WORKSPACE_REMOVED = "int  108"
WORKSPACE_ACTIVATED = "int  109"
WORKSPACE_DEACTIVATED = "int  110"
WORKSPACE_REINITIALIZED = "int  111"
DOCKING_AREA_INITIALIZED = "int  112"
DOCKING_LAST = "int  112"
def ():
    '''returns DockingEvent\n\n
    (final int b, final String source)\n
    (final int b, final String[] array)\n
    '''
def getID():
    '''returns int\n\n
    getID()\n
    '''
def getDockableName():
    '''returns String\n\n
    getDockableName()\n
    '''
def getDockableNames():
    '''returns String[]\n\n
    getDockableNames()\n
    '''
def getDockableCount():
    '''returns int\n\n
    getDockableCount()\n
    '''
def getFloatingLocation():
    '''returns Point\n\n
    getFloatingLocation()\n
    '''
def isDocked():
    '''returns boolean\n\n
    isDocked()\n
    '''
def isUndocked():
    '''returns boolean\n\n
    isUndocked()\n
    '''
def getOppositeDockableName():
    '''returns String\n\n
    getOppositeDockableName()\n
    '''
def getWorkspaceName():
    '''returns String\n\n
    getWorkspaceName()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
