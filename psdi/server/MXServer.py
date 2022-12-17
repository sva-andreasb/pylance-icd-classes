serverTimeStampUpdateRate = "int  60"
HTML_CONTENT = "String  \"text/html\""
TEXT_CONTENT = "String  \"text/plain\""
MTENABLEDPROPERTY = "String  \"mxe.mt.enabled\""
REQ_PARAM_S2STOKEN = "String  \"s2stoken\""
API_KEY = "String  \"apikey\""
def getGuid():
    '''returns UUID\n\n
    getGuid()\n
    '''
def getServerHost():
    '''returns String\n\n
    getServerHost()\n
    '''
def setServerHost():
    '''returns None\n\n
    setServerHost(final String address)\n
    '''
def addToMaximoCache():
    '''returns None\n\n
    addToMaximoCache(final String name, final MaximoCache obj)\n
    '''
def removeFromMaximoCache():
    '''returns None\n\n
    removeFromMaximoCache(final String name)\n
    '''
def getFromMaximoCache():
    '''returns Object\n\n
    getFromMaximoCache(final String name)\n
    '''
def reloadMaximoCache():
    '''returns None\n\n
    reloadMaximoCache(final boolean flag)\n
    reloadMaximoCache(final String cacheName, final boolean updateAllServers)\n
    reloadMaximoCache(final String cacheName, final String key, final boolean flag)\n
    '''
def unloadTenantCache():
    '''returns None\n\n
    unloadTenantCache()\n
    unloadTenantCache(final String cacheName)\n
    '''
def unloadInactiveCaches():
    '''returns None\n\n
    unloadInactiveCaches(final long interval)\n
    '''
def getLoadedTenants():
    '''returns Set<String>\n\n
    getLoadedTenants(final String cacheName)\n
    '''
def reloadAdminModeByThread():
    '''returns None\n\n
    reloadAdminModeByThread(final String key, final MboRemote listenerMbo)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getValidApps():
    '''returns HashSet\n\n
    getValidApps()\n
    '''
def isValidApp():
    '''returns boolean\n\n
    isValidApp(final String app)\n
    '''
def addApp():
    '''returns None\n\n
    addApp(final String app)\n
    '''
def removeApp():
    '''returns None\n\n
    removeApp(final String app)\n
    '''
def getLicenseKeys():
    '''returns HashSet\n\n
    getLicenseKeys()\n
    '''
def isReadOnlyApp():
    '''returns boolean\n\n
    isReadOnlyApp(final String app)\n
    '''
def getSystemType():
    '''returns String\n\n
    getSystemType()\n
    '''
def isPermanentLicense():
    '''returns boolean\n\n
    isPermanentLicense()\n
    '''
def getProductKeys():
    '''returns HashSet\n\n
    getProductKeys()\n
    '''
def getEvalDaysRemaining():
    '''returns int\n\n
    getEvalDaysRemaining()\n
    '''
def getBranding():
    '''returns int\n\n
    getBranding()\n
    '''
def getPackagingInfo():
    '''returns None\n\n
    getPackagingInfo(final UserInfo ui)\n
    '''
def getMaxupgValue():
    '''returns String\n\n
    getMaxupgValue()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name, final UserInfo user)\n
    '''
def init():
    '''returns None\n\n
    init(final Connection sysCon)\n
    '''
def getMaximoCacheNames():
    '''returns Set<String>\n\n
    getMaximoCacheNames()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def getDBManager():
    '''returns DBManager\n\n
    getDBManager()\n
    '''
def getCronTaskManager():
    '''returns CronTaskManager\n\n
    getCronTaskManager()\n
    '''
def getNewCronTaskManager():
    '''returns CronTaskManager\n\n
    getNewCronTaskManager()\n
    '''
def isAdminModeOn():
    '''returns boolean\n\n
    isAdminModeOn(final boolean allInstances)\n
    '''
def isAdminModeOff():
    '''returns boolean\n\n
    isAdminModeOff(final boolean allInstances)\n
    '''
def isAdminModePending():
    '''returns boolean\n\n
    isAdminModePending()\n
    '''
