serverTimeStampUpdateRate = "int  60"
HTML_CONTENT = "String  \"text/html\""
TEXT_CONTENT = "String  \"text/plain\""
MTENABLEDPROPERTY = "String  \"mxe.mt.enabled\""
REQ_PARAM_S2STOKEN = "String  \"s2stoken\""
API_KEY = "String  \"apikey\""
def getMXServer():
    '''    public static MXServer getMXServer()
    '''
def getUID():
    '''    public static synchronized Object getUID()
    '''
def getMaxSessionID():
    '''    public static synchronized long getMaxSessionID()
    '''
def getGuid():
    '''    public UUID getGuid()
    '''
def getServerHost():
    '''    public String getServerHost()
    '''
def setServerHost():
    '''    public void setServerHost(final String address)
    '''
def addToMaximoCache():
    '''    public void addToMaximoCache(final String name, final MaximoCache obj)
    '''
def removeFromMaximoCache():
    '''    public void removeFromMaximoCache(final String name)
    '''
def getFromMaximoCache():
    '''    public Object getFromMaximoCache(final String name)
    '''
def reloadMaximoCache():
    '''    public void reloadMaximoCache(final boolean flag)
    public void reloadMaximoCache(final String cacheName, final boolean updateAllServers)
    public void reloadMaximoCache(final String cacheName, final String key, final boolean flag)
    '''
def unloadTenantCache():
    '''    public void unloadTenantCache()
    public void unloadTenantCache(final String cacheName)
    '''
def unloadInactiveCaches():
    '''    public void unloadInactiveCaches(final long interval)
    '''
def getLoadedTenants():
    '''    public Map<String, Set<String>> getLoadedTenants()
    public Set<String> getLoadedTenants(final String cacheName)
    '''
def reloadAdminModeByThread():
    '''    public void reloadAdminModeByThread(final String key, final MboRemote listenerMbo)
    '''
def destroy():
    '''    public void destroy()
    '''
def getValidApps():
    '''    public HashSet getValidApps()
    '''
def isValidApp():
    '''    public boolean isValidApp(final String app)
    '''
def addApp():
    '''    public void addApp(final String app)
    '''
def removeApp():
    '''    public void removeApp(final String app)
    '''
def getLicenseKeys():
    '''    public HashSet getLicenseKeys()
    '''
def isReadOnlyApp():
    '''    public boolean isReadOnlyApp(final String app)
    '''
def getSystemType():
    '''    public String getSystemType()
    '''
def isPermanentLicense():
    '''    public boolean isPermanentLicense()
    '''
def getProductKeys():
    '''    public HashSet getProductKeys()
    '''
def getEvalDaysRemaining():
    '''    public int getEvalDaysRemaining()
    '''
def getBranding():
    '''    public int getBranding()
    '''
def getPackagingInfo():
    '''    public void getPackagingInfo(final UserInfo ui)
    '''
def getMaxupgValue():
    '''    public String getMaxupgValue()
    '''
def getMboSet():
    '''    public MboSetRemote getMboSet(final String name, final UserInfo user)
    '''
def init():
    '''    public void init(final Connection sysCon)
    '''
def getEventTopicTree():
    '''    public static EventTopicTree getEventTopicTree()
    '''
def getEventTopicsCache():
    '''    public static Map getEventTopicsCache()
    '''
def getGlobalEventTopicsCache():
    '''    public static Map getGlobalEventTopicsCache()
    '''
def getMaximoCacheNames():
    '''    public Set<String> getMaximoCacheNames()
    '''
def run():
    '''    public void run()
    public void run()
    public void run()
    public void run()
    '''
def getDBManager():
    '''    public DBManager getDBManager()
    '''
def getCronTaskManager():
    '''    public CronTaskManager getCronTaskManager()
    '''
def getNewCronTaskManager():
    '''    public CronTaskManager getNewCronTaskManager()
    '''
def isAdminModeOn():
    '''    public boolean isAdminModeOn(final boolean allInstances)
    '''
def isAdminModeOff():
    '''    public boolean isAdminModeOff(final boolean allInstances)
    '''
def isAdminModePending():
    '''    public boolean isAdminModePending()
    '''
def listenToAdmin():
    '''    public void listenToAdmin(final MboRemote listenerMbo, final boolean listen)
    '''
def getMaximoDD():
    '''    public MaximoDD getMaximoDD()
    '''
