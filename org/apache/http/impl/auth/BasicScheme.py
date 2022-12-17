def ():
    '''returns BasicScheme\n\n
    (final Charset credentialsCharset)\n
    (final ChallengeState challengeState)\n
    ()\n
    '''
def getSchemeName():
    '''returns String\n\n
    getSchemeName()\n
    '''
def processChallenge():
    '''returns None\n\n
    processChallenge(final Header header)\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
def isConnectionBased():
    '''returns boolean\n\n
    isConnectionBased()\n
    '''
def authenticate():
    '''returns Header\n\n
    authenticate(final Credentials credentials, final HttpRequest request)\n
    authenticate(final Credentials credentials, final HttpRequest request, final HttpContext context)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
