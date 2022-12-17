def ():
    '''returns URLFormatter\n\n
    ()\n
    (final String nullFormat, final String stringQualifier)\n
    '''
def setContext():
    '''returns None\n\n
    setContext(final Map<String, Object> ctx)\n
    '''
def format():
    '''returns String\n\n
    format(final String url, final MboRemote mbo)\n
    format(final String url, final MboRemote mbo, final String relationship, final String resourceType)\n
    format(final String url, final MboRemote mbo, final UserInfo userInfo, final String relationship, final String resourceType, final JSONAnalyzer jsonAnalyzer)\n
    '''
def replaceToken():
    '''returns String\n\n
    replaceToken(final String fullUrl, final String urlQ, final MboRemote mbo, final String resourceType, final String relationship, final boolean pathToken)\n
    '''
