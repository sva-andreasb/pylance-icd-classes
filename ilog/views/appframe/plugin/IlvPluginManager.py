INSTALL_BY_DEFAULT = "String  \"installByDefault\""
NOT_INSTALL_BY_DEFAULT = "String  \"notInstallByDefault\""
NEVER_INSTALL_BY_DEFAULT = "String  \"neverInstallByDefault\""
def IlvPluginManager():
    '''    public IlvPluginManager()
    '''
def readSettings():
    '''    public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    '''
def writeSettings():
    '''    public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    '''
def setApplication():
    '''    public void setApplication(final IlvApplication c)
    '''
def applicationInitializingSettings():
    '''    public void applicationInitializingSettings(final ApplicationEvent applicationEvent)
    '''
def applicationInitialized():
    '''    public void applicationInitialized(final ApplicationEvent applicationEvent)
    '''
def mainWindowInitialized():
    '''    public void mainWindowInitialized(final ApplicationEvent applicationEvent)
    '''
def getApplication():
    '''    public IlvApplication getApplication()
    '''
def setRootURL():
    '''    public void setRootURL(final URL url)
    '''
def getRootURL():
    '''    public URL getRootURL()
    public URL getRootURL(final int index)
    '''
def addRootURL():
    '''    public void addRootURL(final URL e)
    '''
def getRootURLCount():
    '''    public int getRootURLCount()
    '''
def setRootDirectory():
    '''    public void setRootDirectory(final File file)
    '''
def getRootDirectory():
    '''    public File getRootDirectory()
    public File getRootDirectory(final int n)
    '''
def addRootDirectory():
    '''    public void addRootDirectory(final File file)
    '''
def getRootDirectoryCount():
    '''    public int getRootDirectoryCount()
    '''
def readPlugins():
    '''    public void readPlugins()
    '''
def accept():
    '''    public boolean accept(final File file)
    '''
def isInstalled():
    '''    public boolean isInstalled()
    '''
def uninstallPlugins():
    '''    public void uninstallPlugins()
    '''
def installPlugin():
    '''    public boolean installPlugin(final IlvPlugin ilvPlugin)
    '''
def uninstallPlugin():
    '''    public boolean uninstallPlugin(final IlvPlugin ilvPlugin, final boolean b)
    '''
def getPluginCount():
    '''    public int getPluginCount()
    '''
def getPlugins():
    '''    public IlvPlugin[] getPlugins()
    '''
def getPlugin():
    '''    public IlvPlugin getPlugin(final int n)
    public IlvPlugin getPlugin(final String s)
    '''
def getRequiredPlugins():
    '''    public IlvPlugin[] getRequiredPlugins(final IlvPlugin ilvPlugin)
    '''
def getSettings():
    '''    public IlvSettings getSettings()
    '''
def setSettings():
    '''    public void setSettings(final IlvSettings settings)
    '''
def setSettingsQuery():
    '''    public void setSettingsQuery(final IlvSettingsQuery settingsQuery)
    '''
def getSettingsQuery():
    '''    public IlvSettingsQuery getSettingsQuery()
    '''
def setSettingsElement():
    '''    public void setSettingsElement(final IlvSettingsElement settingsElement)
    '''
def getSettingsElement():
    '''    public IlvSettingsElement getSettingsElement()
    '''
def initializedOnUserSettings():
    '''    public boolean initializedOnUserSettings()
    '''
def addPluginListener():
    '''    public void addPluginListener(final PluginListener e)
    '''
def removePluginListener():
    '''    public void removePluginListener(final PluginListener o)
    '''
def getPluginManagers():
    '''    public static ArrayList getPluginManagers(final IlvApplication ilvApplication)
    '''
def DocumentBaseLibrary():
    '''    public DocumentBaseLibrary(final URL url)
    '''
def Library():
    '''    public Library(final URL a)
    '''
def getURL():
    '''    public URL getURL()
    '''
def lock():
    '''    public void lock(final IlvApplication ilvApplication)
    '''
def unlock():
    '''    public void unlock(final IlvApplication ilvApplication)
    '''
def isLocked():
    '''    public boolean isLocked()
    '''
def JarLibrary():
    '''    public JarLibrary(final URL url)
    '''
def isValid():
    '''    public boolean isValid()
    '''
