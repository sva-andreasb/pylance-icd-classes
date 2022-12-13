def DecompressingHttpClient():
    '''    public DecompressingHttpClient()
    public DecompressingHttpClient(final HttpClient backend)
    '''
def getParams():
    '''    public HttpParams getParams()
    '''
def getConnectionManager():
    '''    public ClientConnectionManager getConnectionManager()
    '''
def execute():
    '''    public HttpResponse execute(final HttpUriRequest request)
    public HttpResponse execute(final HttpUriRequest request, final HttpContext context)
    public HttpResponse execute(final HttpHost target, final HttpRequest request)
    public HttpResponse execute(final HttpHost target, final HttpRequest request, final HttpContext context)
    public <T> T execute(final HttpUriRequest request, final ResponseHandler<? extends T> responseHandler)
    public <T> T execute(final HttpUriRequest request, final ResponseHandler<? extends T> responseHandler, final HttpContext context)
    public <T> T execute(final HttpHost target, final HttpRequest request, final ResponseHandler<? extends T> responseHandler)
    public <T> T execute(final HttpHost target, final HttpRequest request, final ResponseHandler<? extends T> responseHandler, final HttpContext context)
    '''
def getHttpClient():
    '''    public HttpClient getHttpClient()
    '''
