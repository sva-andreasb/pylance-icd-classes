def BasicHttpProcessor():
'''public BasicHttpProcessor()
'''
pass
def addRequestInterceptor():
'''public void addRequestInterceptor(final HttpRequestInterceptor itcp)
public void addRequestInterceptor(final HttpRequestInterceptor itcp, final int index)
'''
pass
def addResponseInterceptor():
'''public void addResponseInterceptor(final HttpResponseInterceptor itcp, final int index)
public void addResponseInterceptor(final HttpResponseInterceptor itcp)
'''
pass
def removeRequestInterceptorByClass():
'''public void removeRequestInterceptorByClass(final Class<? extends HttpRequestInterceptor> clazz)
'''
pass
def removeResponseInterceptorByClass():
'''public void removeResponseInterceptorByClass(final Class<? extends HttpResponseInterceptor> clazz)
'''
pass
def addInterceptor():
'''public final void addInterceptor(final HttpRequestInterceptor interceptor)
public final void addInterceptor(final HttpRequestInterceptor interceptor, final int index)
public final void addInterceptor(final HttpResponseInterceptor interceptor)
public final void addInterceptor(final HttpResponseInterceptor interceptor, final int index)
'''
pass
def getRequestInterceptorCount():
'''public int getRequestInterceptorCount()
'''
pass
def getRequestInterceptor():
'''public HttpRequestInterceptor getRequestInterceptor(final int index)
'''
pass
def clearRequestInterceptors():
'''public void clearRequestInterceptors()
'''
pass
def getResponseInterceptorCount():
'''public int getResponseInterceptorCount()
'''
pass
def getResponseInterceptor():
'''public HttpResponseInterceptor getResponseInterceptor(final int index)
'''
pass
def clearResponseInterceptors():
'''public void clearResponseInterceptors()
'''
pass
def setInterceptors():
'''public void setInterceptors(final List<?> list)
'''
pass
def clearInterceptors():
'''public void clearInterceptors()
'''
pass
def process():
'''public void process(final HttpRequest request, final HttpContext context)
public void process(final HttpResponse response, final HttpContext context)
'''
pass
def copy():
'''public BasicHttpProcessor copy()
'''
pass
def clone():
'''public Object clone()
'''
pass
