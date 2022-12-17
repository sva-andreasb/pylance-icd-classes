DEFAULT_BUFFER_SIZE = "int  262144"
def ():
    '''returns FactoryData\n\n
    (final LoggerContext loggerContext, final RandomAccessFile raf, final String fileName, final String pattern, final OutputStream os, final boolean append, final boolean immediateFlush, final int bufferSize, final long size, final long time, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final boolean writeHeader)\n
    (final LoggerContext loggerContext, final RandomAccessFile raf, final String fileName, final String pattern, final OutputStream os, final boolean append, final boolean immediateFlush, final int bufferSize, final long size, final long initialTime, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final boolean writeHeader)\n
    (final String fileName, final String pattern, final boolean append, final boolean immediateFlush, final int bufferSize, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final Configuration configuration)\n
    '''
def isEndOfBatch():
    '''returns Boolean\n\n
    isEndOfBatch()\n
    '''
def setEndOfBatch():
    '''returns None\n\n
    setEndOfBatch(final boolean endOfBatch)\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def updateData():
    '''returns None\n\n
    updateData(final Object data)\n
    '''
def createManager():
    '''returns RollingRandomAccessFileManager\n\n
    createManager(final String name, final FactoryData data)\n
    '''
def getPattern():
    '''returns String\n\n
    getPattern()\n
    '''
def getTriggeringPolicy():
    '''returns TriggeringPolicy\n\n
    getTriggeringPolicy()\n
    '''
def getRolloverStrategy():
    '''returns RolloverStrategy\n\n
    getRolloverStrategy()\n
    '''
