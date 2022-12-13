def convertOnceToSchedule():
'''public static String convertOnceToSchedule(final Date date, final Locale locale, final TimeZone clientTimeZone)
'''
pass
def verifySchedule():
'''public static void verifySchedule(final MboRemote reportSched)
'''
pass
def qualifyWhere():
'''public static String qualifyWhere(final String where, final String baseTable)
'''
pass
def getWhereData():
'''public static WhereData getWhereData(String where, final String baseTable)
'''
pass
def getDBType():
'''public static String getDBType()
'''
pass
def hasParameters():
'''public static boolean hasParameters(final MboRemote reportRemote)
'''
pass
def calculateTotalReservedHours():
'''public static String calculateTotalReservedHours(final Calendar startReserve, final Calendar endReserve)
'''
pass
def checkReserveTimeOverlaps():
'''public static void checkReserveTimeOverlaps(final MboSetRemote reportProcReserveSet, final String appname, final String reportname, final Calendar startReserve, final Calendar endReserve, final String day, final long currentMboUniqueIDValue)
'''
pass
def validateAvailSchedulingTime():
'''public static boolean validateAvailSchedulingTime(final String appname, final String reportname, final Date date, final String scheduleType, final UserInfo userInfo)
'''
pass
def toHourMinSecFromMiliSec():
'''public static String toHourMinSecFromMiliSec(final long runTimeMilliSeconds)
'''
pass
def resetScheduleAvailability():
'''public static void resetScheduleAvailability(final String currAppname, final String currReportname, final UserInfo userInfo)
'''
pass
def addReportProcSchedulableRecord():
'''public static void addReportProcSchedulableRecord(final MboRemote reportProcSched, final String appname, final String reportname, final String day, final Date startSchedulable, final Date endSchedulable, final String timezone)
'''
pass
def finishReportProcSchedulableRecord():
'''public static void finishReportProcSchedulableRecord(final MboSetRemote reportProcSchedSet, final MboRemote reportProcSched, final String appname, final String reportname, final String day, Integer dayNum, final Date startSchedulable, final boolean needsEndingTime, final boolean setFullDayAvailability, final String timezone)
'''
pass
def writeFullDayAvailability():
'''public static void writeFullDayAvailability(final MboSetRemote reportProcSchedSet, MboRemote reportProcSched, final String appname, final String reportname, final Integer dayNum, final UserInfo userInfo, final String timezone)
'''
pass
def scheduleEndTime():
'''public static void scheduleEndTime(final int reserveStartMin, final Calendar endSchedulableTime, final Calendar startReserve)
'''
pass
def scheduleStartTime():
'''public static void scheduleStartTime(final int reserveEndMin, final Calendar startSchedulableTime, final Calendar endReserve)
'''
pass
def getDayName():
'''public static String getDayName(String dayNum, final UserInfo userInfo)
'''
pass
def convertDateToMXServer():
'''public static Date convertDateToMXServer(final Locale clientLocale, final String clientTimezone, final Date date)
'''
pass
def convertDateToClientTimezone():
'''public static Date convertDateToClientTimezone(final Locale clientLocale, final String clientTimezone, final Date date)
'''
pass
def hasSubSelects():
'''public static boolean hasSubSelects(final String whereClause)
'''
pass
def getViewerURL():
'''public static String getViewerURL(final String contextPath, final String sessionId, final UserInfo userInfo, final Hashtable reportParams)
public static String getViewerURL(final String contextPath, final String sessionId, final UserInfo userInfo, final Hashtable reportParams, final boolean isDirectPrint)
'''
pass
def getViewerURLToFindBaseUrl():
'''public static String getViewerURLToFindBaseUrl(final String contextPath, final boolean isDirectPrint)
'''
pass
def createReportName():
'''public static String createReportName(final String appName, final String userName)
'''
pass
def getUserFolderName():
'''public static String getUserFolderName(final UserInfo userInfo)
public static String getUserFolderName(final String userName)
'''
pass
def addParamstring():
'''public static void addParamstring(final String key, final String value, final Hashtable reportParams)
'''
pass
def updateReportLabelsAllLangs():
'''public static void updateReportLabelsAllLangs(final UserInfo ui)
'''
pass
def updateReportLabels():
'''public static void updateReportLabels(final UserInfo ui)
'''
pass
def makeSafeForXML():
'''public static String makeSafeForXML(String value)
'''
pass
def replaceString():
'''public static String replaceString(String str, final String pattern, final String replacement)
'''
pass
def getcurrentSecAttKeyRecord():
'''public static ReportSecAttKeyRecord getcurrentSecAttKeyRecord(final UserInfo userInfo)
'''
pass
def getKey():
'''public static byte[] getKey(final String seqNumberString)
'''
pass
def addToReportAttachDocs():
'''public static String addToReportAttachDocs(final String userId, final String url)
'''
pass
def getReportAttachDocsUrl():
'''public static String getReportAttachDocsUrl(final String userId, final String key)
'''
pass
def getRandomString():
'''public static String getRandomString(final int len)
public static String getRandomString()
'''
pass
def formatWhere():
'''public static String formatWhere(String whereClause, final String baseTable, final UserInfo ui)
'''
pass
def addToReportBrosParam():
'''public static void addToReportBrosParam(final Hashtable paramHashtable, final boolean isSessionParam, final long brosUniqueID, final UserInfo userInfo)
public static void addToReportBrosParam(final String paramName, final String ParamValue, final boolean isSessionParam, final long brosUniqueID, final UserInfo userInfo)
'''
pass
def addToReportBrosUrl():
'''public static void addToReportBrosUrl(final Vector<String> reporUrlParam, final Vector<Boolean> securedAttachFlags, final boolean isQpixUrl, final long brosUniqueID, final UserInfo userInfo)
'''
pass
def getEmailAddress():
'''public static String getEmailAddress(final String userId)
'''
pass
def hasAttribute():
'''public static boolean hasAttribute(final String expression, final String objectName, final Set<String> validAttributes)
public static boolean hasAttribute(final Node expression, final String objectName, final Set<String> validAttributes)
'''
pass
def getValidAttributes():
'''public static Set<String> getValidAttributes(final MosDetailInfo detailInfo)
public static Set<String> getValidAttributes(final String objectName)
'''
pass
def getMosDetailInfo():
'''public static MosDetailInfo getMosDetailInfo(final String intObjectName, final int objectID)
'''
pass
def getColumnName():
'''public static String getColumnName(final MboValueInfo mvi)
'''
pass
def getEntityName():
'''public static String getEntityName(final String objectName)
'''
pass
def getCurrentDateFunction():
'''public static String getCurrentDateFunction()
'''
pass
def getCurrentTimestampFunction():
'''public static String getCurrentTimestampFunction()
'''
pass
def parseExpression():
'''public static Node parseExpression(final String expression, final ULocale icuLocale)
'''
pass
def validateExpression():
'''public static void validateExpression(final Node parsedExpr, final String objectName, final Set<String> validAttributes, final String category)
'''
pass
def getExportReportList():
'''public static String[] getExportReportList()
'''
pass
def isMultiLang():
'''public static boolean isMultiLang()
'''
pass
def setLabelSyncFlag():
'''public static void setLabelSyncFlag()
'''
pass
def encrypt():
'''public static String encrypt(final String source)
'''
pass
def decrypt():
'''public static String decrypt(final String source)
'''
pass
def addToHyperlinkQueryUrl():
'''public static String addToHyperlinkQueryUrl(final String sessionid, final String queryUrl)
'''
pass
def getHyperlinkQueryUrl():
'''public static HashMap getHyperlinkQueryUrl(final String sessionid, final String maxhlparam)
'''
pass
def addToReportWhere():
'''public static String addToReportWhere(final String userId, final String where, final String displaywhere)
public static String addToReportWhere(final String userId, final String where, final String displaywhere, final String reportName)
'''
pass
def getReportWhere():
'''public static HashMap getReportWhere(final String userId, final String whereId)
'''
pass
def userSelectDynamicQueryEnabled():
'''public static boolean userSelectDynamicQueryEnabled()
'''
pass
def excludeDynamicQuery():
'''public static boolean excludeDynamicQuery(final MboRemote reportAdHoc)
'''
pass
def getRelation():
'''public static RelationInfo getRelation(final String objectName, final String relationName)
'''
pass
def concatAttachmentPDFFiles():
'''public static void concatAttachmentPDFFiles(final String outPutDirPath, final String outPutFilePath, final Vector<PathAndReportFlag> listOfFiles, final MXLogger logger)
public static void concatAttachmentPDFFiles(final String outPutDirPath, final String outPutFilePath, final Vector<PathAndReportFlag> listOfFiles, final boolean DuplexPrintEnabledOverride, final MXLogger logger)
'''
pass
def addEmptyPage():
'''public static void addEmptyPage(final PdfCopy writer, final String emptyFilePath, final MXLogger logger)
'''
pass
def isOddPage():
'''public static boolean isOddPage(final int pagesMerged)
'''
pass
def createEmptyPdfFile():
'''public static boolean createEmptyPdfFile(final String filePath, final MXLogger logger)
'''
pass
def getBooleanProperty():
'''public static boolean getBooleanProperty(final String propertyname)
'''
pass
def validateLocalFile():
'''public static boolean validateLocalFile(String attchUrl)
'''
pass
def convertAllPrintableAttachmentsOfThisMboToPDF():
'''public static int convertAllPrintableAttachmentsOfThisMboToPDF(final MboRemote baseMbo, final Vector listOfFilesVector, final String outputFolder, int currentDocIndex, final MXLogger logger)
'''
pass
def getFileForGivenUrl():
'''public static String getFileForGivenUrl(final String imagePath, final boolean debugLocal)
'''
pass
def addAndCleanupDirectoty():
'''public static void addAndCleanupDirectoty(final String dirPath)
'''
pass
def deleteFolder():
'''public static boolean deleteFolder(final String folderName)
'''
pass
def deleteAllFilesFromFolder():
'''public static void deleteAllFilesFromFolder(final File folder)
'''
pass
def getByteArrayforUrl():
'''public static byte[] getByteArrayforUrl(final String docpath)
'''
pass
def getFileTypeList():
'''public static List<ReportEmailFileTypeInfo> getFileTypeList()
'''
pass
def validateDPKey():
'''public static boolean validateDPKey(final String directPrintKey)
'''
pass
def getWhereClause():
'''public String getWhereClause()
'''
pass
def hasExtendedFields():
'''public boolean hasExtendedFields()
'''
pass
