AUTH_SCHEME = "String  OAuth""
GET = "String  GET""
POST = "String  POST""
PUT = "String  PUT""
DELETE = "String  DELETE""
def OAuthMessage():
'''public OAuthMessage(final String method, final String URL, final Collection<? extends Map.Entry> parameters)
public OAuthMessage(final String method, final String URL, final Collection<? extends Map.Entry> parameters, final InputStream bodyAsStream)
'''
pass
def toString():
'''public String toString()
'''
pass
def addParameter():
'''public void addParameter(final String key, final String value)
public void addParameter(final Map.Entry<String, String> parameter)
'''
pass
def addParameters():
'''public void addParameters(final Collection<? extends Map.Entry<String, String>> parameters)
'''
pass
def getParameter():
'''public String getParameter(final String name)
'''
pass
def getConsumerKey():
'''public String getConsumerKey()
'''
pass
def getToken():
'''public String getToken()
'''
pass
def getSignatureMethod():
'''public String getSignatureMethod()
'''
pass
def getSignature():
'''public String getSignature()
'''
pass
def getBodyType():
'''public String getBodyType()
'''
pass
def getBodyEncoding():
'''public String getBodyEncoding()
'''
pass
def getHeader():
'''public final String getHeader(final String name)
'''
pass
def readBodyAsString():
'''public final String readBodyAsString()
'''
pass
def getBodyAsStream():
'''public InputStream getBodyAsStream()
'''
pass
def getDump():
'''public Map<String, Object> getDump()
'''
pass
def requireParameters():
'''public void requireParameters(final String... names)
'''
pass
def addRequiredParameters():
'''public void addRequiredParameters(final OAuthAccessor accessor)
'''
pass
def sign():
'''public void sign(final OAuthAccessor accessor)
'''
pass
def getAuthorizationHeader():
'''public String getAuthorizationHeader(final String realm)
'''
pass
def readAll():
'''public static String readAll(final InputStream from, final String encoding)
'''
pass
