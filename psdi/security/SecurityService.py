SAMESYSTEMCONNECTIONKEYPERTHREAD = "String  SameSystemConnectionKeyPerThread""
TENANTDBUSERNAMETOKEN = "String  TENANTDBUSERNAME""
LANDLORDTENANTID = "int  2"
def SecurityService():
'''public SecurityService(final MXServer mxServer)
public SecurityService(final String url)
public SecurityService(final String url, final MXServer mxServer)
'''
pass
def configure():
'''public void configure(final Properties configData)
'''
pass
def init():
'''public void init()
'''
pass
def initLandlordUserInfo():
'''public void initLandlordUserInfo()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def authenticateUser():
'''public UserInfo authenticateUser(final String user, final String password, final String clientHostAddr)
public UserInfo authenticateUser(final String user, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
public UserInfo authenticateUser(final String user, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
public UserInfo authenticateUser(final String loginID, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
public UserInfo authenticateUser(final String loginID, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
public UserInfo authenticateUser(final String userIdentity)
public UserInfo authenticateUser(final String userIdentity, final boolean silentLogin)
'''
pass
def authenticateUserM():
'''public UserInfo authenticateUserM(final String[] user, final String password, final String clientHostAddr)
public UserInfo authenticateUserM(final String[] user, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
public UserInfo authenticateUserM(final String[] user, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String clientHostAddr)
public UserInfo authenticateUserM(final String[] loginID, final Object cert, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
public UserInfo authenticateUserM(final String[] loginID, final String password, final Locale locale, final TimeZone timeZone, final String siteId, final String clientHostAddr)
public UserInfo authenticateUserM(final String[] userIdentity, final boolean silentLogin)
'''
pass
def authenticateToken():
'''public UserInfo authenticateToken()
'''
pass
def authenticateApiKey():
'''public UserInfo authenticateApiKey()
public UserInfo authenticateApiKey(final String tenantCode)
public UserInfo authenticateApiKey(final int tenantId)
public UserInfo authenticateApiKey(final String tenantCode, final String userId)
'''
pass
def authenticateThisApiKey():
'''public UserInfo authenticateThisApiKey(final String apiKey)
'''
pass
def generateSessionToken():
'''public String generateSessionToken(final UserInfo userInfo, final String sessionId)
'''
pass
def authenticateSessionToken():
'''public UserInfo authenticateSessionToken(final String userId, final String sessionToken)
'''
pass
def authenticateSessionTokenM():
'''public UserInfo authenticateSessionTokenM(final String[] userAndTenant, final String sessionToken)
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Object cert, final Locale locale, final TimeZone timeZone)
public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Object cert, final Locale locale, final TimeZone timeZone, final String clientHost, final String clientAddr)
public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Locale locale, final TimeZone timeZone)
public UserInfo getUserInfo(final AuthenticatedAccessToken session, final Locale locale, final TimeZone timeZone, String clientHost, String clientAddr)
public UserInfo getUserInfo(String userIdentity)
public UserInfo getUserInfo()
'''
pass
def authenticateUserForLoginID():
'''public UserInfo authenticateUserForLoginID(final String loginID, final boolean silentLogin)
public UserInfo authenticateUserForLoginID(final String[] loginID, final boolean silentLogin)
'''
pass
def authenticateUserForLoginIDAndTenantID():
'''public UserInfo authenticateUserForLoginIDAndTenantID(final String[] loginID, final boolean silentLogin)
'''
pass
def authenticateUserMTenantID():
'''public UserInfo authenticateUserMTenantID(final String[] userIdentity, final boolean silentLogin)
'''
pass
def isUser():
'''public boolean isUser(final UserInfo userinfo, final String loginCheck, final String passCheck)
'''
pass
def checkConcurrentUser():
'''public void checkConcurrentUser(final String userId, String loginID)
'''
pass
def getSystemUserInfo():
'''public UserInfo getSystemUserInfo()
'''
pass
def isSystemUserInfo():
'''public boolean isSystemUserInfo(final UserInfo ui)
'''
pass
def setSystemCredential():
'''public void setSystemCredential(final UserInfo uiObject)
'''
pass
def getProfile():
'''public ProfileRemote getProfile(final UserInfo userInfo)
public ProfileRemote getProfile(String userID)
public Profile getProfile()
public Profile getProfile(final boolean instanciateNew)
'''
pass
def refreshProfile():
'''public void refreshProfile(final UserInfo userInfo, final Profile profile)
public void refreshProfile(final String userID, final Profile profile)
public void refreshProfile(final Profile newProfile)
'''
pass
def refreshSecurityInfo():
'''public void refreshSecurityInfo(final String userID, final MboRemote userMbo, final MboRemote personMbo)
'''
pass
def getDBUrl():
'''public String getDBUrl()
'''
pass
def disconnectUser():
'''public void disconnectUser(final UserInfo userInfo)
public void disconnectUser(final UserInfo userInfo, final int disconnectType)
public void disconnectUser(final String userid, final long maxsessionid, final int disconnectType, final String adminUserID)
'''
pass
def getURL():
'''public String getURL()
'''
pass
def setURL():
'''public void setURL(final String url)
'''
pass
def isAppService():
'''public boolean isAppService()
'''
pass
def restart():
'''public void restart()
'''
pass
def isSingletonService():
'''public boolean isSingletonService()
'''
pass
def getSessionCounter():
'''public int getSessionCounter()
public int getSessionCounter()
'''
pass
def isValidTenant():
'''public boolean isValidTenant(final String tenantCode)
'''
pass
def getTenantCode():
'''public String getTenantCode(final UserInfo ui)
'''
pass
def isLandlord():
'''public static boolean isLandlord(final int tenantID)
'''
pass
def reloadTenantReg():
'''public void reloadTenantReg(final String tenantCode)
'''
pass
def getTempUserInfoForTenant():
'''public UserInfo getTempUserInfoForTenant(final UserInfo landlordUserInfo, final int tenantID, final String tenantUserName, final String tenantLoginID, final String dbUserName, final Locale l, final String langCode)
'''
pass
def createDb2TenantDbUserId():
'''public boolean createDb2TenantDbUserId(final UserInfo landlordUi, final String tenantDbUserId)
'''
pass
def isValidDBUserForMT():
'''public boolean isValidDBUserForMT(final UserInfo landlordUI, final String dbUserName)
'''
pass
def getDBUserNameForTenant():
'''public String getDBUserNameForTenant(final UserInfo landlordUserInfo)
'''
pass
def getMasterModifiedObjects():
'''public Map<String, String> getMasterModifiedObjects()
'''
pass
def getMasterMboValueInfo():
'''public MboValueInfo getMasterMboValueInfo(final MboRemote tenantMbo)
'''
pass
def createExtensionView():
'''public Map<String, String> createExtensionView(final Map<String, Map<String, Map<String, String>>> tableNames, final Set<String> deleteTables)
'''
pass
def getMasterConfigLevel():
'''public int getMasterConfigLevel()
'''
pass
def resetSystemUserInfo():
'''public void resetSystemUserInfo()
'''
pass
def getRealmName():
'''public String getRealmName()
'''
pass
def allowNewSessions():
'''public boolean allowNewSessions()
public boolean allowNewSessions()
'''
pass
def getAllowNewSessions():
'''public AllowNewSessions getAllowNewSessions()
'''
pass
def processVMMParameters():
'''public void processVMMParameters(final LoadVMMSyncSettings settings)
'''
pass
def checkUniqueLoginID():
'''public void checkUniqueLoginID(String loginID)
'''
pass
def associateTenantsToConsultant():
'''public void associateTenantsToConsultant(final String loginID, final List<ConsultantInfo> alltenants)
'''
pass
def populateConsultantFields():
'''public void populateConsultantFields(final String origLoginID, final String newLoginID, final MboRemote landlordMbo)
public void populateConsultantFields(final MboRemote landlordMbo, final MboRemote tenantMbo)
'''
pass
def loadCopyFieldsInfo():
'''public Map<String, List<List<String>>> loadCopyFieldsInfo()
'''
pass
def processConsultant():
'''public void processConsultant(final MboRemote consultMbo, final boolean isConsultant, final boolean validate)
'''
pass
def checkIfUserLoaded():
'''public boolean checkIfUserLoaded(String loginID, final int intendedTenancy)
'''
pass
def changeToAdminUser():
'''public Connection changeToAdminUser(final UserInfo lndlordInfo)
'''
pass
def isValidDBUser():
'''public boolean isValidDBUser(final UserInfo lndlordInfo, final String tenantDbUserId)
'''
pass
def registerConsultantUserListener():
'''public void registerConsultantUserListener()
'''
pass
def isConsultantFieldModified():
'''public boolean isConsultantFieldModified(final MboRemote landlordMbo)
'''
pass
def blockConsultantUser():
'''public void blockConsultantUser(final MboRemote landlordUser)
'''
pass
def getLtpaToken():
'''public String getLtpaToken(final HttpServletRequest request)
'''
pass
def killLtpaToken():
'''public static boolean killLtpaToken()
'''
pass
def validateLtpaToken():
'''public void validateLtpaToken(final HttpServletRequest request)
'''
pass
def invalidateLtpaToken():
'''public void invalidateLtpaToken(final HttpServletRequest request)
'''
pass
def SecurityInfo():
'''public SecurityInfo(final UserInfo ui)
'''
pass
def setLastUsed():
'''public void setLastUsed(final Date date)
public void setLastUsed(final Date date, final long maxsessionid)
'''
pass
def getLastUsed():
'''public Date getLastUsed()
public Date getLastUsed(final long maxsessionid)
'''
pass
def getSessions():
'''public Map<Long, Date> getSessions()
'''
pass
def removeSession():
'''public void removeSession(final long maxsessionid)
'''
pass
def refreshUserInfo():
'''public void refreshUserInfo(final UserInfo newUserInfo)
'''
pass
def UserMonitor():
'''public UserMonitor()
'''
pass
def run():
'''public void run()
public void run()
public void run()
'''
pass
def SessionCounter():
'''public SessionCounter()
'''
pass
def masterAllowNewSessions():
'''public boolean masterAllowNewSessions()
'''
pass
def LtpaTokenMonitor():
'''public LtpaTokenMonitor()
'''
pass