def getMaximoMLDD():
    '''    public MaximoMLDD getMaximoMLDD()
    '''
def getMaxMessageCache():
    '''    public MaxMessageCache getMaxMessageCache()
    '''
def getAutoKeyCache():
    '''    public AutoKeyCache getAutoKeyCache()
    '''
def getAppServiceNames():
    '''    public String[] getAppServiceNames()
    '''
def lookup():
    '''    public ServiceRemote lookup(final String name)
    public ServiceRemote lookup(final String name, final UserInfo ui)
    '''
def lookupLocal():
    '''    public ServiceRemote lookupLocal(final String name)
    '''
def getLocalAppList():
    '''    public String[] getLocalAppList()
    '''
def getSrvComm():
    '''    public SrvCommRemote getSrvComm(final String name, final String passwd)
    '''
def getRemoteUsers():
    '''    public Hashtable getRemoteUsers()
    '''
def getDate():
    '''    public Date getDate()
    public Date getDate(final Locale l, final TimeZone tz)
    '''
def isRMIEnabled():
    '''    public static boolean isRMIEnabled()
    '''
def start():
    '''    public static void start(final Properties propsFromFile)
    '''
def isMTEnabled():
    '''    public static boolean isMTEnabled()
    '''
def isBotcInstalled():
    '''    public static boolean isBotcInstalled()
    '''
def isInlineThreadLog():
    '''    public static boolean isInlineThreadLog()
    '''
def useClassicMaximo():
    '''    public static boolean useClassicMaximo()
    '''
def hasFeatureToggle():
    '''    public static boolean hasFeatureToggle()
    '''
def setTenantRegContext():
    '''    public static void setTenantRegContext(final Integer tenantID)
    '''
def isTenantRegContext():
    '''    public static boolean isTenantRegContext()
    '''
def setTenantContext():
    '''    public static void setTenantContext(final UserInfo ui)
    public static int setTenantContext(final UserInfo ui, final int tenantID)
    '''
def clearTenantContext():
    '''    public static void clearTenantContext()
    '''
def getTenantContext():
    '''    public static int getTenantContext()
    public static int getTenantContext(final boolean tenantNotSetCheck)
    '''
def isMasterContext():
    '''    public static boolean isMasterContext()
    '''
def removeMaxSessionEntriesDeadForAnHour():
    '''    public void removeMaxSessionEntriesDeadForAnHour(final Connection con)
    '''
def retryAsyncTask():
    '''    public void retryAsyncTask(final Connection con, final String serverName, final String serverHost)
    '''
def getMAXUPGValue():
    '''    public String getMAXUPGValue(final Connection con, final String name)
    '''
def needToRunUpdateDB():
    '''    public void needToRunUpdateDB(final String product, final String maxupg, final String newRelDBVersion, final String lastRelDBVersion, final String varName, final boolean checkHF)
    '''
def getConfig():
    '''    public Properties getConfig()
    public Properties getConfig(final UserInfo userInfo)
    '''
def getProperty():
    '''    public String getProperty(final String propName)
    public String getProperty(final String propName, final boolean checkExists)
    public String getProperty(final String propName, final UserInfo userInfo)
    public String getProperty(final String propName, final String lang)
    public String getProperty(final String propName, final String lang, final UserInfo userInfo)
    '''
def getPublicProperty():
    '''    public String getPublicProperty(final String propName)
    public String getPublicProperty(final String propName, final String lang)
    '''
def getSystemUserInfo():
    '''    public UserInfo getSystemUserInfo()
    '''
def getUserInfo():
    '''    public UserInfo getUserInfo(final String userIdentity)
    '''
def enableService():
    '''    public void enableService(final String svc)
    '''
def disableService():
    '''    public void disableService(final String svc)
    '''
def getURL():
    '''    public String getURL()
    '''
def getRegistryHostName():
    '''    public String getRegistryHostName()
    '''
def getRegistryPort():
    '''    public String getRegistryPort()
    '''
def getMXServerInfo():
    '''    public MXServerInfo getMXServerInfo()
    '''
def getName():
    '''    public String getName()
    '''
def validateS2stokenConfigValue():
    '''    public void validateS2stokenConfigValue()
    '''
def validateThisApiKeyConfigValue():
    '''    public String validateThisApiKeyConfigValue(final String apiKey)
    '''
def resolveApiKey():
    '''    public String resolveApiKey(final String apikey)
    '''
