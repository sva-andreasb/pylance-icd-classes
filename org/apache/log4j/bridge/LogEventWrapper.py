def LogEventWrapper():
    '''    public LogEventWrapper(final LoggingEvent event)
    '''
def toImmutable():
    '''    public LogEvent toImmutable()
    '''
def getContextMap():
    '''    public Map<String, String> getContextMap()
    '''
def getContextData():
    '''    public ReadOnlyStringMap getContextData()
    '''
def getLoggerFqcn():
    '''    public String getLoggerFqcn()
    '''
def getLevel():
    '''    public Level getLevel()
    '''
def getLoggerName():
    '''    public String getLoggerName()
    '''
def getMarker():
    '''    public Marker getMarker()
    '''
def getMessage():
    '''    public Message getMessage()
    '''
def getTimeMillis():
    '''    public long getTimeMillis()
    '''
def getInstant():
    '''    public Instant getInstant()
    '''
def getSource():
    '''    public StackTraceElement getSource()
    '''
def getThreadName():
    '''    public String getThreadName()
    '''
def getThreadId():
    '''    public long getThreadId()
    '''
def getThreadPriority():
    '''    public int getThreadPriority()
    '''
def getThrown():
    '''    public Throwable getThrown()
    '''
def getThrownProxy():
    '''    public ThrowableProxy getThrownProxy()
    '''
def isEndOfBatch():
    '''    public boolean isEndOfBatch()
    '''
def isIncludeLocation():
    '''    public boolean isIncludeLocation()
    '''
def setEndOfBatch():
    '''    public void setEndOfBatch(final boolean endOfBatch)
    '''
def setIncludeLocation():
    '''    public void setIncludeLocation(final boolean locationRequired)
    '''
def getNanoTime():
    '''    public long getNanoTime()
    '''
def toMap():
    '''    public Map<String, String> toMap()
    '''
def containsKey():
    '''    public boolean containsKey(final String key)
    '''
def forEach():
    '''    public <V> void forEach(final BiConsumer<String, ? super V> action)
    public <V, S> void forEach(final TriConsumer<String, ? super V, S> action, final S state)
    '''
def getValue():
    '''    public <V> V getValue(final String key)
    '''
