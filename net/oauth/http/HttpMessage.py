REQUEST = "String  HTTP request""
RESPONSE = "String  HTTP response""
STATUS_CODE = "String  HTTP status""
ACCEPT_ENCODING = "String  Accept-Encoding""
CONTENT_ENCODING = "String  Content-Encoding""
CONTENT_LENGTH = "String  Content-Length""
CONTENT_TYPE = "String  Content-Type""
DEFAULT_CHARSET = "String  ISO-8859-1""
def HttpMessage():
'''public HttpMessage()
public HttpMessage(final String method, final URL url)
public HttpMessage(final String method, final URL url, final InputStream body)
'''
pass
def getHeader():
'''public final String getHeader(final String name)
'''
pass
def removeHeaders():
'''public String removeHeaders(final String name)
'''
pass
def getContentCharset():
'''public final String getContentCharset()
'''
pass
def getBody():
'''public final InputStream getBody()
'''
pass
def dump():
'''public void dump(final Map<String, Object> into)
'''
pass
def newRequest():
'''public static HttpMessage newRequest(final OAuthMessage from, ParameterStyle style)
'''
pass
