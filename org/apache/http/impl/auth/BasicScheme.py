def BasicScheme():
'''public BasicScheme(final Charset credentialsCharset)
public BasicScheme(final ChallengeState challengeState)
public BasicScheme()
'''
pass
def getSchemeName():
'''public String getSchemeName()
'''
pass
def processChallenge():
'''public void processChallenge(final Header header)
'''
pass
def isComplete():
'''public boolean isComplete()
'''
pass
def isConnectionBased():
'''public boolean isConnectionBased()
'''
pass
def authenticate():
'''public Header authenticate(final Credentials credentials, final HttpRequest request)
public Header authenticate(final Credentials credentials, final HttpRequest request, final HttpContext context)
public static Header authenticate(final Credentials credentials, final String charset, final boolean proxy)
'''
pass
def toString():
'''public String toString()
'''
pass
