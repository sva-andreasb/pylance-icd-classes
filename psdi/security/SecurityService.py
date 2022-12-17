SAMESYSTEMCONNECTIONKEYPERTHREAD = "String  \"SameSystemConnectionKeyPerThread\""
TENANTDBUSERNAMETOKEN = "String  \"TENANTDBUSERNAME\""
LANDLORDTENANTID = "int  2"
def ():
    '''returns LtpaTokenMonitor\n\n
    (final MXServer mxServer)\n
    (final String url)\n
    (final String url, final MXServer mxServer)\n
    (final UserInfo ui)\n
    ()\n
    ()\n
    ()\n
    '''
def configure():
    '''returns None\n\n
    configure(final Properties configData)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initLandlordUserInfo():
    '''returns None\n\n
    initLandlordUserInfo()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def authenticateUser():
    '''returns UserInfo\n\n
    authenticateUser(final String user, final String password, final String clientHostAddr)\n
    authenticateUser(final String user, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)\n
    authenticateUser(final String user, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)\n
    authenticateUser(final String loginID, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)\n
    authenticateUser(final String loginID, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)\n
    authenticateUser(final String userIdentity)\n
    authenticateUser(final String userIdentity, final boolean silentLogin)\n
    '''
def authenticateUserM():
    '''returns UserInfo\n\n
    authenticateUserM(final String[] user, final String password, final String clientHostAddr)\n
    authenticateUserM(final String[] user, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)\n
    authenticateUserM(final String[] user, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)\n
    authenticateUserM(final String[] loginID, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)\n
    authenticateUserM(final String[] loginID, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)\n
    authenticateUserM(final String[] userIdentity, final boolean silentLogin)\n
    '''
def authenticateToken():
    '''returns UserInfo\n\n
    authenticateToken()\n
    '''
def authenticateApiKey():
    '''returns UserInfo\n\n
    authenticateApiKey()\n
    authenticateApiKey(final String tenantCode)\n
    authenticateApiKey(final int tenantId)\n
    authenticateApiKey(final String tenantCode, final String userId)\n
    '''
def authenticateThisApiKey():
    '''returns UserInfo\n\n
    authenticateThisApiKey(final String apiKey)\n
    '''
def generateSessionToken():
    '''returns String\n\n
    generateSessionToken(final UserInfo userInfo, final String sessionId)\n
    '''
def authenticateSessionToken():
    '''returns UserInfo\n\n
    authenticateSessionToken(final String userId, final String sessionToken)\n
    '''
def authenticateSessionTokenM():
    '''returns UserInfo\n\n
    authenticateSessionTokenM(final String[] userAndTenant, final String sessionToken)\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo(final AuthenticatedAccessToken session, final Object cert, final Locale locale, final TimeZone timeZone)\n
    getUserInfo(final AuthenticatedAccessToken session, final Object cert, final Locale locale, final TimeZone timeZone, final String clientHost, final String clientAddr)\n
    getUserInfo(final AuthenticatedAccessToken session, final Locale locale, final TimeZone timeZone)\n
    getUserInfo(final AuthenticatedAccessToken session, final Locale locale, final TimeZone timeZone, String clientHost, String clientAddr)\n
    getUserInfo(String userIdentity)\n
    getUserInfo()\n
    '''
def authenticateUserForLoginID():
    '''returns UserInfo\n\n
    authenticateUserForLoginID(final String loginID, final boolean silentLogin)\n
    authenticateUserForLoginID(final String[] loginID, final boolean silentLogin)\n
    '''
def authenticateUserForLoginIDAndTenantID():
    '''returns UserInfo\n\n
    authenticateUserForLoginIDAndTenantID(final String[] loginID, final boolean silentLogin)\n
    '''
def authenticateUserMTenantID():
    '''returns UserInfo\n\n
    authenticateUserMTenantID(final String[] userIdentity, final boolean silentLogin)\n
    '''
def isUser():
    '''returns boolean\n\n
    isUser(final UserInfo userinfo, final String loginCheck, final String passCheck)\n
    '''
def checkConcurrentUser():
    '''returns None\n\n
    checkConcurrentUser(final String userId, String loginID)\n
    '''
def getSystemUserInfo():
    '''returns UserInfo\n\n
    getSystemUserInfo()\n
    '''
def isSystemUserInfo():
    '''returns boolean\n\n
    isSystemUserInfo(final UserInfo ui)\n
    '''
def setSystemCredential():
    '''returns None\n\n
    setSystemCredential(final UserInfo uiObject)\n
    '''
def getProfile():
    '''returns Profile\n\n
    getProfile(final UserInfo userInfo)\n
    getProfile(String userID)\n
    getProfile()\n
    getProfile(final boolean instanciateNew)\n
    '''
def refreshProfile():
    '''returns None\n\n
    refreshProfile(final UserInfo userInfo, final Profile profile)\n
    refreshProfile(final String userID, final Profile profile)\n
    refreshProfile(final Profile newProfile)\n
    '''
def refreshSecurityInfo():
    '''returns None\n\n
    refreshSecurityInfo(final String userID, final MboRemote userMbo, final MboRemote personMbo)\n
    '''
