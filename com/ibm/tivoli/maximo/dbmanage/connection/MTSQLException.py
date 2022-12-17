def ():
    '''returns MTSQLException\n\n
    ()\n
    '''
def addException():
    '''returns None\n\n
    addException(final MTContext context, final SQLException se)\n
    '''
def getErrorCode():
    '''returns int\n\n
    getErrorCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def getDefaultMessage():
    '''returns String\n\n
    getDefaultMessage()\n
    '''
def getErrorGroup():
    '''returns String\n\n
    getErrorGroup()\n
    '''
def getErrorKey():
    '''returns String\n\n
    getErrorKey()\n
    '''
def getParameters():
    '''returns Object[]\n\n
    getParameters()\n
    '''
def getCause():
    '''returns Throwable\n\n
    getCause()\n
    '''
def replaceInChain():
    '''returns int\n\n
    replaceInChain(final DoubleKey<MTContext, SQLException> target, final DoubleKey<MTContext, SQLException> replacement)\n
    '''
def removeFromChain():
    '''returns None\n\n
    removeFromChain(final int pos)\n
    '''
