DEFAULT_MAX_CONCURRENT_THREADCOUNT = "int  3"
PROPERTY_MAXCONCURRENTRUN = "String  \"mxe.report.birt.maxconcurrentrun\""
def getActiveReportThreadManager():
    '''public static ActiveReportThreadManager getActiveReportThreadManager()
    '''
def addActiveThread():
    '''public synchronized Long addActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob)
    '''
def createReportJob():
    '''public long createReportJob(final UserInfo userInfo, final String reportName, final String appName, final String userName, final boolean scheduledJob, final long startTime)
    '''
def getReportJobId():
    '''public long getReportJobId(final String threadName)
    public long getReportJobId()
    '''
def removeActiveThread():
    '''public void removeActiveThread(final String threadName)
    public void removeActiveThread(final String threadName, final boolean removeIf12MinIdle)
    '''
def removeReportJob():
    '''public void removeReportJob(final UserInfo userInfo, final long reportJobId)
    '''
def setActiveThreadsFromScriptContext():
    '''public void setActiveThreadsFromScriptContext(final String jobCancelThreadName, final HashSet<String> listOfActiveThreadsParam)
    '''
def cancelReportJob():
    '''public void cancelReportJob(final long reportJobId)
    '''
def cancelReportJobOnThisServer():
    '''public boolean cancelReportJobOnThisServer(final long reportJobId)
    '''
def isReportJobCancelled():
    '''public boolean isReportJobCancelled(final long reportJobId)
    '''
def renewActiveThread():
    '''public void renewActiveThread(final String threadName)
    '''
def updateActiveThread():
    '''public void updateActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob, final long scheduleJobId)
    '''
def isOverloaded():
    '''public boolean isOverloaded()
    '''
def getMaxAllowedActiveReportThreads():
    '''public int getMaxAllowedActiveReportThreads()
    '''
def getNumberOfActiveReports():
    '''public int getNumberOfActiveReports()
    '''
def setStartTime():
    '''public void setStartTime(final long sTime)
    '''
def getStartTime():
    '''public long getStartTime()
    '''
def setRenewTime():
    '''public void setRenewTime(final long rTime)
    '''
def getRenewTime():
    '''public long getRenewTime()
    '''
def getAppName():
    '''public String getAppName()
    '''
def setAppName():
    '''public void setAppName(final String appName)
    '''
def getReportName():
    '''public String getReportName()
    '''
def setReportName():
    '''public void setReportName(final String reportName)
    '''
def getUserName():
    '''public String getUserName()
    '''
def setUserName():
    '''public void setUserName(final String userName)
    '''
def isScheduledJob():
    '''public boolean isScheduledJob()
    '''
def setScheduledJob():
    '''public void setScheduledJob(final boolean scheduledJob)
    '''
def getScheduledJobId():
    '''public long getScheduledJobId()
    '''
def setScheduledJobId():
    '''public void setScheduledJobId(final long scheduleJobId)
    '''
def setReportJobId():
    '''public void setReportJobId(final long reportJobId)
    '''
def getJobStatus():
    '''public int getJobStatus()
    '''
def setJobStatus():
    '''public void setJobStatus(final int jobStatus)
    '''
def clone():
    '''public Object clone()
    '''
def setCancelTime():
    '''public void setCancelTime()
    '''
def getCancelTime():
    '''public long getCancelTime()
    '''
def ReportStuckThreadLoggerThread():
    '''public ReportStuckThreadLoggerThread()
    '''
def run():
    '''public void run()
    public void run()
    '''
def ReportCancelStatusUpdateThread():
    '''public ReportCancelStatusUpdateThread()
    '''
