PROPERTY_SHARING_POLICY = "String  \"sharing-policy\""
PROPERTY_SHARINGPOLICY = "String  \"sharingpolicy\""
PROPERTY_PERSIST_TO_DISK = "String  \"persist-to-disk\""
PROPERTY_DELAY_INVALIDATIONS = "String  \"delay-invalidations\""
PROPERTY_TIMEOUT = "String  \"timeout\""
PROPERTY_INACTIVITY = "String  \"inactivity\""
PROPERTY_PRIORITY = "String  \"priority\""
PROPERTY_DO_NOT_CACHE = "String  \"do-not-cache\""
def ():
    '''returns CacheProcessor\n\n
    ()\n
    (final ConfigEntry configEntry)\n
    '''
def reset():
    '''returns None\n\n
    reset(final ConfigEntry configEntry)\n
    '''
def preProcess():
    '''returns boolean\n\n
    preProcess(final ConfigEntry configEntry)\n
    preProcess(final CacheId cacheId)\n
    '''
def processCacheIdProperties():
    '''returns None\n\n
    processCacheIdProperties(final CacheId cacheid)\n
    '''
def processConfigEntryProperties():
    '''returns None\n\n
    processConfigEntryProperties()\n
    '''
def getBaseName():
    '''returns String\n\n
    getBaseName()\n
    '''
def execute():
    '''returns boolean\n\n
    execute()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getGroupIds():
    '''returns ArrayList\n\n
    getGroupIds()\n
    '''
def getInvalidationIds():
    '''returns ArrayList\n\n
    getInvalidationIds()\n
    '''
def getSharingPolicy():
    '''returns int\n\n
    getSharingPolicy()\n
    '''
def getTimeout():
    '''returns int\n\n
    getTimeout()\n
    '''
def getInactivity():
    '''returns int\n\n
    getInactivity()\n
    '''
def getPriority():
    '''returns int\n\n
    getPriority()\n
    '''
def setEntryInfo():
    '''returns None\n\n
    setEntryInfo(final EntryInfo entryInfo)\n
    '''
def setInvalidationIds():
    '''returns None\n\n
    setInvalidationIds()\n
    '''
def isDelayInvalidations():
    '''returns boolean\n\n
    isDelayInvalidations()\n
    '''
def getDoNotCache():
    '''returns boolean\n\n
    getDoNotCache()\n
    '''
