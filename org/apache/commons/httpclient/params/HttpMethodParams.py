USER_AGENT = "String  \"http.useragent\""
PROTOCOL_VERSION = "String  \"http.protocol.version\""
UNAMBIGUOUS_STATUS_LINE = "String  \"http.protocol.unambiguous-statusline\""
SINGLE_COOKIE_HEADER = "String  \"http.protocol.single-cookie-header\""
STRICT_TRANSFER_ENCODING = "String  \"http.protocol.strict-transfer-encoding\""
REJECT_HEAD_BODY = "String  \"http.protocol.reject-head-body\""
HEAD_BODY_CHECK_TIMEOUT = "String  \"http.protocol.head-body-timeout\""
USE_EXPECT_CONTINUE = "String  \"http.protocol.expect-continue\""
CREDENTIAL_CHARSET = "String  \"http.protocol.credential-charset\""
HTTP_ELEMENT_CHARSET = "String  \"http.protocol.element-charset\""
HTTP_URI_CHARSET = "String  \"http.protocol.uri-charset\""
HTTP_CONTENT_CHARSET = "String  \"http.protocol.content-charset\""
COOKIE_POLICY = "String  \"http.protocol.cookie-policy\""
WARN_EXTRA_INPUT = "String  \"http.protocol.warn-extra-input\""
STATUS_LINE_GARBAGE_LIMIT = "String  \"http.protocol.status-line-garbage-limit\""
SO_TIMEOUT = "String  \"http.socket.timeout\""
DATE_PATTERNS = "String  \"http.dateparser.patterns\""
RETRY_HANDLER = "String  \"http.method.retry-handler\""
BUFFER_WARN_TRIGGER_LIMIT = "String  \"http.method.response.buffer.warnlimit\""
VIRTUAL_HOST = "String  \"http.virtual-host\""
MULTIPART_BOUNDARY = "String  \"http.method.multipart.boundary\""
def HttpMethodParams():
    '''public HttpMethodParams()
    public HttpMethodParams(final HttpParams defaults)
    '''
def getHttpElementCharset():
    '''public String getHttpElementCharset()
    '''
def setHttpElementCharset():
    '''public void setHttpElementCharset(final String charset)
    '''
def getContentCharset():
    '''public String getContentCharset()
    '''
def setUriCharset():
    '''public void setUriCharset(final String charset)
    '''
def getUriCharset():
    '''public String getUriCharset()
    '''
def setContentCharset():
    '''public void setContentCharset(final String charset)
    '''
def getCredentialCharset():
    '''public String getCredentialCharset()
    '''
def setCredentialCharset():
    '''public void setCredentialCharset(final String charset)
    '''
def getVersion():
    '''public HttpVersion getVersion()
    '''
def setVersion():
    '''public void setVersion(final HttpVersion version)
    '''
def getCookiePolicy():
    '''public String getCookiePolicy()
    '''
def setCookiePolicy():
    '''public void setCookiePolicy(final String policy)
    '''
def getSoTimeout():
    '''public int getSoTimeout()
    '''
def setSoTimeout():
    '''public void setSoTimeout(final int timeout)
    '''
def setVirtualHost():
    '''public void setVirtualHost(final String hostname)
    '''
def getVirtualHost():
    '''public String getVirtualHost()
    '''
def makeStrict():
    '''public void makeStrict()
    '''
def makeLenient():
    '''public void makeLenient()
    '''
