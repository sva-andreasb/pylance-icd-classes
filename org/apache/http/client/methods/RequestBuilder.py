def create():
'''public static RequestBuilder create(final String method)
'''
pass
def get():
'''public static RequestBuilder get()
public static RequestBuilder get(final URI uri)
public static RequestBuilder get(final String uri)
'''
pass
def head():
'''public static RequestBuilder head()
public static RequestBuilder head(final URI uri)
public static RequestBuilder head(final String uri)
'''
pass
def patch():
'''public static RequestBuilder patch()
public static RequestBuilder patch(final URI uri)
public static RequestBuilder patch(final String uri)
'''
pass
def post():
'''public static RequestBuilder post()
public static RequestBuilder post(final URI uri)
public static RequestBuilder post(final String uri)
'''
pass
def put():
'''public static RequestBuilder put()
public static RequestBuilder put(final URI uri)
public static RequestBuilder put(final String uri)
'''
pass
def delete():
'''public static RequestBuilder delete()
public static RequestBuilder delete(final URI uri)
public static RequestBuilder delete(final String uri)
'''
pass
def trace():
'''public static RequestBuilder trace()
public static RequestBuilder trace(final URI uri)
public static RequestBuilder trace(final String uri)
'''
pass
def options():
'''public static RequestBuilder options()
public static RequestBuilder options(final URI uri)
public static RequestBuilder options(final String uri)
'''
pass
def copy():
'''public static RequestBuilder copy(final HttpRequest request)
'''
pass
def setCharset():
'''public RequestBuilder setCharset(final Charset charset)
'''
pass
def getCharset():
'''public Charset getCharset()
'''
pass
def getMethod():
'''public String getMethod()
public String getMethod()
public String getMethod()
'''
pass
def getVersion():
'''public ProtocolVersion getVersion()
'''
pass
def setVersion():
'''public RequestBuilder setVersion(final ProtocolVersion version)
'''
pass
def getUri():
'''public URI getUri()
'''
pass
def setUri():
'''public RequestBuilder setUri(final URI uri)
public RequestBuilder setUri(final String uri)
'''
pass
def getFirstHeader():
'''public Header getFirstHeader(final String name)
'''
pass
def getLastHeader():
'''public Header getLastHeader(final String name)
'''
pass
def getHeaders():
'''public Header[] getHeaders(final String name)
'''
pass
def addHeader():
'''public RequestBuilder addHeader(final Header header)
public RequestBuilder addHeader(final String name, final String value)
'''
pass
def removeHeader():
'''public RequestBuilder removeHeader(final Header header)
'''
pass
def removeHeaders():
'''public RequestBuilder removeHeaders(final String name)
'''
pass
def setHeader():
'''public RequestBuilder setHeader(final Header header)
public RequestBuilder setHeader(final String name, final String value)
'''
pass
def getEntity():
'''public HttpEntity getEntity()
'''
pass
def setEntity():
'''public RequestBuilder setEntity(final HttpEntity entity)
'''
pass
def getParameters():
'''public List<NameValuePair> getParameters()
'''
pass
def addParameter():
'''public RequestBuilder addParameter(final NameValuePair nvp)
public RequestBuilder addParameter(final String name, final String value)
'''
pass
def addParameters():
'''public RequestBuilder addParameters(final NameValuePair... nvps)
'''
pass
def getConfig():
'''public RequestConfig getConfig()
'''
pass
def setConfig():
'''public RequestBuilder setConfig(final RequestConfig config)
'''
pass
def build():
'''public HttpUriRequest build()
'''
pass
