def start():
    '''    public void start()
    '''
def stop():
    '''    public boolean stop(final long timeout, final TimeUnit timeUnit)
    '''
def append():
    '''    public void append(final LogEvent logEvent)
    '''
def logMessageInCurrentThread():
    '''    public void logMessageInCurrentThread(final LogEvent logEvent)
    '''
def logMessageInBackgroundThread():
    '''    public void logMessageInBackgroundThread(final LogEvent logEvent)
    '''
def createAppender():
    '''    public static AsyncAppender createAppender(final AppenderRef[] appenderRefs, final String errorRef, final boolean blocking, final long shutdownTimeout, final int size, final String name, final boolean includeLocation, final Filter filter, final Configuration config, final boolean ignoreExceptions)
    '''
def newBuilder():
    '''    public static Builder newBuilder()
    '''
def getAppenderRefStrings():
    '''    public String[] getAppenderRefStrings()
    '''
def isIncludeLocation():
    '''    public boolean isIncludeLocation()
    '''
def isBlocking():
    '''    public boolean isBlocking()
    '''
def getErrorRef():
    '''    public String getErrorRef()
    '''
def getQueueCapacity():
    '''    public int getQueueCapacity()
    '''
def getQueueRemainingCapacity():
    '''    public int getQueueRemainingCapacity()
    '''
def getQueueSize():
    '''    public int getQueueSize()
    '''
def Builder():
    '''    public Builder()
    '''
def setAppenderRefs():
    '''    public Builder setAppenderRefs(final AppenderRef[] appenderRefs)
    '''
def setErrorRef():
    '''    public Builder setErrorRef(final String errorRef)
    '''
def setBlocking():
    '''    public Builder setBlocking(final boolean blocking)
    '''
def setShutdownTimeout():
    '''    public Builder setShutdownTimeout(final long shutdownTimeout)
    '''
def setBufferSize():
    '''    public Builder setBufferSize(final int bufferSize)
    '''
def setName():
    '''    public Builder setName(final String name)
    '''
def setIncludeLocation():
    '''    public Builder setIncludeLocation(final boolean includeLocation)
    '''
def setConfiguration():
    '''    public Builder setConfiguration(final Configuration configuration)
    '''
def setIgnoreExceptions():
    '''    public Builder setIgnoreExceptions(final boolean ignoreExceptions)
    '''
def setBlockingQueueFactory():
    '''    public Builder setBlockingQueueFactory(final BlockingQueueFactory<LogEvent> blockingQueueFactory)
    '''
def build():
    '''    public AsyncAppender build()
    '''
