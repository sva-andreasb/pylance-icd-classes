def create():
    '''public static RequestBuilder create(final String method)
    '''
def get():
    '''public static RequestBuilder get()
    public static RequestBuilder get(final URI uri)
    public static RequestBuilder get(final String uri)
    '''
def head():
    '''public static RequestBuilder head()
    public static RequestBuilder head(final URI uri)
    public static RequestBuilder head(final String uri)
    '''
def patch():
    '''public static RequestBuilder patch()
    public static RequestBuilder patch(final URI uri)
    public static RequestBuilder patch(final String uri)
    '''
def post():
    '''public static RequestBuilder post()
    public static RequestBuilder post(final URI uri)
    public static RequestBuilder post(final String uri)
    '''
def put():
    '''public static RequestBuilder put()
    public static RequestBuilder put(final URI uri)
    public static RequestBuilder put(final String uri)
    '''
def delete():
    '''public static RequestBuilder delete()
    public static RequestBuilder delete(final URI uri)
    public static RequestBuilder delete(final String uri)
    '''
def trace():
    '''public static RequestBuilder trace()
    public static RequestBuilder trace(final URI uri)
    public static RequestBuilder trace(final String uri)
    '''
def options():
    '''public static RequestBuilder options()
    public static RequestBuilder options(final URI uri)
    public static RequestBuilder options(final String uri)
    '''
def copy():
    '''public static RequestBuilder copy(final HttpRequest request)
    '''
def setCharset():
    '''public RequestBuilder setCharset(final Charset charset)
    '''
def getCharset():
    '''public Charset getCharset()
    '''
def getMethod():
    '''public String getMethod()
    public String getMethod()
    public String getMethod()
    '''
def getVersion():
    '''public ProtocolVersion getVersion()
    '''
def setVersion():
    '''public RequestBuilder setVersion(final ProtocolVersion version)
    '''
def getUri():
    '''public URI getUri()
    '''
def setUri():
    '''public RequestBuilder setUri(final URI uri)
    public RequestBuilder setUri(final String uri)
    '''
def getFirstHeader():
    '''public Header getFirstHeader(final String name)
    '''
def getLastHeader():
    '''public Header getLastHeader(final String name)
    '''
def getHeaders():
    '''public Header[] getHeaders(final String name)
    '''
def addHeader():
    '''public RequestBuilder addHeader(final Header header)
    public RequestBuilder addHeader(final String name, final String value)
    '''
def removeHeader():
    '''public RequestBuilder removeHeader(final Header header)
    '''
def removeHeaders():
    '''public RequestBuilder removeHeaders(final String name)
    '''
def setHeader():
    '''public RequestBuilder setHeader(final Header header)
    public RequestBuilder setHeader(final String name, final String value)
    '''
def getEntity():
    '''public HttpEntity getEntity()
    '''
def setEntity():
    '''public RequestBuilder setEntity(final HttpEntity entity)
    '''
def getParameters():
    '''public List<NameValuePair> getParameters()
    '''
def addParameter():
    '''public RequestBuilder addParameter(final NameValuePair nvp)
    public RequestBuilder addParameter(final String name, final String value)
    '''
def addParameters():
    '''public RequestBuilder addParameters(final NameValuePair... nvps)
    '''
def getConfig():
    '''public RequestConfig getConfig()
    '''
def setConfig():
    '''public RequestBuilder setConfig(final RequestConfig config)
    '''
def build():
    '''public HttpUriRequest build()
    '''
