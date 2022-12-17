def getId():
    '''returns String\n\n
    getId()\n
    '''
def getRoute():
    '''returns HttpRoute\n\n
    getRoute()\n
    '''
def open():
    '''returns None\n\n
    open(final HttpRoute route, final HttpContext context, final HttpParams params)\n
    '''
def tunnelTarget():
    '''returns None\n\n
    tunnelTarget(final boolean secure, final HttpParams params)\n
    '''
def tunnelProxy():
    '''returns None\n\n
    tunnelProxy(final HttpHost next, final boolean secure, final HttpParams params)\n
    '''
def layerProtocol():
    '''returns None\n\n
    layerProtocol(final HttpContext context, final HttpParams params)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getState():
    '''returns Object\n\n
    getState()\n
    '''
def setState():
    '''returns None\n\n
    setState(final Object state)\n
    '''
