def MTSQLException():
    '''public MTSQLException()
    '''
def addException():
    '''public void addException(final MTContext context, final SQLException se)
    '''
def getErrorCode():
    '''public int getErrorCode()
    '''
def getExceptionsWithContext():
    '''public List<DoubleKey<MTContext, SQLException>> getExceptionsWithContext()
    '''
def toString():
    '''public String toString()
    '''
def getMessage():
    '''public String getMessage()
    '''
def getDefaultMessage():
    '''public String getDefaultMessage()
    '''
def getErrorGroup():
    '''public String getErrorGroup()
    '''
def getErrorKey():
    '''public String getErrorKey()
    '''
def getParameters():
    '''public Object[] getParameters()
    '''
def getCause():
    '''public Throwable getCause()
    '''
def replaceInChain():
    '''public int replaceInChain(final DoubleKey<MTContext, SQLException> target, final DoubleKey<MTContext, SQLException> replacement)
    '''
def removeFromChain():
    '''public void removeFromChain(final int pos)
    '''
