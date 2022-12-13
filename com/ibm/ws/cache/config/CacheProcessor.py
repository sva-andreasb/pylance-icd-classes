PROPERTY_SHARING_POLICY = "String  sharing-policy""
PROPERTY_SHARINGPOLICY = "String  sharingpolicy""
PROPERTY_PERSIST_TO_DISK = "String  persist-to-disk""
PROPERTY_DELAY_INVALIDATIONS = "String  delay-invalidations""
PROPERTY_TIMEOUT = "String  timeout""
PROPERTY_INACTIVITY = "String  inactivity""
PROPERTY_PRIORITY = "String  priority""
PROPERTY_DO_NOT_CACHE = "String  do-not-cache""
def CacheProcessor():
'''public CacheProcessor()
public CacheProcessor(final ConfigEntry configEntry)
'''
pass
def reset():
'''public void reset(final ConfigEntry configEntry)
'''
pass
def preProcess():
'''public boolean preProcess(final ConfigEntry configEntry)
public boolean preProcess(final CacheId cacheId)
'''
pass
def processCacheIdProperties():
'''public void processCacheIdProperties(final CacheId cacheid)
'''
pass
def processConfigEntryProperties():
'''public void processConfigEntryProperties()
'''
pass
def getBaseName():
'''public String getBaseName()
'''
pass
def execute():
'''public boolean execute()
'''
pass
def getId():
'''public String getId()
'''
pass
def getGroupIds():
'''public ArrayList getGroupIds()
'''
pass
def getInvalidationIds():
'''public ArrayList getInvalidationIds()
'''
pass
def getSharingPolicy():
'''public int getSharingPolicy()
'''
pass
def getTimeout():
'''public int getTimeout()
'''
pass
def getInactivity():
'''public int getInactivity()
'''
pass
def getPriority():
'''public int getPriority()
'''
pass
def setEntryInfo():
'''public void setEntryInfo(final EntryInfo entryInfo)
'''
pass
def setInvalidationIds():
'''public void setInvalidationIds()
'''
pass
def isDelayInvalidations():
'''public boolean isDelayInvalidations()
'''
pass
def getDoNotCache():
'''public boolean getDoNotCache()
'''
pass
