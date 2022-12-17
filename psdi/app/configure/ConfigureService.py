VALIDATION_LENGTH = "String  \"LENGTH\""
VALIDATION_ALL = "String  \"ALL\""
VALIDATION_PENDINGCHG = "String  \"PENDINGCHG\""
def ():
    '''returns ConfigDBThread\n\n
    ()\n
    (final MXServer mxServer)\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    init(final int configLevel, final Util util, final ConnectionKey conKey, final UserInfo ui)\n
    '''
def isValidChar():
    '''returns boolean\n\n
    isValidChar(final String checkString)\n
    '''
def validateFormat():
    '''returns boolean\n\n
    validateFormat(final Locale locale, final TimeZone timezone, final String value, final String maxtype, final int length, final int scale, final boolean checkCase)\n
    '''
def convertToLocale():
    '''returns String\n\n
    convertToLocale(final String inputValue, final String maxtype, final Locale fromLocale, final TimeZone fromTimeZone, final Locale toLocale, final TimeZone toTimeZone)\n
    '''
def removeChanges():
    '''returns None\n\n
    removeChanges()\n
    '''
def removeTenantChanges():
    '''returns None\n\n
    removeTenantChanges(final UserInfo tenantInfo, final int tenanatId)\n
    '''
def applyTenantChanges():
    '''returns None\n\n
    applyTenantChanges(final UserInfo tenantInfo, final int tenanatId)\n
    applyTenantChanges(final UserInfo tenantInfo, final int tenantId, final boolean isPreview)\n
    '''
def createSelectedExtensionViews():
    '''returns None\n\n
    createSelectedExtensionViews(final Map<String, Map<String, Map<String, String>>> objectNames, final Set<String> deleteObjects, final Connection masterCon, final int tenantId)\n
    '''
def createExtensionTable():
    '''returns boolean\n\n
    createExtensionTable(final UserInfo masterInfo, final String tableName)\n
    '''
def changeAmountFormat():
    '''returns None\n\n
    changeAmountFormat(final int newLength, final int newScale, final int origLength, final int origScale)\n
    changeAmountFormat(final int newLength, final int newScale)\n
    '''
def changeIntFormat():
    '''returns None\n\n
    changeIntFormat(final int newIntLength, final int newSmallintLength, final int origIntLength, final int origSmallintLength)\n
    changeIntFormat(final int newIntLength, final int newSmallintLength)\n
    '''
def updateStatistics():
    '''returns None\n\n
    updateStatistics(final MboSetRemote objectSet)\n
    updateStatistics(String tablename)\n
    '''
def refreshIndexMetadata():
    '''returns None\n\n
    refreshIndexMetadata(final MboSetRemote objectSet)\n
    refreshIndexMetadata(String tablename)\n
    '''
def getUnrestoredTables():
    '''returns MboSetRemote\n\n
    getUnrestoredTables(final UserInfo userInfo)\n
    '''
def getOldBackupTables():
    '''returns MboSetRemote\n\n
    getOldBackupTables(final UserInfo userInfo)\n
    '''
def dropBackup():
    '''returns None\n\n
    dropBackup(final MboSetRemote tableSet)\n
    dropBackup(String tablenames)\n
    '''
def getConfigLevel():
    '''returns int\n\n
    getConfigLevel()\n
    getConfigLevel(final UserInfo ui)\n
    '''
def runConfigDB():
    '''returns None\n\n
    runConfigDB(final MboRemote listenerMbo)\n
    runConfigDB(final MboRemote listenerMbo, final HashMap<String, String> params)\n
    '''
def listenToConfigDB():
    '''returns None\n\n
    listenToConfigDB(final MboRemote listenerMbo, final boolean listen)\n
    '''
def configIsRunning():
    '''returns boolean\n\n
    configIsRunning()\n
    '''
def getNumConfigMsgs():
    '''returns int\n\n
    getNumConfigMsgs()\n
    '''
def getMaxColumnLength():
    '''returns int\n\n
    getMaxColumnLength(final String tablename, final String columnname)\n
    '''
