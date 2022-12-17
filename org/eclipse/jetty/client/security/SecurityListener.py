def ():
    '''returns SecurityListener\n\n
    (final HttpDestination destination, final HttpExchange ex)\n
    '''
def onResponseStatus():
    '''returns None\n\n
    onResponseStatus(final Buffer version, final int status, final Buffer reason)\n
    '''
def onResponseHeader():
    '''returns None\n\n
    onResponseHeader(final Buffer name, final Buffer value)\n
    '''
def onRequestComplete():
    '''returns None\n\n
    onRequestComplete()\n
    '''
def onResponseComplete():
    '''returns None\n\n
    onResponseComplete()\n
    '''
def onRetry():
    '''returns None\n\n
    onRetry()\n
    '''
