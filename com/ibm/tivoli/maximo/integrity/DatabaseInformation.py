def ():
    '''returns DatabaseInformation\n\n
    (final Connection con)\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    getConnection(final MTContext c)\n
    '''
def getServerType():
    '''returns ServerType\n\n
    getServerType()\n
    '''
def setSelectedTenants():
    '''returns None\n\n
    setSelectedTenants(final Set<MTContext> tenants)\n
    '''
def getSelectedTenants():
    '''returns Set<MTContext>\n\n
    getSelectedTenants()\n
    '''
def isPreMerlin():
    '''returns boolean\n\n
    isPreMerlin()\n
    '''
def isMTEnabled():
    '''returns boolean\n\n
    isMTEnabled()\n
    '''
def getMTConnection():
    '''returns MTConnection\n\n
    getMTConnection()\n
    '''
def getSelectedUsers():
    '''returns Set<MTContext>\n\n
    getSelectedUsers()\n
    '''
def getSchema():
    '''returns String\n\n
    getSchema()\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final String schema)\n
    '''
def setSelectedTenant():
    '''returns None\n\n
    setSelectedTenant(final String targetTenant)\n
    '''
def getSQLTransform():
    '''returns SQLSpecificTransform\n\n
    getSQLTransform()\n
    '''
def getMaxUpgVersion():
    '''returns String\n\n
    getMaxUpgVersion()\n
    '''
def setPendingChanges():
    '''returns None\n\n
    setPendingChanges(final boolean hasPending)\n
    '''
def hasPendingChanges():
    '''returns boolean\n\n
    hasPendingChanges()\n
    '''
def getIntegerLength():
    '''returns int\n\n
    getIntegerLength()\n
    '''
def getSmallIntLength():
    '''returns int\n\n
    getSmallIntLength()\n
    '''
def getAmountLength():
    '''returns int\n\n
    getAmountLength()\n
    '''
def getAmountScale():
    '''returns int\n\n
    getAmountScale()\n
    '''
def isV510():
    '''returns boolean\n\n
    isV510()\n
    '''
def isUsingVarGraphic():
    '''returns boolean\n\n
    isUsingVarGraphic()\n
    '''
def getMaxVarCharLength():
    '''returns int\n\n
    getMaxVarCharLength()\n
    '''
def getVarCharMultiple():
    '''returns int\n\n
    getVarCharMultiple()\n
    '''
def getMTStorageType():
    '''returns MTStorageType\n\n
    getMTStorageType(final String tablename)\n
    '''
def isImportedTable():
    '''returns boolean\n\n
    isImportedTable(final String tableName)\n
    '''
def getSynonymMaxValue():
    '''returns String\n\n
    getSynonymMaxValue(final String synonym, final String domainid)\n
    '''
def getDefaultSynonym():
    '''returns String\n\n
    getDefaultSynonym(final String domainid, final String maxvalue)\n
    '''
def getBaseLangCode():
    '''returns String\n\n
    getBaseLangCode()\n
    '''
def hasExtension():
    '''returns boolean\n\n
    hasExtension(final String baseTable)\n
    '''
def resetHasExtension():
    '''returns None\n\n
    resetHasExtension()\n
    '''
def getNavtiveViewList():
    '''returns List<String>\n\n
    getNavtiveViewList()\n
    '''
def getMaximoViewList():
    '''returns List<String>\n\n
    getMaximoViewList()\n
    '''
def getNickName():
    '''returns String\n\n
    getNickName()\n
    '''
def hasTable():
    '''returns boolean\n\n
    hasTable(final String tbname)\n
    '''
def hasTableColumn():
    '''returns boolean\n\n
    hasTableColumn(final String objName, final String attrName)\n
    '''
def getUtil():
    '''returns Util\n\n
    getUtil()\n
    '''
def maxVarSetup():
    '''returns None\n\n
    maxVarSetup(final TreeMap<String, String> maxVarMap)\n
    '''
def getMaxVarValueFromCache():
    '''returns String\n\n
    getMaxVarValueFromCache(final String varName)\n
    '''
def getSequenceIncrement():
    '''returns int\n\n
    getSequenceIncrement()\n
    '''
def isMaxInst():
    '''returns boolean\n\n
    isMaxInst()\n
    '''
