DEFAULT_MAX_CONCURRENT_THREADCOUNT = "int  3"
PROPERTY_MAXCONCURRENTRUN = "String  \"mxe.report.birt.maxconcurrentrun\""
def createReportJob():
    '''returns long\n\n
    createReportJob(final UserInfo userInfo, final String reportName, final String appName, final String userName, final boolean scheduledJob, final long startTime)\n
    '''
def getReportJobId():
    '''returns long\n\n
    getReportJobId(final String threadName)\n
    getReportJobId()\n
    '''
def removeActiveThread():
    '''returns None\n\n
    removeActiveThread(final String threadName)\n
    removeActiveThread(final String threadName, final boolean removeIf12MinIdle)\n
    '''
def removeReportJob():
    '''returns None\n\n
    removeReportJob(final UserInfo userInfo, final long reportJobId)\n
    '''
def setActiveThreadsFromScriptContext():
    '''returns None\n\n
    setActiveThreadsFromScriptContext(final String jobCancelThreadName, final HashSet<String> listOfActiveThreadsParam)\n
    '''
def cancelReportJob():
    '''returns None\n\n
    cancelReportJob(final long reportJobId)\n
    '''
def cancelReportJobOnThisServer():
    '''returns boolean\n\n
    cancelReportJobOnThisServer(final long reportJobId)\n
    '''
def isReportJobCancelled():
    '''returns boolean\n\n
    isReportJobCancelled(final long reportJobId)\n
    '''
def renewActiveThread():
    '''returns None\n\n
    renewActiveThread(final String threadName)\n
    '''
def updateActiveThread():
    '''returns None\n\n
    updateActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob, final long scheduleJobId)\n
    '''
def isOverloaded():
    '''returns boolean\n\n
    isOverloaded()\n
    '''
def getMaxAllowedActiveReportThreads():
    '''returns int\n\n
    getMaxAllowedActiveReportThreads()\n
    '''
def getNumberOfActiveReports():
    '''returns int\n\n
    getNumberOfActiveReports()\n
    '''
def setStartTime():
    '''returns None\n\n
    setStartTime(final long sTime)\n
    '''
def getStartTime():
    '''returns long\n\n
    getStartTime()\n
    '''
def setRenewTime():
    '''returns None\n\n
    setRenewTime(final long rTime)\n
    '''
def getRenewTime():
    '''returns long\n\n
    getRenewTime()\n
    '''
def getAppName():
    '''returns String\n\n
    getAppName()\n
    '''
def setAppName():
    '''returns None\n\n
    setAppName(final String appName)\n
    '''
def getReportName():
    '''returns String\n\n
    getReportName()\n
    '''
def setReportName():
    '''returns None\n\n
    setReportName(final String reportName)\n
    '''
def getUserName():
    '''returns String\n\n
    getUserName()\n
    '''
def setUserName():
    '''returns None\n\n
    setUserName(final String userName)\n
    '''
def isScheduledJob():
    '''returns boolean\n\n
    isScheduledJob()\n
    '''
def setScheduledJob():
    '''returns None\n\n
    setScheduledJob(final boolean scheduledJob)\n
    '''
def getScheduledJobId():
    '''returns long\n\n
    getScheduledJobId()\n
    '''
def setScheduledJobId():
    '''returns None\n\n
    setScheduledJobId(final long scheduleJobId)\n
    '''
def setReportJobId():
    '''returns None\n\n
    setReportJobId(final long reportJobId)\n
    '''
def getJobStatus():
    '''returns int\n\n
    getJobStatus()\n
    '''
def setJobStatus():
    '''returns None\n\n
    setJobStatus(final int jobStatus)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def setCancelTime():
    '''returns None\n\n
    setCancelTime()\n
    '''
def getCancelTime():
    '''returns long\n\n
    getCancelTime()\n
    '''
def ():
    '''returns ReportCancelStatusUpdateThread\n\n
    ()\n
    ()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
