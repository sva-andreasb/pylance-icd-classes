DEFAULT_QUEUE_IDLETIME_SECONDS = "int  60"
PROPERTY_QUEUEIDLETIMESECONDS = "String  mxe.report.birt.queueidletimeseconds""
PROPERTY_DISABLEQUEUEMANAGER = "String  mxe.report.birt.disablequeuemanager""
DEFAULT_MAX_CONCURRENT_THREADCOUNT = "int  3"
PROPERTY_MAXCONCURRENTRUN = "String  mxe.report.birt.maxconcurrentrun""
def ReportQueueManager():
'''public ReportQueueManager()
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def acquireLock():
'''public boolean acquireLock(final long runQueueId)
'''
pass
def removeRunReport():
'''public void removeRunReport(final long runQueueId)
'''
pass
def getMaxAllowedActiveReportThreads():
'''public int getMaxAllowedActiveReportThreads()
'''
pass
def getQueueIdleTime():
'''public int getQueueIdleTime()
'''
pass
def createFileFromStream():
'''public void createFileFromStream(final File file, final InputStream inputStream)
'''
pass
def ReportRunThread():
'''public ReportRunThread()
'''
pass
def startDoingWork():
'''public void startDoingWork()
'''
pass
def markShutdown():
'''public void markShutdown()
'''
pass
def isWaitingForWork():
'''public boolean isWaitingForWork()
'''
pass
