APPFRAME_LAYER = "String  \"AppFrame\""
APPLICATION_DATA_LAYER = "String  \"ApplicationData\""
CLIENT_DEVICE_LAYER = "String  \"ClientDevice\""
ROLE_LAYER = "String  \"Roles\""
USER_LAYER = "String  \"User\""
DEFAULT_NAME = "String  \"DefaultManager\""
def ():
    '''returns SettingsAddedAction\n\n
    (final String s)\n
    ()\n
    (final IlvSettings settings, final int mode)\n
    (final String name)\n
    (final IlvSettings a)\n
    (final IlvSettings a)\n
    (final IlvSettings a)\n
    '''
def initializeSettings():
    '''returns boolean\n\n
    initializeSettings()\n
    '''
def areSettingsInitialized():
    '''returns boolean\n\n
    areSettingsInitialized()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication g)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def addSettings():
    '''returns SettingsInfo\n\n
    addSettings(final IlvSettings ilvSettings, final String s)\n
    addSettings(final IlvSettings e)\n
    '''
def removeSettings():
    '''returns boolean\n\n
    removeSettings(final IlvSettings key)\n
    removeSettings(final IlvSettings ilvSettings)\n
    '''
def containsSettings():
    '''returns boolean\n\n
    containsSettings(final IlvSettings ilvSettings)\n
    '''
def createSettingsElement():
    '''returns IlvSettingsElement\n\n
    createSettingsElement(final String s)\n
    '''
def getSettings():
    '''returns IlvSettings\n\n
    getSettings(final String s)\n
    getSettings()\n
    getSettings()\n
    getSettings(final int n)\n
    '''
def setWritableSettings():
    '''returns None\n\n
    setWritableSettings(final IlvSettings e)\n
    '''
def getWritableSettings():
    '''returns IlvSettings\n\n
    getWritableSettings()\n
    '''
def insertLayer():
    '''returns boolean\n\n
    insertLayer(final String s, final String s2, final boolean b)\n
    '''
def removeLayer():
    '''returns boolean\n\n
    removeLayer(final String s)\n
    '''
def getLayerName():
    '''returns String\n\n
    getLayerName(final IlvSettings ilvSettings)\n
    '''
def getLayers():
    '''returns String[]\n\n
    getLayers()\n
    '''
def addSettingsListener():
    '''returns None\n\n
    addSettingsListener(final SettingsListener e)\n
    '''
def removeSettingsListener():
    '''returns boolean\n\n
    removeSettingsListener(final SettingsListener o)\n
    '''
def freezeMutationNotifications():
    '''returns None\n\n
    freezeMutationNotifications()\n
    '''
def unFreezeMutationNotifications():
    '''returns None\n\n
    unFreezeMutationNotifications()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def getLayer():
    '''returns Layer\n\n
    getLayer()\n
    '''
def setLayer():
    '''returns None\n\n
    setLayer(final Layer layer)\n
    '''
def getSettingsIndex():
    '''returns int\n\n
    getSettingsIndex(final String s)\n
    getSettingsIndex(final IlvSettings o)\n
    '''
def getSettingsInfo():
    '''returns SettingsInfo\n\n
    getSettingsInfo(final String s)\n
    '''
def getSettingsCount():
    '''returns int\n\n
    getSettingsCount()\n
    '''
def notifyListener():
    '''returns None\n\n
    notifyListener(final SettingsListener settingsListener)\n
    notifyListener(final SettingsListener settingsListener)\n
    notifyListener(final SettingsListener settingsListener)\n
    '''
