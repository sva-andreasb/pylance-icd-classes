INSTALL_BY_DEFAULT = "String  installByDefault""
NOT_INSTALL_BY_DEFAULT = "String  notInstallByDefault""
NEVER_INSTALL_BY_DEFAULT = "String  neverInstallByDefault""
def IlvPluginManager():
'''public IlvPluginManager()
'''
pass
def readSettings():
'''public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
'''
pass
def writeSettings():
'''public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
'''
pass
def setApplication():
'''public void setApplication(final IlvApplication c)
'''
pass
def applicationInitializingSettings():
'''public void applicationInitializingSettings(final ApplicationEvent applicationEvent)
'''
pass
def applicationInitialized():
'''public void applicationInitialized(final ApplicationEvent applicationEvent)
'''
pass
def mainWindowInitialized():
'''public void mainWindowInitialized(final ApplicationEvent applicationEvent)
'''
pass
def getApplication():
'''public IlvApplication getApplication()
'''
pass
def setRootURL():
'''public void setRootURL(final URL url)
'''
pass
def getRootURL():
'''public URL getRootURL()
public URL getRootURL(final int index)
'''
pass
def addRootURL():
'''public void addRootURL(final URL e)
'''
pass
def getRootURLCount():
'''public int getRootURLCount()
'''
pass
def setRootDirectory():
'''public void setRootDirectory(final File file)
'''
pass
def getRootDirectory():
'''public File getRootDirectory()
public File getRootDirectory(final int n)
'''
pass
def addRootDirectory():
'''public void addRootDirectory(final File file)
'''
pass
def getRootDirectoryCount():
'''public int getRootDirectoryCount()
'''
pass
def readPlugins():
'''public void readPlugins()
'''
pass
def accept():
'''public boolean accept(final File file)
'''
pass
def isInstalled():
'''public boolean isInstalled()
'''
pass
def uninstallPlugins():
'''public void uninstallPlugins()
'''
pass
def installPlugin():
'''public boolean installPlugin(final IlvPlugin ilvPlugin)
'''
pass
def uninstallPlugin():
'''public boolean uninstallPlugin(final IlvPlugin ilvPlugin, final boolean b)
'''
pass
def getPluginCount():
'''public int getPluginCount()
'''
pass
def getPlugins():
'''public IlvPlugin[] getPlugins()
'''
pass
def getPlugin():
'''public IlvPlugin getPlugin(final int n)
public IlvPlugin getPlugin(final String s)
'''
pass
def getRequiredPlugins():
'''public IlvPlugin[] getRequiredPlugins(final IlvPlugin ilvPlugin)
'''
pass
def getSettings():
'''public IlvSettings getSettings()
'''
pass
def setSettings():
'''public void setSettings(final IlvSettings settings)
'''
pass
def setSettingsQuery():
'''public void setSettingsQuery(final IlvSettingsQuery settingsQuery)
'''
pass
def getSettingsQuery():
'''public IlvSettingsQuery getSettingsQuery()
'''
pass
def setSettingsElement():
'''public void setSettingsElement(final IlvSettingsElement settingsElement)
'''
pass
def getSettingsElement():
'''public IlvSettingsElement getSettingsElement()
'''
pass
def initializedOnUserSettings():
'''public boolean initializedOnUserSettings()
'''
pass
def addPluginListener():
'''public void addPluginListener(final PluginListener e)
'''
pass
def removePluginListener():
'''public void removePluginListener(final PluginListener o)
'''
pass
def getPluginManagers():
'''public static ArrayList getPluginManagers(final IlvApplication ilvApplication)
'''
pass
def DocumentBaseLibrary():
'''public DocumentBaseLibrary(final URL url)
'''
pass
def Library():
'''public Library(final URL a)
'''
pass
def getURL():
'''public URL getURL()
'''
pass
def lock():
'''public void lock(final IlvApplication ilvApplication)
'''
pass
def unlock():
'''public void unlock(final IlvApplication ilvApplication)
'''
pass
def isLocked():
'''public boolean isLocked()
'''
pass
def JarLibrary():
'''public JarLibrary(final URL url)
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
