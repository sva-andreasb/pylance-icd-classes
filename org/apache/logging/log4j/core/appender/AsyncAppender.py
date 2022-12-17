def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns boolean\n\n
    stop(final long timeout, final TimeUnit timeUnit)\n
    '''
def append():
    '''returns None\n\n
    append(final LogEvent logEvent)\n
    '''
def logMessageInCurrentThread():
    '''returns None\n\n
    logMessageInCurrentThread(final LogEvent logEvent)\n
    '''
def logMessageInBackgroundThread():
    '''returns None\n\n
    logMessageInBackgroundThread(final LogEvent logEvent)\n
    '''
def getAppenderRefStrings():
    '''returns String[]\n\n
    getAppenderRefStrings()\n
    '''
def isIncludeLocation():
    '''returns boolean\n\n
    isIncludeLocation()\n
    '''
def isBlocking():
    '''returns boolean\n\n
    isBlocking()\n
    '''
def getErrorRef():
    '''returns String\n\n
    getErrorRef()\n
    '''
def getQueueCapacity():
    '''returns int\n\n
    getQueueCapacity()\n
    '''
def getQueueRemainingCapacity():
    '''returns int\n\n
    getQueueRemainingCapacity()\n
    '''
def getQueueSize():
    '''returns int\n\n
    getQueueSize()\n
    '''
def ():
    '''returns Builder\n\n
    ()\n
    '''
def setAppenderRefs():
    '''returns Builder\n\n
    setAppenderRefs(final AppenderRef[] appenderRefs)\n
    '''
def setErrorRef():
    '''returns Builder\n\n
    setErrorRef(final String errorRef)\n
    '''
def setBlocking():
    '''returns Builder\n\n
    setBlocking(final boolean blocking)\n
    '''
def setShutdownTimeout():
    '''returns Builder\n\n
    setShutdownTimeout(final long shutdownTimeout)\n
    '''
def setBufferSize():
    '''returns Builder\n\n
    setBufferSize(final int bufferSize)\n
    '''
def setName():
    '''returns Builder\n\n
    setName(final String name)\n
    '''
def setIncludeLocation():
    '''returns Builder\n\n
    setIncludeLocation(final boolean includeLocation)\n
    '''
def setConfiguration():
    '''returns Builder\n\n
    setConfiguration(final Configuration configuration)\n
    '''
def setIgnoreExceptions():
    '''returns Builder\n\n
    setIgnoreExceptions(final boolean ignoreExceptions)\n
    '''
def setBlockingQueueFactory():
    '''returns Builder\n\n
    setBlockingQueueFactory(final BlockingQueueFactory<LogEvent> blockingQueueFactory)\n
    '''
def build():
    '''returns AsyncAppender\n\n
    build()\n
    '''
