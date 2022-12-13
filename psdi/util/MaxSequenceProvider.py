MAXVALUE = "long  Long.MAX_VALUE"
def MaxSequenceProvider():
'''public MaxSequenceProvider()
public MaxSequenceProvider(final MXLogger methodLogger, final MXLogger sqlLogger)
'''
pass
def resetProviders():
'''public static void resetProviders()
'''
pass
def init():
'''public void init(final Connection con)
public void init(final Connection conn, final boolean loadAll)
'''
pass
def exists():
'''public boolean exists(final Connection con, final String query)
'''
pass
def getUniqueID():
'''public synchronized Long getUniqueID(final Connection con, final String seqName)
public synchronized long getUniqueID(final Connection conn, final String tbname, final String name)
'''
pass
def resetSequence():
'''public void resetSequence(final Connection connection, final String sequence)
'''
pass
def reserveMultiple():
'''public Long reserveMultiple(final Connection con, final String seqName, final int numToReserve)
'''
pass
def isDebugEnabled():
'''public boolean isDebugEnabled()
'''
pass
def isErrorEnabled():
'''public boolean isErrorEnabled()
'''
pass
def isFatalEnabled():
'''public boolean isFatalEnabled()
'''
pass
def isInfoEnabled():
'''public boolean isInfoEnabled()
'''
pass
def isWarnEnabled():
'''public boolean isWarnEnabled()
'''
pass
def debug():
'''public void debug(final Object message)
public void debug(final Object message, final Throwable t)
'''
pass
def info():
'''public void info(final Object message)
public void info(final Object message, final Throwable t)
'''
pass
def warn():
'''public void warn(final Object message)
public void warn(final Object message, final Throwable t)
'''
pass
def error():
'''public void error(final Object message)
public void error(final Object message, final Throwable t)
'''
pass
def fatal():
'''public void fatal(final Object message)
public void fatal(final Object message, final Throwable t)
'''
pass
def setLevel():
'''public void setLevel(final Level level)
'''
pass
def getLevel():
'''public Level getLevel()
'''
pass
def logDisregardLevel():
'''public void logDisregardLevel(final String msgGroup, final String msgKey, final Object[] params)
'''
pass
def MaxSeq():
'''public MaxSeq(final String seqname, final Connection con)
'''
pass
def nextNumber():
'''public long nextNumber(final Connection con)
'''
pass
def nextNumberSet():
'''public long nextNumberSet(final Connection con, final int numToReserve)
'''
pass