def listenToAdmin():
    '''returns None\n\n
    listenToAdmin(final MboRemote listenerMbo, final boolean listen)\n
    '''
def getMaximoDD():
    '''returns MaximoDD\n\n
    getMaximoDD()\n
    '''
def getMaximoMLDD():
    '''returns MaximoMLDD\n\n
    getMaximoMLDD()\n
    '''
def getMaxMessageCache():
    '''returns MaxMessageCache\n\n
    getMaxMessageCache()\n
    '''
def getAutoKeyCache():
    '''returns AutoKeyCache\n\n
    getAutoKeyCache()\n
    '''
def getAppServiceNames():
    '''returns String[]\n\n
    getAppServiceNames()\n
    '''
def lookup():
    '''returns ServiceRemote\n\n
    lookup(final String name)\n
    lookup(final String name, final UserInfo ui)\n
    '''
def lookupLocal():
    '''returns ServiceRemote\n\n
    lookupLocal(final String name)\n
    '''
def getLocalAppList():
    '''returns String[]\n\n
    getLocalAppList()\n
    '''
def getSrvComm():
    '''returns SrvCommRemote\n\n
    getSrvComm(final String name, final String passwd)\n
    '''
def getRemoteUsers():
    '''returns Hashtable\n\n
    getRemoteUsers()\n
    '''
def getDate():
    '''returns Date\n\n
    getDate()\n
    getDate(final Locale l, final TimeZone tz)\n
    '''
def removeMaxSessionEntriesDeadForAnHour():
    '''returns None\n\n
    removeMaxSessionEntriesDeadForAnHour(final Connection con)\n
    '''
def retryAsyncTask():
    '''returns None\n\n
    retryAsyncTask(final Connection con, final String serverName, final String serverHost)\n
    '''
def getMAXUPGValue():
    '''returns String\n\n
    getMAXUPGValue(final Connection con, final String name)\n
    '''
def needToRunUpdateDB():
    '''returns None\n\n
    needToRunUpdateDB(final String product, final String maxupg, final String newRelDBVersion, final String lastRelDBVersion, final String varName, final boolean checkHF)\n
    '''
def getConfig():
    '''returns Properties\n\n
    getConfig()\n
    getConfig(final UserInfo userInfo)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String propName)\n
    getProperty(final String propName, final boolean checkExists)\n
    getProperty(final String propName, final UserInfo userInfo)\n
    getProperty(final String propName, final String lang)\n
    getProperty(final String propName, final String lang, final UserInfo userInfo)\n
    '''
def getPublicProperty():
    '''returns String\n\n
    getPublicProperty(final String propName)\n
    getPublicProperty(final String propName, final String lang)\n
    '''
def getSystemUserInfo():
    '''returns UserInfo\n\n
    getSystemUserInfo()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo(final String userIdentity)\n
    '''
def enableService():
    '''returns None\n\n
    enableService(final String svc)\n
    '''
def disableService():
    '''returns None\n\n
    disableService(final String svc)\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
def getRegistryHostName():
    '''returns String\n\n
    getRegistryHostName()\n
    '''
def getRegistryPort():
    '''returns String\n\n
    getRegistryPort()\n
    '''
def getMXServerInfo():
    '''returns MXServerInfo\n\n
    getMXServerInfo()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def validateS2stokenConfigValue():
    '''returns None\n\n
    validateS2stokenConfigValue()\n
    '''
def validateThisApiKeyConfigValue():
    '''returns String\n\n
    validateThisApiKeyConfigValue(final String apiKey)\n
    '''
def resolveApiKey():
    '''returns String\n\n
    resolveApiKey(final String apikey)\n
    '''
def validateApiKeyConfigValue():
    '''returns String\n\n
    validateApiKeyConfigValue()\n
    '''
def isLocal():
    '''returns boolean\n\n
    isLocal(final String serviceUrl)\n
    '''
def createMXTransaction():
    '''returns MXTransaction\n\n
    createMXTransaction()\n
    '''
def getSystemProperties():
    '''returns Properties\n\n
    getSystemProperties()\n
    '''
