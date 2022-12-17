def ():
    '''returns Wrapper\n\n
    (final String source, final int code, final String message, final Object[] data)\n
    (final int severity, final String source, final int code, final String message, final Object[] data)\n
    (final String source, final int code, final List children, final String message, final Object[] data)\n
    (final Diagnostic diagnostic)\n
    '''
def getSeverity():
    '''returns int\n\n
    getSeverity()\n
    getSeverity()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    getMessage()\n
    '''
def getData():
    '''returns List\n\n
    getData()\n
    '''
def getChildren():
    '''returns IStatus[]\n\n
    getChildren()\n
    getChildren()\n
    '''
def getSource():
    '''returns String\n\n
    getSource()\n
    '''
def getCode():
    '''returns int\n\n
    getCode()\n
    getCode()\n
    '''
def add():
    '''returns None\n\n
    add(final Diagnostic diagnostic)\n
    '''
def addAll():
    '''returns None\n\n
    addAll(final Diagnostic diagnostic)\n
    '''
def merge():
    '''returns None\n\n
    merge(final Diagnostic diagnostic)\n
    '''
def recomputeSeverity():
    '''returns int\n\n
    recomputeSeverity()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getException():
    '''returns Throwable\n\n
    getException()\n
    '''
def getPlugin():
    '''returns String\n\n
    getPlugin()\n
    '''
def isMultiStatus():
    '''returns boolean\n\n
    isMultiStatus()\n
    '''
def isOK():
    '''returns boolean\n\n
    isOK()\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final int severityMask)\n
    '''
