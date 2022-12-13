def convertOnceToSchedule():
    '''public static String convertOnceToSchedule(final Date date, final Locale locale, final TimeZone clientTimeZone)
    '''
def verifySchedule():
    '''public static void verifySchedule(final MboRemote reportSched)
    '''
def qualifyWhere():
    '''public static String qualifyWhere(final String where, final String baseTable)
    '''
def getWhereData():
    '''public static WhereData getWhereData(String where, final String baseTable)
    '''
def getDBType():
    '''public static String getDBType()
    '''
def hasParameters():
    '''public static boolean hasParameters(final MboRemote reportRemote)
    '''
def calculateTotalReservedHours():
    '''public static String calculateTotalReservedHours(final Calendar startReserve, final Calendar endReserve)
    '''
def checkReserveTimeOverlaps():
    '''public static void checkReserveTimeOverlaps(final MboSetRemote reportProcReserveSet, final String appname, final String reportname, final Calendar startReserve, final Calendar endReserve, final String day, final long currentMboUniqueIDValue)
    '''
def validateAvailSchedulingTime():
    '''public static boolean validateAvailSchedulingTime(final String appname, final String reportname, final Date date, final String scheduleType, final UserInfo userInfo)
    '''
def toHourMinSecFromMiliSec():
    '''public static String toHourMinSecFromMiliSec(final long runTimeMilliSeconds)
    '''
def resetScheduleAvailability():
    '''public static void resetScheduleAvailability(final String currAppname, final String currReportname, final UserInfo userInfo)
    '''
def addReportProcSchedulableRecord():
    '''public static void addReportProcSchedulableRecord(final MboRemote reportProcSched, final String appname, final String reportname, final String day, final Date startSchedulable, final Date endSchedulable, final String timezone)
    '''
def finishReportProcSchedulableRecord():
    '''public static void finishReportProcSchedulableRecord(final MboSetRemote reportProcSchedSet, final MboRemote reportProcSched, final String appname, final String reportname, final String day, Integer dayNum, final Date startSchedulable, final boolean needsEndingTime, final boolean setFullDayAvailability, final String timezone)
    '''
def writeFullDayAvailability():
    '''public static void writeFullDayAvailability(final MboSetRemote reportProcSchedSet, MboRemote reportProcSched, final String appname, final String reportname, final Integer dayNum, final UserInfo userInfo, final String timezone)
    '''
def scheduleEndTime():
    '''public static void scheduleEndTime(final int reserveStartMin, final Calendar endSchedulableTime, final Calendar startReserve)
    '''
def scheduleStartTime():
    '''public static void scheduleStartTime(final int reserveEndMin, final Calendar startSchedulableTime, final Calendar endReserve)
    '''
def getDayName():
    '''public static String getDayName(String dayNum, final UserInfo userInfo)
    '''
def convertDateToMXServer():
    '''public static Date convertDateToMXServer(final Locale clientLocale, final String clientTimezone, final Date date)
    '''
def convertDateToClientTimezone():
    '''public static Date convertDateToClientTimezone(final Locale clientLocale, final String clientTimezone, final Date date)
    '''
def hasSubSelects():
    '''public static boolean hasSubSelects(final String whereClause)
    '''
def getViewerURL():
    '''public static String getViewerURL(final String contextPath, final String sessionId, final UserInfo userInfo, final Hashtable reportParams)
    public static String getViewerURL(final String contextPath, final String sessionId, final UserInfo userInfo, final Hashtable reportParams, final boolean isDirectPrint)
    '''
def getViewerURLToFindBaseUrl():
    '''public static String getViewerURLToFindBaseUrl(final String contextPath, final boolean isDirectPrint)
    '''
def createReportName():
    '''public static String createReportName(final String appName, final String userName)
    '''
def getUserFolderName():
    '''public static String getUserFolderName(final UserInfo userInfo)
    public static String getUserFolderName(final String userName)
    '''
def addParamstring():
    '''public static void addParamstring(final String key, final String value, final Hashtable reportParams)
    '''
def updateReportLabelsAllLangs():
    '''public static void updateReportLabelsAllLangs(final UserInfo ui)
    '''
def updateReportLabels():
    '''public static void updateReportLabels(final UserInfo ui)
    '''
def makeSafeForXML():
    '''public static String makeSafeForXML(String value)
    '''
def replaceString():
    '''public static String replaceString(String str, final String pattern, final String replacement)
    '''
def getcurrentSecAttKeyRecord():
    '''public static ReportSecAttKeyRecord getcurrentSecAttKeyRecord(final UserInfo userInfo)
    '''
def getKey():
    '''public static byte[] getKey(final String seqNumberString)
    '''
def addToReportAttachDocs():
    '''public static String addToReportAttachDocs(final String userId, final String url)
    '''
def getReportAttachDocsUrl():
    '''public static String getReportAttachDocsUrl(final String userId, final String key)
    '''
def getRandomString():
    '''public static String getRandomString(final int len)
    public static String getRandomString()
    '''
def formatWhere():
    '''public static String formatWhere(String whereClause, final String baseTable, final UserInfo ui)
    '''
