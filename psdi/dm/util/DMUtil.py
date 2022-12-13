def createJarArchive():
'''public static JarOutputStream createJarArchive(final JarOutputStream archiveStream, final String inFileName, final ByteArrayInputStream in)
'''
pass
def getPackageName():
'''public static String getPackageName(final String source, final String pkgDefName)
'''
pass
def getDatedFile():
'''public static File getDatedFile(final File folder, final String prefix, final String suffix)
'''
pass
def dateInDigits():
'''public static String dateInDigits(final boolean includeMilliseconds)
'''
pass
def getDDCfgGroups():
'''public static MboSetRemote getDDCfgGroups()
public static MboSetRemote getDDCfgGroups(final UserInfo ui)
'''
pass
def getDDCfgGroupNames():
'''public static String[] getDDCfgGroupNames()
public static String[] getDDCfgGroupNames(final UserInfo ui)
'''
pass
def getTenantID():
'''public static int getTenantID(final MboRemote mbo)
'''
pass
def getPKGMETADATACfgGroup():
'''public static MboRemote getPKGMETADATACfgGroup()
'''
pass
def getPKGMETADATAGroupName():
'''public static String getPKGMETADATAGroupName()
'''
pass
def getPkgAndSourceFromJarName():
'''public static String[] getPkgAndSourceFromJarName(final String jarName)
'''
pass
def getTypeAndOrderFromFileName():
'''public static String[] getTypeAndOrderFromFileName(final String fileName, final String pkgSrc)
'''
pass
def readJarArchive():
'''public static void readJarArchive(final File jarF, final String pkgFileName, final UserInfo ui)
'''
pass
def deleteInvalidStagingRows():
'''public static void deleteInvalidStagingRows(final String pkgDefName, final String source, final String pkg, final UserInfo ui)
'''
pass
def getSourceName():
'''public static String getSourceName()
public static String getSourceName(final Connection conn)
'''
pass
def getDatabaseName():
'''public static String getDatabaseName(final Connection conn)
public static String getDatabaseName()
'''
pass
def getSchemaName():
'''public static String getSchemaName(final Connection conn)
public static String getSchemaName()
'''
pass
def getDBHostName():
'''public static String getDBHostName(final Connection conn)
public static String getDBHostName()
'''
pass
def checkRestriction():
'''public static boolean checkRestriction(final Connection conn, final String source)
'''
pass
def inMEATransaction():
'''public static boolean inMEATransaction(final MXTransaction txn)
public static boolean inMEATransaction()
'''
pass
def createBulletinBoard():
'''public static long createBulletinBoard(final UserInfo ui, final boolean isCreate)
'''
pass
def removeBulletinBoard():
'''public static void removeBulletinBoard(final UserInfo ui, final long bbId)
'''
pass
def redistributePackage():
'''public static MboRemote redistributePackage(MboRemote pkgMbo)
'''
pass
def redistributePkgMetaData():
'''public static MboRemote redistributePkgMetaData(final MboRemote pkgDefMbo, final MboRemote pkgMbo)
'''
pass
def writeToDMMessage():
'''public static String writeToDMMessage(final MboRemote ownerMbo, final String pkgName, final String type, final String errorKey, final Throwable t, final String msgDetail, final Object[] params, final boolean isLongOpMsg)
public static String writeToDMMessage(final MboRemote ownerMbo, final String pkgName, final String type, final String errorKey, final Throwable t, final String msgDetail, final Object[] params, final boolean isLongOpMsg, final UserInfo msgUI)
'''
pass
def getLongKey():
'''public static long getLongKey(final String key)
'''
pass
def getDeployDefaultValueSet():
'''public static Map<String, String> getDeployDefaultValueSet()
'''
pass
def getAttrValues():
'''public static String getAttrValues(final MboSet mboSet, final String attrName, final int maxCount)
'''
pass
def getManifestFromFile():
'''public static byte[] getManifestFromFile(final String fileName, final String direction)
'''
pass
def writeLongOpMsg():
'''public static void writeLongOpMsg(final MboSetRemote mboSet, final String msg)
public static void writeLongOpMsg(final UserInfo msgUI, final MboSetRemote mboSet, final String msg)
'''
pass
def putNewDeployValues():
'''public static void putNewDeployValues(final String key, final Object value)
'''
pass
def clearNewDeployValues():
'''public static void clearNewDeployValues()
'''
pass
def getNewDeployValues():
'''public static HashMap getNewDeployValues()
'''
pass
def getPkgFileName():
'''public static String getPkgFileName(final MboRemote stageMbo)
'''
pass
def getManifestFromStaging():
'''public static byte[] getManifestFromStaging(final UserInfo ui, final String pkgName)
'''
pass
def getDMLogger():
'''public static MXLogger getDMLogger(final UserInfo ui)
'''
pass
def deletePreviewLogs():
'''public static void deletePreviewLogs(final String pkgName)
'''
pass
def getMessageText():
'''public static String getMessageText(final UserInfo msgUserInfo, final String errorKey, final Object[] params)
'''
pass
def getCfgObjsForGrp():
'''public static LinkedHashMap<String, LinkedList<String>> getCfgObjsForGrp(final MboRemote defMbo)
'''
pass
def getDatabaseType():
'''public static int getDatabaseType(final Connection conn)
'''
pass
def findTopLevelMosForChild():
'''public static MboRemote findTopLevelMosForChild(final MosInfo mosInfo, final MboRemote childMbo)
'''
pass
def getPKInfo():
'''public static String getPKInfo(final MboRemote topMbo)
'''
pass
def dmMapDefCheck():
'''public static void dmMapDefCheck(final MboRemote pkgMbo)
'''
pass
