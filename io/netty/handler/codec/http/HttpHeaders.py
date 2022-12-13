ACCEPT = "String  \"Accept\""
ACCEPT_CHARSET = "String  \"Accept-Charset\""
ACCEPT_ENCODING = "String  \"Accept-Encoding\""
ACCEPT_LANGUAGE = "String  \"Accept-Language\""
ACCEPT_RANGES = "String  \"Accept-Ranges\""
ACCEPT_PATCH = "String  \"Accept-Patch\""
ACCESS_CONTROL_ALLOW_CREDENTIALS = "String  \"Access-Control-Allow-Credentials\""
ACCESS_CONTROL_ALLOW_HEADERS = "String  \"Access-Control-Allow-Headers\""
ACCESS_CONTROL_ALLOW_METHODS = "String  \"Access-Control-Allow-Methods\""
ACCESS_CONTROL_ALLOW_ORIGIN = "String  \"Access-Control-Allow-Origin\""
ACCESS_CONTROL_EXPOSE_HEADERS = "String  \"Access-Control-Expose-Headers\""
ACCESS_CONTROL_MAX_AGE = "String  \"Access-Control-Max-Age\""
ACCESS_CONTROL_REQUEST_HEADERS = "String  \"Access-Control-Request-Headers\""
ACCESS_CONTROL_REQUEST_METHOD = "String  \"Access-Control-Request-Method\""
AGE = "String  \"Age\""
ALLOW = "String  \"Allow\""
AUTHORIZATION = "String  \"Authorization\""
CACHE_CONTROL = "String  \"Cache-Control\""
CONNECTION = "String  \"Connection\""
CONTENT_BASE = "String  \"Content-Base\""
CONTENT_ENCODING = "String  \"Content-Encoding\""
CONTENT_LANGUAGE = "String  \"Content-Language\""
CONTENT_LENGTH = "String  \"Content-Length\""
CONTENT_LOCATION = "String  \"Content-Location\""
CONTENT_TRANSFER_ENCODING = "String  \"Content-Transfer-Encoding\""
CONTENT_MD5 = "String  \"Content-MD5\""
CONTENT_RANGE = "String  \"Content-Range\""
CONTENT_TYPE = "String  \"Content-Type\""
COOKIE = "String  \"Cookie\""
DATE = "String  \"Date\""
ETAG = "String  \"ETag\""
EXPECT = "String  \"Expect\""
EXPIRES = "String  \"Expires\""
FROM = "String  \"From\""
HOST = "String  \"Host\""
IF_MATCH = "String  \"If-Match\""
IF_MODIFIED_SINCE = "String  \"If-Modified-Since\""
IF_NONE_MATCH = "String  \"If-None-Match\""
IF_RANGE = "String  \"If-Range\""
IF_UNMODIFIED_SINCE = "String  \"If-Unmodified-Since\""
LAST_MODIFIED = "String  \"Last-Modified\""
LOCATION = "String  \"Location\""
MAX_FORWARDS = "String  \"Max-Forwards\""
ORIGIN = "String  \"Origin\""
PRAGMA = "String  \"Pragma\""
PROXY_AUTHENTICATE = "String  \"Proxy-Authenticate\""
PROXY_AUTHORIZATION = "String  \"Proxy-Authorization\""
RANGE = "String  \"Range\""
REFERER = "String  \"Referer\""
RETRY_AFTER = "String  \"Retry-After\""
SEC_WEBSOCKET_KEY1 = "String  \"Sec-WebSocket-Key1\""
SEC_WEBSOCKET_KEY2 = "String  \"Sec-WebSocket-Key2\""
SEC_WEBSOCKET_LOCATION = "String  \"Sec-WebSocket-Location\""
SEC_WEBSOCKET_ORIGIN = "String  \"Sec-WebSocket-Origin\""
SEC_WEBSOCKET_PROTOCOL = "String  \"Sec-WebSocket-Protocol\""
SEC_WEBSOCKET_VERSION = "String  \"Sec-WebSocket-Version\""
SEC_WEBSOCKET_KEY = "String  \"Sec-WebSocket-Key\""
SEC_WEBSOCKET_ACCEPT = "String  \"Sec-WebSocket-Accept\""
SERVER = "String  \"Server\""
SET_COOKIE = "String  \"Set-Cookie\""
SET_COOKIE2 = "String  \"Set-Cookie2\""
TE = "String  \"TE\""
TRAILER = "String  \"Trailer\""
TRANSFER_ENCODING = "String  \"Transfer-Encoding\""
UPGRADE = "String  \"Upgrade\""
USER_AGENT = "String  \"User-Agent\""
VARY = "String  \"Vary\""
VIA = "String  \"Via\""
WARNING = "String  \"Warning\""
WEBSOCKET_LOCATION = "String  \"WebSocket-Location\""
WEBSOCKET_ORIGIN = "String  \"WebSocket-Origin\""
WEBSOCKET_PROTOCOL = "String  \"WebSocket-Protocol\""
WWW_AUTHENTICATE = "String  \"WWW-Authenticate\""
APPLICATION_JSON = "String  \"application/json\""
APPLICATION_X_WWW_FORM_URLENCODED = "String  \"application/x-www-form-urlencoded\""
BASE64 = "String  \"base64\""
BINARY = "String  \"binary\""
BOUNDARY = "String  \"boundary\""
BYTES = "String  \"bytes\""
CHARSET = "String  \"charset\""
CHUNKED = "String  \"chunked\""
CLOSE = "String  \"close\""
COMPRESS = "String  \"compress\""
CONTINUE = "String  \"100-continue\""
DEFLATE = "String  \"deflate\""
GZIP = "String  \"gzip\""
GZIP_DEFLATE = "String  \"gzip,deflate\""
IDENTITY = "String  \"identity\""
KEEP_ALIVE = "String  \"keep-alive\""
MAX_AGE = "String  \"max-age\""
MAX_STALE = "String  \"max-stale\""
MIN_FRESH = "String  \"min-fresh\""
MULTIPART_FORM_DATA = "String  \"multipart/form-data\""
MUST_REVALIDATE = "String  \"must-revalidate\""
NO_CACHE = "String  \"no-cache\""
NO_STORE = "String  \"no-store\""
NO_TRANSFORM = "String  \"no-transform\""
NONE = "String  \"none\""
ONLY_IF_CACHED = "String  \"only-if-cached\""
PRIVATE = "String  \"private\""
PROXY_REVALIDATE = "String  \"proxy-revalidate\""
PUBLIC = "String  \"public\""
QUOTED_PRINTABLE = "String  \"quoted-printable\""
S_MAXAGE = "String  \"s-maxage\""
TRAILERS = "String  \"trailers\""
WEBSOCKET = "String  \"WebSocket\""
def isKeepAlive():
    '''    public static boolean isKeepAlive(final HttpMessage message)
    '''