def validateApiKeyConfigValue():
    '''    public String validateApiKeyConfigValue()
    '''
def isLocal():
    '''    public boolean isLocal(final String serviceUrl)
    '''
def createMXTransaction():
    '''    public MXTransaction createMXTransaction()
    '''
def getBulletinBoard():
    '''    public static BulletinBoardServiceRemote getBulletinBoard()
    '''
def sendEMail():
    '''    public static void sendEMail(final String to, final String from, final String subject, final Throwable t)
    public static void sendEMail(final String to, final String from, final String subject, final String message)
    public static void sendEMail(final String to, final String from, final String subject, final String message, final String attachment, final String filename)
    public static void sendEMail(final String[] to, final String from, final String subject, final Throwable t)
    public static void sendEMail(final String[] to, final String from, final String subject, final String message)
    public static void sendEMail(final String[] to, final String from, String subject, String message, final String attachment, final String filename)
    public static void sendEMail(final String to, final String cc, final String bcc, final String from, final String subject, final String message, final String ReplyTo, final String[] fileName, final String[] urlName)
    public static void sendEMail(final String to, final String cc, final String bcc, final String from, String subject, String message, final String ReplyTo, final String[] fileName, final String[] urlName, final Properties overrideProps)
    '''
def getSystemProperties():
    '''    public Properties getSystemProperties()
    '''
def getDatabaseProductName():
    '''    public String getDatabaseProductName()
    '''
def getDatabaseProductSimpleVersion():
    '''    public String getDatabaseProductSimpleVersion()
    '''
def getDatabaseProductVersion():
    '''    public String getDatabaseProductVersion()
    '''
def getDBPlatform():
    '''    public int getDBPlatform()
    '''
def getDBConnUsed():
    '''    public int getDBConnUsed()
    '''
def getFreeMemory():
    '''    public String[] getFreeMemory()
    '''
def getUserLicenseKey():
    '''    public String getUserLicenseKey()
    '''
def getAppServerNameandVersion():
    '''    public String getAppServerNameandVersion()
    '''
def getMEAServerVersion():
    '''    public ArrayList getMEAServerVersion()
    '''