def getGLMaxtypeLengthFromGLConfigure():
    '''returns int\n\n
    getGLMaxtypeLengthFromGLConfigure(final UserInfo userInfo)\n
    '''
def getDefaultStoragePartition():
    '''returns String\n\n
    getDefaultStoragePartition()\n
    '''
def nativeTableExists():
    '''returns boolean\n\n
    nativeTableExists(final String tablename)\n
    '''
def nativeViewExists():
    '''returns boolean\n\n
    nativeViewExists(final String viewname)\n
    '''
def descendingIndexesSupported():
    '''returns boolean\n\n
    descendingIndexesSupported()\n
    '''
def getMaxLengthColumnInIndex():
    '''returns int\n\n
    getMaxLengthColumnInIndex()\n
    '''
def getMaxLengthIndex():
    '''returns int\n\n
    getMaxLengthIndex()\n
    '''
def spaceIsSysManaged():
    '''returns boolean\n\n
    spaceIsSysManaged(final String spaceName)\n
    '''
def getGrants():
    '''returns HashMap\n\n
    getGrants(final String dbUserID, final String entityname)\n
    '''
def grantNative():
    '''returns None\n\n
    grantNative(final String dbUserID, final String entityname, final String privilege, final boolean grant)\n
    '''
def getDBPlatform():
    '''returns int\n\n
    getDBPlatform()\n
    '''
def isReservedWord():
    '''returns boolean\n\n
    isReservedWord(final String testWord)\n
    '''
def doSql():
    '''returns None\n\n
    doSql(final List list)\n
    doSql(final String sql)\n
    '''
def getJoinAttributes():
    '''returns HashMap\n\n
    getJoinAttributes(final MboRemote object1, final MboSetRemote object1Attrs, final MboRemote object2, final MboSetRemote object2Attrs)\n
    '''
def getAllCommonAttributes():
    '''returns HashSet\n\n
    getAllCommonAttributes(final MboSetRemote object1Attrs, final MboSetRemote object2Attrs)\n
    '''
def getMaxtypeCategory():
    '''returns int\n\n
    getMaxtypeCategory(String maxtype)\n
    '''
def nativeTypesAreCompatible():
    '''returns boolean\n\n
    nativeTypesAreCompatible(final String oldNativeType, final String newNativeType)\n
    '''
def logException():
    '''returns None\n\n
    logException(final Exception e)\n
    '''
def checkDomainLinks():
    '''returns MXException\n\n
    checkDomainLinks(final UserInfo ui, final HashSet<String> options)\n
    checkDomainLinks(final UserInfo ui, final MaxAttributeCfgRemote mac, final MboSetRemote domainLinks)\n
    '''
def compare():
    '''returns MXException\n\n
    compare(final HashSet<String> byPass, final String object, final String attr, final HashSet<String> domsOnMeta, String[] domsByLink, final StringBuffer os, final UserInfo ui, final boolean genInsertStatement)\n
    '''
def verifyView():
    '''returns None\n\n
    verifyView(String objectname)\n
    '''
def noDeltaRows():
    '''returns boolean\n\n
    noDeltaRows(final MboRemote masterMbo, final String validationType)\n
    '''
def pendingDeltaRowExist():
    '''returns boolean\n\n
    pendingDeltaRowExist()\n
    '''
def discardALLTenantDeltas():
    '''returns None\n\n
    discardALLTenantDeltas()\n
    '''
def isActiveExtTable():
    '''returns boolean\n\n
    isActiveExtTable(final String objectName)\n
    '''
def canDeleteFromConfigExtTable():
    '''returns boolean\n\n
    canDeleteFromConfigExtTable(final String attributeName, final String objectName)\n
    '''
def areTenantsOnboarded():
    '''returns boolean\n\n
    areTenantsOnboarded()\n
    '''
def setUserLangCode():
    '''returns None\n\n
    setUserLangCode(final String value)\n
    '''
def setParams():
    '''returns None\n\n
    setParams(final HashMap<String, String> params)\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final Connection inCon, final UserInfo ui)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
