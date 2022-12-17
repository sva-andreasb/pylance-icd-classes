def ():
    '''returns MaxPropCache\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    init(final Properties propsFromFile)\n
    '''
def override():
    '''returns None\n\n
    override(final String url, final String user, final String password, final String schemaOwner)\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def reloadFromFile():
    '''returns None\n\n
    reloadFromFile()\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties()\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String propName)\n
    getProperty(final String propName, final boolean checkExists)\n
    getProperty(final String propName, final String lang)\n
    getProperty(final String propName, final String lang, final UserInfo userInfo, final UUID uuid)\n
    getProperty(final String propName, final UserInfo userInfo, final UUID uuid)\n
    '''
def getPropertyAsObject():
    '''returns Object\n\n
    getPropertyAsObject(final String propName)\n
    '''
def propertyExistsInCache():
    '''returns boolean\n\n
    propertyExistsInCache(final String propName)\n
    propertyExistsInCache(final String propName, final String lang)\n
    '''
def getPublicProperty():
    '''returns String\n\n
    getPublicProperty(final String propName)\n
    getPublicProperty(final String propName, final String lang)\n
    '''
def canTenantSee():
    '''returns boolean\n\n
    canTenantSee(final String propName)\n
    '''
def isEncrypted():
    '''returns boolean\n\n
    isEncrypted(final String propName)\n
    '''
def getEncryptedProps():
    '''returns Set\n\n
    getEncryptedProps()\n
    '''
def isPublic():
    '''returns boolean\n\n
    isPublic(final String propName)\n
    '''
def isPrivate():
    '''returns boolean\n\n
    isPrivate(final String propName)\n
    '''
def isMTSecure():
    '''returns boolean\n\n
    isMTSecure(final String propName)\n
    '''
def getPrivateProps():
    '''returns Set\n\n
    getPrivateProps()\n
    '''
def getFilePropNames():
    '''returns Set\n\n
    getFilePropNames()\n
    '''
def singleToDoubleQuotes():
    '''returns String\n\n
    singleToDoubleQuotes(final String in)\n
    '''
