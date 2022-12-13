def start():
'''public void start()
'''
pass
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def append():
'''public void append(final LogEvent logEvent)
'''
pass
def logMessageInCurrentThread():
'''public void logMessageInCurrentThread(final LogEvent logEvent)
'''
pass
def logMessageInBackgroundThread():
'''public void logMessageInBackgroundThread(final LogEvent logEvent)
'''
pass
def createAppender():
'''public static AsyncAppender createAppender(final AppenderRef[] appenderRefs, final String errorRef, final boolean blocking, final long shutdownTimeout, final int size, final String name, final boolean includeLocation, final Filter filter, final Configuration config, final boolean ignoreExceptions)
'''
pass
def newBuilder():
'''public static Builder newBuilder()
'''
pass
def getAppenderRefStrings():
'''public String[] getAppenderRefStrings()
'''
pass
def isIncludeLocation():
'''public boolean isIncludeLocation()
'''
pass
def isBlocking():
'''public boolean isBlocking()
'''
pass
def getErrorRef():
'''public String getErrorRef()
'''
pass
def getQueueCapacity():
'''public int getQueueCapacity()
'''
pass
def getQueueRemainingCapacity():
'''public int getQueueRemainingCapacity()
'''
pass
def getQueueSize():
'''public int getQueueSize()
'''
pass
def Builder():
'''public Builder()
'''
pass
def setAppenderRefs():
'''public Builder setAppenderRefs(final AppenderRef[] appenderRefs)
'''
pass
def setErrorRef():
'''public Builder setErrorRef(final String errorRef)
'''
pass
def setBlocking():
'''public Builder setBlocking(final boolean blocking)
'''
pass
def setShutdownTimeout():
'''public Builder setShutdownTimeout(final long shutdownTimeout)
'''
pass
def setBufferSize():
'''public Builder setBufferSize(final int bufferSize)
'''
pass
def setName():
'''public Builder setName(final String name)
'''
pass
def setIncludeLocation():
'''public Builder setIncludeLocation(final boolean includeLocation)
'''
pass
def setConfiguration():
'''public Builder setConfiguration(final Configuration configuration)
'''
pass
def setIgnoreExceptions():
'''public Builder setIgnoreExceptions(final boolean ignoreExceptions)
'''
pass
def setBlockingQueueFactory():
'''public Builder setBlockingQueueFactory(final BlockingQueueFactory<LogEvent> blockingQueueFactory)
'''
pass
def build():
'''public AsyncAppender build()
'''
pass
