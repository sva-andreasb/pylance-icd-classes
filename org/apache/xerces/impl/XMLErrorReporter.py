SEVERITY_WARNING = "short  0"
SEVERITY_ERROR = "short  1"
SEVERITY_FATAL_ERROR = "short  2"
def XMLErrorReporter():
'''public XMLErrorReporter()
'''
pass
def setLocale():
'''public void setLocale(final Locale fLocale)
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def setDocumentLocator():
'''public void setDocumentLocator(final XMLLocator fLocator)
'''
pass
def putMessageFormatter():
'''public void putMessageFormatter(final String key, final MessageFormatter value)
'''
pass
def getMessageFormatter():
'''public MessageFormatter getMessageFormatter(final String key)
'''
pass
def removeMessageFormatter():
'''public MessageFormatter removeMessageFormatter(final String key)
'''
pass
def reportError():
'''public String reportError(final String s, final String s2, final Object[] array, final short n)
public String reportError(final String s, final String s2, final Object[] array, final short n, final Exception ex)
public String reportError(final XMLLocator xmlLocator, final String s, final String s2, final Object[] array, final short n)
public String reportError(final XMLLocator xmlLocator, final String str, final String str2, final Object[] array, final short n, final Exception ex)
'''
pass
def reset():
'''public void reset(final XMLComponentManager xmlComponentManager)
'''
pass
def getRecognizedFeatures():
'''public String[] getRecognizedFeatures()
'''
pass
def setFeature():
'''public void setFeature(final String s, final boolean fContinueAfterFatalError)
'''
pass
def getFeature():
'''public boolean getFeature(final String s)
'''
pass
def getRecognizedProperties():
'''public String[] getRecognizedProperties()
'''
pass
def setProperty():
'''public void setProperty(final String s, final Object o)
'''
pass
def getFeatureDefault():
'''public Boolean getFeatureDefault(final String anObject)
'''
pass
def getPropertyDefault():
'''public Object getPropertyDefault(final String anObject)
'''
pass
def getErrorHandler():
'''public XMLErrorHandler getErrorHandler()
'''
pass
def getSAXErrorHandler():
'''public ErrorHandler getSAXErrorHandler()
'''
pass
