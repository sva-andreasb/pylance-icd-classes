def getOAuthConsumer():
    '''public static OAuthConsumer getOAuthConsumer(final String endPointName, final HttpServletRequest request)
    '''
def getAccessor():
    '''public static OAuthAccessor getAccessor(final HttpServletRequest request, final HttpServletResponse response, final OAuthConsumer consumer)
    '''
def newAccessor():
    '''public static OAuthAccessor newAccessor(final OAuthConsumer consumer, final CookieMap cookies)
    '''
def getAccessToken():
    '''public static void getAccessToken(final HttpServletRequest request, final CookieMap cookies, final OAuthAccessor accessor)
    '''
def handleException():
    '''public static void handleException(final Exception e, final HttpServletRequest request, final HttpServletResponse response, final OAuthConsumer consumer)
    '''