def getMXServerVersion():
    '''    public String[] getMXServerVersion()
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
def getOrganization():
    '''    public String getOrganization(final String siteId)
    '''
def isMxserverStarted():
    '''    public boolean isMxserverStarted()
    '''
def checkAdminRestart():
    '''    public void checkAdminRestart()
    '''
def checkFailedTenants():
    '''    public void checkFailedTenants()
    '''
def getMXCipher():
    '''    public MXCipher getMXCipher()
    '''
def encData():
    '''    public byte[] encData(final String in, final int type)
    '''
def getMXCipherX():
    '''    public MXCipherX getMXCipherX()
    '''
def getNativeSql():
    '''    public String getNativeSql(final String jdbcSql)
    '''
def getBulletin():
    '''    public UserInputBulletin getBulletin()
    '''
def postUserInput():
    '''    public void postUserInput(final String id, final Object value, final UserInfo ui)
    '''
def getUserInput():
    '''    public Object getUserInput(final String id, final UserInfo ui)
    '''
def removeUserInput():
    '''    public void removeUserInput(final String id, final UserInfo ui)
    '''
def clearUserInput():
    '''    public void clearUserInput(final UserInfo ui)
    '''
def getBaseLang():
    '''    public String getBaseLang()
    '''
def getLanguageList():
    '''    public String[][] getLanguageList()
    '''
def getMessage():
    '''    public String getMessage(final String group, final String key, String langCode)
    public String getMessage(final MXException mxe, final String langCode)
    '''
def getTaggedMessage():
    '''    public String getTaggedMessage(final String group, final String key, String langCode)
    public String getTaggedMessage(final MXException mxe, final String langCode)
    '''
def getMessages():
    '''    public String[] getMessages(final String group, final String[] key, final String langCode)
    '''
def getMasterModifiedObjects():
    '''    public Map<String, String> getMasterModifiedObjects()
    '''
def getMasterMboValueInfo():
    '''    public MboValueInfo getMasterMboValueInfo(final MboRemote tenantMbo)
    '''
def getWarnings():
    '''    public ArrayList getWarnings(final Object id)
    '''
def clearWarnings():
    '''    public void clearWarnings(final Object id)
    '''
def addWarning():
    '''    public void addWarning(final MXException e, final Object id)
    '''
def hasWarnings():
    '''    public boolean hasWarnings(final Object id)
    '''
def incrementMboCount():
    '''    public void incrementMboCount(final String name, final int tenantID)
    '''
def decrementMboCount():
    '''    public void decrementMboCount(final String name, final int tenantID)
    '''
def incrementMbosetCount():
    '''    public void incrementMbosetCount(final String name, final int tenantID)
    '''
def decrementMbosetCount():
    '''    public void decrementMbosetCount(final String name)
    public void decrementMbosetCount(final String name, final int tenantID)
    '''
def incrementMbosetIPCount():
    '''    public void incrementMbosetIPCount(String objName, final String clientHost, final String clientAddr)
    '''
def decrementMbosetIPCount():
    '''    public void decrementMbosetIPCount(String objName, final String clientHost, final String clientAddr)
    '''
def getMboSetIPCount():
    '''    public int getMboSetIPCount(String objName, final String clientHost, final String clientAddr)
    '''
def printMaxsessionInfo():
    '''    public String printMaxsessionInfo()
    '''
def getMboCount():
    '''    public String getMboCount()
    '''
def getMboSetCount():
    '''    public int getMboSetCount(String objName)
    '''
def getAllTenantsMboCountAsJSON():
    '''    public JSONObject getAllTenantsMboCountAsJSON()
    '''
def getConditionCache():
    '''    public MaxConditionCache getConditionCache()
    '''
def getDataRestrictionCache():
    '''    public DataRestrictionCache getDataRestrictionCache()
    '''
def getMaxDomainCache():
    '''    public MaxDomainCache getMaxDomainCache()
    '''
def setupLongOpPipe():
    '''    public InputStream setupLongOpPipe()
    '''
def clearLongOpPipe():
    '''    public void clearLongOpPipe()
    '''
def writeLongOpMsg():
    '''    public void writeLongOpMsg(String msg)
    '''
def getSQLServerPrefetchRows():
    '''    public int getSQLServerPrefetchRows()
    '''
def getSecurityContext():
    '''    public SecurityContextFlag getSecurityContext()
    '''
def clearSecurityContext():
    '''    public void clearSecurityContext()
    '''
def setSecurityCheck():
    '''    public void setSecurityCheck(final SecurityContextFlag securityFlag)
    '''
def isSQLServerPrefetchRowsNeeded():
    '''    public boolean isSQLServerPrefetchRowsNeeded()
    '''
def getMxServerConfig():
    '''    public Properties getMxServerConfig()
    '''
def getServerCommandRemote():
    '''    public SrvCommRemote getServerCommandRemote(final String name, final String passwd)
    public SrvCommRemote getServerCommandRemote(final UserInfo userInfo)
    '''
def getMboCounts():
    '''    public ArrayList getMboCounts()
    public ArrayList getMboCounts(final int tenantID)
    '''
def getMailAuth():
    '''    public static SmtpAuthenticator getMailAuth()
    '''
def getBaseCalendar():
    '''    public String getBaseCalendar()
    '''
def getTenantIdsList():
    '''    public List<Integer> getTenantIdsList(final UserInfo landlordInfo, final int status)
    '''
def getAllTenantIdsList():
    '''    public List<Integer> getAllTenantIdsList(final UserInfo landlordInfo)
    '''
def collectTenantDBConnInfo():
    '''    public void collectTenantDBConnInfo(final UserInfo info)
    '''
def collectTenantDBConForThisServer():
    '''    public void collectTenantDBConForThisServer(final UserInfo info)
    '''
def setProxy():
    '''    public void setProxy(final Remote proxy)
    '''
def getProxy():
    '''    public Remote getProxy()
    '''
def getTenantRealmMap():
    '''    public HashMap<String, String> getTenantRealmMap()
    '''
def clearTenantRealmMap():
    '''    public void clearTenantRealmMap()
    '''
def loadCustomApps():
    '''    public void loadCustomApps()
    public void loadCustomApps(final Connection con)
    '''
def AdminModeThread():
    '''    public AdminModeThread()
    '''
def setKey():
    '''    public void setKey(final String value)
    '''
def UnloadInactiveCachesThread():
    '''    public UnloadInactiveCachesThread()
    '''
def SmtpAuthenticator():
    '''    public SmtpAuthenticator(final String user, final String password)
    '''
def DBConnStatThread():
    '''    public DBConnStatThread(final UserInfo infoT)
    '''
