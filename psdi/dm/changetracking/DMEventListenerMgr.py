def getName():
    '''public String getName()
    '''
def init():
    '''public void init()
    '''
def getActiveEventListeners():
    '''public Map getActiveEventListeners()
    '''
def getRegisteredMbosForPackage():
    '''public List getRegisteredMbosForPackage(final String pkgDefName, final String source)
    '''
def getPersonsForPackage():
    '''public List getPersonsForPackage(final String pkgDefName, final String source)
    '''
def reload():
    '''public void reload()
    public void reload(final String key)
    '''
def unregisterEventListenerForPackage():
    '''public void unregisterEventListenerForPackage(final String pkgDefName, final String source, final boolean remove)
    '''
def unregisterAllEventListeners():
    '''public void unregisterAllEventListeners()
    '''
def registerListnersForMbosInPkg():
    '''public void registerListnersForMbosInPkg(final String pkgDefName, final String source)
    '''
def registerListenersForPackage():
    '''public void registerListenersForPackage(final MboRemote pkgDef)
    '''
def loadActiveChangePkgListeners():
    '''public void loadActiveChangePkgListeners()
    '''
def loadAllGroupsForPkg():
    '''public void loadAllGroupsForPkg(final MboRemote pkgDef)
    '''
def loadPersonsForPkg():
    '''public void loadPersonsForPkg(final MboRemote pkgDef)
    '''
def loadAllCfgObjsForPkg():
    '''public void loadAllCfgObjsForPkg(final String pkgDefName, final String source, final List grpV, final UserInfo ui)
    '''
def getPkgDefForNameAndSource():
    '''public MboRemote getPkgDefForNameAndSource(final String pkgDefName, final String source)
    '''
