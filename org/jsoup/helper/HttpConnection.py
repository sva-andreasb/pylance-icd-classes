CONTENT_ENCODING = "String  \"Content-Encoding\""
DEFAULT_UA = "String  \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36\""
CONTENT_TYPE = "String  \"Content-Type\""
MULTIPART_FORM_DATA = "String  \"multipart/form-data\""
FORM_URL_ENCODED = "String  \"application/x-www-form-urlencoded\""
def connect():
    '''public static Connection connect(final String url)
    public static Connection connect(final URL url)
    '''
def HttpConnection():
    '''public HttpConnection()
    '''
def url():
    '''public Connection url(final URL url)
    public Connection url(final String url)
    public URL url()
    public T url(final URL url)
    '''
def proxy():
    '''public Connection proxy(final Proxy proxy)
    public Connection proxy(final String host, final int port)
    public Proxy proxy()
    public Request proxy(final Proxy proxy)
    public Request proxy(final String host, final int port)
    '''
def userAgent():
    '''public Connection userAgent(final String userAgent)
    '''
def timeout():
    '''public Connection timeout(final int millis)
    public int timeout()
    public Request timeout(final int millis)
    '''
def maxBodySize():
    '''public Connection maxBodySize(final int bytes)
    public int maxBodySize()
    '''
def followRedirects():
    '''public Connection followRedirects(final boolean followRedirects)
    public boolean followRedirects()
    '''
def referrer():
    '''public Connection referrer(final String referrer)
    '''
def method():
    '''public Connection method(final Method method)
    public Method method()
    public T method(final Method method)
    '''
def ignoreHttpErrors():
    '''public Connection ignoreHttpErrors(final boolean ignoreHttpErrors)
    public boolean ignoreHttpErrors()
    '''
def ignoreContentType():
    '''public Connection ignoreContentType(final boolean ignoreContentType)
    public boolean ignoreContentType()
    '''
def data():
    '''public Connection data(final String key, final String value)
    public Connection data(final String key, final String filename, final InputStream inputStream)
    public Connection data(final String key, final String filename, final InputStream inputStream, final String contentType)
    public Connection data(final Map<String, String> data)
    public Connection data(final String... keyvals)
    public Connection data(final Collection<Connection.KeyVal> data)
    public Request data(final Connection.KeyVal keyval)
    '''
def sslSocketFactory():
    '''public Connection sslSocketFactory(final SSLSocketFactory sslSocketFactory)
    public SSLSocketFactory sslSocketFactory()
    public void sslSocketFactory(final SSLSocketFactory sslSocketFactory)
    '''
def requestBody():
    '''public Connection requestBody(final String body)
    public String requestBody()
    '''
def header():
    '''public Connection header(final String name, final String value)
    public String header(final String name)
    public T header(final String name, final String value)
    '''
def headers():
    '''public Connection headers(final Map<String, String> headers)
    public List<String> headers(final String name)
    public Map<String, String> headers()
    '''
def cookie():
    '''public Connection cookie(final String name, final String value)
    public String cookie(final String name)
    public T cookie(final String name, final String value)
    '''
def cookies():
    '''public Connection cookies(final Map<String, String> cookies)
    public Map<String, String> cookies()
    '''
def parser():
    '''public Connection parser(final Parser parser)
    public Request parser(final Parser parser)
    public Parser parser()
    '''
def get():
    '''public Document get()
    '''
def post():
    '''public Document post()
    '''
def request():
    '''public Connection request(final Connection.Request request)
    '''
def response():
    '''public Connection response(final Connection.Response response)
    '''
def postDataCharset():
    '''public Connection postDataCharset(final String charset)
    public String postDataCharset()
    '''
def addHeader():
    '''public T addHeader(final String name, String value)
    '''
def hasHeader():
    '''public boolean hasHeader(final String name)
    '''
def hasHeaderWithValue():
    '''public boolean hasHeaderWithValue(final String name, final String value)
    '''
def removeHeader():
    '''public T removeHeader(final String name)
    '''
def multiHeaders():
    '''public Map<String, List<String>> multiHeaders()
    '''
def hasCookie():
    '''public boolean hasCookie(final String name)
    '''
def removeCookie():
    '''public T removeCookie(final String name)
    '''
def statusCode():
    '''public int statusCode()
    '''
def statusMessage():
    '''public String statusMessage()
    '''
def charset():
    '''public String charset()
    public Response charset(final String charset)
    '''
def contentType():
    '''public String contentType()
    public String contentType()
    '''
def parse():
    '''public Document parse()
    '''
def body():
    '''public String body()
    '''
def bodyAsBytes():
    '''public byte[] bodyAsBytes()
    '''
def bodyStream():
    '''public BufferedInputStream bodyStream()
    '''
def create():
    '''public static KeyVal create(final String key, final String value)
    public static KeyVal create(final String key, final String filename, final InputStream stream)
    '''
def key():
    '''public KeyVal key(final String key)
    public String key()
    '''
def value():
    '''public KeyVal value(final String value)
    public String value()
    '''
def inputStream():
    '''public KeyVal inputStream(final InputStream inputStream)
    public InputStream inputStream()
    '''
def hasInputStream():
    '''public boolean hasInputStream()
    '''
def toString():
    '''public String toString()
    '''
