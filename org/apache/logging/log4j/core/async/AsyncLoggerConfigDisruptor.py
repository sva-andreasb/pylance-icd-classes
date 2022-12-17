def ():
    '''returns Log4jEventWrapper\n\n
    ()\n
    ()\n
    (final MutableLogEvent mutableLogEvent)\n
    '''
def setLogEventFactory():
    '''returns None\n\n
    setLogEventFactory(final LogEventFactory logEventFactory)\n
    '''
def newThread():
    '''returns Thread\n\n
    newThread(final Runnable r)\n
    '''
def stop():
    '''returns boolean\n\n
    stop(final long timeout, final TimeUnit timeUnit)\n
    '''
def getEventRoute():
    '''returns EventRoute\n\n
    getEventRoute(final Level logLevel)\n
    '''
def enqueueEvent():
    '''returns None\n\n
    enqueueEvent(final LogEvent event, final AsyncLoggerConfig asyncLoggerConfig)\n
    '''
def tryEnqueue():
    '''returns boolean\n\n
    tryEnqueue(final LogEvent event, final AsyncLoggerConfig asyncLoggerConfig)\n
    '''
def createRingBufferAdmin():
    '''returns RingBufferAdmin\n\n
    createRingBufferAdmin(final String contextName, final String loggerConfigName)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setSequenceCallback():
    '''returns None\n\n
    setSequenceCallback(final Sequence sequenceCallback)\n
    '''
def onEvent():
    '''returns None\n\n
    onEvent(final Log4jEventWrapper event, final long sequence, final boolean endOfBatch)\n
    '''
