MAX_FILE_COUNT = "int  4"
RECENT_FILES_CMD = "String  RecentFiles""
SETTINGS_TYPE = "String  RecentFiles""
APPLICATION_MRU_NAME = "String  main""
def IlvRecentFileList():
'''public IlvRecentFileList(final FileHandler h, final String settingsName, final IlvApplication application)
'''
pass
def readSettings():
'''public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
public void readSettings(final IlvSettingsElement ilvSettingsElement)
'''
pass
def applicationEventReceived():
'''public void applicationEventReceived(final ApplicationEvent applicationEvent)
'''
pass
def writeSettings():
'''public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
public void writeSettings(IlvSettingsElement settingsElement)
'''
pass
def getRecentFileCount():
'''public int getRecentFileCount()
'''
pass
def getRecentFileURL():
'''public URL getRecentFileURL(final int n)
'''
pass
def getRecentFile():
'''public String getRecentFile(final int n)
'''
pass
def addRecentFileURL():
'''public void addRecentFileURL(final URL url)
'''
pass
def addRecentFileInfo():
'''public void addRecentFileInfo(final FileInfo fileInfo)
'''
pass
def setMaximumFileCount():
'''public int setMaximumFileCount(final int d)
'''
pass
def getMaximumFileCount():
'''public int getMaximumFileCount()
'''
pass
def moveRecentFileToTop():
'''public void moveRecentFileToTop(final int n)
'''
pass
def openRecentFile():
'''public void openRecentFile(final int n)
'''
pass
def removeRecentFileURL():
'''public boolean removeRecentFileURL(final URL url)
'''
pass
def getRecentFileIndex():
'''public int getRecentFileIndex(final URL url)
public int getRecentFileIndex(final FileInfo obj)
'''
pass
def setActionCommand():
'''public void setActionCommand(final String e)
'''
pass
def getActionCommand():
'''public String getActionCommand()
'''
pass
def setApplication():
'''public void setApplication(final IlvApplication ilvApplication)
'''
pass
def getApplication():
'''public IlvApplication getApplication()
'''
pass
def setAction():
'''public void setAction(final Action i)
'''
pass
def getAction():
'''public Action getAction()
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
def getSettingsName():
'''public String getSettingsName()
'''
pass
def setSettingsName():
'''public void setSettingsName(final String settingsName)
'''
pass
def propertyChange():
'''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
'''
pass
def FileInfo():
'''public FileInfo(final String b, final IlvRecentFileList recentFileList)
public FileInfo(final URL a, final IlvRecentFileList recentFileList)
'''
pass
def getURL():
'''public URL getURL()
'''
pass
def setURL():
'''public void setURL(final URL a)
'''
pass
def setPathname():
'''public void setPathname(final String b)
'''
pass
def getPathname():
'''public String getPathname()
'''
pass
def toString():
'''public String toString()
'''
pass
