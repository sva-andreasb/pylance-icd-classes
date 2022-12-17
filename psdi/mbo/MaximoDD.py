ID_SEED = "long  100000L"
fetchResultStopLimit = "String  \"mxe.db.fetchResultStopLimit\""
fetchStopLimitEnabled = "String  \"mxe.db.fetchStopLimitEnabled\""
fetchStopExclusion = "String  \"mxe.db.fetchStopExclusion\""
lookupMaxRowProperty = "String  \"mxe.db.lookupMaxRow\""
MT_OFFSET = "long  11111L"
def ():
    '''returns MaximoDD\n\n
    ()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def getDBPlatform():
    '''returns int\n\n
    getDBPlatform()\n
    '''
def getOraVersion():
    '''returns double\n\n
    getOraVersion()\n
    '''
def getDB2Version():
    '''returns double\n\n
    getDB2Version()\n
    '''
def getSequenceName():
    '''returns String\n\n
    getSequenceName(final String tbName, final String colName)\n
    '''
def updateMboValueInfoWithDomainInfo():
    '''returns None\n\n
    updateMboValueInfoWithDomainInfo()\n
    updateMboValueInfoWithDomainInfo(final String domainId)\n
    '''
def isLongDescriptionSearchable():
    '''returns boolean\n\n
    isLongDescriptionSearchable()\n
    '''
def getDomainFactoryName():
    '''returns String\n\n
    getDomainFactoryName(final String domainType)\n
    '''
def getOrgId():
    '''returns String\n\n
    getOrgId(String siteId)\n
    '''
def isValidSite():
    '''returns boolean\n\n
    isValidSite(final String siteId)\n
    '''
def isValidOrganization():
    '''returns boolean\n\n
    isValidOrganization(final String orgId)\n
    '''
def isSiteInOrganization():
    '''returns boolean\n\n
    isSiteInOrganization(final String siteId, final String orgId)\n
    '''
def isESigEnabled():
    '''returns boolean\n\n
    isESigEnabled(final String applicationName, final String optionName)\n
    '''
def getBaseCurrency():
    '''returns String\n\n
    getBaseCurrency(String orgId)\n
    '''
def getTranslator():
    '''returns Translate\n\n
    getTranslator()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getServiceInfo():
    '''returns ServiceInfo\n\n
    getServiceInfo(final String service)\n
    '''
def getServicesInfo():
    '''returns Iterator\n\n
    getServicesInfo()\n
    '''
def getIndexInfo():
    '''returns String[]\n\n
    getIndexInfo(String ixname)\n
    '''
def getMboSetInfo():
    '''returns MboSetInfo\n\n
    getMboSetInfo(final String ms)\n
    '''
def getMboSetsInfo():
    '''returns Iterator\n\n
    getMboSetsInfo()\n
    '''
def getRelationInfo():
    '''returns RelationInfo\n\n
    getRelationInfo(final String n)\n
    '''
def getRelationsInfo():
    '''returns Iterator\n\n
    getRelationsInfo()\n
    '''
def getDomainsInfo():
    '''returns Iterator\n\n
    getDomainsInfo()\n
    '''
def getDomainInfo():
    '''returns DomainInfo\n\n
    getDomainInfo(final String name)\n
    '''
def storeClobAsClob():
    '''returns boolean\n\n
    storeClobAsClob()\n
    '''
def storeLongalnAsClob():
    '''returns boolean\n\n
    storeLongalnAsClob()\n
    '''
def storeBlobAsBlob():
    '''returns boolean\n\n
    storeBlobAsBlob()\n
    '''
def getLangTableName():
    '''returns String\n\n
    getLangTableName(final String table)\n
    '''
def getUniqueIdColumn():
    '''returns String\n\n
    getUniqueIdColumn(final String table)\n
    '''
def getContentAttrName():
    '''returns String\n\n
    getContentAttrName(final String table)\n
    '''
def getLangCodeColumn():
    '''returns String\n\n
    getLangCodeColumn(final String table)\n
    '''
def isMLInUse():
    '''returns boolean\n\n
    isMLInUse(final String table)\n
    '''
def getAltIxName():
    '''returns String\n\n
    getAltIxName(final String table)\n
    '''
def getStorageType():
    '''returns int\n\n
    getStorageType(String table)\n
    '''
def isDeltaStorageObject():
    '''returns boolean\n\n
    isDeltaStorageObject(final String objectName)\n
    '''
def getExtTableName():
    '''returns String\n\n
    getExtTableName(final String table)\n
    '''
def isExtTable():
    '''returns boolean\n\n
    isExtTable(final String tableName)\n
    '''
def getBaseObjectName():
    '''returns String\n\n
    getBaseObjectName(final String tableName)\n
    '''
def eventValidate():
    '''returns boolean\n\n
    eventValidate(final EventMessage em)\n
    '''
def preSaveEventAction():
    '''returns None\n\n
    preSaveEventAction(final EventMessage em)\n
    '''
def eventAction():
    '''returns None\n\n
    eventAction(final EventMessage em)\n
    '''
def postCommitEventAction():
    '''returns None\n\n
    postCommitEventAction(final EventMessage em)\n
    '''
