MENU_TYPE = "String  \"menu\""
TOOLBAR_TYPE = "String  \"toolbar\""
def ():
    '''returns IlvDockingBarArea\n\n
    ()\n
    '''
def getUIClassID():
    '''returns String\n\n
    getUIClassID()\n
    '''
def getClientContainer():
    '''returns Container\n\n
    getClientContainer()\n
    '''
def setClientContainer():
    '''returns None\n\n
    setClientContainer(final Container clientContainer)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication application)\n
    '''
def setConfiguration():
    '''returns None\n\n
    setConfiguration(final String s)\n
    '''
def getConfiguration():
    '''returns String\n\n
    getConfiguration()\n
    '''
def getBar():
    '''returns JComponent\n\n
    getBar(final String s)\n
    '''
def createBar():
    '''returns JComponent\n\n
    createBar(final String s, final String s2)\n
    '''
def getDockingInfo():
    '''returns DockingBarInfo\n\n
    getDockingInfo(final String s)\n
    '''
def registerBar():
    '''returns None\n\n
    registerBar(final String s, final JComponent component, final boolean b, final boolean b2, final String s2)\n
    '''
def dock():
    '''returns DockingBarInfo\n\n
    dock(final String s, final int n)\n
    '''
def undock():
    '''returns DockingBarInfo\n\n
    undock(final String s, final Point point)\n
    '''
def setBarVisible():
    '''returns DockingBarInfo\n\n
    setBarVisible(final String s, final boolean b)\n
    '''
def isBarVisible():
    '''returns boolean\n\n
    isBarVisible(final String s)\n
    '''
def isBarExtensible():
    '''returns boolean\n\n
    isBarExtensible(final String s)\n
    '''
def getBarVisibilityActionHandler():
    '''returns IlvComponentVisibilityActionHandler\n\n
    getBarVisibilityActionHandler(final String s, final String s2)\n
    '''
def isBarDockable():
    '''returns boolean\n\n
    isBarDockable(final String s)\n
    '''
def addNotify():
    '''returns None\n\n
    addNotify()\n
    '''
def getBarComponents():
    '''returns JComponent[]\n\n
    getBarComponents()\n
    '''
def hierarchyChanged():
    '''returns None\n\n
    hierarchyChanged(final HierarchyEvent hierarchyEvent)\n
    '''
def componentResized():
    '''returns None\n\n
    componentResized(final ComponentEvent componentEvent)\n
    '''
def componentMoved():
    '''returns None\n\n
    componentMoved(final ComponentEvent componentEvent)\n
    '''
def componentShown():
    '''returns None\n\n
    componentShown(final ComponentEvent componentEvent)\n
    '''
def componentHidden():
    '''returns None\n\n
    componentHidden(final ComponentEvent componentEvent)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
