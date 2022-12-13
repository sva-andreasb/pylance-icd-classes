CONTENT_ENCODING = "String  Content-Encoding""
DEFAULT_UA = "String  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36""
CONTENT_TYPE = "String  Content-Type""
MULTIPART_FORM_DATA = "String  multipart/form-data""
FORM_URL_ENCODED = "String  application/x-www-form-urlencoded""
def connect():
'''public static Connection connect(final String url)
public static Connection connect(final URL url)
'''
pass
def HttpConnection():
'''public HttpConnection()
'''
pass
def url():
'''public Connection url(final URL url)
public Connection url(final String url)
public URL url()
public T url(final URL url)
'''
pass
def proxy():
'''public Connection proxy(final Proxy proxy)
public Connection proxy(final String host, final int port)
public Proxy proxy()
public Request proxy(final Proxy proxy)
public Request proxy(final String host, final int port)
'''
pass
def userAgent():
'''public Connection userAgent(final String userAgent)
'''
pass
def timeout():
'''public Connection timeout(final int millis)
public int timeout()
public Request timeout(final int millis)
'''
pass
def maxBodySize():
'''public Connection maxBodySize(final int bytes)
public int maxBodySize()
'''
pass
def followRedirects():
'''public Connection followRedirects(final boolean followRedirects)
public boolean followRedirects()
'''
pass
def referrer():
'''public Connection referrer(final String referrer)
'''
pass
def method():
'''public Connection method(final Method method)
public Method method()
public T method(final Method method)
'''
pass
def ignoreHttpErrors():
'''public Connection ignoreHttpErrors(final boolean ignoreHttpErrors)
public boolean ignoreHttpErrors()
'''
pass
def ignoreContentType():
'''public Connection ignoreContentType(final boolean ignoreContentType)
public boolean ignoreContentType()
'''
pass
def data():
'''public Connection data(final String key, final String value)
public Connection data(final String key, final String filename, final InputStream inputStream)
public Connection data(final String key, final String filename, final InputStream inputStream, final String contentType)
public Connection data(final Map<String, String> data)
public Connection data(final String... keyvals)
public Connection data(final Collection<Connection.KeyVal> data)
public Request data(final Connection.KeyVal keyval)
'''
pass
def sslSocketFactory():
'''public Connection sslSocketFactory(final SSLSocketFactory sslSocketFactory)
public SSLSocketFactory sslSocketFactory()
public void sslSocketFactory(final SSLSocketFactory sslSocketFactory)
'''
pass
def requestBody():
'''public Connection requestBody(final String body)
public String requestBody()
'''
pass
def header():
'''public Connection header(final String name, final String value)
public String header(final String name)
public T header(final String name, final String value)
'''
pass
def headers():
'''public Connection headers(final Map<String, String> headers)
public List<String> headers(final String name)
public Map<String, String> headers()
'''
pass
def cookie():
'''public Connection cookie(final String name, final String value)
public String cookie(final String name)
public T cookie(final String name, final String value)
'''
pass
def cookies():
'''public Connection cookies(final Map<String, String> cookies)
public Map<String, String> cookies()
'''
pass
def parser():
'''public Connection parser(final Parser parser)
public Request parser(final Parser parser)
public Parser parser()
'''
pass
def get():
'''public Document get()
'''
pass
def post():
'''public Document post()
'''
pass
def request():
'''public Connection request(final Connection.Request request)
'''
pass
def response():
'''public Connection response(final Connection.Response response)
'''
pass
def postDataCharset():
'''public Connection postDataCharset(final String charset)
public String postDataCharset()
'''
pass
def addHeader():
'''public T addHeader(final String name, String value)
'''
pass
def hasHeader():
'''public boolean hasHeader(final String name)
'''
pass
def hasHeaderWithValue():
'''public boolean hasHeaderWithValue(final String name, final String value)
'''
pass
def removeHeader():
'''public T removeHeader(final String name)
'''
pass
def multiHeaders():
'''public Map<String, List<String>> multiHeaders()
'''
pass
def hasCookie():
'''public boolean hasCookie(final String name)
'''
pass
def removeCookie():
'''public T removeCookie(final String name)
'''
pass
def statusCode():
'''public int statusCode()
'''
pass
def statusMessage():
'''public String statusMessage()
'''
pass
def charset():
'''public String charset()
public Response charset(final String charset)
'''
pass
def contentType():
'''public String contentType()
public String contentType()
'''
pass
def parse():
'''public Document parse()
'''
pass
def body():
'''public String body()
'''
pass
def bodyAsBytes():
'''public byte[] bodyAsBytes()
'''
pass
def bodyStream():
'''public BufferedInputStream bodyStream()
'''
pass
def create():
'''public static KeyVal create(final String key, final String value)
public static KeyVal create(final String key, final String filename, final InputStream stream)
'''
pass
def key():
'''public KeyVal key(final String key)
public String key()
'''
pass
def value():
'''public KeyVal value(final String value)
public String value()
'''
pass
def inputStream():
'''public KeyVal inputStream(final InputStream inputStream)
public InputStream inputStream()
'''
pass
def hasInputStream():
'''public boolean hasInputStream()
'''
pass
def toString():
'''public String toString()
'''
pass
