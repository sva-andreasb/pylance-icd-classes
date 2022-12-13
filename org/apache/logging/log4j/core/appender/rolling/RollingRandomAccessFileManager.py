DEFAULT_BUFFER_SIZE = "int  262144"
def RollingRandomAccessFileManager():
    '''    public RollingRandomAccessFileManager(final LoggerContext loggerContext, final RandomAccessFile raf, final String fileName, final String pattern, final OutputStream os, final boolean append, final boolean immediateFlush, final int bufferSize, final long size, final long time, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final boolean writeHeader)
    public RollingRandomAccessFileManager(final LoggerContext loggerContext, final RandomAccessFile raf, final String fileName, final String pattern, final OutputStream os, final boolean append, final boolean immediateFlush, final int bufferSize, final long size, final long initialTime, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final boolean writeHeader)
    '''
def getRollingRandomAccessFileManager():
    '''    public static RollingRandomAccessFileManager getRollingRandomAccessFileManager(final String fileName, final String filePattern, final boolean isAppend, final boolean immediateFlush, final int bufferSize, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final Configuration configuration)
    '''
def isEndOfBatch():
    '''    public Boolean isEndOfBatch()
    '''
def setEndOfBatch():
    '''    public void setEndOfBatch(final boolean endOfBatch)
    '''
def flush():
    '''    public synchronized void flush()
    '''
def closeOutputStream():
    '''    public synchronized boolean closeOutputStream()
    '''
def getBufferSize():
    '''    public int getBufferSize()
    '''
def updateData():
    '''    public void updateData(final Object data)
    '''
def createManager():
    '''    public RollingRandomAccessFileManager createManager(final String name, final FactoryData data)
    '''
def FactoryData():
    '''    public FactoryData(final String fileName, final String pattern, final boolean append, final boolean immediateFlush, final int bufferSize, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final Configuration configuration)
    '''
def getPattern():
    '''    public String getPattern()
    '''
def getTriggeringPolicy():
    '''    public TriggeringPolicy getTriggeringPolicy()
    '''
def getRolloverStrategy():
    '''    public RolloverStrategy getRolloverStrategy()
    '''
