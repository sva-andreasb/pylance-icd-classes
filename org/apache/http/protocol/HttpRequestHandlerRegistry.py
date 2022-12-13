def HttpRequestHandlerRegistry():
    '''public HttpRequestHandlerRegistry()
    '''
def register():
    '''public void register(final String pattern, final HttpRequestHandler handler)
    '''
def unregister():
    '''public void unregister(final String pattern)
    '''
def setHandlers():
    '''public void setHandlers(final Map<String, HttpRequestHandler> map)
    '''
def getHandlers():
    '''public Map<String, HttpRequestHandler> getHandlers()
    '''
def lookup():
    '''public HttpRequestHandler lookup(final String requestURI)
    '''
