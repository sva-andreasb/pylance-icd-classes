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
def get():
    '''returns String\n\n
    get(final CharSequence name)\n
    get(final CharSequence name, final String defaultValue)\n
    '''
def getAll():
    '''returns List<String>\n\n
    getAll(final CharSequence name)\n
    '''
def valueStringIterator():
    '''returns Iterator<String>\n\n
    valueStringIterator(final CharSequence name)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final CharSequence name)\n
    contains(final String name, final String value, final boolean ignoreCase)\n
    contains(final CharSequence name, final CharSequence value, final boolean ignoreCase)\n
    '''
def add():
    '''returns HttpHeaders\n\n
    add(final CharSequence name, final Object value)\n
    add(final CharSequence name, final Iterable<?> values)\n
    add(final HttpHeaders headers)\n
    '''
def set():
    '''returns HttpHeaders\n\n
    set(final CharSequence name, final Object value)\n
    set(final CharSequence name, final Iterable<?> values)\n
    set(final HttpHeaders headers)\n
    '''
def setAll():
    '''returns HttpHeaders\n\n
    setAll(final HttpHeaders headers)\n
    '''
def remove():
    '''returns HttpHeaders\n\n
    remove(final CharSequence name)\n
    '''
def containsValue():
    '''returns boolean\n\n
    containsValue(final CharSequence name, final CharSequence value, final boolean ignoreCase)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def copy():
    '''returns HttpHeaders\n\n
    copy()\n
    '''
