def ContextedRuntimeException():
'''public ContextedRuntimeException()
public ContextedRuntimeException(final String message)
public ContextedRuntimeException(final Throwable cause)
public ContextedRuntimeException(final String message, final Throwable cause)
public ContextedRuntimeException(final String message, final Throwable cause, ExceptionContext context)
'''
pass
def addContextValue():
'''public ContextedRuntimeException addContextValue(final String label, final Object value)
'''
pass
def setContextValue():
'''public ContextedRuntimeException setContextValue(final String label, final Object value)
'''
pass
def getContextValues():
'''public List<Object> getContextValues(final String label)
'''
pass
def getFirstContextValue():
'''public Object getFirstContextValue(final String label)
'''
pass
def getContextEntries():
'''public List<Pair<String, Object>> getContextEntries()
'''
pass
def getContextLabels():
'''public Set<String> getContextLabels()
'''
pass
def getMessage():
'''public String getMessage()
'''
pass
def getRawMessage():
'''public String getRawMessage()
'''
pass
def getFormattedExceptionMessage():
'''public String getFormattedExceptionMessage(final String baseMessage)
'''
pass
