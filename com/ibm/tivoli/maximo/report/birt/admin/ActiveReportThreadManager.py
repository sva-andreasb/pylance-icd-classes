DEFAULT_MAX_CONCURRENT_THREADCOUNT = "int  3"
PROPERTY_MAXCONCURRENTRUN = "String  mxe.report.birt.maxconcurrentrun""
def getActiveReportThreadManager():
'''public static ActiveReportThreadManager getActiveReportThreadManager()
'''
pass
def addActiveThread():
'''public synchronized Long addActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob)
'''
pass
def createReportJob():
'''public long createReportJob(final UserInfo userInfo, final String reportName, final String appName, final String userName, final boolean scheduledJob, final long startTime)
'''
pass
def getReportJobId():
'''public long getReportJobId(final String threadName)
public long getReportJobId()
'''
pass
def removeActiveThread():
'''public void removeActiveThread(final String threadName)
public void removeActiveThread(final String threadName, final boolean removeIf12MinIdle)
'''
pass
def removeReportJob():
'''public void removeReportJob(final UserInfo userInfo, final long reportJobId)
'''
pass
def setActiveThreadsFromScriptContext():
'''public void setActiveThreadsFromScriptContext(final String jobCancelThreadName, final HashSet<String> listOfActiveThreadsParam)
'''
pass
def cancelReportJob():
'''public void cancelReportJob(final long reportJobId)
'''
pass
def cancelReportJobOnThisServer():
'''public boolean cancelReportJobOnThisServer(final long reportJobId)
'''
pass
def isReportJobCancelled():
'''public boolean isReportJobCancelled(final long reportJobId)
'''
pass
def renewActiveThread():
'''public void renewActiveThread(final String threadName)
'''
pass
def updateActiveThread():
'''public void updateActiveThread(final String threadName, final String reportName, final String appName, final String userName, final boolean scheduledJob, final long scheduleJobId)
'''
pass
def isOverloaded():
'''public boolean isOverloaded()
'''
pass
def getMaxAllowedActiveReportThreads():
'''public int getMaxAllowedActiveReportThreads()
'''
pass
def getNumberOfActiveReports():
'''public int getNumberOfActiveReports()
'''
pass
def setStartTime():
'''public void setStartTime(final long sTime)
'''
pass
def getStartTime():
'''public long getStartTime()
'''
pass
def setRenewTime():
'''public void setRenewTime(final long rTime)
'''
pass
def getRenewTime():
'''public long getRenewTime()
'''
pass
def getAppName():
'''public String getAppName()
'''
pass
def setAppName():
'''public void setAppName(final String appName)
'''
pass
def getReportName():
'''public String getReportName()
'''
pass
def setReportName():
'''public void setReportName(final String reportName)
'''
pass
def getUserName():
'''public String getUserName()
'''
pass
def setUserName():
'''public void setUserName(final String userName)
'''
pass
def isScheduledJob():
'''public boolean isScheduledJob()
'''
pass
def setScheduledJob():
'''public void setScheduledJob(final boolean scheduledJob)
'''
pass
def getScheduledJobId():
'''public long getScheduledJobId()
'''
pass
def setScheduledJobId():
'''public void setScheduledJobId(final long scheduleJobId)
'''
pass
def setReportJobId():
'''public void setReportJobId(final long reportJobId)
'''
pass
def getJobStatus():
'''public int getJobStatus()
'''
pass
def setJobStatus():
'''public void setJobStatus(final int jobStatus)
'''
pass
def clone():
'''public Object clone()
'''
pass
def setCancelTime():
'''public void setCancelTime()
'''
pass
def getCancelTime():
'''public long getCancelTime()
'''
pass
def ReportStuckThreadLoggerThread():
'''public ReportStuckThreadLoggerThread()
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def ReportCancelStatusUpdateThread():
'''public ReportCancelStatusUpdateThread()
'''
pass
