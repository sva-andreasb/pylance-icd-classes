VALIDATION_LENGTH = "String  LENGTH""
VALIDATION_ALL = "String  ALL""
VALIDATION_PENDINGCHG = "String  PENDINGCHG""
def ConfigureService():
'''public ConfigureService()
public ConfigureService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
public void init(final int configLevel, final Util util, final ConnectionKey conKey, final UserInfo ui)
'''
pass
def isValidChar():
'''public boolean isValidChar(final String checkString)
'''
pass
def validateFormat():
'''public boolean validateFormat(final Locale locale, final TimeZone timezone, final String value, final String maxtype, final int length, final int scale, final boolean checkCase)
'''
pass
def convertToLocale():
'''public String convertToLocale(final String inputValue, final String maxtype, final Locale fromLocale, final TimeZone fromTimeZone, final Locale toLocale, final TimeZone toTimeZone)
'''
pass
def removeChanges():
'''public void removeChanges()
'''
pass
def removeTenantChanges():
'''public void removeTenantChanges(final UserInfo tenantInfo, final int tenanatId)
'''
pass
def applyTenantChanges():
'''public void applyTenantChanges(final UserInfo tenantInfo, final int tenanatId)
public void applyTenantChanges(final UserInfo tenantInfo, final int tenantId, final boolean isPreview)
'''
pass
def createSelectedExtensionViews():
'''public void createSelectedExtensionViews(final Map<String, Map<String, Map<String, String>>> objectNames, final Set<String> deleteObjects, final Connection masterCon, final int tenantId)
'''
pass
def createExtensionTable():
'''public boolean createExtensionTable(final UserInfo masterInfo, final String tableName)
'''
pass
def changeAmountFormat():
'''public void changeAmountFormat(final int newLength, final int newScale, final int origLength, final int origScale)
public void changeAmountFormat(final int newLength, final int newScale)
'''
pass
def changeIntFormat():
'''public void changeIntFormat(final int newIntLength, final int newSmallintLength, final int origIntLength, final int origSmallintLength)
public void changeIntFormat(final int newIntLength, final int newSmallintLength)
'''
pass
def updateStatistics():
'''public void updateStatistics(final MboSetRemote objectSet)
public void updateStatistics(String tablename)
'''
pass
def refreshIndexMetadata():
'''public void refreshIndexMetadata(final MboSetRemote objectSet)
public void refreshIndexMetadata(String tablename)
'''
pass
def getUnrestoredTables():
'''public MboSetRemote getUnrestoredTables(final UserInfo userInfo)
'''
pass
def getOldBackupTables():
'''public MboSetRemote getOldBackupTables(final UserInfo userInfo)
'''
pass
def dropBackup():
'''public void dropBackup(final MboSetRemote tableSet)
public void dropBackup(String tablenames)
'''
pass
def getConfigLevel():
'''public int getConfigLevel()
public int getConfigLevel(final UserInfo ui)
'''
pass
def runConfigDB():
'''public void runConfigDB(final MboRemote listenerMbo)
public void runConfigDB(final MboRemote listenerMbo, final HashMap<String, String> params)
'''
pass
def listenToConfigDB():
'''public void listenToConfigDB(final MboRemote listenerMbo, final boolean listen)
'''
pass
def configIsRunning():
'''public boolean configIsRunning()
'''
pass
def addConfigMsg():
'''public synchronized void addConfigMsg(final String msg)
'''
pass
def setConfigStatus():
'''public synchronized void setConfigStatus(final int status)
'''
pass
def getNumConfigMsgs():
'''public int getNumConfigMsgs()
'''
pass
def getMaxColumnLength():
'''public int getMaxColumnLength(final String tablename, final String columnname)
'''
pass
def getGLMaxtypeLengthFromGLConfigure():
'''public int getGLMaxtypeLengthFromGLConfigure(final UserInfo userInfo)
'''
pass
def getDefaultStoragePartition():
'''public String getDefaultStoragePartition()
'''
pass
def nativeTableExists():
'''public boolean nativeTableExists(final String tablename)
'''
pass
def nativeViewExists():
'''public boolean nativeViewExists(final String viewname)
'''
pass
def descendingIndexesSupported():
'''public boolean descendingIndexesSupported()
'''
pass
def getMaxLengthColumnInIndex():
'''public int getMaxLengthColumnInIndex()
'''
pass
def getMaxLengthIndex():
'''public int getMaxLengthIndex()
'''
pass
def spaceIsSysManaged():
'''public boolean spaceIsSysManaged(final String spaceName)
'''
pass
def getGrants():
'''public HashMap getGrants(final String dbUserID, final String entityname)
'''
pass
def grantNative():
'''public void grantNative(final String dbUserID, final String entityname, final String privilege, final boolean grant)
'''
pass
def getDBPlatform():
'''public int getDBPlatform()
'''
pass
def isReservedWord():
'''public boolean isReservedWord(final String testWord)
'''
pass
def doSql():
'''public void doSql(final List list)
public void doSql(final String sql)
'''
pass
def getJoinAttributes():
'''public HashMap getJoinAttributes(final MboRemote object1, final MboSetRemote object1Attrs, final MboRemote object2, final MboSetRemote object2Attrs)
'''
pass
def getAllCommonAttributes():
'''public HashSet getAllCommonAttributes(final MboSetRemote object1Attrs, final MboSetRemote object2Attrs)
'''
pass
def getMaxtypeCategory():
'''public int getMaxtypeCategory(String maxtype)
'''
pass
def nativeTypesAreCompatible():
'''public boolean nativeTypesAreCompatible(final String oldNativeType, final String newNativeType)
'''
pass
def logException():
'''public void logException(final Exception e)
'''
pass
def checkDomainLinks():
'''public StringBuffer checkDomainLinks(final UserInfo ui, final HashSet<String> options)
public MXException checkDomainLinks(final UserInfo ui, final MaxAttributeCfgRemote mac, final MboSetRemote domainLinks)
'''
pass
def compare():
'''public MXException compare(final HashSet<String> byPass, final String object, final String attr, final HashSet<String> domsOnMeta, String[] domsByLink, final StringBuffer os, final UserInfo ui, final boolean genInsertStatement)
'''
pass
def loadDomainLinks():
'''public HashMap<String, String[]> loadDomainLinks(final UserInfo ui)
'''
pass
def verifyView():
'''public void verifyView(String objectname)
'''
pass
def noDeltaRows():
'''public boolean noDeltaRows(final MboRemote masterMbo, final String validationType)
'''
pass
def pendingDeltaRowExist():
'''public boolean pendingDeltaRowExist()
'''
pass
def discardALLTenantDeltas():
'''public void discardALLTenantDeltas()
'''
pass
def isActiveExtTable():
'''public boolean isActiveExtTable(final String objectName)
'''
pass
def canDeleteFromConfigExtTable():
'''public boolean canDeleteFromConfigExtTable(final String attributeName, final String objectName)
'''
pass
def areTenantsOnboarded():
'''public boolean areTenantsOnboarded()
'''
pass
def ConfigDBThread():
'''public ConfigDBThread()
'''
pass
def setUserLangCode():
'''public void setUserLangCode(final String value)
'''
pass
def setParams():
'''public void setParams(final HashMap<String, String> params)
'''
pass
def setConnection():
'''public void setConnection(final Connection inCon, final UserInfo ui)
'''
pass
def run():
'''public void run()
'''
pass
