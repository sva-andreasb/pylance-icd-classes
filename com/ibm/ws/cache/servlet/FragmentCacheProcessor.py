PROPERTY_EDGEABLE = "String  \"edgeable\""
PROPERTY_CONSUME_SUBFRAGMENTS = "String  \"consume-subfragments\""
PROPERTY_DO_NOT_CONSUME = "String  \"do-not-consume\""
PROPERTY_EXTERNALCACHE = "String  \"externalcache\""
PROPERTY_ALTERNATE_URL = "String  \"alternate_url\""
PROPERTY_SAVE_ATTRIBUTES = "String  \"save-attributes\""
PROPERTY_STORE_COOKIES = "String  \"store-cookies\""
PROPERTY_IGNORE_GET_POST = "String  \"ignore-get-post\""
PROPERTY_IGNORE_CHAR_ENCODING = "String  \"ignore-char-encoding\""
def FragmentCacheProcessor():
    '''    public FragmentCacheProcessor()
    '''
def reset():
    '''    public void reset(final ConfigEntry ce)
    '''
def preProcess():
    '''    public boolean preProcess(final ConfigEntry configEntry)
    public boolean preProcess(final CacheId cacheId)
    '''
def processCacheIdProperties():
    '''    public void processCacheIdProperties(final CacheId cacheid)
    '''
def processConfigEntryProperties():
    '''    public void processConfigEntryProperties()
    '''
def getBaseName():
    '''    public String getBaseName()
    '''
def populateFragmentInfo():
    '''    public void populateFragmentInfo(final FragmentInfo fi)
    '''
def execute():
    '''    public boolean execute(final CacheProxyRequest request, final CacheProxyResponse response, final Servlet servlet)
    '''
def getESICacheId():
    '''    public String getESICacheId(final ConfigEntry ce)
    '''
def getESIQueryString():
    '''    public String getESIQueryString(final CacheId ci)
    '''
def getESIRule():
    '''    public void getESIRule(final CacheId ci, final StringBuffer sb, final String identifier)
    '''
