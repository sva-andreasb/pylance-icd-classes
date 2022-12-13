SAMESYSTEMCONNECTIONKEYPERTHREAD = "String  \"SameSystemConnectionKeyPerThread\""
TENANTDBUSERNAMETOKEN = "String  \"TENANTDBUSERNAME\""
LANDLORDTENANTID = "int  2"
def SecurityService():
    '''    public SecurityService(final MXServer mxServer)
    public SecurityService(final String url)
    public SecurityService(final String url, final MXServer mxServer)
    '''
def configure():
    '''    public void configure(final Properties configData)
    '''
def init():
    '''    public void init()
    '''
def initLandlordUserInfo():
    '''    public void initLandlordUserInfo()
    '''
def destroy():
    '''    public void destroy()
    '''
def authenticateUser():
    '''    public UserInfo authenticateUser(final String user, final String password, final String clientHostAddr)
    public UserInfo authenticateUser(final String user, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
    public UserInfo authenticateUser(final String user, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
    public UserInfo authenticateUser(final String loginID, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
    public UserInfo authenticateUser(final String loginID, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
    public UserInfo authenticateUser(final String userIdentity)
    public UserInfo authenticateUser(final String userIdentity, final boolean silentLogin)
    '''
def authenticateUserM():
    '''    public UserInfo authenticateUserM(final String[] user, final String password, final String clientHostAddr)
    public UserInfo authenticateUserM(final String[] user, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
    public UserInfo authenticateUserM(final String[] user, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
    public UserInfo authenticateUserM(final String[] loginID, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
    public UserInfo authenticateUserM(final String[] loginID, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
    public UserInfo authenticateUserM(final String[] userIdentity, final boolean silentLogin)
    '''
def authenticateToken():
    '''    public UserInfo authenticateToken()
    '''
def authenticateApiKey():
    '''    public UserInfo authenticateApiKey()
    public UserInfo authenticateApiKey(final String tenantCode)
    public UserInfo authenticateApiKey(final int tenantId)
    public UserInfo authenticateApiKey(final String tenantCode, final String userId)
    '''
def authenticateThisApiKey():
    '''    public UserInfo authenticateThisApiKey(final String apiKey)
    '''
def generateSessionToken():
    '''    public String generateSessionToken(final UserInfo userInfo, final String sessionId)
    '''
def authenticateSessionToken():
    '''    public UserInfo authenticateSessionToken(final String userId, final String sessionToken)
    '''
def authenticateSessionTokenM():
    '''    public UserInfo authenticateSessionTokenM(final String[] userAndTenant, final String sessionToken)
    '''
def getUserInfo():
    '''    public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Object cert, final Locale locale, final TimeZone timeZone)
    public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Object cert, final Locale locale, final TimeZone timeZone, final String clientHost, final String clientAddr)
    public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Locale locale, final TimeZone timeZone)
    public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Locale locale, final TimeZone timeZone, String clientHost, String clientAddr)
    public UserInfo getUserInfo(String userIdentity)
    public UserInfo getUserInfo()
    '''
def authenticateUserForLoginID():
    '''    public UserInfo authenticateUserForLoginID(final String loginID, final boolean silentLogin)
    public UserInfo authenticateUserForLoginID(final String[] loginID, final boolean silentLogin)
    '''
def authenticateUserForLoginIDAndTenantID():
    '''    public UserInfo authenticateUserForLoginIDAndTenantID(final String[] loginID, final boolean silentLogin)
    '''
def authenticateUserMTenantID():
    '''    public UserInfo authenticateUserMTenantID(final String[] userIdentity, final boolean silentLogin)
    '''
def isUser():
    '''    public boolean isUser(final UserInfo userinfo, final String loginCheck, final String passCheck)
    '''
def checkConcurrentUser():
    '''    public void checkConcurrentUser(final String userId, String loginID)
    '''
def getSystemUserInfo():
    '''    public UserInfo getSystemUserInfo()
    '''
def isSystemUserInfo():
    '''    public boolean isSystemUserInfo(final UserInfo ui)
    '''
def setSystemCredential():
    '''    public void setSystemCredential(final UserInfo uiObject)
    '''
def getProfile():
    '''    public ProfileRemote getProfile(final UserInfo userInfo)
    public ProfileRemote getProfile(String userID)
    public Profile getProfile()
    public Profile getProfile(final boolean instanciateNew)
    '''
def refreshProfile():
    '''    public void refreshProfile(final UserInfo userInfo, final Profile profile)
    public void refreshProfile(final String userID, final Profile profile)
    public void refreshProfile(final Profile newProfile)
    '''
def refreshSecurityInfo():
    '''    public void refreshSecurityInfo(final String userID, final MboRemote userMbo, final MboRemote personMbo)
    '''
def getDBUrl():
    '''    public String getDBUrl()
    '''
def disconnectUser():
    '''    public void disconnectUser(final UserInfo userInfo)
    public void disconnectUser(final UserInfo userInfo, final int disconnectType)
    public void disconnectUser(final String userid, final long maxsessionid, final int disconnectType, final String adminUserID)
    '''
def getURL():
    '''    public String getURL()
    '''
def setURL():
    '''    public void setURL(final String url)
    '''
