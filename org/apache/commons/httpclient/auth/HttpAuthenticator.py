WWW_AUTH = "String  \"WWW-Authenticate\""
WWW_AUTH_RESP = "String  \"Authorization\""
PROXY_AUTH = "String  \"Proxy-Authenticate\""
PROXY_AUTH_RESP = "String  \"Proxy-Authorization\""
def selectAuthScheme():
    '''public static AuthScheme selectAuthScheme(final Header[] challenges)
    '''
def authenticateDefault():
    '''public static boolean authenticateDefault(final HttpMethod method, final HttpConnection conn, final HttpState state)
    '''
def authenticateProxyDefault():
    '''public static boolean authenticateProxyDefault(final HttpMethod method, final HttpConnection conn, final HttpState state)
    '''
def authenticate():
    '''public static boolean authenticate(final AuthScheme authscheme, final HttpMethod method, final HttpConnection conn, final HttpState state)
    '''
def authenticateProxy():
    '''public static boolean authenticateProxy(final AuthScheme authscheme, final HttpMethod method, final HttpConnection conn, final HttpState state)
    '''
