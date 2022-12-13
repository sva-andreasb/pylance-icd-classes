ID_SEED = "long  100000L"
fetchResultStopLimit = "String  \"mxe.db.fetchResultStopLimit\""
fetchStopLimitEnabled = "String  \"mxe.db.fetchStopLimitEnabled\""
fetchStopExclusion = "String  \"mxe.db.fetchStopExclusion\""
lookupMaxRowProperty = "String  \"mxe.db.lookupMaxRow\""
MT_OFFSET = "long  11111L"
def MaximoDD():
    '''    public MaximoDD()
    '''
def getName():
    '''    public String getName()
    '''
def init():
    '''    public void init()
    '''
def reload():
    '''    public void reload()
    public void reload(final String key)
    '''
def getDBPlatform():
    '''    public int getDBPlatform()
    '''
def getOraVersion():
    '''    public double getOraVersion()
    '''
def getDB2Version():
    '''    public double getDB2Version()
    '''
def getAppFieldDefaults():
    '''    public HashMap<String, String> getAppFieldDefaults(final String appName, final String objectName, final String siteid, final String userName, final HashSet groupNames)
    '''
def getSequenceName():
    '''    public String getSequenceName(final String tbName, final String colName)
    '''
def getRelationships():
    '''    public HashMap<String, RelationInfo> getRelationships(final String objectName)
    '''
def updateMboValueInfoWithDomainInfo():
    '''    public void updateMboValueInfoWithDomainInfo()
    public void updateMboValueInfoWithDomainInfo(final String domainId)
    '''
def isLongDescriptionSearchable():
    '''    public boolean isLongDescriptionSearchable()
    '''
def getDomainFactoryName():
    '''    public String getDomainFactoryName(final String domainType)
    '''
def getOrgId():
    '''    public String getOrgId(String siteId)
    '''
def isValidSite():
    '''    public boolean isValidSite(final String siteId)
    '''
def isValidOrganization():
    '''    public boolean isValidOrganization(final String orgId)
    '''
def isSiteInOrganization():
    '''    public boolean isSiteInOrganization(final String siteId, final String orgId)
    '''
def getGLConfigure():
    '''    public TreeMap<Integer, HashMap<String, Object>> getGLConfigure()
    public TreeMap<Integer, HashMap<String, Object>> getGLConfigure(final String orgid)
    '''
def isESigEnabled():
    '''    public boolean isESigEnabled(final String applicationName, final String optionName)
    '''
def getBaseCurrency():
    '''    public String getBaseCurrency(String orgId)
    '''
def getTranslator():
    '''    public Translate getTranslator()
    '''
def toString():
    '''    public String toString()
    '''
def getServiceInfo():
    '''    public ServiceInfo getServiceInfo(final String service)
    '''
def getServicesInfo():
    '''    public Iterator getServicesInfo()
    '''
def getIndexInfo():
    '''    public String[] getIndexInfo(String ixname)
    '''
def getMboSetInfo():
    '''    public MboSetInfo getMboSetInfo(final String ms)
    '''
def getMboSetsInfo():
    '''    public Iterator getMboSetsInfo()
    '''
def getRelationInfo():
    '''    public RelationInfo getRelationInfo(final String n)
    '''
def getRelationsInfo():
    '''    public Iterator getRelationsInfo()
    '''
def getDomainsInfo():
    '''    public Iterator getDomainsInfo()
    '''
def getDomainInfo():
    '''    public DomainInfo getDomainInfo(final String name)
    '''
def storeClobAsClob():
    '''    public boolean storeClobAsClob()
    '''
def storeLongalnAsClob():
    '''    public boolean storeLongalnAsClob()
    '''
def storeBlobAsBlob():
    '''    public boolean storeBlobAsBlob()
    '''
def getLangTableName():
    '''    public String getLangTableName(final String table)
    '''
def getUniqueIdColumn():
    '''    public String getUniqueIdColumn(final String table)
    '''
def getContentAttrName():
    '''    public String getContentAttrName(final String table)
    '''
def getLangCodeColumn():
    '''    public String getLangCodeColumn(final String table)
    '''
def isMLInUse():
    '''    public boolean isMLInUse(final String table)
    '''
def getAltIxName():
    '''    public String getAltIxName(final String table)
    '''
def getStorageType():
    '''    public int getStorageType(String table)
    '''
def isDeltaStorageObject():
    '''    public boolean isDeltaStorageObject(final String objectName)
    '''
def getExtTableName():
    '''    public String getExtTableName(final String table)
    '''
def isExtTable():
    '''    public boolean isExtTable(final String tableName)
    '''
def getBaseObjectName():
    '''    public String getBaseObjectName(final String tableName)
    '''
def eventValidate():
    '''    public boolean eventValidate(final EventMessage em)
    '''
def preSaveEventAction():
    '''    public void preSaveEventAction(final EventMessage em)
    '''
def eventAction():
    '''    public void eventAction(final EventMessage em)
    '''
def postCommitEventAction():
    '''    public void postCommitEventAction(final EventMessage em)
    '''
