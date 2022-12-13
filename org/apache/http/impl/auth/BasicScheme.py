def BasicScheme():
    '''public BasicScheme(final Charset credentialsCharset)
    public BasicScheme(final ChallengeState challengeState)
    public BasicScheme()
    '''
def getSchemeName():
    '''public String getSchemeName()
    '''
def processChallenge():
    '''public void processChallenge(final Header header)
    '''
def isComplete():
    '''public boolean isComplete()
    '''
def isConnectionBased():
    '''public boolean isConnectionBased()
    '''
def authenticate():
    '''public Header authenticate(final Credentials credentials, final HttpRequest request)
    public Header authenticate(final Credentials credentials, final HttpRequest request, final HttpContext context)
    public static Header authenticate(final Credentials credentials, final String charset, final boolean proxy)
    '''
def toString():
    '''public String toString()
    '''
