DEFAULT_QUEUE_IDLETIME_SECONDS = "int  60"
PROPERTY_QUEUEIDLETIMESECONDS = "String  \"mxe.report.birt.queueidletimeseconds\""
PROPERTY_DISABLEQUEUEMANAGER = "String  \"mxe.report.birt.disablequeuemanager\""
DEFAULT_MAX_CONCURRENT_THREADCOUNT = "int  3"
PROPERTY_MAXCONCURRENTRUN = "String  \"mxe.report.birt.maxconcurrentrun\""
def ReportQueueManager():
    '''public ReportQueueManager()
    '''
def run():
    '''public void run()
    public void run()
    '''
def acquireLock():
    '''public boolean acquireLock(final long runQueueId)
    '''
def removeRunReport():
    '''public void removeRunReport(final long runQueueId)
    '''
def getMaxAllowedActiveReportThreads():
    '''public int getMaxAllowedActiveReportThreads()
    '''
def getQueueIdleTime():
    '''public int getQueueIdleTime()
    '''
def createFileFromStream():
    '''public void createFileFromStream(final File file, final InputStream inputStream)
    '''
def ReportRunThread():
    '''public ReportRunThread()
    '''
def startDoingWork():
    '''public void startDoingWork()
    '''
def markShutdown():
    '''public void markShutdown()
    '''
def isWaitingForWork():
    '''public boolean isWaitingForWork()
    '''
