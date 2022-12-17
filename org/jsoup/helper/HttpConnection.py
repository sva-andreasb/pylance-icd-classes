CONTENT_ENCODING = "String  \"Content-Encoding\""
DEFAULT_UA = "String  \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36\""
CONTENT_TYPE = "String  \"Content-Type\""
MULTIPART_FORM_DATA = "String  \"multipart/form-data\""
FORM_URL_ENCODED = "String  \"application/x-www-form-urlencoded\""
def ():
    '''returns HttpConnection\n\n
    ()\n
    '''
def url():
    '''returns T\n\n
    url(final URL url)\n
    url(final String url)\n
    url()\n
    url(final URL url)\n
    '''
def proxy():
    '''returns Request\n\n
    proxy(final Proxy proxy)\n
    proxy(final String host, final int port)\n
    proxy()\n
    proxy(final Proxy proxy)\n
    proxy(final String host, final int port)\n
    '''
def userAgent():
    '''returns Connection\n\n
    userAgent(final String userAgent)\n
    '''
def timeout():
    '''returns Request\n\n
    timeout(final int millis)\n
    timeout()\n
    timeout(final int millis)\n
    '''
def maxBodySize():
    '''returns int\n\n
    maxBodySize(final int bytes)\n
    maxBodySize()\n
    '''
def followRedirects():
    '''returns boolean\n\n
    followRedirects(final boolean followRedirects)\n
    followRedirects()\n
    '''
def referrer():
    '''returns Connection\n\n
    referrer(final String referrer)\n
    '''
def method():
    '''returns T\n\n
    method(final Method method)\n
    method()\n
    method(final Method method)\n
    '''
def ignoreHttpErrors():
    '''returns boolean\n\n
    ignoreHttpErrors(final boolean ignoreHttpErrors)\n
    ignoreHttpErrors()\n
    '''
def ignoreContentType():
    '''returns boolean\n\n
    ignoreContentType(final boolean ignoreContentType)\n
    ignoreContentType()\n
    '''
def data():
    '''returns Request\n\n
    data(final String key, final String value)\n
    data(final String key, final String filename, final InputStream inputStream)\n
    data(final String key, final String filename, final InputStream inputStream, final String contentType)\n
    data(final Map<String, String> data)\n
    data(final String... keyvals)\n
    data(final Collection<Connection.KeyVal> data)\n
    data(final Connection.KeyVal keyval)\n
    '''
def sslSocketFactory():
    '''returns None\n\n
    sslSocketFactory(final SSLSocketFactory sslSocketFactory)\n
    sslSocketFactory()\n
    sslSocketFactory(final SSLSocketFactory sslSocketFactory)\n
    '''
def requestBody():
    '''returns String\n\n
    requestBody(final String body)\n
    requestBody()\n
    '''
def header():
    '''returns T\n\n
    header(final String name, final String value)\n
    header(final String name)\n
    header(final String name, final String value)\n
    '''
def headers():
    '''returns List<String>\n\n
    headers(final Map<String, String> headers)\n
    headers(final String name)\n
    '''
def cookie():
    '''returns T\n\n
    cookie(final String name, final String value)\n
    cookie(final String name)\n
    cookie(final String name, final String value)\n
    '''
def cookies():
    '''returns Connection\n\n
    cookies(final Map<String, String> cookies)\n
    '''
def parser():
    '''returns Parser\n\n
    parser(final Parser parser)\n
    parser(final Parser parser)\n
    parser()\n
    '''
def get():
    '''returns Document\n\n
    get()\n
    '''
def post():
    '''returns Document\n\n
    post()\n
    '''
def request():
    '''returns Connection\n\n
    request(final Connection.Request request)\n
    '''
def response():
    '''returns Connection\n\n
    response(final Connection.Response response)\n
    '''
def postDataCharset():
    '''returns String\n\n
    postDataCharset(final String charset)\n
    postDataCharset()\n
    '''
def addHeader():
    '''returns T\n\n
    addHeader(final String name, String value)\n
    '''
def hasHeader():
    '''returns boolean\n\n
    hasHeader(final String name)\n
    '''
def hasHeaderWithValue():
    '''returns boolean\n\n
    hasHeaderWithValue(final String name, final String value)\n
    '''
def removeHeader():
    '''returns T\n\n
    removeHeader(final String name)\n
    '''
def hasCookie():
    '''returns boolean\n\n
    hasCookie(final String name)\n
    '''
def removeCookie():
    '''returns T\n\n
    removeCookie(final String name)\n
    '''
def statusCode():
    '''returns int\n\n
    statusCode()\n
    '''
def statusMessage():
    '''returns String\n\n
    statusMessage()\n
    '''
def charset():
    '''returns Response\n\n
    charset()\n
    charset(final String charset)\n
    '''
def contentType():
    '''returns String\n\n
    contentType()\n
    contentType()\n
    '''
def parse():
    '''returns Document\n\n
    parse()\n
    '''
def body():
    '''returns String\n\n
    body()\n
    '''
def bodyAsBytes():
    '''returns byte[]\n\n
    bodyAsBytes()\n
    '''
def bodyStream():
    '''returns BufferedInputStream\n\n
    bodyStream()\n
    '''
def key():
    '''returns String\n\n
    key(final String key)\n
    key()\n
    '''
def value():
    '''returns String\n\n
    value(final String value)\n
    value()\n
    '''
def inputStream():
    '''returns InputStream\n\n
    inputStream(final InputStream inputStream)\n
    inputStream()\n
    '''
def hasInputStream():
    '''returns boolean\n\n
    hasInputStream()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
