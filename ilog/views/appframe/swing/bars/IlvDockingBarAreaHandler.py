DOCKING_MANAGER_PROPERTY = "String  \"DockingManager\""
MENU_TYPE = "String  \"menu\""
TOOLBAR_TYPE = "String  \"toolbar\""
def ():
    '''returns IlvDockingBarAreaHandler\n\n
    (final Container a)\n
    '''
def getComponent():
    '''returns Component\n\n
    getComponent(final String s)\n
    '''
def isComponentExtensible():
    '''returns boolean\n\n
    isComponentExtensible(final String s)\n
    '''
def isComponentDockable():
    '''returns boolean\n\n
    isComponentDockable(final String s)\n
    '''
def setComponentDockingProperties():
    '''returns None\n\n
    setComponentDockingProperties(final String s, final boolean b)\n
    setComponentDockingProperties(final Component component, final boolean b)\n
    '''
def setComponentOrientation():
    '''returns None\n\n
    setComponentOrientation(final String s, final boolean b)\n
    setComponentOrientation(final Component component, final boolean b)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication b)\n
    '''
def isBarVisible():
    '''returns boolean\n\n
    isBarVisible(final String s)\n
    '''
def getBarVisibilityActionHandler():
    '''returns IlvComponentVisibilityActionHandler\n\n
    getBarVisibilityActionHandler(final String s, final String s2)\n
    '''
def setCurrentWorkspace():
    '''returns None\n\n
    setCurrentWorkspace(final IlvBarWorkspace e)\n
    setCurrentWorkspace(final String s)\n
    '''
def startDragging():
    '''returns boolean\n\n
    startDragging()\n
    '''
def hideFloatingWindow():
    '''returns None\n\n
    hideFloatingWindow(final String s)\n
    '''
def setParentFrame():
    '''returns None\n\n
    setParentFrame(final Frame j)\n
    '''
def getParentFrame():
    '''returns Frame\n\n
    getParentFrame()\n
    '''
def getFloatingWindowCount():
    '''returns int\n\n
    getFloatingWindowCount()\n
    '''
def getFloatableWindow():
    '''returns Container\n\n
    getFloatableWindow(final int index)\n
    '''
def register():
    '''returns None\n\n
    register(final JComponent component)\n
    '''
def unregister():
    '''returns None\n\n
    unregister(final JComponent component)\n
    '''
def getWorkspaceConfiguration():
    '''returns String\n\n
    getWorkspaceConfiguration()\n
    '''
def hasWorkspace():
    '''returns boolean\n\n
    hasWorkspace(final String key)\n
    '''
def getWorkspace():
    '''returns IlvBarWorkspace\n\n
    getWorkspace(final String key)\n
    '''
def getCurrentWorkspace():
    '''returns IlvBarWorkspace\n\n
    getCurrentWorkspace()\n
    '''
def applyWorkspace():
    '''returns None\n\n
    applyWorkspace(final String s)\n
    '''
def getBarComponents():
    '''returns JComponent[]\n\n
    getBarComponents()\n
    '''
def getBar():
    '''returns JComponent\n\n
    getBar(final String key)\n
    '''
def createBar():
    '''returns JComponent\n\n
    createBar(final String s, final String s2)\n
    '''
def isBarExtensible():
    '''returns boolean\n\n
    isBarExtensible(final String s)\n
    '''
def isBarDockable():
    '''returns boolean\n\n
    isBarDockable(final String s)\n
    '''
def ensureBarStyle():
    '''returns IlvBarStyle\n\n
    ensureBarStyle(final String s, final String barType)\n
    '''
def registerBar():
    '''returns None\n\n
    registerBar(final String key, final JComponent value, final boolean dockable, final boolean extensible, final String title)\n
    '''
def getClientContainer():
    '''returns Container\n\n
    getClientContainer()\n
    '''
def setClientContainer():
    '''returns None\n\n
    setClientContainer(final Container container)\n
    '''
def readSettings():
    '''returns None\n\n
    readSettings(final IlvSettingsElement ilvSettingsElement)\n
    '''
def applyExtension():
    '''returns None\n\n
    applyExtension(final IlvConfigurationExtension ilvConfigurationExtension, final boolean b)\n
    '''
def writeSettings():
    '''returns None\n\n
    writeSettings(final IlvSettingsElement ilvSettingsElement)\n
    '''
