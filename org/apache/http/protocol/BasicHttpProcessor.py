def BasicHttpProcessor():
    '''    public BasicHttpProcessor()
    '''
def addRequestInterceptor():
    '''    public void addRequestInterceptor(final HttpRequestInterceptor itcp)
    public void addRequestInterceptor(final HttpRequestInterceptor itcp, final int index)
    '''
def addResponseInterceptor():
    '''    public void addResponseInterceptor(final HttpResponseInterceptor itcp, final int index)
    public void addResponseInterceptor(final HttpResponseInterceptor itcp)
    '''
def removeRequestInterceptorByClass():
    '''    public void removeRequestInterceptorByClass(final Class<? extends HttpRequestInterceptor> clazz)
    '''
def removeResponseInterceptorByClass():
    '''    public void removeResponseInterceptorByClass(final Class<? extends HttpResponseInterceptor> clazz)
    '''
def addInterceptor():
    '''    public final void addInterceptor(final HttpRequestInterceptor interceptor)
    public final void addInterceptor(final HttpRequestInterceptor interceptor, final int index)
    public final void addInterceptor(final HttpResponseInterceptor interceptor)
    public final void addInterceptor(final HttpResponseInterceptor interceptor, final int index)
    '''
def getRequestInterceptorCount():
    '''    public int getRequestInterceptorCount()
    '''
def getRequestInterceptor():
    '''    public HttpRequestInterceptor getRequestInterceptor(final int index)
    '''
def clearRequestInterceptors():
    '''    public void clearRequestInterceptors()
    '''
def getResponseInterceptorCount():
    '''    public int getResponseInterceptorCount()
    '''
def getResponseInterceptor():
    '''    public HttpResponseInterceptor getResponseInterceptor(final int index)
    '''
def clearResponseInterceptors():
    '''    public void clearResponseInterceptors()
    '''
def setInterceptors():
    '''    public void setInterceptors(final List<?> list)
    '''
def clearInterceptors():
    '''    public void clearInterceptors()
    '''
def process():
    '''    public void process(final HttpRequest request, final HttpContext context)
    public void process(final HttpResponse response, final HttpContext context)
    '''
def copy():
    '''    public BasicHttpProcessor copy()
    '''
def clone():
    '''    public Object clone()
    '''
