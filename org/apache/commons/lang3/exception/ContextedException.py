def ():
    '''returns ContextedException\n\n
    ()\n
    (final String message)\n
    (final Throwable cause)\n
    (final String message, final Throwable cause)\n
    (final String message, final Throwable cause, ExceptionContext context)\n
    '''
def addContextValue():
    '''returns ContextedException\n\n
    addContextValue(final String label, final Object value)\n
    '''
def setContextValue():
    '''returns ContextedException\n\n
    setContextValue(final String label, final Object value)\n
    '''
def getContextValues():
    '''returns List<Object>\n\n
    getContextValues(final String label)\n
    '''
def getFirstContextValue():
    '''returns Object\n\n
    getFirstContextValue(final String label)\n
    '''
def getContextLabels():
    '''returns Set<String>\n\n
    getContextLabels()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def getRawMessage():
    '''returns String\n\n
    getRawMessage()\n
    '''
def getFormattedExceptionMessage():
    '''returns String\n\n
    getFormattedExceptionMessage(final String baseMessage)\n
    '''
