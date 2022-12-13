SEVERITY_WARNING = "short  0"
SEVERITY_ERROR = "short  1"
SEVERITY_FATAL_ERROR = "short  2"
def XMLErrorReporter():
    '''public XMLErrorReporter()
    '''
def setLocale():
    '''public void setLocale(final Locale fLocale)
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def setDocumentLocator():
    '''public void setDocumentLocator(final XMLLocator fLocator)
    '''
def putMessageFormatter():
    '''public void putMessageFormatter(final String key, final MessageFormatter value)
    '''
def getMessageFormatter():
    '''public MessageFormatter getMessageFormatter(final String key)
    '''
def removeMessageFormatter():
    '''public MessageFormatter removeMessageFormatter(final String key)
    '''
def reportError():
    '''public String reportError(final String s, final String s2, final Object[] array, final short n)
    public String reportError(final String s, final String s2, final Object[] array, final short n, final Exception ex)
    public String reportError(final XMLLocator xmlLocator, final String s, final String s2, final Object[] array, final short n)
    public String reportError(final XMLLocator xmlLocator, final String str, final String str2, final Object[] array, final short n, final Exception ex)
    '''
def reset():
    '''public void reset(final XMLComponentManager xmlComponentManager)
    '''
def getRecognizedFeatures():
    '''public String[] getRecognizedFeatures()
    '''
def setFeature():
    '''public void setFeature(final String s, final boolean fContinueAfterFatalError)
    '''
def getFeature():
    '''public boolean getFeature(final String s)
    '''
def getRecognizedProperties():
    '''public String[] getRecognizedProperties()
    '''
def setProperty():
    '''public void setProperty(final String s, final Object o)
    '''
def getFeatureDefault():
    '''public Boolean getFeatureDefault(final String anObject)
    '''
def getPropertyDefault():
    '''public Object getPropertyDefault(final String anObject)
    '''
def getErrorHandler():
    '''public XMLErrorHandler getErrorHandler()
    '''
def getSAXErrorHandler():
    '''public ErrorHandler getSAXErrorHandler()
    '''
