MAX_FILE_COUNT = "int  4"
RECENT_FILES_CMD = "String  \"RecentFiles\""
SETTINGS_TYPE = "String  \"RecentFiles\""
APPLICATION_MRU_NAME = "String  \"main\""
def IlvRecentFileList():
    '''    public IlvRecentFileList(final FileHandler h, final String settingsName, final IlvApplication application)
    '''
def readSettings():
    '''    public void readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    public void readSettings(final IlvSettingsElement ilvSettingsElement)
    '''
def applicationEventReceived():
    '''    public void applicationEventReceived(final ApplicationEvent applicationEvent)
    '''
def writeSettings():
    '''    public void writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)
    public void writeSettings(IlvSettingsElement settingsElement)
    '''
def getRecentFileCount():
    '''    public int getRecentFileCount()
    '''
def getRecentFileURL():
    '''    public URL getRecentFileURL(final int n)
    '''
def getRecentFile():
    '''    public String getRecentFile(final int n)
    '''
def addRecentFileURL():
    '''    public void addRecentFileURL(final URL url)
    '''
def addRecentFileInfo():
    '''    public void addRecentFileInfo(final FileInfo fileInfo)
    '''
def setMaximumFileCount():
    '''    public int setMaximumFileCount(final int d)
    '''
def getMaximumFileCount():
    '''    public int getMaximumFileCount()
    '''
def moveRecentFileToTop():
    '''    public void moveRecentFileToTop(final int n)
    '''
def openRecentFile():
    '''    public void openRecentFile(final int n)
    '''
def removeRecentFileURL():
    '''    public boolean removeRecentFileURL(final URL url)
    '''
def getRecentFileIndex():
    '''    public int getRecentFileIndex(final URL url)
    public int getRecentFileIndex(final FileInfo obj)
    '''
def setActionCommand():
    '''    public void setActionCommand(final String e)
    '''
def getActionCommand():
    '''    public String getActionCommand()
    '''
def setApplication():
    '''    public void setApplication(final IlvApplication ilvApplication)
    '''
def getApplication():
    '''    public IlvApplication getApplication()
    '''
def setAction():
    '''    public void setAction(final Action i)
    '''
def getAction():
    '''    public Action getAction()
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
def getSettingsName():
    '''    public String getSettingsName()
    '''
def setSettingsName():
    '''    public void setSettingsName(final String settingsName)
    '''
def propertyChange():
    '''    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    '''
def FileInfo():
    '''    public FileInfo(final String b, final IlvRecentFileList recentFileList)
    public FileInfo(final URL a, final IlvRecentFileList recentFileList)
    '''
def getURL():
    '''    public URL getURL()
    '''
def setURL():
    '''    public void setURL(final URL a)
    '''
def setPathname():
    '''    public void setPathname(final String b)
    '''
def getPathname():
    '''    public String getPathname()
    '''
def toString():
    '''    public String toString()
    '''
