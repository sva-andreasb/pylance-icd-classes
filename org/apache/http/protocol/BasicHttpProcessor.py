def ():
    '''returns BasicHttpProcessor\n\n
    ()\n
    '''
def addRequestInterceptor():
    '''returns None\n\n
    addRequestInterceptor(final HttpRequestInterceptor itcp)\n
    addRequestInterceptor(final HttpRequestInterceptor itcp, final int index)\n
    '''
def addResponseInterceptor():
    '''returns None\n\n
    addResponseInterceptor(final HttpResponseInterceptor itcp, final int index)\n
    addResponseInterceptor(final HttpResponseInterceptor itcp)\n
    '''
def removeRequestInterceptorByClass():
    '''returns None\n\n
    removeRequestInterceptorByClass(final Class<? extends HttpRequestInterceptor> clazz)\n
    '''
def removeResponseInterceptorByClass():
    '''returns None\n\n
    removeResponseInterceptorByClass(final Class<? extends HttpResponseInterceptor> clazz)\n
    '''
def getRequestInterceptorCount():
    '''returns int\n\n
    getRequestInterceptorCount()\n
    '''
def getRequestInterceptor():
    '''returns HttpRequestInterceptor\n\n
    getRequestInterceptor(final int index)\n
    '''
def clearRequestInterceptors():
    '''returns None\n\n
    clearRequestInterceptors()\n
    '''
def getResponseInterceptorCount():
    '''returns int\n\n
    getResponseInterceptorCount()\n
    '''
def getResponseInterceptor():
    '''returns HttpResponseInterceptor\n\n
    getResponseInterceptor(final int index)\n
    '''
def clearResponseInterceptors():
    '''returns None\n\n
    clearResponseInterceptors()\n
    '''
def setInterceptors():
    '''returns None\n\n
    setInterceptors(final List<?> list)\n
    '''
def clearInterceptors():
    '''returns None\n\n
    clearInterceptors()\n
    '''
def process():
    '''returns None\n\n
    process(final HttpRequest request, final HttpContext context)\n
    process(final HttpResponse response, final HttpContext context)\n
    '''
def copy():
    '''returns BasicHttpProcessor\n\n
    copy()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
