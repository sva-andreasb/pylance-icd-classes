TAG_DATASTORE = "String  \"datastore\""
DATASTORE_ID = "String  \"id\""
DATASTORE_DATAATTRIBUTE = "String  \"dataattribute\""
DATASTORE_DATASRC = "String  \"datasrc\""
DATASTORE_DOMAIN = "String  \"domain\""
DATASTORE_VALIDFOR = "String  \"validfor\""
DATASTORE_CACHEDATA = "String  \"cachedata\""
PROP_DOMAINATTRIBUTE = "String  \"domainattribute\""
PROP_KEYATTRIBUTE = "String  \"keyattribute\""
PROP_FROMATTRIBUTE = "String  \"fromattribute\""
PROP_TOATTRIBUTE = "String  \"toattribute\""
PROP_TODATASRC = "String  \"todatasrc\""
PROP_FROMDATASRC = "String  \"fromdatasrc\""
JSONKEY_DATASTORES = "String  \"datastores\""
JSONKEY_SETVALUES = "String  \"setvalues\""
JSONKEY_FILTERS = "String  \"filters\""
JSONKEY_SITEORGFILTER = "String  \"siteorgfilter\""
JSONKEY_TYPEAHEAD = "String  \"typeahead\""
def DataStoreInfo():
    '''public DataStoreInfo(final Element dataStoreElement, final EntityRelationshipModel erm, final boolean designMode)
    public DataStoreInfo(final String id, final DomainInfo domainInfo)
    '''
def getMboSetForDataStore():
    '''public MboSetRemote getMboSetForDataStore(final WebClientSession wcs, final boolean useZombie)
    '''
def getDomainAttributes():
    '''public String[] getDomainAttributes()
    '''
def isSimpleDomain():
    '''public boolean isSimpleDomain()
    '''
def getDomainInfo():
    '''public DomainInfo getDomainInfo()
    '''
def getId():
    '''public String getId()
    '''
def getFilterMap():
    '''public Map<UIERMAttribute, String> getFilterMap()
    '''
def getTypeAhead():
    '''public JSONObject getTypeAhead()
    '''
def getSetValueMap():
    '''public Map<UIERMAttribute, String> getSetValueMap()
    '''
def getValidFor():
    '''public int getValidFor()
    '''
def getAsJSON():
    '''public JSONObject getAsJSON(final PageInstance page)
    '''
def getFiltersAsJSON():
    '''public JSONObject getFiltersAsJSON(final PageInstance page)
    '''
def getSetValuesAsJSON():
    '''public JSONObject getSetValuesAsJSON(final PageInstance page)
    '''
def getDomainType():
    '''public DomainType getDomainType()
    '''
def getDomainTimeStamp():
    '''public String getDomainTimeStamp()
    '''
def getElementId():
    '''public String getElementId()
    '''
def needsToConsiderSiteOrg():
    '''public boolean needsToConsiderSiteOrg()
    '''
def getAsJSONForDownload():
    '''public JSONObject getAsJSONForDownload()
    '''
def cleanup():
    '''public void cleanup()
    '''
def getTableName():
    '''public String getTableName()
    '''
def InvalidDataStoreElementException():
    '''public InvalidDataStoreElementException(final String message)
    '''
