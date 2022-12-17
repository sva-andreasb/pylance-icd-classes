MAX_FILE_COUNT = "int  4"
RECENT_FILES_CMD = "String  \"RecentFiles\""
SETTINGS_TYPE = "String  \"RecentFiles\""
APPLICATION_MRU_NAME = "String  \"main\""
def ():
    '''returns FileInfo\n\n
    (final FileHandler h, final String settingsName, final IlvApplication application)\n
    (final String b, final IlvRecentFileList recentFileList)\n
    (final URL a, final IlvRecentFileList recentFileList)\n
    '''
def readSettings():
    '''returns None\n\n
    readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    readSettings(final IlvSettingsElement ilvSettingsElement)\n
    '''
def applicationEventReceived():
    '''returns None\n\n
    applicationEventReceived(final ApplicationEvent applicationEvent)\n
    '''
def writeSettings():
    '''returns None\n\n
    writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    writeSettings(IlvSettingsElement settingsElement)\n
    '''
def getRecentFileCount():
    '''returns int\n\n
    getRecentFileCount()\n
    '''
def getRecentFileURL():
    '''returns URL\n\n
    getRecentFileURL(final int n)\n
    '''
def getRecentFile():
    '''returns String\n\n
    getRecentFile(final int n)\n
    '''
def addRecentFileURL():
    '''returns None\n\n
    addRecentFileURL(final URL url)\n
    '''
def addRecentFileInfo():
    '''returns None\n\n
    addRecentFileInfo(final FileInfo fileInfo)\n
    '''
def setMaximumFileCount():
    '''returns int\n\n
    setMaximumFileCount(final int d)\n
    '''
def getMaximumFileCount():
    '''returns int\n\n
    getMaximumFileCount()\n
    '''
def moveRecentFileToTop():
    '''returns None\n\n
    moveRecentFileToTop(final int n)\n
    '''
def openRecentFile():
    '''returns None\n\n
    openRecentFile(final int n)\n
    '''
def removeRecentFileURL():
    '''returns boolean\n\n
    removeRecentFileURL(final URL url)\n
    '''
def getRecentFileIndex():
    '''returns int\n\n
    getRecentFileIndex(final URL url)\n
    getRecentFileIndex(final FileInfo obj)\n
    '''
def setActionCommand():
    '''returns None\n\n
    setActionCommand(final String e)\n
    '''
def getActionCommand():
    '''returns String\n\n
    getActionCommand()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication ilvApplication)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final Action i)\n
    '''
def getAction():
    '''returns Action\n\n
    getAction()\n
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
def getSettingsName():
    '''returns String\n\n
    getSettingsName()\n
    '''
def setSettingsName():
    '''returns None\n\n
    setSettingsName(final String settingsName)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL()\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final URL a)\n
    '''
def setPathname():
    '''returns None\n\n
    setPathname(final String b)\n
    '''
def getPathname():
    '''returns String\n\n
    getPathname()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
