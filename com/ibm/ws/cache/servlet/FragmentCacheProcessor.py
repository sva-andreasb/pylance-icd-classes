PROPERTY_EDGEABLE = "String  \"edgeable\""
PROPERTY_CONSUME_SUBFRAGMENTS = "String  \"consume-subfragments\""
PROPERTY_DO_NOT_CONSUME = "String  \"do-not-consume\""
PROPERTY_EXTERNALCACHE = "String  \"externalcache\""
PROPERTY_ALTERNATE_URL = "String  \"alternate_url\""
PROPERTY_SAVE_ATTRIBUTES = "String  \"save-attributes\""
PROPERTY_STORE_COOKIES = "String  \"store-cookies\""
PROPERTY_IGNORE_GET_POST = "String  \"ignore-get-post\""
PROPERTY_IGNORE_CHAR_ENCODING = "String  \"ignore-char-encoding\""
def ():
    '''returns FragmentCacheProcessor\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset(final ConfigEntry ce)\n
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
def populateFragmentInfo():
    '''returns None\n\n
    populateFragmentInfo(final FragmentInfo fi)\n
    '''
def execute():
    '''returns boolean\n\n
    execute(final CacheProxyRequest request, final CacheProxyResponse response, final Servlet servlet)\n
    '''
def getESICacheId():
    '''returns String\n\n
    getESICacheId(final ConfigEntry ce)\n
    '''
def getESIQueryString():
    '''returns String\n\n
    getESIQueryString(final CacheId ci)\n
    '''
def getESIRule():
    '''returns None\n\n
    getESIRule(final CacheId ci, final StringBuffer sb, final String identifier)\n
    '''
