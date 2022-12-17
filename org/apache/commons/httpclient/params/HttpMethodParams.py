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
def ():
    '''returns HttpMethodParams\n\n
    ()\n
    (final HttpParams defaults)\n
    '''
def getHttpElementCharset():
    '''returns String\n\n
    getHttpElementCharset()\n
    '''
def setHttpElementCharset():
    '''returns None\n\n
    setHttpElementCharset(final String charset)\n
    '''
def getContentCharset():
    '''returns String\n\n
    getContentCharset()\n
    '''
def setUriCharset():
    '''returns None\n\n
    setUriCharset(final String charset)\n
    '''
def getUriCharset():
    '''returns String\n\n
    getUriCharset()\n
    '''
def setContentCharset():
    '''returns None\n\n
    setContentCharset(final String charset)\n
    '''
def getCredentialCharset():
    '''returns String\n\n
    getCredentialCharset()\n
    '''
def setCredentialCharset():
    '''returns None\n\n
    setCredentialCharset(final String charset)\n
    '''
def getVersion():
    '''returns HttpVersion\n\n
    getVersion()\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final HttpVersion version)\n
    '''
def getCookiePolicy():
    '''returns String\n\n
    getCookiePolicy()\n
    '''
def setCookiePolicy():
    '''returns None\n\n
    setCookiePolicy(final String policy)\n
    '''
def getSoTimeout():
    '''returns int\n\n
    getSoTimeout()\n
    '''
def setSoTimeout():
    '''returns None\n\n
    setSoTimeout(final int timeout)\n
    '''
def setVirtualHost():
    '''returns None\n\n
    setVirtualHost(final String hostname)\n
    '''
def getVirtualHost():
    '''returns String\n\n
    getVirtualHost()\n
    '''
def makeStrict():
    '''returns None\n\n
    makeStrict()\n
    '''
def makeLenient():
    '''returns None\n\n
    makeLenient()\n
    '''
