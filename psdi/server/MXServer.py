serverTimeStampUpdateRate = "int  60"
HTML_CONTENT = "String  text/html""
TEXT_CONTENT = "String  text/plain""
MTENABLEDPROPERTY = "String  mxe.mt.enabled""
REQ_PARAM_S2STOKEN = "String  s2stoken""
API_KEY = "String  apikey""
def getMXServer():
'''public static MXServer getMXServer()
'''
pass
def getUID():
'''public static synchronized Object getUID()
'''
pass
def getMaxSessionID():
'''public static synchronized long getMaxSessionID()
'''
pass
def getGuid():
'''public UUID getGuid()
'''
pass
def getServerHost():
'''public String getServerHost()
'''
pass
def setServerHost():
'''public void setServerHost(final String address)
'''
pass
def addToMaximoCache():
'''public void addToMaximoCache(final String name, final MaximoCache obj)
'''
pass
def removeFromMaximoCache():
'''public void removeFromMaximoCache(final String name)
'''
pass
def getFromMaximoCache():
'''public Object getFromMaximoCache(final String name)
'''
pass
def reloadMaximoCache():
'''public void reloadMaximoCache(final boolean flag)
public void reloadMaximoCache(final String cacheName, final boolean updateAllServers)
public void reloadMaximoCache(final String cacheName, final String key, final boolean flag)
'''
pass
def unloadTenantCache():
'''public void unloadTenantCache()
public void unloadTenantCache(final String cacheName)
'''
pass
def unloadInactiveCaches():
'''public void unloadInactiveCaches(final long interval)
'''
pass
def getLoadedTenants():
'''public Map<String, Set<String>> getLoadedTenants()
public Set<String> getLoadedTenants(final String cacheName)
'''
pass
def reloadAdminModeByThread():
'''public void reloadAdminModeByThread(final String key, final MboRemote listenerMbo)
'''
pass
def destroy():
'''public void destroy()
'''
pass
def getValidApps():
'''public HashSet getValidApps()
'''
pass
def isValidApp():
'''public boolean isValidApp(final String app)
'''
pass
def addApp():
'''public void addApp(final String app)
'''
pass
def removeApp():
'''public void removeApp(final String app)
'''
pass
def getLicenseKeys():
'''public HashSet getLicenseKeys()
'''
pass
def isReadOnlyApp():
'''public boolean isReadOnlyApp(final String app)
'''
pass
def getSystemType():
'''public String getSystemType()
'''
pass
def isPermanentLicense():
'''public boolean isPermanentLicense()
'''
pass
def getProductKeys():
'''public HashSet getProductKeys()
'''
pass
def getEvalDaysRemaining():
'''public int getEvalDaysRemaining()
'''
pass
def getBranding():
'''public int getBranding()
'''
pass
def getPackagingInfo():
'''public void getPackagingInfo(final UserInfo ui)
'''
pass
def getMaxupgValue():
'''public String getMaxupgValue()
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name, final UserInfo user)
'''
pass
def init():
'''public void init(final Connection sysCon)
'''
pass
def getEventTopicTree():
'''public static EventTopicTree getEventTopicTree()
'''
pass
def getEventTopicsCache():
'''public static Map getEventTopicsCache()
'''
pass
def getGlobalEventTopicsCache():
'''public static Map getGlobalEventTopicsCache()
'''
pass
def getMaximoCacheNames():
'''public Set<String> getMaximoCacheNames()
'''
pass
def run():
'''public void run()
public void run()
public void run()
public void run()
'''
pass
def getDBManager():
'''public DBManager getDBManager()
'''
pass
def getCronTaskManager():
'''public CronTaskManager getCronTaskManager()
'''
pass
def getNewCronTaskManager():
'''public CronTaskManager getNewCronTaskManager()
'''
pass
def isAdminModeOn():
'''public boolean isAdminModeOn(final boolean allInstances)
'''
pass
def isAdminModeOff():
'''public boolean isAdminModeOff(final boolean allInstances)
'''
pass
def isAdminModePending():
'''public boolean isAdminModePending()
'''
pass
def listenToAdmin():
'''public void listenToAdmin(final MboRemote listenerMbo, final boolean listen)
'''
pass
def getMaximoDD():
'''public MaximoDD getMaximoDD()
'''
pass
def getMaximoMLDD():
'''public MaximoMLDD getMaximoMLDD()
'''
pass
def getMaxMessageCache():
'''public MaxMessageCache getMaxMessageCache()
'''
pass
def getAutoKeyCache():
'''public AutoKeyCache getAutoKeyCache()
'''
pass
def getAppServiceNames():
'''public String[] getAppServiceNames()
'''
pass
def lookup():
'''public ServiceRemote lookup(final String name)
public ServiceRemote lookup(final String name, final UserInfo ui)
'''
pass
def lookupLocal():
'''public ServiceRemote lookupLocal(final String name)
'''
pass
def getLocalAppList():
'''public String[] getLocalAppList()
'''
pass
def getSrvComm():
'''public SrvCommRemote getSrvComm(final String name, final String passwd)
'''
pass
def getRemoteUsers():
'''public Hashtable getRemoteUsers()
'''
pass
def getDate():
'''public Date getDate()
public Date getDate(final Locale l, final TimeZone tz)
'''
pass
def isRMIEnabled():
'''public static boolean isRMIEnabled()
'''
pass
def start():
'''public static void start(final Properties propsFromFile)
'''
pass
def isMTEnabled():
'''public static boolean isMTEnabled()
'''
pass
def isBotcInstalled():
'''public static boolean isBotcInstalled()
'''
pass
def isInlineThreadLog():
'''public static boolean isInlineThreadLog()
'''
pass
def useClassicMaximo():
'''public static boolean useClassicMaximo()
'''
pass
def hasFeatureToggle():
'''public static boolean hasFeatureToggle()
'''
pass
def setTenantRegContext():
'''public static void setTenantRegContext(final Integer tenantID)
'''
pass
def isTenantRegContext():
'''public static boolean isTenantRegContext()
'''
pass
def setTenantContext():
'''public static void setTenantContext(final UserInfo ui)
public static int setTenantContext(final UserInfo ui, final int tenantID)
'''
pass
def clearTenantContext():
'''public static void clearTenantContext()
'''
pass
def getTenantContext():
'''public static int getTenantContext()
public static int getTenantContext(final boolean tenantNotSetCheck)
'''
pass
def isMasterContext():
'''public static boolean isMasterContext()
'''
pass
def removeMaxSessionEntriesDeadForAnHour():
'''public void removeMaxSessionEntriesDeadForAnHour(final Connection con)
'''
pass
def retryAsyncTask():
'''public void retryAsyncTask(final Connection con, final String serverName, final String serverHost)
'''
pass
def getMAXUPGValue():
'''public String getMAXUPGValue(final Connection con, final String name)
'''
pass
def needToRunUpdateDB():
'''public void needToRunUpdateDB(final String product, final String maxupg, final String newRelDBVersion, final String lastRelDBVersion, final String varName, final boolean checkHF)
'''
pass
def getConfig():
'''public Properties getConfig()
public Properties getConfig(final UserInfo userInfo)
'''
pass
def getProperty():
'''public String getProperty(final String propName)
public String getProperty(final String propName, final boolean checkExists)
public String getProperty(final String propName, final UserInfo userInfo)
public String getProperty(final String propName, final String lang)
public String getProperty(final String propName, final String lang, final UserInfo userInfo)
'''
pass
def getPublicProperty():
'''public String getPublicProperty(final String propName)
public String getPublicProperty(final String propName, final String lang)
'''
pass
def getSystemUserInfo():
'''public UserInfo getSystemUserInfo()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo(final String userIdentity)
'''
pass
def enableService():
'''public void enableService(final String svc)
'''
pass
def disableService():
'''public void disableService(final String svc)
'''
pass
def getURL():
'''public String getURL()
'''
pass
def getRegistryHostName():
'''public String getRegistryHostName()
'''
pass
def getRegistryPort():
'''public String getRegistryPort()
'''
pass
def getMXServerInfo():
'''public MXServerInfo getMXServerInfo()
'''
pass
def getName():
'''public String getName()
'''
pass
def validateS2stokenConfigValue():
'''public void validateS2stokenConfigValue()
'''
pass
def validateThisApiKeyConfigValue():
'''public String validateThisApiKeyConfigValue(final String apiKey)
'''
pass
def resolveApiKey():
'''public String resolveApiKey(final String apikey)
'''
pass
def validateApiKeyConfigValue():
'''public String validateApiKeyConfigValue()
'''
pass
def isLocal():
'''public boolean isLocal(final String serviceUrl)
'''
pass
def createMXTransaction():
'''public MXTransaction createMXTransaction()
'''
pass
def getBulletinBoard():
'''public static BulletinBoardServiceRemote getBulletinBoard()
'''
pass
def sendEMail():
'''public static void sendEMail(final String to, final String from, final String subject, final Throwable t)
public static void sendEMail(final String to, final String from, final String subject, final String message)
public static void sendEMail(final String to, final String from, final String subject, final String message, final String attachment, final String filename)
public static void sendEMail(final String[] to, final String from, final String subject, final Throwable t)
public static void sendEMail(final String[] to, final String from, final String subject, final String message)
public static void sendEMail(final String[] to, final String from, String subject, String message, final String attachment, final String filename)
public static void sendEMail(final String to, final String cc, final String bcc, final String from, final String subject, final String message, final String ReplyTo, final String[] fileName, final String[] urlName)
public static void sendEMail(final String to, final String cc, final String bcc, final String from, String subject, String message, final String ReplyTo, final String[] fileName, final String[] urlName, final Properties overrideProps)
'''
pass
def getSystemProperties():
'''public Properties getSystemProperties()
'''
pass
def getDatabaseProductName():
'''public String getDatabaseProductName()
'''
pass
def getDatabaseProductSimpleVersion():
'''public String getDatabaseProductSimpleVersion()
'''
pass
def getDatabaseProductVersion():
'''public String getDatabaseProductVersion()
'''
pass
def getDBPlatform():
'''public int getDBPlatform()
'''
pass
def getDBConnUsed():
'''public int getDBConnUsed()
'''
pass
def getFreeMemory():
'''public String[] getFreeMemory()
'''
pass
def getUserLicenseKey():
'''public String getUserLicenseKey()
'''
pass
def getAppServerNameandVersion():
'''public String getAppServerNameandVersion()
'''
pass
def getMEAServerVersion():
'''public ArrayList getMEAServerVersion()
'''
pass
def getMXServerVersion():
'''public String[] getMXServerVersion()
'''
pass
def isValidSite():
'''public boolean isValidSite(final String siteId)
'''
pass
def isValidOrganization():
'''public boolean isValidOrganization(final String orgId)
'''
pass
def isSiteInOrganization():
'''public boolean isSiteInOrganization(final String siteId, final String orgId)
'''
pass
def getOrganization():
'''public String getOrganization(final String siteId)
'''
pass
def isMxserverStarted():
'''public boolean isMxserverStarted()
'''
pass
def checkAdminRestart():
'''public void checkAdminRestart()
'''
pass
def checkFailedTenants():
'''public void checkFailedTenants()
'''
pass
def getMXCipher():
'''public MXCipher getMXCipher()
'''
pass
def encData():
'''public byte[] encData(final String in, final int type)
'''
pass
def getMXCipherX():
'''public MXCipherX getMXCipherX()
'''
pass
def getNativeSql():
'''public String getNativeSql(final String jdbcSql)
'''
pass
def getBulletin():
'''public UserInputBulletin getBulletin()
'''
pass
def postUserInput():
'''public void postUserInput(final String id, final Object value, final UserInfo ui)
'''
pass
def getUserInput():
'''public Object getUserInput(final String id, final UserInfo ui)
'''
pass
def removeUserInput():
'''public void removeUserInput(final String id, final UserInfo ui)
'''
pass
def clearUserInput():
'''public void clearUserInput(final UserInfo ui)
'''
pass
def getBaseLang():
'''public String getBaseLang()
'''
pass
def getLanguageList():
'''public String[][] getLanguageList()
'''
pass
def getMessage():
'''public String getMessage(final String group, final String key, String langCode)
public String getMessage(final MXException mxe, final String langCode)
'''
pass
def getTaggedMessage():
'''public String getTaggedMessage(final String group, final String key, String langCode)
public String getTaggedMessage(final MXException mxe, final String langCode)
'''
pass
def getMessages():
'''public String[] getMessages(final String group, final String[] key, final String langCode)
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
def getWarnings():
'''public ArrayList getWarnings(final Object id)
'''
pass
def clearWarnings():
'''public void clearWarnings(final Object id)
'''
pass
def addWarning():
'''public void addWarning(final MXException e, final Object id)
'''
pass
def hasWarnings():
'''public boolean hasWarnings(final Object id)
'''
pass
def incrementMboCount():
'''public void incrementMboCount(final String name, final int tenantID)
'''
pass
def decrementMboCount():
'''public void decrementMboCount(final String name, final int tenantID)
'''
pass
def incrementMbosetCount():
'''public void incrementMbosetCount(final String name, final int tenantID)
'''
pass
def decrementMbosetCount():
'''public void decrementMbosetCount(final String name)
public void decrementMbosetCount(final String name, final int tenantID)
'''
pass
def incrementMbosetIPCount():
'''public void incrementMbosetIPCount(String objName, final String clientHost, final String clientAddr)
'''
pass
def decrementMbosetIPCount():
'''public void decrementMbosetIPCount(String objName, final String clientHost, final String clientAddr)
'''
pass
def getMboSetIPCount():
'''public int getMboSetIPCount(String objName, final String clientHost, final String clientAddr)
'''
pass
def printMaxsessionInfo():
'''public String printMaxsessionInfo()
'''
pass
def getMboCount():
'''public String getMboCount()
'''
pass
def getMboSetCount():
'''public int getMboSetCount(String objName)
'''
pass
def getAllTenantsMboCountAsJSON():
'''public JSONObject getAllTenantsMboCountAsJSON()
'''
pass
def getConditionCache():
'''public MaxConditionCache getConditionCache()
'''
pass
def getDataRestrictionCache():
'''public DataRestrictionCache getDataRestrictionCache()
'''
pass
def getMaxDomainCache():
'''public MaxDomainCache getMaxDomainCache()
'''
pass
def setupLongOpPipe():
'''public InputStream setupLongOpPipe()
'''
pass
def clearLongOpPipe():
'''public void clearLongOpPipe()
'''
pass
def writeLongOpMsg():
'''public void writeLongOpMsg(String msg)
'''
pass
def getSQLServerPrefetchRows():
'''public int getSQLServerPrefetchRows()
'''
pass
def getSecurityContext():
'''public SecurityContextFlag getSecurityContext()
'''
pass
def clearSecurityContext():
'''public void clearSecurityContext()
'''
pass
def setSecurityCheck():
'''public void setSecurityCheck(final SecurityContextFlag securityFlag)
'''
pass
def isSQLServerPrefetchRowsNeeded():
'''public boolean isSQLServerPrefetchRowsNeeded()
'''
pass
def getMxServerConfig():
'''public Properties getMxServerConfig()
'''
pass
def getServerCommandRemote():
'''public SrvCommRemote getServerCommandRemote(final String name, final String passwd)
public SrvCommRemote getServerCommandRemote(final UserInfo userInfo)
'''
pass
def getMboCounts():
'''public ArrayList getMboCounts()
public ArrayList getMboCounts(final int tenantID)
'''
pass
def getMailAuth():
'''public static SmtpAuthenticator getMailAuth()
'''
pass
def getBaseCalendar():
'''public String getBaseCalendar()
'''
pass
def getTenantIdsList():
'''public List<Integer> getTenantIdsList(final UserInfo landlordInfo, final int status)
'''
pass
def getAllTenantIdsList():
'''public List<Integer> getAllTenantIdsList(final UserInfo landlordInfo)
'''
pass
def collectTenantDBConnInfo():
'''public void collectTenantDBConnInfo(final UserInfo info)
'''
pass
def collectTenantDBConForThisServer():
'''public void collectTenantDBConForThisServer(final UserInfo info)
'''
pass
def setProxy():
'''public void setProxy(final Remote proxy)
'''
pass
def getProxy():
'''public Remote getProxy()
'''
pass
def getTenantRealmMap():
'''public HashMap<String, String> getTenantRealmMap()
'''
pass
def clearTenantRealmMap():
'''public void clearTenantRealmMap()
'''
pass
def loadCustomApps():
'''public void loadCustomApps()
public void loadCustomApps(final Connection con)
'''
pass
def AdminModeThread():
'''public AdminModeThread()
'''
pass
def setKey():
'''public void setKey(final String value)
'''
pass
def UnloadInactiveCachesThread():
'''public UnloadInactiveCachesThread()
'''
pass
def SmtpAuthenticator():
'''public SmtpAuthenticator(final String user, final String password)
'''
pass
def DBConnStatThread():
'''public DBConnStatThread(final UserInfo infoT)
'''
pass
