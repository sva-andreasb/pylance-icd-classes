AUTH_SCHEME = "String  \"OAuth\""
GET = "String  \"GET\""
POST = "String  \"POST\""
PUT = "String  \"PUT\""
DELETE = "String  \"DELETE\""
def OAuthMessage():
    '''    public OAuthMessage(final String method, final String URL, final Collection<? extends Map.Entry> parameters)
    public OAuthMessage(final String method, final String URL, final Collection<? extends Map.Entry> parameters, final InputStream bodyAsStream)
    '''
def toString():
    '''    public String toString()
    '''
def addParameter():
    '''    public void addParameter(final String key, final String value)
    public void addParameter(final Map.Entry<String, String> parameter)
    '''
def addParameters():
    '''    public void addParameters(final Collection<? extends Map.Entry<String, String>> parameters)
    '''
def getParameter():
    '''    public String getParameter(final String name)
    '''
def getConsumerKey():
    '''    public String getConsumerKey()
    '''
def getToken():
    '''    public String getToken()
    '''
def getSignatureMethod():
    '''    public String getSignatureMethod()
    '''
def getSignature():
    '''    public String getSignature()
    '''
def getBodyType():
    '''    public String getBodyType()
    '''
def getBodyEncoding():
    '''    public String getBodyEncoding()
    '''
def getHeader():
    '''    public final String getHeader(final String name)
    '''
def readBodyAsString():
    '''    public final String readBodyAsString()
    '''
def getBodyAsStream():
    '''    public InputStream getBodyAsStream()
    '''
def getDump():
    '''    public Map<String, Object> getDump()
    '''
def requireParameters():
    '''    public void requireParameters(final String... names)
    '''
def addRequiredParameters():
    '''    public void addRequiredParameters(final OAuthAccessor accessor)
    '''
def sign():
    '''    public void sign(final OAuthAccessor accessor)
    '''
def getAuthorizationHeader():
    '''    public String getAuthorizationHeader(final String realm)
    '''
def readAll():
    '''    public static String readAll(final InputStream from, final String encoding)
    '''
