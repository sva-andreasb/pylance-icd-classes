def getName():
    '''returns String\n\n
    getName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getActiveEventListeners():
    '''returns Map\n\n
    getActiveEventListeners()\n
    '''
def getRegisteredMbosForPackage():
    '''returns List\n\n
    getRegisteredMbosForPackage(final String pkgDefName, final String source)\n
    '''
def getPersonsForPackage():
    '''returns List\n\n
    getPersonsForPackage(final String pkgDefName, final String source)\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def unregisterEventListenerForPackage():
    '''returns None\n\n
    unregisterEventListenerForPackage(final String pkgDefName, final String source, final boolean remove)\n
    '''
def unregisterAllEventListeners():
    '''returns None\n\n
    unregisterAllEventListeners()\n
    '''
def registerListnersForMbosInPkg():
    '''returns None\n\n
    registerListnersForMbosInPkg(final String pkgDefName, final String source)\n
    '''
def registerListenersForPackage():
    '''returns None\n\n
    registerListenersForPackage(final MboRemote pkgDef)\n
    '''
def loadActiveChangePkgListeners():
    '''returns None\n\n
    loadActiveChangePkgListeners()\n
    '''
def loadAllGroupsForPkg():
    '''returns None\n\n
    loadAllGroupsForPkg(final MboRemote pkgDef)\n
    '''
def loadPersonsForPkg():
    '''returns None\n\n
    loadPersonsForPkg(final MboRemote pkgDef)\n
    '''
def loadAllCfgObjsForPkg():
    '''returns None\n\n
    loadAllCfgObjsForPkg(final String pkgDefName, final String source, final List grpV, final UserInfo ui)\n
    '''
def getPkgDefForNameAndSource():
    '''returns MboRemote\n\n
    getPkgDefForNameAndSource(final String pkgDefName, final String source)\n
    '''
