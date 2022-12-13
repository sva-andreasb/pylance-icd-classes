MAXVALUE = "long  Long.MAX_VALUE"
def MaxSequenceProvider():
    '''public MaxSequenceProvider()
    public MaxSequenceProvider(final MXLogger methodLogger, final MXLogger sqlLogger)
    '''
def resetProviders():
    '''public static void resetProviders()
    '''
def init():
    '''public void init(final Connection con)
    public void init(final Connection conn, final boolean loadAll)
    '''
def exists():
    '''public boolean exists(final Connection con, final String query)
    '''
def getUniqueID():
    '''public synchronized Long getUniqueID(final Connection con, final String seqName)
    public synchronized long getUniqueID(final Connection conn, final String tbname, final String name)
    '''
def resetSequence():
    '''public void resetSequence(final Connection connection, final String sequence)
    '''
def reserveMultiple():
    '''public Long reserveMultiple(final Connection con, final String seqName, final int numToReserve)
    '''
def isDebugEnabled():
    '''public boolean isDebugEnabled()
    '''
def isErrorEnabled():
    '''public boolean isErrorEnabled()
    '''
def isFatalEnabled():
    '''public boolean isFatalEnabled()
    '''
def isInfoEnabled():
    '''public boolean isInfoEnabled()
    '''
def isWarnEnabled():
    '''public boolean isWarnEnabled()
    '''
def debug():
    '''public void debug(final Object message)
    public void debug(final Object message, final Throwable t)
    '''
def info():
    '''public void info(final Object message)
    public void info(final Object message, final Throwable t)
    '''
def warn():
    '''public void warn(final Object message)
    public void warn(final Object message, final Throwable t)
    '''
def error():
    '''public void error(final Object message)
    public void error(final Object message, final Throwable t)
    '''
def fatal():
    '''public void fatal(final Object message)
    public void fatal(final Object message, final Throwable t)
    '''
def setLevel():
    '''public void setLevel(final Level level)
    '''
def getLevel():
    '''public Level getLevel()
    '''
def logDisregardLevel():
    '''public void logDisregardLevel(final String msgGroup, final String msgKey, final Object[] params)
    '''
def MaxSeq():
    '''public MaxSeq(final String seqname, final Connection con)
    '''
def nextNumber():
    '''public long nextNumber(final Connection con)
    '''
def nextNumberSet():
    '''public long nextNumberSet(final Connection con, final int numToReserve)
    '''