def setKeepAlive():
    '''    public static void setKeepAlive(final HttpMessage message, final boolean keepAlive)
    '''
def getHeader():
    '''    public static String getHeader(final HttpMessage message, final String name)
    public static String getHeader(final HttpMessage message, final CharSequence name)
    public static String getHeader(final HttpMessage message, final String name, final String defaultValue)
    public static String getHeader(final HttpMessage message, final CharSequence name, final String defaultValue)
    '''
def setHeader():
    '''    public static void setHeader(final HttpMessage message, final String name, final Object value)
    public static void setHeader(final HttpMessage message, final CharSequence name, final Object value)
    public static void setHeader(final HttpMessage message, final String name, final Iterable<?> values)
    public static void setHeader(final HttpMessage message, final CharSequence name, final Iterable<?> values)
    '''
def addHeader():
    '''    public static void addHeader(final HttpMessage message, final String name, final Object value)
    public static void addHeader(final HttpMessage message, final CharSequence name, final Object value)
    '''
def removeHeader():
    '''    public static void removeHeader(final HttpMessage message, final String name)
    public static void removeHeader(final HttpMessage message, final CharSequence name)
    '''
def clearHeaders():
    '''    public static void clearHeaders(final HttpMessage message)
    '''
def getIntHeader():
    '''    public static int getIntHeader(final HttpMessage message, final String name)
    public static int getIntHeader(final HttpMessage message, final CharSequence name)
    public static int getIntHeader(final HttpMessage message, final String name, final int defaultValue)
    public static int getIntHeader(final HttpMessage message, final CharSequence name, final int defaultValue)
    '''
def setIntHeader():
    '''    public static void setIntHeader(final HttpMessage message, final String name, final int value)
    public static void setIntHeader(final HttpMessage message, final CharSequence name, final int value)
    public static void setIntHeader(final HttpMessage message, final String name, final Iterable<Integer> values)
    public static void setIntHeader(final HttpMessage message, final CharSequence name, final Iterable<Integer> values)
    '''
def addIntHeader():
    '''    public static void addIntHeader(final HttpMessage message, final String name, final int value)
    public static void addIntHeader(final HttpMessage message, final CharSequence name, final int value)
    '''
