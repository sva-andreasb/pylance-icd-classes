PROPERTY_SHARING_POLICY = "String  \"sharing-policy\""
PROPERTY_SHARINGPOLICY = "String  \"sharingpolicy\""
PROPERTY_PERSIST_TO_DISK = "String  \"persist-to-disk\""
PROPERTY_DELAY_INVALIDATIONS = "String  \"delay-invalidations\""
PROPERTY_TIMEOUT = "String  \"timeout\""
PROPERTY_INACTIVITY = "String  \"inactivity\""
PROPERTY_PRIORITY = "String  \"priority\""
PROPERTY_DO_NOT_CACHE = "String  \"do-not-cache\""
def CacheProcessor():
    '''public CacheProcessor()
    public CacheProcessor(final ConfigEntry configEntry)
    '''
def reset():
    '''public void reset(final ConfigEntry configEntry)
    '''
def preProcess():
    '''public boolean preProcess(final ConfigEntry configEntry)
    public boolean preProcess(final CacheId cacheId)
    '''
def processCacheIdProperties():
    '''public void processCacheIdProperties(final CacheId cacheid)
    '''
def processConfigEntryProperties():
    '''public void processConfigEntryProperties()
    '''
def getBaseName():
    '''public String getBaseName()
    '''
def execute():
    '''public boolean execute()
    '''
def getId():
    '''public String getId()
    '''
def getGroupIds():
    '''public ArrayList getGroupIds()
    '''
def getInvalidationIds():
    '''public ArrayList getInvalidationIds()
    '''
def getSharingPolicy():
    '''public int getSharingPolicy()
    '''
def getTimeout():
    '''public int getTimeout()
    '''
def getInactivity():
    '''public int getInactivity()
    '''
def getPriority():
    '''public int getPriority()
    '''
def setEntryInfo():
    '''public void setEntryInfo(final EntryInfo entryInfo)
    '''
def setInvalidationIds():
    '''public void setInvalidationIds()
    '''
def isDelayInvalidations():
    '''public boolean isDelayInvalidations()
    '''
def getDoNotCache():
    '''public boolean getDoNotCache()
    '''
