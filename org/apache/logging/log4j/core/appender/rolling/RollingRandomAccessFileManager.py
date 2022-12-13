DEFAULT_BUFFER_SIZE = "int  262144"
def RollingRandomAccessFileManager():
'''public RollingRandomAccessFileManager(final LoggerContext loggerContext, final RandomAccessFile raf, final String fileName, final String pattern, final OutputStream os, final boolean append, final boolean immediateFlush, final int bufferSize, final long size, final long time, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final boolean writeHeader)
public RollingRandomAccessFileManager(final LoggerContext loggerContext, final RandomAccessFile raf, final String fileName, final String pattern, final OutputStream os, final boolean append, final boolean immediateFlush, final int bufferSize, final long size, final long initialTime, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final boolean writeHeader)
'''
pass
def getRollingRandomAccessFileManager():
'''public static RollingRandomAccessFileManager getRollingRandomAccessFileManager(final String fileName, final String filePattern, final boolean isAppend, final boolean immediateFlush, final int bufferSize, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final Configuration configuration)
'''
pass
def isEndOfBatch():
'''public Boolean isEndOfBatch()
'''
pass
def setEndOfBatch():
'''public void setEndOfBatch(final boolean endOfBatch)
'''
pass
def flush():
'''public synchronized void flush()
'''
pass
def closeOutputStream():
'''public synchronized boolean closeOutputStream()
'''
pass
def getBufferSize():
'''public int getBufferSize()
'''
pass
def updateData():
'''public void updateData(final Object data)
'''
pass
def createManager():
'''public RollingRandomAccessFileManager createManager(final String name, final FactoryData data)
'''
pass
def FactoryData():
'''public FactoryData(final String fileName, final String pattern, final boolean append, final boolean immediateFlush, final int bufferSize, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final Configuration configuration)
'''
pass
def getPattern():
'''public String getPattern()
'''
pass
def getTriggeringPolicy():
'''public TriggeringPolicy getTriggeringPolicy()
'''
pass
def getRolloverStrategy():
'''public RolloverStrategy getRolloverStrategy()
'''
pass
