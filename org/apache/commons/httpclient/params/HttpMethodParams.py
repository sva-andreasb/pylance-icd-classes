USER_AGENT = "String  http.useragent""
PROTOCOL_VERSION = "String  http.protocol.version""
UNAMBIGUOUS_STATUS_LINE = "String  http.protocol.unambiguous-statusline""
SINGLE_COOKIE_HEADER = "String  http.protocol.single-cookie-header""
STRICT_TRANSFER_ENCODING = "String  http.protocol.strict-transfer-encoding""
REJECT_HEAD_BODY = "String  http.protocol.reject-head-body""
HEAD_BODY_CHECK_TIMEOUT = "String  http.protocol.head-body-timeout""
USE_EXPECT_CONTINUE = "String  http.protocol.expect-continue""
CREDENTIAL_CHARSET = "String  http.protocol.credential-charset""
HTTP_ELEMENT_CHARSET = "String  http.protocol.element-charset""
HTTP_URI_CHARSET = "String  http.protocol.uri-charset""
HTTP_CONTENT_CHARSET = "String  http.protocol.content-charset""
COOKIE_POLICY = "String  http.protocol.cookie-policy""
WARN_EXTRA_INPUT = "String  http.protocol.warn-extra-input""
STATUS_LINE_GARBAGE_LIMIT = "String  http.protocol.status-line-garbage-limit""
SO_TIMEOUT = "String  http.socket.timeout""
DATE_PATTERNS = "String  http.dateparser.patterns""
RETRY_HANDLER = "String  http.method.retry-handler""
BUFFER_WARN_TRIGGER_LIMIT = "String  http.method.response.buffer.warnlimit""
VIRTUAL_HOST = "String  http.virtual-host""
MULTIPART_BOUNDARY = "String  http.method.multipart.boundary""
def HttpMethodParams():
'''public HttpMethodParams()
public HttpMethodParams(final HttpParams defaults)
'''
pass
def getHttpElementCharset():
'''public String getHttpElementCharset()
'''
pass
def setHttpElementCharset():
'''public void setHttpElementCharset(final String charset)
'''
pass
def getContentCharset():
'''public String getContentCharset()
'''
pass
def setUriCharset():
'''public void setUriCharset(final String charset)
'''
pass
def getUriCharset():
'''public String getUriCharset()
'''
pass
def setContentCharset():
'''public void setContentCharset(final String charset)
'''
pass
def getCredentialCharset():
'''public String getCredentialCharset()
'''
pass
def setCredentialCharset():
'''public void setCredentialCharset(final String charset)
'''
pass
def getVersion():
'''public HttpVersion getVersion()
'''
pass
def setVersion():
'''public void setVersion(final HttpVersion version)
'''
pass
def getCookiePolicy():
'''public String getCookiePolicy()
'''
pass
def setCookiePolicy():
'''public void setCookiePolicy(final String policy)
'''
pass
def getSoTimeout():
'''public int getSoTimeout()
'''
pass
def setSoTimeout():
'''public void setSoTimeout(final int timeout)
'''
pass
def setVirtualHost():
'''public void setVirtualHost(final String hostname)
'''
pass
def getVirtualHost():
'''public String getVirtualHost()
'''
pass
def makeStrict():
'''public void makeStrict()
'''
pass
def makeLenient():
'''public void makeLenient()
'''
pass
