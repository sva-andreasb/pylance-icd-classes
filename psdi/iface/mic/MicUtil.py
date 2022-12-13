def getItemType():
'''public static String getItemType(final MboRemote mbo, final String relation)
'''
pass
def getProperty():
'''public static String getProperty(final String propName)
'''
pass
def getBooleanProperty():
'''public static boolean getBooleanProperty(final String propName, final boolean dflt)
'''
pass
def getIntegerProperty():
'''public static int getIntegerProperty(final String propName, final int dflt)
'''
pass
def getAltKeyArray():
'''public static String[] getAltKeyArray(final String indexName, final Connection con)
public static String[] getAltKeyArray(final String indexName)
public static String[] getAltKeyArray(final String indexName, final String entityName)
'''
pass
def updateSendersysid():
'''public static void updateSendersysid(String tableName, final String where, final Connection con)
'''
pass
def getFromEmail():
'''public static String getFromEmail()
'''
pass
def getToEmail():
'''public static String getToEmail()
'''
pass
def getKeyArray():
'''public static String[] getKeyArray(final MicSetInfo micInfo)
public static String[] getKeyArray(final String name)
'''
pass
def getContextKeyArray():
'''public static String[] getContextKeyArray(final String name)
'''
pass
def getKeyMboValues():
'''public static Iterator<MboValueInfo> getKeyMboValues(final String name)
'''
pass
def getEntityName():
'''public static String getEntityName(final String name)
'''
pass
def validateOrgSite():
'''public static void validateOrgSite(final StructureData struc, final MboSetRemote mboSet, final String orgName, final String siteName, final String itemSetName, final String companySetName)
public static void validateOrgSite(final StructureObject struc, final MboSetRemote mboSet, final String orgName, final String siteName, final String itemSetName, final String companySetName)
'''
pass
def dateToJmigString():
'''public static String dateToJmigString(final Date in)
'''
pass
def jmigStringToDateTime():
'''public static Date jmigStringToDateTime(final String in)
'''
pass
def deleteFile():
'''public static synchronized void deleteFile(final String filepath)
'''
pass
def getBaseCurrency():
'''public static String getBaseCurrency(final String key, final UserInfo info, final String orgid)
'''
pass
def parseCondition():
'''public static boolean parseCondition(final String str, final MboRemote mbo)
'''
pass
def isCondExpression():
'''public static boolean isCondExpression(final String cond)
'''
pass
def getMaxVar():
'''public static String getMaxVar(final String key, final String orgid, final String siteid)
public static String getMaxVar(final String varname)
'''
pass
def getRemoteConnection():
'''public static Connection getRemoteConnection(final String driver, final String url, final String username, final String password)
'''
pass
def getType():
'''public static int getType(final int maxtype)
'''
pass
def getMaximoType():
'''public static int getMaximoType(final String objectName, final String attributeName)
'''
pass
def serializeData():
'''public static byte[] serializeData(final Serializable obj)
'''
pass
def deserialize():
'''public static Object deserialize(final byte[] objData)
'''
pass
def getMEAProperty():
'''public static String getMEAProperty(final String propertyName)
'''
pass
def getYORNValue():
'''public static String getYORNValue(final int val, final MboSetRemote mboSet)
'''
pass
def getUserYes():
'''public static String getUserYes(final MboSetRemote mboSet)
'''
pass
def getUserNo():
'''public static String getUserNo(final MboSetRemote mboSet)
'''
pass
def getMeaGlobalDir():
'''public static synchronized String getMeaGlobalDir()
public static synchronized String getMeaGlobalDir(final boolean getDefaultDir)
'''
pass
def getExternalValueList():
'''public static String getExternalValueList(final String listName, final String maxValue)
public static String getExternalValueList(final String listName, final String maxValue, final String siteId, final String orgId)
'''
pass
def getInternalValueList():
'''public static String getInternalValueList(final String listName, final String value)
'''
pass
def formatMboColumn():
'''public static String formatMboColumn(final MboRemote mbo, final String name)
'''
pass
def getFileName():
'''public static String getFileName(final Map msgProperties, final String fileType, final boolean queueDir)
public static String getFileName(final String extSystem, final String serviceName, final String messageId, final String queueName, final String fileType, final boolean queueDir)
'''
pass
def getConcatenatedValuesList():
'''public static String getConcatenatedValuesList(final List<String> list, final char separationChar, final int maxLength)
'''
pass
def getMeaTextDelimiter():
'''public static String getMeaTextDelimiter()
'''
pass
def getMeaTextQualifier():
'''public static String getMeaTextQualifier()
'''
pass
def getExtractDir():
'''public static String getExtractDir(final String extSysName, final String fileFormat)
'''
pass
def getAppExportDir():
'''public static String getAppExportDir(final String fileFormat)
'''
pass
def deleteFiles():
'''public static void deleteFiles(final List<String> filesList, final String folder)
'''
pass
def isResponseRequired():
'''public static boolean isResponseRequired(final String messageType)
'''
pass
def getDefaultDirectory():
'''public static String getDefaultDirectory()
'''
pass
def checkLicense():
'''public static boolean checkLicense(final Set<String> allLicences)
'''
pass
def setDefaultSite():
'''public static void setDefaultSite(final UserInfo userInfo)
'''
pass
def prettyPrintJSON():
'''public static String prettyPrintJSON(final byte[] byteData)
'''
pass
def checkStatus():
'''public static boolean checkStatus(final StructureData irData, final String extSystem, final String sendListName, final String orgId, final String siteId, final boolean sendUpdates)
'''
pass
