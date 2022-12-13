def ContextedException():
    '''public ContextedException()
    public ContextedException(final String message)
    public ContextedException(final Throwable cause)
    public ContextedException(final String message, final Throwable cause)
    public ContextedException(final String message, final Throwable cause, ExceptionContext context)
    '''
def addContextValue():
    '''public ContextedException addContextValue(final String label, final Object value)
    '''
def setContextValue():
    '''public ContextedException setContextValue(final String label, final Object value)
    '''
def getContextValues():
    '''public List<Object> getContextValues(final String label)
    '''
def getFirstContextValue():
    '''public Object getFirstContextValue(final String label)
    '''
def getContextEntries():
    '''public List<Pair<String, Object>> getContextEntries()
    '''
def getContextLabels():
    '''public Set<String> getContextLabels()
    '''
def getMessage():
    '''public String getMessage()
    '''
def getRawMessage():
    '''public String getRawMessage()
    '''
def getFormattedExceptionMessage():
    '''public String getFormattedExceptionMessage(final String baseMessage)
    '''
