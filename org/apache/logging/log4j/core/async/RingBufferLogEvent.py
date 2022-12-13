def RingBufferLogEvent():
'''public RingBufferLogEvent()
'''
pass
def setValues():
'''public void setValues(final AsyncLogger anAsyncLogger, final String aLoggerName, final Marker aMarker, final String theFqcn, final Level aLevel, final Message msg, final Throwable aThrowable, final StringMap mutableContextData, final ThreadContext.ContextStack aContextStack, final long threadId, final String threadName, final int threadPriority, final StackTraceElement aLocation, final Clock clock, final NanoClock nanoClock)
'''
pass
def toImmutable():
'''public LogEvent toImmutable()
'''
pass
def execute():
'''public void execute(final boolean endOfBatch)
'''
pass
def isPopulated():
'''public boolean isPopulated()
'''
pass
def isEndOfBatch():
'''public boolean isEndOfBatch()
'''
pass
def setEndOfBatch():
'''public void setEndOfBatch(final boolean endOfBatch)
'''
pass
def isIncludeLocation():
'''public boolean isIncludeLocation()
'''
pass
def setIncludeLocation():
'''public void setIncludeLocation(final boolean includeLocation)
'''
pass
def getLoggerName():
'''public String getLoggerName()
'''
pass
def getMarker():
'''public Marker getMarker()
'''
pass
def getLoggerFqcn():
'''public String getLoggerFqcn()
'''
pass
def getLevel():
'''public Level getLevel()
'''
pass
def getMessage():
'''public Message getMessage()
'''
pass
def getFormattedMessage():
'''public String getFormattedMessage()
'''
pass
def getFormat():
'''public String getFormat()
'''
pass
def getParameters():
'''public Object[] getParameters()
'''
pass
def getThrowable():
'''public Throwable getThrowable()
'''
pass
def formatTo():
'''public void formatTo(final StringBuilder buffer)
'''
pass
def swapParameters():
'''public Object[] swapParameters(final Object[] emptyReplacement)
'''
pass
def getParameterCount():
'''public short getParameterCount()
'''
pass
def forEachParameter():
'''public <S> void forEachParameter(final ParameterConsumer<S> action, final S state)
'''
pass
def memento():
'''public Message memento()
'''
pass
def length():
'''public int length()
'''
pass
def charAt():
'''public char charAt(final int index)
'''
pass
def subSequence():
'''public CharSequence subSequence(final int start, final int end)
'''
pass
def getThrown():
'''public Throwable getThrown()
'''
pass
def getThrownProxy():
'''public ThrowableProxy getThrownProxy()
'''
pass
def getContextData():
'''public ReadOnlyStringMap getContextData()
'''
pass
def getContextMap():
'''public Map<String, String> getContextMap()
'''
pass
def getThreadId():
'''public long getThreadId()
'''
pass
def getThreadName():
'''public String getThreadName()
'''
pass
def getThreadPriority():
'''public int getThreadPriority()
'''
pass
def getSource():
'''public StackTraceElement getSource()
'''
pass
def getTimeMillis():
'''public long getTimeMillis()
'''
pass
def getInstant():
'''public Instant getInstant()
'''
pass
def getNanoTime():
'''public long getNanoTime()
'''
pass
def clear():
'''public void clear()
'''
pass
def createMemento():
'''public LogEvent createMemento()
'''
pass
def initializeBuilder():
'''public void initializeBuilder(final Log4jLogEvent.Builder builder)
'''
pass
def newInstance():
'''public RingBufferLogEvent newInstance()
'''
pass
