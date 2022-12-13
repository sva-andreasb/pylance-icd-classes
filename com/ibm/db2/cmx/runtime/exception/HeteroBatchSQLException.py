def HeteroBatchSQLException():
    '''public HeteroBatchSQLException()
    public HeteroBatchSQLException(final SQLException exceptionContainer_, final int originalOffsetInChain_)
    '''
def getNextException():
    '''public SQLException getNextException()
    '''
def getNextHeteroBatchSQLException():
    '''public HeteroBatchSQLException getNextHeteroBatchSQLException()
    '''
def getOriginalOffsetInChain():
    '''public int getOriginalOffsetInChain()
    '''
def getUnderlyingSQLException():
    '''public SQLException getUnderlyingSQLException()
    '''
def isRowSpecificSQLException():
    '''public boolean isRowSpecificSQLException()
    '''
def implementsDB2Diagnosable():
    '''public boolean implementsDB2Diagnosable()
    '''
def setNextException():
    '''public synchronized void setNextException(final SQLException ex)
    '''
def setNextHeteroBatchSQLException():
    '''public synchronized void setNextHeteroBatchSQLException(final HeteroBatchSQLException ex)
    '''
def getBindDiagnostics():
    '''public DBBindDiagnostics getBindDiagnostics()
    '''
def getSqlca():
    '''public DB2Sqlca getSqlca()
    '''
def getThrowable():
    '''public Throwable getThrowable()
    '''
def printTrace():
    '''public void printTrace(final PrintWriter printWriter, final String s)
    '''
def getBatchElementOffset():
    '''public int getBatchElementOffset()
    '''
def getStmtOffset():
    '''public int getStmtOffset()
    '''
def getErrorCode():
    '''public int getErrorCode()
    '''
def getSQLState():
    '''public String getSQLState()
    '''
def fillInStackTrace():
    '''public Throwable fillInStackTrace()
    '''
def getCause():
    '''public Throwable getCause()
    '''
def getLocalizedMessage():
    '''public String getLocalizedMessage()
    '''
def getMessage():
    '''public String getMessage()
    '''
def getStackTrace():
    '''public StackTraceElement[] getStackTrace()
    '''
def initCause():
    '''public synchronized Throwable initCause(final Throwable t)
    '''
def printStackTrace():
    '''public void printStackTrace()
    public void printStackTrace(final PrintStream printStream)
    public void printStackTrace(final PrintWriter printWriter)
    '''
def setStackTrace():
    '''public void setStackTrace(final StackTraceElement[] array)
    '''
def toString():
    '''public String toString()
    '''
