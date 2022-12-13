def getItemType():
    '''    public static String getItemType(final MboRemote mbo, final String relation)
    '''
def getProperty():
    '''    public static String getProperty(final String propName)
    '''
def getBooleanProperty():
    '''    public static boolean getBooleanProperty(final String propName, final boolean dflt)
    '''
def getIntegerProperty():
    '''    public static int getIntegerProperty(final String propName, final int dflt)
    '''
def getAltKeyArray():
    '''    public static String[] getAltKeyArray(final String indexName, final Connection con)
    public static String[] getAltKeyArray(final String indexName)
    public static String[] getAltKeyArray(final String indexName, final String entityName)
    '''
def updateSendersysid():
    '''    public static void updateSendersysid(String tableName, final String where, final Connection con)
    '''
def getFromEmail():
    '''    public static String getFromEmail()
    '''
def getToEmail():
    '''    public static String getToEmail()
    '''
def getKeyArray():
    '''    public static String[] getKeyArray(final MicSetInfo micInfo)
    public static String[] getKeyArray(final String name)
    '''
def getContextKeyArray():
    '''    public static String[] getContextKeyArray(final String name)
    '''
def getKeyMboValues():
    '''    public static Iterator<MboValueInfo> getKeyMboValues(final String name)
    '''
def getEntityName():
    '''    public static String getEntityName(final String name)
    '''
def validateOrgSite():
    '''    public static void validateOrgSite(final StructureData struc, final MboSetRemote mboSet, final String orgName, final String siteName, final String itemSetName, final String companySetName)
    public static void validateOrgSite(final StructureObject struc, final MboSetRemote mboSet, final String orgName, final String siteName, final String itemSetName, final String companySetName)
    '''
def dateToJmigString():
    '''    public static String dateToJmigString(final Date in)
    '''
def jmigStringToDateTime():
    '''    public static Date jmigStringToDateTime(final String in)
    '''
def deleteFile():
    '''    public static synchronized void deleteFile(final String filepath)
    '''
def getBaseCurrency():
    '''    public static String getBaseCurrency(final String key, final UserInfo info, final String orgid)
    '''
def parseCondition():
    '''    public static boolean parseCondition(final String str, final MboRemote mbo)
    '''
def isCondExpression():
    '''    public static boolean isCondExpression(final String cond)
    '''
def getMaxVar():
    '''    public static String getMaxVar(final String key, final String orgid, final String siteid)
    public static String getMaxVar(final String varname)
    '''
def getRemoteConnection():
    '''    public static Connection getRemoteConnection(final String driver, final String url, final String username, final String password)
    '''
def getType():
    '''    public static int getType(final int maxtype)
    '''
def getMaximoType():
    '''    public static int getMaximoType(final String objectName, final String attributeName)
    '''
def serializeData():
    '''    public static byte[] serializeData(final Serializable obj)
    '''
def deserialize():
    '''    public static Object deserialize(final byte[] objData)
    '''
def getMEAProperty():
    '''    public static String getMEAProperty(final String propertyName)
    '''
def getYORNValue():
    '''    public static String getYORNValue(final int val, final MboSetRemote mboSet)
    '''
def getUserYes():
    '''    public static String getUserYes(final MboSetRemote mboSet)
    '''
def getUserNo():
    '''    public static String getUserNo(final MboSetRemote mboSet)
    '''
def getMeaGlobalDir():
    '''    public static synchronized String getMeaGlobalDir()
    public static synchronized String getMeaGlobalDir(final boolean getDefaultDir)
    '''
def getExternalValueList():
    '''    public static String getExternalValueList(final String listName, final String maxValue)
    public static String getExternalValueList(final String listName, final String maxValue, final String siteId, final String orgId)
    '''
def getInternalValueList():
    '''    public static String getInternalValueList(final String listName, final String value)
    '''
def formatMboColumn():
    '''    public static String formatMboColumn(final MboRemote mbo, final String name)
    '''
def getFileName():
    '''    public static String getFileName(final Map msgProperties, final String fileType, final boolean queueDir)
    public static String getFileName(final String extSystem, final String serviceName, final String messageId, final String queueName, final String fileType, final boolean queueDir)
    '''
def getConcatenatedValuesList():
    '''    public static String getConcatenatedValuesList(final List<String> list, final char separationChar, final int maxLength)
    '''
def getMeaTextDelimiter():
    '''    public static String getMeaTextDelimiter()
    '''
def getMeaTextQualifier():
    '''    public static String getMeaTextQualifier()
    '''
def getExtractDir():
    '''    public static String getExtractDir(final String extSysName, final String fileFormat)
    '''
def getAppExportDir():
    '''    public static String getAppExportDir(final String fileFormat)
    '''
def deleteFiles():
    '''    public static void deleteFiles(final List<String> filesList, final String folder)
    '''
def isResponseRequired():
    '''    public static boolean isResponseRequired(final String messageType)
    '''
def getDefaultDirectory():
    '''    public static String getDefaultDirectory()
    '''
def checkLicense():
    '''    public static boolean checkLicense(final Set<String> allLicences)
    '''
def setDefaultSite():
    '''    public static void setDefaultSite(final UserInfo userInfo)
    '''
def prettyPrintJSON():
    '''    public static String prettyPrintJSON(final byte[] byteData)
    '''
def checkStatus():
    '''    public static boolean checkStatus(final StructureData irData, final String extSystem, final String sendListName, final String orgId, final String siteId, final boolean sendUpdates)
    '''
