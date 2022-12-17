def ():
    '''returns HttpAuthenticator\n\n
    (final Log log)\n
    ()\n
    '''
def isAuthenticationRequested():
    '''returns boolean\n\n
    isAuthenticationRequested(final HttpHost host, final HttpResponse response, final AuthenticationStrategy authStrategy, final AuthState authState, final HttpContext context)\n
    '''
def handleAuthChallenge():
    '''returns boolean\n\n
    handleAuthChallenge(final HttpHost host, final HttpResponse response, final AuthenticationStrategy authStrategy, final AuthState authState, final HttpContext context)\n
    '''
def generateAuthResponse():
    '''returns None\n\n
    generateAuthResponse(final HttpRequest request, final AuthState authState, final HttpContext context)\n
    '''