def getDatabaseProductName():
    '''returns String\n\n
    getDatabaseProductName()\n
    '''
def getDatabaseProductSimpleVersion():
    '''returns String\n\n
    getDatabaseProductSimpleVersion()\n
    '''
def getDatabaseProductVersion():
    '''returns String\n\n
    getDatabaseProductVersion()\n
    '''
def getDBPlatform():
    '''returns int\n\n
    getDBPlatform()\n
    '''
def getDBConnUsed():
    '''returns int\n\n
    getDBConnUsed()\n
    '''
def getFreeMemory():
    '''returns String[]\n\n
    getFreeMemory()\n
    '''
def getUserLicenseKey():
    '''returns String\n\n
    getUserLicenseKey()\n
    '''
def getAppServerNameandVersion():
    '''returns String\n\n
    getAppServerNameandVersion()\n
    '''
def getMEAServerVersion():
    '''returns ArrayList\n\n
    getMEAServerVersion()\n
    '''
def getMXServerVersion():
    '''returns String[]\n\n
    getMXServerVersion()\n
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
def getOrganization():
    '''returns String\n\n
    getOrganization(final String siteId)\n
    '''
def isMxserverStarted():
    '''returns boolean\n\n
    isMxserverStarted()\n
    '''
def checkAdminRestart():
    '''returns None\n\n
    checkAdminRestart()\n
    '''
def checkFailedTenants():
    '''returns None\n\n
    checkFailedTenants()\n
    '''
def getMXCipher():
    '''returns MXCipher\n\n
    getMXCipher()\n
    '''
def encData():
    '''returns byte[]\n\n
    encData(final String in, final int type)\n
    '''
def getMXCipherX():
    '''returns MXCipherX\n\n
    getMXCipherX()\n
    '''
def getNativeSql():
    '''returns String\n\n
    getNativeSql(final String jdbcSql)\n
    '''
def getBulletin():
    '''returns UserInputBulletin\n\n
    getBulletin()\n
    '''
def postUserInput():
    '''returns None\n\n
    postUserInput(final String id, final Object value, final UserInfo ui)\n
    '''
def getUserInput():
    '''returns Object\n\n
    getUserInput(final String id, final UserInfo ui)\n
    '''
def removeUserInput():
    '''returns None\n\n
    removeUserInput(final String id, final UserInfo ui)\n
    '''
def clearUserInput():
    '''returns None\n\n
    clearUserInput(final UserInfo ui)\n
    '''
def getBaseLang():
    '''returns String\n\n
    getBaseLang()\n
    '''
def getLanguageList():
    '''returns String[][]\n\n
    getLanguageList()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final String group, final String key, String langCode)\n
    getMessage(final MXException mxe, final String langCode)\n
    '''
def getTaggedMessage():
    '''returns String\n\n
    getTaggedMessage(final String group, final String key, String langCode)\n
    getTaggedMessage(final MXException mxe, final String langCode)\n
    '''
def getMessages():
    '''returns String[]\n\n
    getMessages(final String group, final String[] key, final String langCode)\n
    '''
def getMasterMboValueInfo():
    '''returns MboValueInfo\n\n
    getMasterMboValueInfo(final MboRemote tenantMbo)\n
    '''
def getWarnings():
    '''returns ArrayList\n\n
    getWarnings(final Object id)\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings(final Object id)\n
    '''
def addWarning():
    '''returns None\n\n
    addWarning(final MXException e, final Object id)\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings(final Object id)\n
    '''
def incrementMboCount():
    '''returns None\n\n
    incrementMboCount(final String name, final int tenantID)\n
    '''
def decrementMboCount():
    '''returns None\n\n
    decrementMboCount(final String name, final int tenantID)\n
    '''
def incrementMbosetCount():
    '''returns None\n\n
    incrementMbosetCount(final String name, final int tenantID)\n
    '''
def decrementMbosetCount():
    '''returns None\n\n
    decrementMbosetCount(final String name)\n
    decrementMbosetCount(final String name, final int tenantID)\n
    '''
def incrementMbosetIPCount():
    '''returns None\n\n
    incrementMbosetIPCount(String objName, final String clientHost, final String clientAddr)\n
    '''
def decrementMbosetIPCount():
    '''returns None\n\n
    decrementMbosetIPCount(String objName, final String clientHost, final String clientAddr)\n
    '''
def getMboSetIPCount():
    '''returns int\n\n
    getMboSetIPCount(String objName, final String clientHost, final String clientAddr)\n
    '''
def printMaxsessionInfo():
    '''returns String\n\n
    printMaxsessionInfo()\n
    '''
def getMboCount():
    '''returns String\n\n
    getMboCount()\n
    '''
def getMboSetCount():
    '''returns int\n\n
    getMboSetCount(String objName)\n
    '''
def getAllTenantsMboCountAsJSON():
    '''returns JSONObject\n\n
    getAllTenantsMboCountAsJSON()\n
    '''
def getConditionCache():
    '''returns MaxConditionCache\n\n
    getConditionCache()\n
    '''
def getDataRestrictionCache():
    '''returns DataRestrictionCache\n\n
    getDataRestrictionCache()\n
    '''
def getMaxDomainCache():
    '''returns MaxDomainCache\n\n
    getMaxDomainCache()\n
    '''
def setupLongOpPipe():
    '''returns InputStream\n\n
    setupLongOpPipe()\n
    '''
def clearLongOpPipe():
    '''returns None\n\n
    clearLongOpPipe()\n
    '''
def writeLongOpMsg():
    '''returns None\n\n
    writeLongOpMsg(String msg)\n
    '''
def getSQLServerPrefetchRows():
    '''returns int\n\n
    getSQLServerPrefetchRows()\n
    '''
def getSecurityContext():
    '''returns SecurityContextFlag\n\n
    getSecurityContext()\n
    '''
def clearSecurityContext():
    '''returns None\n\n
    clearSecurityContext()\n
    '''
def setSecurityCheck():
    '''returns None\n\n
    setSecurityCheck(final SecurityContextFlag securityFlag)\n
    '''
def isSQLServerPrefetchRowsNeeded():
    '''returns boolean\n\n
    isSQLServerPrefetchRowsNeeded()\n
    '''
def getMxServerConfig():
    '''returns Properties\n\n
    getMxServerConfig()\n
    '''
def getServerCommandRemote():
    '''returns SrvCommRemote\n\n
    getServerCommandRemote(final String name, final String passwd)\n
    getServerCommandRemote(final UserInfo userInfo)\n
    '''
def getMboCounts():
    '''returns ArrayList\n\n
    getMboCounts()\n
    getMboCounts(final int tenantID)\n
    '''
def getBaseCalendar():
    '''returns String\n\n
    getBaseCalendar()\n
    '''
def getTenantIdsList():
    '''returns List<Integer>\n\n
    getTenantIdsList(final UserInfo landlordInfo, final int status)\n
    '''
def getAllTenantIdsList():
    '''returns List<Integer>\n\n
    getAllTenantIdsList(final UserInfo landlordInfo)\n
    '''
def collectTenantDBConnInfo():
    '''returns None\n\n
    collectTenantDBConnInfo(final UserInfo info)\n
    '''
def collectTenantDBConForThisServer():
    '''returns None\n\n
    collectTenantDBConForThisServer(final UserInfo info)\n
    '''
def setProxy():
    '''returns None\n\n
    setProxy(final Remote proxy)\n
    '''
def getProxy():
    '''returns Remote\n\n
    getProxy()\n
    '''
def clearTenantRealmMap():
    '''returns None\n\n
    clearTenantRealmMap()\n
    '''
def loadCustomApps():
    '''returns None\n\n
    loadCustomApps()\n
    loadCustomApps(final Connection con)\n
    '''
def ():
    '''returns DBConnStatThread\n\n
    ()\n
    ()\n
    (final String user, final String password)\n
    (final UserInfo infoT)\n
    '''
def setKey():
    '''returns None\n\n
    setKey(final String value)\n
    '''
