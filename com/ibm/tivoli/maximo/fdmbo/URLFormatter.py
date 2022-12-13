def URLFormatter():
    '''public URLFormatter()
    public URLFormatter(final String nullFormat, final String stringQualifier)
    '''
def setContext():
    '''public void setContext(final Map<String, Object> ctx)
    '''
def format():
    '''public String format(final String url, final MboRemote mbo)
    public String format(final String url, final MboRemote mbo, final String relationship, final String resourceType)
    public String format(final String url, final MboRemote mbo, final UserInfo userInfo, final String relationship, final String resourceType, final JSONAnalyzer jsonAnalyzer)
    '''
def replaceToken():
    '''public String replaceToken(final String fullUrl, final String urlQ, final MboRemote mbo, final String resourceType, final String relationship, final boolean pathToken)
    '''
def encode():
    '''public static String encode(String token, final boolean pathToken)
    '''
def decode():
    '''public static String decode(String token)
    '''
