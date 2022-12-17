MAXVALUE = "long  Long.MAX_VALUE"
def ():
    '''returns MaxSeq\n\n
    ()\n
    (final MXLogger methodLogger, final MXLogger sqlLogger)\n
    (final String seqname, final Connection con)\n
    '''
def init():
    '''returns None\n\n
    init(final Connection con)\n
    init(final Connection conn, final boolean loadAll)\n
    '''
def exists():
    '''returns boolean\n\n
    exists(final Connection con, final String query)\n
    '''
def resetSequence():
    '''returns None\n\n
    resetSequence(final Connection connection, final String sequence)\n
    '''
def reserveMultiple():
    '''returns Long\n\n
    reserveMultiple(final Connection con, final String seqName, final int numToReserve)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def isErrorEnabled():
    '''returns boolean\n\n
    isErrorEnabled()\n
    '''
def isFatalEnabled():
    '''returns boolean\n\n
    isFatalEnabled()\n
    '''
def isInfoEnabled():
    '''returns boolean\n\n
    isInfoEnabled()\n
    '''
def isWarnEnabled():
    '''returns boolean\n\n
    isWarnEnabled()\n
    '''
def debug():
    '''returns None\n\n
    debug(final Object message)\n
    debug(final Object message, final Throwable t)\n
    '''
def info():
    '''returns None\n\n
    info(final Object message)\n
    info(final Object message, final Throwable t)\n
    '''
def warn():
    '''returns None\n\n
    warn(final Object message)\n
    warn(final Object message, final Throwable t)\n
    '''
def error():
    '''returns None\n\n
    error(final Object message)\n
    error(final Object message, final Throwable t)\n
    '''
def fatal():
    '''returns None\n\n
    fatal(final Object message)\n
    fatal(final Object message, final Throwable t)\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final Level level)\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def logDisregardLevel():
    '''returns None\n\n
    logDisregardLevel(final String msgGroup, final String msgKey, final Object[] params)\n
    '''
def nextNumber():
    '''returns long\n\n
    nextNumber(final Connection con)\n
    '''
def nextNumberSet():
    '''returns long\n\n
    nextNumberSet(final Connection con, final int numToReserve)\n
    '''
