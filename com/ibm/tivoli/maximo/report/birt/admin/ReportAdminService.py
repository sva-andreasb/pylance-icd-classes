PROPERTY_VIEWERURL = "String  \"mxe.report.birt.viewerurl\""
def ():
    '''returns PropertiesFileFilter\n\n
    (final MXServer mxServer)\n
    ()\n
    (final String propertiesName)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def startBatchAllReportsImport():
    '''returns None\n\n
    startBatchAllReportsImport(final UserInfo userInfo, final boolean isSynchronous)\n
    '''
def startBatchReportImport():
    '''returns None\n\n
    startBatchReportImport()\n
    startBatchReportImport(final boolean allTenants)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def updateReportDesign():
    '''returns byte[]\n\n
    updateReportDesign(final UserInfo userInfo, final String reportName, final String appName, final boolean saveChanges)\n
    updateReportDesign(final UserInfo userInfo, final String reportName, final String appName, final boolean saveChanges, final String updateType)\n
    '''
def importReport():
    '''returns None\n\n
    importReport(final UserInfo userInfo, final ReportImportInfo reportImportInfo, final boolean fromUI)\n
    '''
def importReportLibrary():
    '''returns None\n\n
    importReportLibrary(final UserInfo userInfo, final ReportImportInfo reportImportInfo)\n
    '''
def prepareReportForRun():
    '''returns ReportRunInfo\n\n
    prepareReportForRun(final UserInfo userInfo, final String reportName, final String appName)\n
    '''
def cleanupReportResources():
    '''returns None\n\n
    cleanupReportResources(final ReportRunInfo reportRunInfo)\n
    '''
def prepareReportLibraryForExport():
    '''returns ReportRunInfo\n\n
    prepareReportLibraryForExport(final UserInfo userInfo, final String reportName)\n
    '''
def prepareReportDesignForRun():
    '''returns ReportRunInfo\n\n
    prepareReportDesignForRun(final UserInfo userInfo, final String reportName, final boolean extractAll)\n
    prepareReportDesignForRun(final UserInfo userInfo, final String reportName, final boolean extractAll, final boolean forExport)\n
    '''
def extractResourcesFromByteArray():
    '''returns None\n\n
    extractResourcesFromByteArray(final ByteArrayInputStream resources, final String outputFolder)\n
    '''
def exportReport():
    '''returns byte[]\n\n
    exportReport(final UserInfo userInfo, final String reportName, final String appName)\n
    '''
def getExportReportFolder():
    '''returns String\n\n
    getExportReportFolder(final UserInfo userInfo, final String reportName, final String appName)\n
    '''
def exportReportLibrary():
    '''returns byte[]\n\n
    exportReportLibrary(final UserInfo userInfo, final String reportName)\n
    '''
def getReportLibraryNameList():
    '''returns ArrayList<String>\n\n
    getReportLibraryNameList(final UserInfo userInfo)\n
    '''
def getDateFormat():
    '''returns String\n\n
    getDateFormat(final UserInfo userInfo)\n
    '''
def getTimeFormat():
    '''returns String\n\n
    getTimeFormat(final UserInfo userInfo)\n
    '''
def getDateTimeFormat():
    '''returns String\n\n
    getDateTimeFormat(final UserInfo userInfo)\n
    getDateTimeFormat(final UserInfo userInfo, final String objectName, final String attributeName)\n
    '''
def getNumberFormat():
    '''returns String\n\n
    getNumberFormat(final UserInfo userInfo)\n
    getNumberFormat(final UserInfo userInfo, final String objectName, final String attributeName)\n
    '''
def getDecimalFormat():
    '''returns String\n\n
    getDecimalFormat(final UserInfo userInfo, final int fractionDigits)\n
    '''
def runReportWithAttachments():
    '''returns String\n\n
    runReportWithAttachments(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)\n
    runReportWithAttachments(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final boolean withAttachment, final Map<String, Object> additionalInfoMap)\n
    '''
def runReportInImmediateMode():
    '''returns byte[]\n\n
    runReportInImmediateMode(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)\n
    runReportInImmediateMode(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap)\n
    '''
def runReport():
    '''returns byte[]\n\n
    runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat)\n
    runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap)\n
    runReport(final UserInfo userInfo, final String reportName, final String appName, final ReportParameterData parameterData, final String outputFileName, final String outputFormat, final Map<String, Object> additionalInfoMap, final boolean scheduled)\n
    '''
def createReportUsageLog():
    '''returns None\n\n
    createReportUsageLog(final UserInfo userInfo, final ReportUsageLogInfo usageLogInfo)\n
    '''
def isOverloaded():
    '''returns boolean\n\n
    isOverloaded()\n
    '''
def getReportEngineState():
    '''returns int\n\n
    getReportEngineState()\n
    '''
def addActiveThread():
    '''returns Long\n\n
    addActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob)\n
    '''
def removeActiveThread():
    '''returns None\n\n
    removeActiveThread(final String threadName)\n
    '''
def renewActiveThread():
    '''returns None\n\n
    renewActiveThread(final String threadName)\n
    '''
def setActiveThreadsFromScriptContext():
    '''returns None\n\n
    setActiveThreadsFromScriptContext(final String contextThreadName, final HashSet listOfActiveThreads)\n
    '''
def exportReportImportInputInfo():
    '''returns String\n\n
    exportReportImportInputInfo(final UserInfo userInfo, final String reportName, final String appName)\n
    '''
def exportLibraryImportInputInfo():
    '''returns String\n\n
    exportLibraryImportInputInfo(final UserInfo userInfo, final String reportName)\n
    '''
def createReportDesign():
    '''returns None\n\n
    createReportDesign(final UserInfo userInfo, final CreateReportInputInfo reportInputInfo)\n
    '''
def getFileContent():
    '''returns byte[]\n\n
    getFileContent(final String fileName)\n
    '''
def createResourcesZip():
    '''returns byte[]\n\n
    createResourcesZip(final File[] files)\n
    '''
def isAuthorizedToRunReport():
    '''returns boolean\n\n
    isAuthorizedToRunReport(final UserInfo userInfo, final String reportName, final String appName)\n
    '''
def getReportViewerURL():
    '''returns String\n\n
    getReportViewerURL()\n
    '''
def cancelReportJob():
    '''returns None\n\n
    cancelReportJob(final long reportJobId)\n
    '''
def cancelReportJobOnThisServer():
    '''returns None\n\n
    cancelReportJobOnThisServer(final long reportJobId)\n
    '''
def isReportJobCancelled():
    '''returns boolean\n\n
    isReportJobCancelled(final long reportJobId)\n
    '''
def exportTransientQBRContent():
    '''returns None\n\n
    exportTransientQBRContent(final String brosId, final MXSession session)\n
    '''
def getTransientQBRParamsMboSet():
    '''returns MboSetRemote\n\n
    getTransientQBRParamsMboSet(final String brosId, final MXSession session)\n
    '''
def removeBROSReport():
    '''returns None\n\n
    removeBROSReport(final String brosId)\n
    '''
def sendEmail():
    '''returns None\n\n
    sendEmail(MXLogger logger, UserInfo userInfo, final String templateID, final String[] to, final String from, final MboRemote report, final TextReplacement replacer)\n
    '''
def getReport():
    '''returns MboRemote\n\n
    getReport(final UserInfo userInfo, final String reportName, final String appName)\n
    '''
def deleteNeededFileFromAttachmentTempDirectory():
    '''returns None\n\n
    deleteNeededFileFromAttachmentTempDirectory(final String outputFolder, final Vector<PathAndReportFlag> listOfFilesVector, final MXLogger logger)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File pathname)\n
    '''
