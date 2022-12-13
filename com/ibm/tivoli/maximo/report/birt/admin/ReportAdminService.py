PROPERTY_VIEWERURL = "String  \"mxe.report.birt.viewerurl\""
def ReportAdminService():
    '''public ReportAdminService(final MXServer mxServer)
    '''
def init():
    '''public void init()
    '''
def startBatchAllReportsImport():
    '''public void startBatchAllReportsImport(final UserInfo userInfo, final boolean isSynchronous)
    '''
def startBatchReportImport():
    '''public void startBatchReportImport()
    public void startBatchReportImport(final boolean allTenants)
    '''
def destroy():
    '''public void destroy()
    '''
def updateReportDesign():
    '''public byte[] updateReportDesign(final UserInfo userInfo, final String reportName, final String appName, final boolean saveChanges)
    public byte[] updateReportDesign(final UserInfo userInfo, final String reportName, final String appName, final boolean saveChanges, final String updateType)
    '''
def importReport():
    '''public void importReport(final UserInfo userInfo, final ReportImportInfo reportImportInfo, final boolean fromUI)
    '''
def importReportLibrary():
    '''public void importReportLibrary(final UserInfo userInfo, final ReportImportInfo reportImportInfo)
    '''
def prepareReportForRun():
    '''public ReportRunInfo prepareReportForRun(final UserInfo userInfo, final String reportName, final String appName)
    '''
def cleanupReportResources():
    '''public void cleanupReportResources(final ReportRunInfo reportRunInfo)
    '''
def prepareReportLibraryForExport():
    '''public ReportRunInfo prepareReportLibraryForExport(final UserInfo userInfo, final String reportName)
    '''
def prepareReportDesignForRun():
    '''public ReportRunInfo prepareReportDesignForRun(final UserInfo userInfo, final String reportName, final boolean extractAll)
    public ReportRunInfo prepareReportDesignForRun(final UserInfo userInfo, final String reportName, final boolean extractAll, final boolean forExport)
    '''
def createUniqueTempFolder():
    '''public static String createUniqueTempFolder(final String parentFolderName)
    '''
def extractResourcesFromByteArray():
    '''public void extractResourcesFromByteArray(final ByteArrayInputStream resources, final String outputFolder)
    '''
def exportReport():
    '''public byte[] exportReport(final UserInfo userInfo, final String reportName, final String appName)
    '''
def getExportReportFolder():
    '''public String getExportReportFolder(final UserInfo userInfo, final String reportName, final String appName)
    '''
def exportReportLibrary():
    '''public byte[] exportReportLibrary(final UserInfo userInfo, final String reportName)
    '''
def getReportLibraryNameList():
    '''public ArrayList<String> getReportLibraryNameList(final UserInfo userInfo)
    '''
def getReportNameList():
    '''public TreeMap<String, List> getReportNameList(final UserInfo userInfo)
    public TreeMap<String, List> getReportNameList(final UserInfo userInfo, final int reportType)
    '''
def getDateFormat():
    '''public String getDateFormat(final UserInfo userInfo)
    '''
def getTimeFormat():
    '''public String getTimeFormat(final UserInfo userInfo)
    '''
def getDateTimeFormat():
    '''public String getDateTimeFormat(final UserInfo userInfo)
    public String getDateTimeFormat(final UserInfo userInfo, final String objectName, final String attributeName)
    '''
def getNumberFormat():
    '''public String getNumberFormat(final UserInfo userInfo)
    public String getNumberFormat(final UserInfo userInfo, final String objectName, final String attributeName)
    '''
def getDecimalFormat():
    '''public String getDecimalFormat(final UserInfo userInfo, final int fractionDigits)
    '''
def runReportWithAttachments():
    '''public String runReportWithAttachments(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)
    public String runReportWithAttachments(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final boolean withAttachment, final Map<String, Object> additionalInfoMap)
    '''
def runReportInImmediateMode():
    '''public byte[] runReportInImmediateMode(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)
    public byte[] runReportInImmediateMode(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap)
    '''
def runReport():
    '''public byte[] runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)
    public byte[] runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap)
    public byte[] runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap, final boolean scheduled)
    '''
def createReportUsageLog():
    '''public void createReportUsageLog(final UserInfo userInfo, final ReportUsageLogInfo usageLogInfo)
    '''
def isOverloaded():
    '''public boolean isOverloaded()
    '''
def getReportEngineState():
    '''public int getReportEngineState()
    '''
def addActiveThread():
    '''public Long addActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob)
    '''
def removeActiveThread():
    '''public void removeActiveThread(final String threadName)
    '''
def renewActiveThread():
    '''public void renewActiveThread(final String threadName)
    '''
def setActiveThreadsFromScriptContext():
    '''public void setActiveThreadsFromScriptContext(final String contextThreadName, final HashSet listOfActiveThreads)
    '''
def exportReportImportInputInfo():
    '''public String exportReportImportInputInfo(final UserInfo userInfo, final String reportName, final String appName)
    '''
def exportLibraryImportInputInfo():
    '''public String exportLibraryImportInputInfo(final UserInfo userInfo, final String reportName)
    '''
def createReportDesign():
    '''public void createReportDesign(final UserInfo userInfo, final CreateReportInputInfo reportInputInfo)
    '''
def getFileContent():
    '''public byte[] getFileContent(final String fileName)
    '''
def createResourcesZip():
    '''public byte[] createResourcesZip(final File[] files)
    '''
def isAuthorizedToRunReport():
    '''public boolean isAuthorizedToRunReport(final UserInfo userInfo, final String reportName, final String appName)
    '''
def getReportViewerURL():
    '''public String getReportViewerURL()
    '''
def cancelReportJob():
    '''public void cancelReportJob(final long reportJobId)
    '''
def cancelReportJobOnThisServer():
    '''public void cancelReportJobOnThisServer(final long reportJobId)
    '''
def isReportJobCancelled():
    '''public boolean isReportJobCancelled(final long reportJobId)
    '''
def exportTransientQBRContent():
    '''public void exportTransientQBRContent(final String brosId, final MXSession session)
    '''
def getTransientQBRParamsMboSet():
    '''public MboSetRemote getTransientQBRParamsMboSet(final String brosId, final MXSession session)
    '''
def removeBROSReport():
    '''public void removeBROSReport(final String brosId)
    '''
def createBROSUniqueTempFolder():
    '''public static String createBROSUniqueTempFolder(final String parentFolderName)
    '''
def sendEmail():
    '''public void sendEmail(MXLogger logger, UserInfo userInfo, final String templateID, final String[] to, final String from, final MboRemote report, final TextReplacement replacer)
    '''
def getReport():
    '''public MboRemote getReport(final UserInfo userInfo, final String reportName, final String appName)
    '''
def deleteNeededFileFromAttachmentTempDirectory():
    '''public void deleteNeededFileFromAttachmentTempDirectory(final String outputFolder, final Vector<PathAndReportFlag> listOfFilesVector, final MXLogger logger)
    '''
def ReportJobCleanupTask():
    '''public ReportJobCleanupTask()
    '''
def run():
    '''public void run()
    '''
def PropertiesFileFilter():
    '''public PropertiesFileFilter(final String propertiesName)
    '''
def accept():
    '''public boolean accept(final File pathname)
    '''
