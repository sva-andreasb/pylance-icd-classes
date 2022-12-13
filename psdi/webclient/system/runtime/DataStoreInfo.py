TAG_DATASTORE = "String  datastore""
DATASTORE_ID = "String  id""
DATASTORE_DATAATTRIBUTE = "String  dataattribute""
DATASTORE_DATASRC = "String  datasrc""
DATASTORE_DOMAIN = "String  domain""
DATASTORE_VALIDFOR = "String  validfor""
DATASTORE_CACHEDATA = "String  cachedata""
PROP_DOMAINATTRIBUTE = "String  domainattribute""
PROP_KEYATTRIBUTE = "String  keyattribute""
PROP_FROMATTRIBUTE = "String  fromattribute""
PROP_TOATTRIBUTE = "String  toattribute""
PROP_TODATASRC = "String  todatasrc""
PROP_FROMDATASRC = "String  fromdatasrc""
JSONKEY_DATASTORES = "String  datastores""
JSONKEY_SETVALUES = "String  setvalues""
JSONKEY_FILTERS = "String  filters""
JSONKEY_SITEORGFILTER = "String  siteorgfilter""
JSONKEY_TYPEAHEAD = "String  typeahead""
def DataStoreInfo():
'''public DataStoreInfo(final Element dataStoreElement, final EntityRelationshipModel erm, final boolean designMode)
public DataStoreInfo(final String id, final DomainInfo domainInfo)
'''
pass
def getMboSetForDataStore():
'''public MboSetRemote getMboSetForDataStore(final WebClientSession wcs, final boolean useZombie)
'''
pass
def getDomainAttributes():
'''public String[] getDomainAttributes()
'''
pass
def isSimpleDomain():
'''public boolean isSimpleDomain()
'''
pass
def getDomainInfo():
'''public DomainInfo getDomainInfo()
'''
pass
def getId():
'''public String getId()
'''
pass
def getFilterMap():
'''public Map<UIERMAttribute, String> getFilterMap()
'''
pass
def getTypeAhead():
'''public JSONObject getTypeAhead()
'''
pass
def getSetValueMap():
'''public Map<UIERMAttribute, String> getSetValueMap()
'''
pass
def getValidFor():
'''public int getValidFor()
'''
pass
def getAsJSON():
'''public JSONObject getAsJSON(final PageInstance page)
'''
pass
def getFiltersAsJSON():
'''public JSONObject getFiltersAsJSON(final PageInstance page)
'''
pass
def getSetValuesAsJSON():
'''public JSONObject getSetValuesAsJSON(final PageInstance page)
'''
pass
def getDomainType():
'''public DomainType getDomainType()
'''
pass
def getDomainTimeStamp():
'''public String getDomainTimeStamp()
'''
pass
def getElementId():
'''public String getElementId()
'''
pass
def needsToConsiderSiteOrg():
'''public boolean needsToConsiderSiteOrg()
'''
pass
def getAsJSONForDownload():
'''public JSONObject getAsJSONForDownload()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def getTableName():
'''public String getTableName()
'''
pass
def InvalidDataStoreElementException():
'''public InvalidDataStoreElementException(final String message)
'''
pass