def isAppService():
    '''    public boolean isAppService()
    '''
def restart():
    '''    public void restart()
    '''
def isSingletonService():
    '''    public boolean isSingletonService()
    '''
def getSessionCounter():
    '''    public int getSessionCounter()
    public int getSessionCounter()
    '''
def isValidTenant():
    '''    public boolean isValidTenant(final String tenantCode)
    '''
def getTenantCode():
    '''    public String getTenantCode(final UserInfo ui)
    '''
def isLandlord():
    '''    public static boolean isLandlord(final int tenantID)
    '''
def reloadTenantReg():
    '''    public void reloadTenantReg(final String tenantCode)
    '''
def getTempUserInfoForTenant():
    '''    public UserInfo getTempUserInfoForTenant(final UserInfo landlordUserInfo, final int tenantID, final String tenantUserName, final String tenantLoginID, final String dbUserName, final Locale l, final String langCode)
    '''
def createDb2TenantDbUserId():
    '''    public boolean createDb2TenantDbUserId(final UserInfo landlordUi, final String tenantDbUserId)
    '''
def isValidDBUserForMT():
    '''    public boolean isValidDBUserForMT(final UserInfo landlordUI, final String dbUserName)
    '''
def getDBUserNameForTenant():
    '''    public String getDBUserNameForTenant(final UserInfo landlordUserInfo)
    '''
def getMasterModifiedObjects():
    '''    public Map<String, String> getMasterModifiedObjects()
    '''
def getMasterMboValueInfo():
    '''    public MboValueInfo getMasterMboValueInfo(final MboRemote tenantMbo)
    '''
def createExtensionView():
    '''    public Map<String, String> createExtensionView(final Map<String, Map<String, Map<String, String>>> tableNames, final Set<String> deleteTables)
    '''
def getMasterConfigLevel():
    '''    public int getMasterConfigLevel()
    '''
def resetSystemUserInfo():
    '''    public void resetSystemUserInfo()
    '''
def getRealmName():
    '''    public String getRealmName()
    '''
def allowNewSessions():
    '''    public boolean allowNewSessions()
    public boolean allowNewSessions()
    '''
def getAllowNewSessions():
    '''    public AllowNewSessions getAllowNewSessions()
    '''
def processVMMParameters():
    '''    public void processVMMParameters(final LoadVMMSyncSettings settings)
    '''
def checkUniqueLoginID():
    '''    public void checkUniqueLoginID(String loginID)
    '''
def associateTenantsToConsultant():
    '''    public void associateTenantsToConsultant(final String loginID, final List<ConsultantInfo> alltenants)
    '''
def populateConsultantFields():
    '''    public void populateConsultantFields(final String origLoginID, final String newLoginID, final MboRemote landlordMbo)
    public void populateConsultantFields(final MboRemote landlordMbo, final MboRemote tenantMbo)
    '''
def loadCopyFieldsInfo():
    '''    public Map<String, List<List<String>>> loadCopyFieldsInfo()
    '''
def processConsultant():
    '''    public void processConsultant(final MboRemote consultMbo, final boolean isConsultant, final boolean validate)
    '''
def checkIfUserLoaded():
    '''    public boolean checkIfUserLoaded(String loginID, final int intendedTenancy)
    '''
def changeToAdminUser():
    '''    public Connection changeToAdminUser(final UserInfo lndlordInfo)
    '''
def isValidDBUser():
    '''    public boolean isValidDBUser(final UserInfo lndlordInfo, final String tenantDbUserId)
    '''
def registerConsultantUserListener():
    '''    public void registerConsultantUserListener()
    '''
def isConsultantFieldModified():
    '''    public boolean isConsultantFieldModified(final MboRemote landlordMbo)
    '''
def blockConsultantUser():
    '''    public void blockConsultantUser(final MboRemote landlordUser)
    '''
def getLtpaToken():
    '''    public String getLtpaToken(final HttpServletRequest request)
    '''
def killLtpaToken():
    '''    public static boolean killLtpaToken()
    '''
def validateLtpaToken():
    '''    public void validateLtpaToken(final HttpServletRequest request)
    '''
def invalidateLtpaToken():
    '''    public void invalidateLtpaToken(final HttpServletRequest request)
    '''
def SecurityInfo():
    '''    public SecurityInfo(final UserInfo ui)
    '''
def setLastUsed():
    '''    public void setLastUsed(final Date date)
    public void setLastUsed(final Date date, final long maxsessionid)
    '''
def getLastUsed():
    '''    public Date getLastUsed()
    public Date getLastUsed(final long maxsessionid)
    '''
def getSessions():
    '''    public Map<Long, Date> getSessions()
    '''
def removeSession():
    '''    public void removeSession(final long maxsessionid)
    '''
def refreshUserInfo():
    '''    public void refreshUserInfo(final UserInfo newUserInfo)
    '''
def UserMonitor():
    '''    public UserMonitor()
    '''
def run():
    '''    public void run()
    public void run()
    public void run()
    '''
def SessionCounter():
    '''    public SessionCounter()
    '''
def masterAllowNewSessions():
    '''    public boolean masterAllowNewSessions()
    '''
def LtpaTokenMonitor():
    '''    public LtpaTokenMonitor()
    '''
