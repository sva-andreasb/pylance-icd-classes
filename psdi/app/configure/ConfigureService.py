VALIDATION_LENGTH = "String  \"LENGTH\""
VALIDATION_ALL = "String  \"ALL\""
VALIDATION_PENDINGCHG = "String  \"PENDINGCHG\""
def ConfigureService():
    '''public ConfigureService()
    public ConfigureService(final MXServer mxServer)
    '''
def init():
    '''public void init()
    public void init(final int configLevel, final Util util, final ConnectionKey conKey, final UserInfo ui)
    '''
def isValidChar():
    '''public boolean isValidChar(final String checkString)
    '''
def validateFormat():
    '''public boolean validateFormat(final Locale locale, final TimeZone timezone, final String value, final String maxtype, final int length, final int scale, final boolean checkCase)
    '''
def convertToLocale():
    '''public String convertToLocale(final String inputValue, final String maxtype, final Locale fromLocale, final TimeZone fromTimeZone, final Locale toLocale, final TimeZone toTimeZone)
    '''
def removeChanges():
    '''public void removeChanges()
    '''
def removeTenantChanges():
    '''public void removeTenantChanges(final UserInfo tenantInfo, final int tenanatId)
    '''
def applyTenantChanges():
    '''public void applyTenantChanges(final UserInfo tenantInfo, final int tenanatId)
    public void applyTenantChanges(final UserInfo tenantInfo, final int tenantId, final boolean isPreview)
    '''
def createSelectedExtensionViews():
    '''public void createSelectedExtensionViews(final Map<String, Map<String, Map<String, String>>> objectNames, final Set<String> deleteObjects, final Connection masterCon, final int tenantId)
    '''
def createExtensionTable():
    '''public boolean createExtensionTable(final UserInfo masterInfo, final String tableName)
    '''
def changeAmountFormat():
    '''public void changeAmountFormat(final int newLength, final int newScale, final int origLength, final int origScale)
    public void changeAmountFormat(final int newLength, final int newScale)
    '''
def changeIntFormat():
    '''public void changeIntFormat(final int newIntLength, final int newSmallintLength, final int origIntLength, final int origSmallintLength)
    public void changeIntFormat(final int newIntLength, final int newSmallintLength)
    '''
def updateStatistics():
    '''public void updateStatistics(final MboSetRemote objectSet)
    public void updateStatistics(String tablename)
    '''
def refreshIndexMetadata():
    '''public void refreshIndexMetadata(final MboSetRemote objectSet)
    public void refreshIndexMetadata(String tablename)
    '''
def getUnrestoredTables():
    '''public MboSetRemote getUnrestoredTables(final UserInfo userInfo)
    '''
def getOldBackupTables():
    '''public MboSetRemote getOldBackupTables(final UserInfo userInfo)
    '''
def dropBackup():
    '''public void dropBackup(final MboSetRemote tableSet)
    public void dropBackup(String tablenames)
    '''
def getConfigLevel():
    '''public int getConfigLevel()
    public int getConfigLevel(final UserInfo ui)
    '''
def runConfigDB():
    '''public void runConfigDB(final MboRemote listenerMbo)
    public void runConfigDB(final MboRemote listenerMbo, final HashMap<String, String> params)
    '''
def listenToConfigDB():
    '''public void listenToConfigDB(final MboRemote listenerMbo, final boolean listen)
    '''
def configIsRunning():
    '''public boolean configIsRunning()
    '''
def addConfigMsg():
    '''public synchronized void addConfigMsg(final String msg)
    '''
def setConfigStatus():
    '''public synchronized void setConfigStatus(final int status)
    '''
def getNumConfigMsgs():
    '''public int getNumConfigMsgs()
    '''
def getMaxColumnLength():
    '''public int getMaxColumnLength(final String tablename, final String columnname)
    '''
def getGLMaxtypeLengthFromGLConfigure():
    '''public int getGLMaxtypeLengthFromGLConfigure(final UserInfo userInfo)
    '''
def getDefaultStoragePartition():
    '''public String getDefaultStoragePartition()
    '''
def nativeTableExists():
    '''public boolean nativeTableExists(final String tablename)
    '''
def nativeViewExists():
    '''public boolean nativeViewExists(final String viewname)
    '''
def descendingIndexesSupported():
    '''public boolean descendingIndexesSupported()
    '''
def getMaxLengthColumnInIndex():
    '''public int getMaxLengthColumnInIndex()
    '''
def getMaxLengthIndex():
    '''public int getMaxLengthIndex()
    '''
def spaceIsSysManaged():
    '''public boolean spaceIsSysManaged(final String spaceName)
    '''
def getGrants():
    '''public HashMap getGrants(final String dbUserID, final String entityname)
    '''
def grantNative():
    '''public void grantNative(final String dbUserID, final String entityname, final String privilege, final boolean grant)
    '''
def getDBPlatform():
    '''public int getDBPlatform()
    '''
def isReservedWord():
    '''public boolean isReservedWord(final String testWord)
    '''
def doSql():
    '''public void doSql(final List list)
    public void doSql(final String sql)
    '''
def getJoinAttributes():
    '''public HashMap getJoinAttributes(final MboRemote object1, final MboSetRemote object1Attrs, final MboRemote object2, final MboSetRemote object2Attrs)
    '''
def getAllCommonAttributes():
    '''public HashSet getAllCommonAttributes(final MboSetRemote object1Attrs, final MboSetRemote object2Attrs)
    '''
def getMaxtypeCategory():
    '''public int getMaxtypeCategory(String maxtype)
    '''
def nativeTypesAreCompatible():
    '''public boolean nativeTypesAreCompatible(final String oldNativeType, final String newNativeType)
    '''
def logException():
    '''public void logException(final Exception e)
    '''
def checkDomainLinks():
    '''public StringBuffer checkDomainLinks(final UserInfo ui, final HashSet<String> options)
    public MXException checkDomainLinks(final UserInfo ui, final MaxAttributeCfgRemote mac, final MboSetRemote domainLinks)
    '''
def compare():
    '''public MXException compare(final HashSet<String> byPass, final String object, final String attr, final HashSet<String> domsOnMeta, String[] domsByLink, final StringBuffer os, final UserInfo ui, final boolean genInsertStatement)
    '''
def loadDomainLinks():
    '''public HashMap<String, String[]> loadDomainLinks(final UserInfo ui)
    '''
def verifyView():
    '''public void verifyView(String objectname)
    '''
def noDeltaRows():
    '''public boolean noDeltaRows(final MboRemote masterMbo, final String validationType)
    '''
def pendingDeltaRowExist():
    '''public boolean pendingDeltaRowExist()
    '''
def discardALLTenantDeltas():
    '''public void discardALLTenantDeltas()
    '''
def isActiveExtTable():
    '''public boolean isActiveExtTable(final String objectName)
    '''
def canDeleteFromConfigExtTable():
    '''public boolean canDeleteFromConfigExtTable(final String attributeName, final String objectName)
    '''
def areTenantsOnboarded():
    '''public boolean areTenantsOnboarded()
    '''
def ConfigDBThread():
    '''public ConfigDBThread()
    '''
def setUserLangCode():
    '''public void setUserLangCode(final String value)
    '''
def setParams():
    '''public void setParams(final HashMap<String, String> params)
    '''
def setConnection():
    '''public void setConnection(final Connection inCon, final UserInfo ui)
    '''
def run():
    '''public void run()
    '''
