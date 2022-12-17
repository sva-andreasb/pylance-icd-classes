PARAMETER_STYLE = "String  \"parameterStyle\""
ACCEPT_ENCODING = "String  \"HTTP.header.Accept-Encoding\""
def ():
    '''returns OAuthClient\n\n
    (final HttpClient http)\n
    '''
def setHttpClient():
    '''returns None\n\n
    setHttpClient(final HttpClient http)\n
    '''
def getHttpClient():
    '''returns HttpClient\n\n
    getHttpClient()\n
    '''
def getRequestToken():
    '''returns None\n\n
    getRequestToken(final OAuthAccessor accessor)\n
    getRequestToken(final OAuthAccessor accessor, final String httpMethod)\n
    getRequestToken(final OAuthAccessor accessor, final String httpMethod, final Collection<? extends Map.Entry> parameters)\n
    '''
def getRequestTokenResponse():
    '''returns OAuthMessage\n\n
    getRequestTokenResponse(final OAuthAccessor accessor, final String httpMethod, Collection<? extends Map.Entry> parameters)\n
    '''
def getAccessToken():
    '''returns OAuthMessage\n\n
    getAccessToken(final OAuthAccessor accessor, final String httpMethod, Collection<? extends Map.Entry> parameters)\n
    '''
def invoke():
    '''returns OAuthMessage\n\n
    invoke(final OAuthAccessor accessor, final String httpMethod, final String url, final Collection<? extends Map.Entry> parameters)\n
    invoke(final OAuthAccessor accessor, final String url, final Collection<? extends Map.Entry> parameters)\n
    invoke(final OAuthMessage request, final ParameterStyle style)\n
    '''
def access():
    '''returns OAuthResponseMessage\n\n
    access(final OAuthMessage request, final ParameterStyle style)\n
    '''
