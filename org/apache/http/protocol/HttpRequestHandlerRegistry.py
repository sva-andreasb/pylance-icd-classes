def ():
    '''returns HttpRequestHandlerRegistry\n\n
    ()\n
    '''
def register():
    '''returns None\n\n
    register(final String pattern, final HttpRequestHandler handler)\n
    '''
def unregister():
    '''returns None\n\n
    unregister(final String pattern)\n
    '''
def setHandlers():
    '''returns None\n\n
    setHandlers(final Map<String, HttpRequestHandler> map)\n
    '''
def lookup():
    '''returns HttpRequestHandler\n\n
    lookup(final String requestURI)\n
    '''
