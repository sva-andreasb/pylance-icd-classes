def createJarArchive():
    '''public static JarOutputStream createJarArchive(final JarOutputStream archiveStream, final String inFileName, final ByteArrayInputStream in)
    '''
def getPackageName():
    '''public static String getPackageName(final String source, final String pkgDefName)
    '''
def getDatedFile():
    '''public static File getDatedFile(final File folder, final String prefix, final String suffix)
    '''
def dateInDigits():
    '''public static String dateInDigits(final boolean includeMilliseconds)
    '''
def getDDCfgGroups():
    '''public static MboSetRemote getDDCfgGroups()
    public static MboSetRemote getDDCfgGroups(final UserInfo ui)
    '''
def getDDCfgGroupNames():
    '''public static String[] getDDCfgGroupNames()
    public static String[] getDDCfgGroupNames(final UserInfo ui)
    '''
def getTenantID():
    '''public static int getTenantID(final MboRemote mbo)
    '''
def getPKGMETADATACfgGroup():
    '''public static MboRemote getPKGMETADATACfgGroup()
    '''
def getPKGMETADATAGroupName():
    '''public static String getPKGMETADATAGroupName()
    '''
def getPkgAndSourceFromJarName():
    '''public static String[] getPkgAndSourceFromJarName(final String jarName)
    '''
def getTypeAndOrderFromFileName():
    '''public static String[] getTypeAndOrderFromFileName(final String fileName, final String pkgSrc)
    '''
def readJarArchive():
    '''public static void readJarArchive(final File jarF, final String pkgFileName, final UserInfo ui)
    '''
def deleteInvalidStagingRows():
    '''public static void deleteInvalidStagingRows(final String pkgDefName, final String source, final String pkg, final UserInfo ui)
    '''
def getSourceName():
    '''public static String getSourceName()
    public static String getSourceName(final Connection conn)
    '''
def getDatabaseName():
    '''public static String getDatabaseName(final Connection conn)
    public static String getDatabaseName()
    '''
def getSchemaName():
    '''public static String getSchemaName(final Connection conn)
    public static String getSchemaName()
    '''
def getDBHostName():
    '''public static String getDBHostName(final Connection conn)
    public static String getDBHostName()
    '''
def checkRestriction():
    '''public static boolean checkRestriction(final Connection conn, final String source)
    '''
def inMEATransaction():
    '''public static boolean inMEATransaction(final MXTransaction txn)
    public static boolean inMEATransaction()
    '''
def createBulletinBoard():
    '''public static long createBulletinBoard(final UserInfo ui, final boolean isCreate)
    '''
def removeBulletinBoard():
    '''public static void removeBulletinBoard(final UserInfo ui, final long bbId)
    '''
def redistributePackage():
    '''public static MboRemote redistributePackage(MboRemote pkgMbo)
    '''
def redistributePkgMetaData():
    '''public static MboRemote redistributePkgMetaData(final MboRemote pkgDefMbo, final MboRemote pkgMbo)
    '''
def writeToDMMessage():
    '''public static String writeToDMMessage(final MboRemote ownerMbo, final String pkgName, final String type, final String errorKey, final Throwable t, final String msgDetail, final Object[] params, final boolean isLongOpMsg)
    public static String writeToDMMessage(final MboRemote ownerMbo, final String pkgName, final String type, final String errorKey, final Throwable t, final String msgDetail, final Object[] params, final boolean isLongOpMsg, final UserInfo msgUI)
    '''
def getLongKey():
    '''public static long getLongKey(final String key)
    '''
def getDeployDefaultValueSet():
    '''public static Map<String, String> getDeployDefaultValueSet()
    '''
def getAttrValues():
    '''public static String getAttrValues(final MboSet mboSet, final String attrName, final int maxCount)
    '''
def getManifestFromFile():
    '''public static byte[] getManifestFromFile(final String fileName, final String direction)
    '''
def writeLongOpMsg():
    '''public static void writeLongOpMsg(final MboSetRemote mboSet, final String msg)
    public static void writeLongOpMsg(final UserInfo msgUI, final MboSetRemote mboSet, final String msg)
    '''
def putNewDeployValues():
    '''public static void putNewDeployValues(final String key, final Object value)
    '''
def clearNewDeployValues():
    '''public static void clearNewDeployValues()
    '''
def getNewDeployValues():
    '''public static HashMap getNewDeployValues()
    '''
def getPkgFileName():
    '''public static String getPkgFileName(final MboRemote stageMbo)
    '''
def getManifestFromStaging():
    '''public static byte[] getManifestFromStaging(final UserInfo ui, final String pkgName)
    '''
def getDMLogger():
    '''public static MXLogger getDMLogger(final UserInfo ui)
    '''
def deletePreviewLogs():
    '''public static void deletePreviewLogs(final String pkgName)
    '''
def getMessageText():
    '''public static String getMessageText(final UserInfo msgUserInfo, final String errorKey, final Object[] params)
    '''
def getCfgObjsForGrp():
    '''public static LinkedHashMap<String, LinkedList<String>> getCfgObjsForGrp(final MboRemote defMbo)
    '''
def getDatabaseType():
    '''public static int getDatabaseType(final Connection conn)
    '''
def findTopLevelMosForChild():
    '''public static MboRemote findTopLevelMosForChild(final MosInfo mosInfo, final MboRemote childMbo)
    '''
def getPKInfo():
    '''public static String getPKInfo(final MboRemote topMbo)
    '''
def dmMapDefCheck():
    '''public static void dmMapDefCheck(final MboRemote pkgMbo)
    '''
