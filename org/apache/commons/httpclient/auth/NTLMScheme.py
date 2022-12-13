def NTLMScheme():
    '''public NTLMScheme()
    public NTLMScheme(final String challenge)
    '''
def processChallenge():
    '''public void processChallenge(final String challenge)
    '''
def isComplete():
    '''public boolean isComplete()
    '''
def getSchemeName():
    '''public String getSchemeName()
    '''
def getRealm():
    '''public String getRealm()
    '''
def getID():
    '''public String getID()
    '''
def getParameter():
    '''public String getParameter(final String name)
    '''
def isConnectionBased():
    '''public boolean isConnectionBased()
    '''
def authenticate():
    '''public static String authenticate(final NTCredentials credentials, final String challenge)
    public static String authenticate(final NTCredentials credentials, final String challenge, final String charset)
    public String authenticate(final Credentials credentials, final String method, final String uri)
    public String authenticate(final Credentials credentials, final HttpMethod method)
    '''
