AUTH_SCHEME = "String  \"OAuth\""
GET = "String  \"GET\""
POST = "String  \"POST\""
PUT = "String  \"PUT\""
DELETE = "String  \"DELETE\""
def ():
    '''returns OAuthMessage\n\n
    (final String method, final String URL, final Collection<? extends Map.Entry> parameters)\n
    (final String method, final String URL, final Collection<? extends Map.Entry> parameters, final InputStream bodyAsStream)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addParameter():
    '''returns None\n\n
    addParameter(final String key, final String value)\n
    addParameter(final Map.Entry<String, String> parameter)\n
    '''
def addParameters():
    '''returns None\n\n
    addParameters(final Collection<? extends Map.Entry<String, String>> parameters)\n
    '''
def getParameter():
    '''returns String\n\n
    getParameter(final String name)\n
    '''
def getConsumerKey():
    '''returns String\n\n
    getConsumerKey()\n
    '''
def getToken():
    '''returns String\n\n
    getToken()\n
    '''
def getSignatureMethod():
    '''returns String\n\n
    getSignatureMethod()\n
    '''
def getSignature():
    '''returns String\n\n
    getSignature()\n
    '''
def getBodyType():
    '''returns String\n\n
    getBodyType()\n
    '''
def getBodyEncoding():
    '''returns String\n\n
    getBodyEncoding()\n
    '''
def getBodyAsStream():
    '''returns InputStream\n\n
    getBodyAsStream()\n
    '''
def requireParameters():
    '''returns None\n\n
    requireParameters(final String... names)\n
    '''
def addRequiredParameters():
    '''returns None\n\n
    addRequiredParameters(final OAuthAccessor accessor)\n
    '''
def sign():
    '''returns None\n\n
    sign(final OAuthAccessor accessor)\n
    '''
def getAuthorizationHeader():
    '''returns String\n\n
    getAuthorizationHeader(final String realm)\n
    '''
