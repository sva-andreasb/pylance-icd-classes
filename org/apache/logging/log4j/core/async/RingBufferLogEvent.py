def RingBufferLogEvent():
    '''    public RingBufferLogEvent()
    '''
def setValues():
    '''    public void setValues(final AsyncLogger anAsyncLogger, final String aLoggerName, final Marker aMarker, final String theFqcn, final Level aLevel, final Message msg, final Throwable aThrowable, final StringMap mutableContextData, final ThreadContext.ContextStack aContextStack, final long threadId, final String threadName, final int threadPriority, final StackTraceElement aLocation, final Clock clock, final NanoClock nanoClock)
    '''
def toImmutable():
    '''    public LogEvent toImmutable()
    '''
def execute():
    '''    public void execute(final boolean endOfBatch)
    '''
def isPopulated():
    '''    public boolean isPopulated()
    '''
def isEndOfBatch():
    '''    public boolean isEndOfBatch()
    '''
def setEndOfBatch():
    '''    public void setEndOfBatch(final boolean endOfBatch)
    '''
def isIncludeLocation():
    '''    public boolean isIncludeLocation()
    '''
def setIncludeLocation():
    '''    public void setIncludeLocation(final boolean includeLocation)
    '''
def getLoggerName():
    '''    public String getLoggerName()
    '''
def getMarker():
    '''    public Marker getMarker()
    '''
def getLoggerFqcn():
    '''    public String getLoggerFqcn()
    '''
def getLevel():
    '''    public Level getLevel()
    '''
def getMessage():
    '''    public Message getMessage()
    '''
def getFormattedMessage():
    '''    public String getFormattedMessage()
    '''
def getFormat():
    '''    public String getFormat()
    '''
def getParameters():
    '''    public Object[] getParameters()
    '''
def getThrowable():
    '''    public Throwable getThrowable()
    '''
def formatTo():
    '''    public void formatTo(final StringBuilder buffer)
    '''
def swapParameters():
    '''    public Object[] swapParameters(final Object[] emptyReplacement)
    '''
def getParameterCount():
    '''    public short getParameterCount()
    '''
def forEachParameter():
    '''    public <S> void forEachParameter(final ParameterConsumer<S> action, final S state)
    '''
def memento():
    '''    public Message memento()
    '''
def length():
    '''    public int length()
    '''
def charAt():
    '''    public char charAt(final int index)
    '''
def subSequence():
    '''    public CharSequence subSequence(final int start, final int end)
    '''
def getThrown():
    '''    public Throwable getThrown()
    '''
def getThrownProxy():
    '''    public ThrowableProxy getThrownProxy()
    '''
def getContextData():
    '''    public ReadOnlyStringMap getContextData()
    '''
def getContextMap():
    '''    public Map<String, String> getContextMap()
    '''
def getThreadId():
    '''    public long getThreadId()
    '''
def getThreadName():
    '''    public String getThreadName()
    '''
def getThreadPriority():
    '''    public int getThreadPriority()
    '''
def getSource():
    '''    public StackTraceElement getSource()
    '''
def getTimeMillis():
    '''    public long getTimeMillis()
    '''
def getInstant():
    '''    public Instant getInstant()
    '''
def getNanoTime():
    '''    public long getNanoTime()
    '''
def clear():
    '''    public void clear()
    '''
def createMemento():
    '''    public LogEvent createMemento()
    '''
def initializeBuilder():
    '''    public void initializeBuilder(final Log4jLogEvent.Builder builder)
    '''
def newInstance():
    '''    public RingBufferLogEvent newInstance()
    '''
