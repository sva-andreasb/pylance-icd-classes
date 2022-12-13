PROPERTY_VIEWERURL = "String  mxe.report.birt.viewerurl""
def ReportAdminService():
'''public ReportAdminService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
'''
pass
def startBatchAllReportsImport():
'''public void startBatchAllReportsImport(final UserInfo userInfo, final boolean isSynchronous)
'''
pass
def startBatchReportImport():
'''public void startBatchReportImport()
public void startBatchReportImport(final boolean allTenants)
'''
pass
def destroy():
'''public void destroy()
'''
pass
def updateReportDesign():
'''public byte[] updateReportDesign(final UserInfo userInfo, final String reportName, final String appName, final boolean saveChanges)
public byte[] updateReportDesign(final UserInfo userInfo, final String reportName, final String appName, final boolean saveChanges, final String updateType)
'''
pass
def importReport():
'''public void importReport(final UserInfo userInfo, final ReportImportInfo reportImportInfo, final boolean fromUI)
'''
pass
def importReportLibrary():
'''public void importReportLibrary(final UserInfo userInfo, final ReportImportInfo reportImportInfo)
'''
pass
def prepareReportForRun():
'''public ReportRunInfo prepareReportForRun(final UserInfo userInfo, final String reportName, final String appName)
'''
pass
def cleanupReportResources():
'''public void cleanupReportResources(final ReportRunInfo reportRunInfo)
'''
pass
def prepareReportLibraryForExport():
'''public ReportRunInfo prepareReportLibraryForExport(final UserInfo userInfo, final String reportName)
'''
pass
def prepareReportDesignForRun():
'''public ReportRunInfo prepareReportDesignForRun(final UserInfo userInfo, final String reportName, final boolean extractAll)
public ReportRunInfo prepareReportDesignForRun(final UserInfo userInfo, final String reportName, final boolean extractAll, final boolean forExport)
'''
pass
def createUniqueTempFolder():
'''public static String createUniqueTempFolder(final String parentFolderName)
'''
pass
def extractResourcesFromByteArray():
'''public void extractResourcesFromByteArray(final ByteArrayInputStream resources, final String outputFolder)
'''
pass
def exportReport():
'''public byte[] exportReport(final UserInfo userInfo, final String reportName, final String appName)
'''
pass
def getExportReportFolder():
'''public String getExportReportFolder(final UserInfo userInfo, final String reportName, final String appName)
'''
pass
def exportReportLibrary():
'''public byte[] exportReportLibrary(final UserInfo userInfo, final String reportName)
'''
pass
def getReportLibraryNameList():
'''public ArrayList<String> getReportLibraryNameList(final UserInfo userInfo)
'''
pass
def getReportNameList():
'''public TreeMap<String, List> getReportNameList(final UserInfo userInfo)
public TreeMap<String, List> getReportNameList(final UserInfo userInfo, final int reportType)
'''
pass
def getDateFormat():
'''public String getDateFormat(final UserInfo userInfo)
'''
pass
def getTimeFormat():
'''public String getTimeFormat(final UserInfo userInfo)
'''
pass
def getDateTimeFormat():
'''public String getDateTimeFormat(final UserInfo userInfo)
public String getDateTimeFormat(final UserInfo userInfo, final String objectName, final String attributeName)
'''
pass
def getNumberFormat():
'''public String getNumberFormat(final UserInfo userInfo)
public String getNumberFormat(final UserInfo userInfo, final String objectName, final String attributeName)
'''
pass
def getDecimalFormat():
'''public String getDecimalFormat(final UserInfo userInfo, final int fractionDigits)
'''
pass
def runReportWithAttachments():
'''public String runReportWithAttachments(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)
public String runReportWithAttachments(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final boolean withAttachment, final Map<String, Object> additionalInfoMap)
'''
pass
def runReportInImmediateMode():
'''public byte[] runReportInImmediateMode(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)
public byte[] runReportInImmediateMode(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap)
'''
pass
def runReport():
'''public byte[] runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)
public byte[] runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap)
public byte[] runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap, final boolean scheduled)
'''
pass
def createReportUsageLog():
'''public void createReportUsageLog(final UserInfo userInfo, final ReportUsageLogInfo usageLogInfo)
'''
pass
def isOverloaded():
'''public boolean isOverloaded()
'''
pass
def getReportEngineState():
'''public int getReportEngineState()
'''
pass
def addActiveThread():
'''public Long addActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob)
'''
pass
def removeActiveThread():
'''public void removeActiveThread(final String threadName)
'''
pass
def renewActiveThread():
'''public void renewActiveThread(final String threadName)
'''
pass
def setActiveThreadsFromScriptContext():
'''public void setActiveThreadsFromScriptContext(final String contextThreadName, final HashSet listOfActiveThreads)
'''
pass
def exportReportImportInputInfo():
'''public String exportReportImportInputInfo(final UserInfo userInfo, final String reportName, final String appName)
'''
pass
def exportLibraryImportInputInfo():
'''public String exportLibraryImportInputInfo(final UserInfo userInfo, final String reportName)
'''
pass
def createReportDesign():
'''public void createReportDesign(final UserInfo userInfo, final CreateReportInputInfo reportInputInfo)
'''
pass
def getFileContent():
'''public byte[] getFileContent(final String fileName)
'''
pass
def createResourcesZip():
'''public byte[] createResourcesZip(final File[] files)
'''
pass
def isAuthorizedToRunReport():
'''public boolean isAuthorizedToRunReport(final UserInfo userInfo, final String reportName, final String appName)
'''
pass
def getReportViewerURL():
'''public String getReportViewerURL()
'''
pass
def cancelReportJob():
'''public void cancelReportJob(final long reportJobId)
'''
pass
def cancelReportJobOnThisServer():
'''public void cancelReportJobOnThisServer(final long reportJobId)
'''
pass
def isReportJobCancelled():
'''public boolean isReportJobCancelled(final long reportJobId)
'''
pass
def exportTransientQBRContent():
'''public void exportTransientQBRContent(final String brosId, final MXSession session)
'''
pass
def getTransientQBRParamsMboSet():
'''public MboSetRemote getTransientQBRParamsMboSet(final String brosId, final MXSession session)
'''
pass
def removeBROSReport():
'''public void removeBROSReport(final String brosId)
'''
pass
def createBROSUniqueTempFolder():
'''public static String createBROSUniqueTempFolder(final String parentFolderName)
'''
pass
def sendEmail():
'''public void sendEmail(MXLogger logger, UserInfo userInfo, final String templateID, final String[] to, final String from, final MboRemote report, final TextReplacement replacer)
'''
pass
def getReport():
'''public MboRemote getReport(final UserInfo userInfo, final String reportName, final String appName)
'''
pass
def deleteNeededFileFromAttachmentTempDirectory():
'''public void deleteNeededFileFromAttachmentTempDirectory(final String outputFolder, final Vector<PathAndReportFlag> listOfFilesVector, final MXLogger logger)
'''
pass
def ReportJobCleanupTask():
'''public ReportJobCleanupTask()
'''
pass
def run():
'''public void run()
'''
pass
def PropertiesFileFilter():
'''public PropertiesFileFilter(final String propertiesName)
'''
pass
def accept():
'''public boolean accept(final File pathname)
'''
pass