def getDateHeader():
    '''    public static Date getDateHeader(final HttpMessage message, final String name)
    public static Date getDateHeader(final HttpMessage message, final CharSequence name)
    public static Date getDateHeader(final HttpMessage message, final String name, final Date defaultValue)
    public static Date getDateHeader(final HttpMessage message, final CharSequence name, final Date defaultValue)
    '''
def setDateHeader():
    '''    public static void setDateHeader(final HttpMessage message, final String name, final Date value)
    public static void setDateHeader(final HttpMessage message, final CharSequence name, final Date value)
    public static void setDateHeader(final HttpMessage message, final String name, final Iterable<Date> values)
    public static void setDateHeader(final HttpMessage message, final CharSequence name, final Iterable<Date> values)
    '''
def addDateHeader():
    '''    public static void addDateHeader(final HttpMessage message, final String name, final Date value)
    public static void addDateHeader(final HttpMessage message, final CharSequence name, final Date value)
    '''
def getContentLength():
    '''    public static long getContentLength(final HttpMessage message)
    public static long getContentLength(final HttpMessage message, final long defaultValue)
    '''
def setContentLength():
    '''    public static void setContentLength(final HttpMessage message, final long length)
    '''
def getHost():
    '''    public static String getHost(final HttpMessage message)
    public static String getHost(final HttpMessage message, final String defaultValue)
    '''
def setHost():
    '''    public static void setHost(final HttpMessage message, final String value)
    public static void setHost(final HttpMessage message, final CharSequence value)
    '''
def getDate():
    '''    public static Date getDate(final HttpMessage message)
    public static Date getDate(final HttpMessage message, final Date defaultValue)
    '''
def setDate():
    '''    public static void setDate(final HttpMessage message, final Date value)
    '''
def is100ContinueExpected():
    '''    public static boolean is100ContinueExpected(final HttpMessage message)
    '''
def set100ContinueExpected():
    '''    public static void set100ContinueExpected(final HttpMessage message)
    public static void set100ContinueExpected(final HttpMessage message, final boolean set)
    '''
def isTransferEncodingChunked():
    '''    public static boolean isTransferEncodingChunked(final HttpMessage message)
    '''
def removeTransferEncodingChunked():
    '''    public static void removeTransferEncodingChunked(final HttpMessage m)
    '''
def setTransferEncodingChunked():
    '''    public static void setTransferEncodingChunked(final HttpMessage m)
    '''
def isContentLengthSet():
    '''    public static boolean isContentLengthSet(final HttpMessage m)
    '''
def equalsIgnoreCase():
    '''    public static boolean equalsIgnoreCase(final CharSequence name1, final CharSequence name2)
    '''
def encodeAscii():
    '''    public static void encodeAscii(final CharSequence seq, final ByteBuf buf)
    '''
def newEntity():
    '''    public static CharSequence newEntity(final String name)
    '''
def get():
    '''    public String get(final CharSequence name)
    public String get(final CharSequence name, final String defaultValue)
    '''
def getAll():
    '''    public List<String> getAll(final CharSequence name)
    '''
def valueStringIterator():
    '''    public Iterator<String> valueStringIterator(final CharSequence name)
    '''
def contains():
    '''    public boolean contains(final CharSequence name)
    public boolean contains(final String name, final String value, final boolean ignoreCase)
    public boolean contains(final CharSequence name, final CharSequence value, final boolean ignoreCase)
    '''
def add():
    '''    public HttpHeaders add(final CharSequence name, final Object value)
    public HttpHeaders add(final CharSequence name, final Iterable<?> values)
    public HttpHeaders add(final HttpHeaders headers)
    '''
def set():
    '''    public HttpHeaders set(final CharSequence name, final Object value)
    public HttpHeaders set(final CharSequence name, final Iterable<?> values)
    public HttpHeaders set(final HttpHeaders headers)
    '''
def setAll():
    '''    public HttpHeaders setAll(final HttpHeaders headers)
    '''
def remove():
    '''    public HttpHeaders remove(final CharSequence name)
    '''
def containsValue():
    '''    public boolean containsValue(final CharSequence name, final CharSequence value, final boolean ignoreCase)
    '''
def getAsString():
    '''    public final String getAsString(final CharSequence name)
    '''
def getAllAsString():
    '''    public final List<String> getAllAsString(final CharSequence name)
    '''
def toString():
    '''    public String toString()
    '''
def copy():
    '''    public HttpHeaders copy()
    '''
