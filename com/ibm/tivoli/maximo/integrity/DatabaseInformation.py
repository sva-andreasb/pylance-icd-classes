def DatabaseInformation():
    '''    public DatabaseInformation(final Connection con)
    '''
def getConnection():
    '''    public Connection getConnection()
    public Connection getConnection(final MTContext c)
    '''
def getServerType():
    '''    public ServerType getServerType()
    '''
def setSelectedTenants():
    '''    public void setSelectedTenants(final Set<MTContext> tenants)
    '''
def getSelectedTenants():
    '''    public Set<MTContext> getSelectedTenants()
    '''
def isPreMerlin():
    '''    public boolean isPreMerlin()
    '''
def isMTEnabled():
    '''    public boolean isMTEnabled()
    '''
def getMTConnection():
    '''    public MTConnection getMTConnection()
    '''
def getSelectedUsers():
    '''    public Set<MTContext> getSelectedUsers()
    '''
def getSchema():
    '''    public String getSchema()
    '''
def setSchema():
    '''    public void setSchema(final String schema)
    '''
def setSelectedTenant():
    '''    public void setSelectedTenant(final String targetTenant)
    '''
def getSQLTransform():
    '''    public SQLSpecificTransform getSQLTransform()
    '''
def getMaxUpgVersion():
    '''    public String getMaxUpgVersion()
    '''
def setPendingChanges():
    '''    public void setPendingChanges(final boolean hasPending)
    '''
def hasPendingChanges():
    '''    public boolean hasPendingChanges()
    '''
def getIntegerLength():
    '''    public int getIntegerLength()
    '''
def getSmallIntLength():
    '''    public int getSmallIntLength()
    '''
def getAmountLength():
    '''    public int getAmountLength()
    '''
def getAmountScale():
    '''    public int getAmountScale()
    '''
def isV510():
    '''    public boolean isV510()
    '''
def isUsingVarGraphic():
    '''    public boolean isUsingVarGraphic()
    '''
def getMaxVarCharLength():
    '''    public int getMaxVarCharLength()
    '''
def getVarCharMultiple():
    '''    public int getVarCharMultiple()
    '''
def getMTStorageType():
    '''    public MTStorageType getMTStorageType(final String tablename)
    '''
def isImportedTable():
    '''    public boolean isImportedTable(final String tableName)
    '''
def getSynonymMaxValue():
    '''    public String getSynonymMaxValue(final String synonym, final String domainid)
    '''
def getDefaultSynonym():
    '''    public String getDefaultSynonym(final String domainid, final String maxvalue)
    '''
def getBaseLangCode():
    '''    public String getBaseLangCode()
    '''
def hasExtension():
    '''    public boolean hasExtension(final String baseTable)
    '''
def resetHasExtension():
    '''    public void resetHasExtension()
    '''
def getNavtiveViewList():
    '''    public List<String> getNavtiveViewList()
    '''
def getMaximoViewList():
    '''    public List<String> getMaximoViewList()
    '''
def getNickName():
    '''    public String getNickName()
    '''
def hasTable():
    '''    public boolean hasTable(final String tbname)
    '''
def hasTableColumn():
    '''    public boolean hasTableColumn(final String objName, final String attrName)
    '''
def getUtil():
    '''    public Util getUtil()
    '''
def maxVarSetup():
    '''    public void maxVarSetup(final TreeMap<String, String> maxVarMap)
    '''
def getMaxVarValueFromCache():
    '''    public String getMaxVarValueFromCache(final String varName)
    '''
def getSequenceIncrement():
    '''    public int getSequenceIncrement()
    '''
def isMaxInst():
    '''    public boolean isMaxInst()
    '''
