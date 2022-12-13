PARAMETER_STYLE = "String  parameterStyle""
ACCEPT_ENCODING = "String  HTTP.header.Accept-Encoding""
def OAuthClient():
'''public OAuthClient(final HttpClient http)
'''
pass
def setHttpClient():
'''public void setHttpClient(final HttpClient http)
'''
pass
def getHttpClient():
'''public HttpClient getHttpClient()
'''
pass
def getHttpParameters():
'''public Map<String, Object> getHttpParameters()
'''
pass
def getRequestToken():
'''public void getRequestToken(final OAuthAccessor accessor)
public void getRequestToken(final OAuthAccessor accessor, final String httpMethod)
public void getRequestToken(final OAuthAccessor accessor, final String httpMethod, final Collection<? extends Map.Entry> parameters)
'''
pass
def getRequestTokenResponse():
'''public OAuthMessage getRequestTokenResponse(final OAuthAccessor accessor, final String httpMethod, Collection<? extends Map.Entry> parameters)
'''
pass
def getAccessToken():
'''public OAuthMessage getAccessToken(final OAuthAccessor accessor, final String httpMethod, Collection<? extends Map.Entry> parameters)
'''
pass
def invoke():
'''public OAuthMessage invoke(final OAuthAccessor accessor, final String httpMethod, final String url, final Collection<? extends Map.Entry> parameters)
public OAuthMessage invoke(final OAuthAccessor accessor, final String url, final Collection<? extends Map.Entry> parameters)
public OAuthMessage invoke(final OAuthMessage request, final ParameterStyle style)
'''
pass
def access():
'''public OAuthResponseMessage access(final OAuthMessage request, final ParameterStyle style)
'''
pass
