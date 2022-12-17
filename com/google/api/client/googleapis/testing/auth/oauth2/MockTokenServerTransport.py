def ():
    '''returns MockTokenServerTransport\n\n
    ()\n
    (final String tokenServerUrl)\n
    '''
def addServiceAccount():
    '''returns None\n\n
    addServiceAccount(final String email, final String accessToken)\n
    '''
def addClient():
    '''returns None\n\n
    addClient(final String clientId, final String clientSecret)\n
    '''
def addRefreshToken():
    '''returns None\n\n
    addRefreshToken(final String refreshToken, final String accessTokenToReturn)\n
    '''
def buildRequest():
    '''returns LowLevelHttpRequest\n\n
    buildRequest(final String method, final String url)\n
    '''
def execute():
    '''returns LowLevelHttpResponse\n\n
    execute()\n
    '''
