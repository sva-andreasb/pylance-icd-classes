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
def ():
    '''returns InvalidDataStoreElementException\n\n
    (final Element dataStoreElement, final EntityRelationshipModel erm, final boolean designMode)\n
    (final String id, final DomainInfo domainInfo)\n
    (final String message)\n
    '''
def getMboSetForDataStore():
    '''returns MboSetRemote\n\n
    getMboSetForDataStore(final WebClientSession wcs, final boolean useZombie)\n
    '''
def getDomainAttributes():
    '''returns String[]\n\n
    getDomainAttributes()\n
    '''
def isSimpleDomain():
    '''returns boolean\n\n
    isSimpleDomain()\n
    '''
def getDomainInfo():
    '''returns DomainInfo\n\n
    getDomainInfo()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getTypeAhead():
    '''returns JSONObject\n\n
    getTypeAhead()\n
    '''
def getValidFor():
    '''returns int\n\n
    getValidFor()\n
    '''
def getAsJSON():
    '''returns JSONObject\n\n
    getAsJSON(final PageInstance page)\n
    '''
def getFiltersAsJSON():
    '''returns JSONObject\n\n
    getFiltersAsJSON(final PageInstance page)\n
    '''
def getSetValuesAsJSON():
    '''returns JSONObject\n\n
    getSetValuesAsJSON(final PageInstance page)\n
    '''
def getDomainType():
    '''returns DomainType\n\n
    getDomainType()\n
    '''
def getDomainTimeStamp():
    '''returns String\n\n
    getDomainTimeStamp()\n
    '''
def getElementId():
    '''returns String\n\n
    getElementId()\n
    '''
def needsToConsiderSiteOrg():
    '''returns boolean\n\n
    needsToConsiderSiteOrg()\n
    '''
def getAsJSONForDownload():
    '''returns JSONObject\n\n
    getAsJSONForDownload()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName()\n
    '''