def addToReportBrosParam():
    '''public static void addToReportBrosParam(final Hashtable paramHashtable, final boolean isSessionParam, final long brosUniqueID, final UserInfo userInfo)
    public static void addToReportBrosParam(final String paramName, final String ParamValue, final boolean isSessionParam, final long brosUniqueID, final UserInfo userInfo)
    '''
def addToReportBrosUrl():
    '''public static void addToReportBrosUrl(final Vector<String> reporUrlParam, final Vector<Boolean> securedAttachFlags, final boolean isQpixUrl, final long brosUniqueID, final UserInfo userInfo)
    '''
def getEmailAddress():
    '''public static String getEmailAddress(final String userId)
    '''
def hasAttribute():
    '''public static boolean hasAttribute(final String expression, final String objectName, final Set<String> validAttributes)
    public static boolean hasAttribute(final Node expression, final String objectName, final Set<String> validAttributes)
    '''
def getValidAttributes():
    '''public static Set<String> getValidAttributes(final MosDetailInfo detailInfo)
    public static Set<String> getValidAttributes(final String objectName)
    '''
def getMosDetailInfo():
    '''public static MosDetailInfo getMosDetailInfo(final String intObjectName, final int objectID)
    '''
def getColumnName():
    '''public static String getColumnName(final MboValueInfo mvi)
    '''
def getEntityName():
    '''public static String getEntityName(final String objectName)
    '''
def getCurrentDateFunction():
    '''public static String getCurrentDateFunction()
    '''
def getCurrentTimestampFunction():
    '''public static String getCurrentTimestampFunction()
    '''
def parseExpression():
    '''public static Node parseExpression(final String expression, final ULocale icuLocale)
    '''
def validateExpression():
    '''public static void validateExpression(final Node parsedExpr, final String objectName, final Set<String> validAttributes, final String category)
    '''
def getExportReportList():
    '''public static String[] getExportReportList()
    '''
def isMultiLang():
    '''public static boolean isMultiLang()
    '''
def setLabelSyncFlag():
    '''public static void setLabelSyncFlag()
    '''
def encrypt():
    '''public static String encrypt(final String source)
    '''
def decrypt():
    '''public static String decrypt(final String source)
    '''
def addToHyperlinkQueryUrl():
    '''public static String addToHyperlinkQueryUrl(final String sessionid, final String queryUrl)
    '''
def getHyperlinkQueryUrl():
    '''public static HashMap getHyperlinkQueryUrl(final String sessionid, final String maxhlparam)
    '''
def addToReportWhere():
    '''public static String addToReportWhere(final String userId, final String where, final String displaywhere)
    public static String addToReportWhere(final String userId, final String where, final String displaywhere, final String reportName)
    '''
def getReportWhere():
    '''public static HashMap getReportWhere(final String userId, final String whereId)
    '''
def userSelectDynamicQueryEnabled():
    '''public static boolean userSelectDynamicQueryEnabled()
    '''
def excludeDynamicQuery():
    '''public static boolean excludeDynamicQuery(final MboRemote reportAdHoc)
    '''
def getRelation():
    '''public static RelationInfo getRelation(final String objectName, final String relationName)
    '''
def concatAttachmentPDFFiles():
    '''public static void concatAttachmentPDFFiles(final String outPutDirPath, final String outPutFilePath, final Vector<PathAndReportFlag> listOfFiles, final MXLogger logger)
    public static void concatAttachmentPDFFiles(final String outPutDirPath, final String outPutFilePath, final Vector<PathAndReportFlag> listOfFiles, final boolean DuplexPrintEnabledOverride, final MXLogger logger)
    '''
def addEmptyPage():
    '''public static void addEmptyPage(final PdfCopy writer, final String emptyFilePath, final MXLogger logger)
    '''
def isOddPage():
    '''public static boolean isOddPage(final int pagesMerged)
    '''
def createEmptyPdfFile():
    '''public static boolean createEmptyPdfFile(final String filePath, final MXLogger logger)
    '''
def getBooleanProperty():
    '''public static boolean getBooleanProperty(final String propertyname)
    '''
def validateLocalFile():
    '''public static boolean validateLocalFile(String attchUrl)
    '''
def convertAllPrintableAttachmentsOfThisMboToPDF():
    '''public static int convertAllPrintableAttachmentsOfThisMboToPDF(final MboRemote baseMbo, final Vector listOfFilesVector, final String outputFolder, int currentDocIndex, final MXLogger logger)
    '''
def getFileForGivenUrl():
    '''public static String getFileForGivenUrl(final String imagePath, final boolean debugLocal)
    '''
def addAndCleanupDirectoty():
    '''public static void addAndCleanupDirectoty(final String dirPath)
    '''
def deleteFolder():
    '''public static boolean deleteFolder(final String folderName)
    '''
def deleteAllFilesFromFolder():
    '''public static void deleteAllFilesFromFolder(final File folder)
    '''
def getByteArrayforUrl():
    '''public static byte[] getByteArrayforUrl(final String docpath)
    '''
def getFileTypeList():
    '''public static List<ReportEmailFileTypeInfo> getFileTypeList()
    '''
def validateDPKey():
    '''public static boolean validateDPKey(final String directPrintKey)
    '''
def getWhereClause():
    '''public String getWhereClause()
    '''
def hasExtendedFields():
    '''public boolean hasExtendedFields()
    '''
