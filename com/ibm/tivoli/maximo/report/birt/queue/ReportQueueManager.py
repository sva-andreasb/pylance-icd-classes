DEFAULT_QUEUE_IDLETIME_SECONDS = "int  60"
PROPERTY_QUEUEIDLETIMESECONDS = "String  \"mxe.report.birt.queueidletimeseconds\""
PROPERTY_DISABLEQUEUEMANAGER = "String  \"mxe.report.birt.disablequeuemanager\""
DEFAULT_MAX_CONCURRENT_THREADCOUNT = "int  3"
PROPERTY_MAXCONCURRENTRUN = "String  \"mxe.report.birt.maxconcurrentrun\""
def ():
    '''returns ReportRunThread\n\n
    ()\n
    ()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def acquireLock():
    '''returns boolean\n\n
    acquireLock(final long runQueueId)\n
    '''
def removeRunReport():
    '''returns None\n\n
    removeRunReport(final long runQueueId)\n
    '''
def getMaxAllowedActiveReportThreads():
    '''returns int\n\n
    getMaxAllowedActiveReportThreads()\n
    '''
def getQueueIdleTime():
    '''returns int\n\n
    getQueueIdleTime()\n
    '''
def createFileFromStream():
    '''returns None\n\n
    createFileFromStream(final File file, final InputStream inputStream)\n
    '''
def startDoingWork():
    '''returns None\n\n
    startDoingWork()\n
    '''
def markShutdown():
    '''returns None\n\n
    markShutdown()\n
    '''
def isWaitingForWork():
    '''returns boolean\n\n
    isWaitingForWork()\n
    '''
