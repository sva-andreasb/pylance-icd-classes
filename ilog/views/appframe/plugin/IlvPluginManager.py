INSTALL_BY_DEFAULT = "String  \"installByDefault\""
NOT_INSTALL_BY_DEFAULT = "String  \"notInstallByDefault\""
NEVER_INSTALL_BY_DEFAULT = "String  \"neverInstallByDefault\""
def ():
    '''returns JarLibrary\n\n
    ()\n
    (final URL url)\n
    (final URL a)\n
    (final URL url)\n
    '''
def readSettings():
    '''returns None\n\n
    readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    '''
def writeSettings():
    '''returns None\n\n
    writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication c)\n
    '''
def applicationInitializingSettings():
    '''returns None\n\n
    applicationInitializingSettings(final ApplicationEvent applicationEvent)\n
    '''
def applicationInitialized():
    '''returns None\n\n
    applicationInitialized(final ApplicationEvent applicationEvent)\n
    '''
def mainWindowInitialized():
    '''returns None\n\n
    mainWindowInitialized(final ApplicationEvent applicationEvent)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setRootURL():
    '''returns None\n\n
    setRootURL(final URL url)\n
    '''
def getRootURL():
    '''returns URL\n\n
    getRootURL()\n
    getRootURL(final int index)\n
    '''
def addRootURL():
    '''returns None\n\n
    addRootURL(final URL e)\n
    '''
def getRootURLCount():
    '''returns int\n\n
    getRootURLCount()\n
    '''
def setRootDirectory():
    '''returns None\n\n
    setRootDirectory(final File file)\n
    '''
def getRootDirectory():
    '''returns File\n\n
    getRootDirectory()\n
    getRootDirectory(final int n)\n
    '''
def addRootDirectory():
    '''returns None\n\n
    addRootDirectory(final File file)\n
    '''
def getRootDirectoryCount():
    '''returns int\n\n
    getRootDirectoryCount()\n
    '''
def readPlugins():
    '''returns None\n\n
    readPlugins()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File file)\n
    '''
def isInstalled():
    '''returns boolean\n\n
    isInstalled()\n
    '''
def uninstallPlugins():
    '''returns None\n\n
    uninstallPlugins()\n
    '''
def installPlugin():
    '''returns boolean\n\n
    installPlugin(final IlvPlugin ilvPlugin)\n
    '''
def uninstallPlugin():
    '''returns boolean\n\n
    uninstallPlugin(final IlvPlugin ilvPlugin, final boolean b)\n
    '''
def getPluginCount():
    '''returns int\n\n
    getPluginCount()\n
    '''
def getPlugins():
    '''returns IlvPlugin[]\n\n
    getPlugins()\n
    '''
def getPlugin():
    '''returns IlvPlugin\n\n
    getPlugin(final int n)\n
    getPlugin(final String s)\n
    '''
def getRequiredPlugins():
    '''returns IlvPlugin[]\n\n
    getRequiredPlugins(final IlvPlugin ilvPlugin)\n
    '''
def getSettings():
    '''returns IlvSettings\n\n
    getSettings()\n
    '''
def setSettings():
    '''returns None\n\n
    setSettings(final IlvSettings settings)\n
    '''
def setSettingsQuery():
    '''returns None\n\n
    setSettingsQuery(final IlvSettingsQuery settingsQuery)\n
    '''
def getSettingsQuery():
    '''returns IlvSettingsQuery\n\n
    getSettingsQuery()\n
    '''
def setSettingsElement():
    '''returns None\n\n
    setSettingsElement(final IlvSettingsElement settingsElement)\n
    '''
def getSettingsElement():
    '''returns IlvSettingsElement\n\n
    getSettingsElement()\n
    '''
def initializedOnUserSettings():
    '''returns boolean\n\n
    initializedOnUserSettings()\n
    '''
def addPluginListener():
    '''returns None\n\n
    addPluginListener(final PluginListener e)\n
    '''
def removePluginListener():
    '''returns None\n\n
    removePluginListener(final PluginListener o)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL()\n
    '''
def lock():
    '''returns None\n\n
    lock(final IlvApplication ilvApplication)\n
    '''
def unlock():
    '''returns None\n\n
    unlock(final IlvApplication ilvApplication)\n
    '''
def isLocked():
    '''returns boolean\n\n
    isLocked()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
