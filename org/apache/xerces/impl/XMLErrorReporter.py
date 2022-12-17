SEVERITY_WARNING = "short  0"
SEVERITY_ERROR = "short  1"
SEVERITY_FATAL_ERROR = "short  2"
def ():
    '''returns XMLErrorReporter\n\n
    ()\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale fLocale)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final XMLLocator fLocator)\n
    '''
def putMessageFormatter():
    '''returns None\n\n
    putMessageFormatter(final String key, final MessageFormatter value)\n
    '''
def getMessageFormatter():
    '''returns MessageFormatter\n\n
    getMessageFormatter(final String key)\n
    '''
def removeMessageFormatter():
    '''returns MessageFormatter\n\n
    removeMessageFormatter(final String key)\n
    '''
def reportError():
    '''returns String\n\n
    reportError(final String s, final String s2, final Object[] array, final short n)\n
    reportError(final String s, final String s2, final Object[] array, final short n, final Exception ex)\n
    reportError(final XMLLocator xmlLocator, final String s, final String s2, final Object[] array, final short n)\n
    reportError(final XMLLocator xmlLocator, final String str, final String str2, final Object[] array, final short n, final Exception ex)\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager xmlComponentManager)\n
    '''
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String s, final boolean fContinueAfterFatalError)\n
    '''
def getFeature():
    '''returns boolean\n\n
    getFeature(final String s)\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String anObject)\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String anObject)\n
    '''
def getErrorHandler():
    '''returns XMLErrorHandler\n\n
    getErrorHandler()\n
    '''
def getSAXErrorHandler():
    '''returns ErrorHandler\n\n
    getSAXErrorHandler()\n
    '''
