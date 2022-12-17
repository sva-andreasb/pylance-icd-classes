def ():
    '''returns RingBufferLogEvent\n\n
    ()\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final AsyncLogger anAsyncLogger, final String aLoggerName, final Marker aMarker, final String theFqcn, final Level aLevel, final Message msg, final Throwable aThrowable, final StringMap mutableContextData, final ThreadContext.ContextStack aContextStack, final long threadId, final String threadName, final int threadPriority, final StackTraceElement aLocation, final Clock clock, final NanoClock nanoClock)\n
    '''
def toImmutable():
    '''returns LogEvent\n\n
    toImmutable()\n
    '''
def execute():
    '''returns None\n\n
    execute(final boolean endOfBatch)\n
    '''
def isPopulated():
    '''returns boolean\n\n
    isPopulated()\n
    '''
def isEndOfBatch():
    '''returns boolean\n\n
    isEndOfBatch()\n
    '''
def setEndOfBatch():
    '''returns None\n\n
    setEndOfBatch(final boolean endOfBatch)\n
    '''
def isIncludeLocation():
    '''returns boolean\n\n
    isIncludeLocation()\n
    '''
def setIncludeLocation():
    '''returns None\n\n
    setIncludeLocation(final boolean includeLocation)\n
    '''
def getLoggerName():
    '''returns String\n\n
    getLoggerName()\n
    '''
def getMarker():
    '''returns Marker\n\n
    getMarker()\n
    '''
def getLoggerFqcn():
    '''returns String\n\n
    getLoggerFqcn()\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def getMessage():
    '''returns Message\n\n
    getMessage()\n
    '''
def getFormattedMessage():
    '''returns String\n\n
    getFormattedMessage()\n
    '''
def getFormat():
    '''returns String\n\n
    getFormat()\n
    '''
def getParameters():
    '''returns Object[]\n\n
    getParameters()\n
    '''
def getThrowable():
    '''returns Throwable\n\n
    getThrowable()\n
    '''
def formatTo():
    '''returns None\n\n
    formatTo(final StringBuilder buffer)\n
    '''
def swapParameters():
    '''returns Object[]\n\n
    swapParameters(final Object[] emptyReplacement)\n
    '''
def getParameterCount():
    '''returns short\n\n
    getParameterCount()\n
    '''
def memento():
    '''returns Message\n\n
    memento()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def charAt():
    '''returns char\n\n
    charAt(final int index)\n
    '''
def subSequence():
    '''returns CharSequence\n\n
    subSequence(final int start, final int end)\n
    '''
def getThrown():
    '''returns Throwable\n\n
    getThrown()\n
    '''
def getThrownProxy():
    '''returns ThrowableProxy\n\n
    getThrownProxy()\n
    '''
def getContextData():
    '''returns ReadOnlyStringMap\n\n
    getContextData()\n
    '''
def getThreadId():
    '''returns long\n\n
    getThreadId()\n
    '''
def getThreadName():
    '''returns String\n\n
    getThreadName()\n
    '''
def getThreadPriority():
    '''returns int\n\n
    getThreadPriority()\n
    '''
def getSource():
    '''returns StackTraceElement\n\n
    getSource()\n
    '''
def getTimeMillis():
    '''returns long\n\n
    getTimeMillis()\n
    '''
def getInstant():
    '''returns Instant\n\n
    getInstant()\n
    '''
def getNanoTime():
    '''returns long\n\n
    getNanoTime()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def createMemento():
    '''returns LogEvent\n\n
    createMemento()\n
    '''
def initializeBuilder():
    '''returns None\n\n
    initializeBuilder(final Log4jLogEvent.Builder builder)\n
    '''
def newInstance():
    '''returns RingBufferLogEvent\n\n
    newInstance()\n
    '''