def getDBUrl():
    '''returns String\n\n
    getDBUrl()\n
    '''
def disconnectUser():
    '''returns None\n\n
    disconnectUser(final UserInfo userInfo)\n
    disconnectUser(final UserInfo userInfo, final int disconnectType)\n
    disconnectUser(final String userid, final long maxsessionid, final int disconnectType, final String adminUserID)\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final String url)\n
    '''
def isAppService():
    '''returns boolean\n\n
    isAppService()\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def isSingletonService():
    '''returns boolean\n\n
    isSingletonService()\n
    '''
def getSessionCounter():
    '''returns int\n\n
    getSessionCounter()\n
    getSessionCounter()\n
    '''
def isValidTenant():
    '''returns boolean\n\n
    isValidTenant(final String tenantCode)\n
    '''
def getTenantCode():
    '''returns String\n\n
    getTenantCode(final UserInfo ui)\n
    '''
def reloadTenantReg():
    '''returns None\n\n
    reloadTenantReg(final String tenantCode)\n
    '''
def getTempUserInfoForTenant():
    '''returns UserInfo\n\n
    getTempUserInfoForTenant(final UserInfo landlordUserInfo, final int tenantID, final String tenantUserName, final String tenantLoginID, final String dbUserName, final Locale l, final String langCode)\n
    '''
def createDb2TenantDbUserId():
    '''returns boolean\n\n
    createDb2TenantDbUserId(final UserInfo landlordUi, final String tenantDbUserId)\n
    '''
def isValidDBUserForMT():
    '''returns boolean\n\n
    isValidDBUserForMT(final UserInfo landlordUI, final String dbUserName)\n
    '''
def getDBUserNameForTenant():
    '''returns String\n\n
    getDBUserNameForTenant(final UserInfo landlordUserInfo)\n
    '''
def getMasterMboValueInfo():
    '''returns MboValueInfo\n\n
    getMasterMboValueInfo(final MboRemote tenantMbo)\n
    '''
def getMasterConfigLevel():
    '''returns int\n\n
    getMasterConfigLevel()\n
    '''
def resetSystemUserInfo():
    '''returns None\n\n
    resetSystemUserInfo()\n
    '''
def getRealmName():
    '''returns String\n\n
    getRealmName()\n
    '''
def allowNewSessions():
    '''returns boolean\n\n
    allowNewSessions()\n
    allowNewSessions()\n
    '''
def getAllowNewSessions():
    '''returns AllowNewSessions\n\n
    getAllowNewSessions()\n
    '''
def processVMMParameters():
    '''returns None\n\n
    processVMMParameters(final LoadVMMSyncSettings settings)\n
    '''
def checkUniqueLoginID():
    '''returns None\n\n
    checkUniqueLoginID(String loginID)\n
    '''
def associateTenantsToConsultant():
    '''returns None\n\n
    associateTenantsToConsultant(final String loginID, final List<ConsultantInfo> alltenants)\n
    '''
def populateConsultantFields():
    '''returns None\n\n
    populateConsultantFields(final String origLoginID, final String newLoginID, final MboRemote landlordMbo)\n
    populateConsultantFields(final MboRemote landlordMbo, final MboRemote tenantMbo)\n
    '''
def processConsultant():
    '''returns None\n\n
    processConsultant(final MboRemote consultMbo, final boolean isConsultant, final boolean validate)\n
    '''
def checkIfUserLoaded():
    '''returns boolean\n\n
    checkIfUserLoaded(String loginID, final int intendedTenancy)\n
    '''
def changeToAdminUser():
    '''returns Connection\n\n
    changeToAdminUser(final UserInfo lndlordInfo)\n
    '''
def isValidDBUser():
    '''returns boolean\n\n
    isValidDBUser(final UserInfo lndlordInfo, final String tenantDbUserId)\n
    '''
def registerConsultantUserListener():
    '''returns None\n\n
    registerConsultantUserListener()\n
    '''
def isConsultantFieldModified():
    '''returns boolean\n\n
    isConsultantFieldModified(final MboRemote landlordMbo)\n
    '''
def blockConsultantUser():
    '''returns None\n\n
    blockConsultantUser(final MboRemote landlordUser)\n
    '''
def getLtpaToken():
    '''returns String\n\n
    getLtpaToken(final HttpServletRequest request)\n
    '''
def validateLtpaToken():
    '''returns None\n\n
    validateLtpaToken(final HttpServletRequest request)\n
    '''
def invalidateLtpaToken():
    '''returns None\n\n
    invalidateLtpaToken(final HttpServletRequest request)\n
    '''
def setLastUsed():
    '''returns None\n\n
    setLastUsed(final Date date)\n
    setLastUsed(final Date date, final long maxsessionid)\n
    '''
def getLastUsed():
    '''returns Date\n\n
    getLastUsed()\n
    getLastUsed(final long maxsessionid)\n
    '''
def removeSession():
    '''returns None\n\n
    removeSession(final long maxsessionid)\n
    '''
def refreshUserInfo():
    '''returns None\n\n
    refreshUserInfo(final UserInfo newUserInfo)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    '''
def masterAllowNewSessions():
    '''returns boolean\n\n
    masterAllowNewSessions()\n
    '''
