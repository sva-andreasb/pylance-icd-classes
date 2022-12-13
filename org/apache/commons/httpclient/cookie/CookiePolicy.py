BROWSER_COMPATIBILITY = "String  \"compatibility\""
NETSCAPE = "String  \"netscape\""
RFC_2109 = "String  \"rfc2109\""
RFC_2965 = "String  \"rfc2965\""
IGNORE_COOKIES = "String  \"ignoreCookies\""
DEFAULT = "String  \"default\""
COMPATIBILITY = "int  0"
NETSCAPE_DRAFT = "int  1"
RFC2109 = "int  2"
RFC2965 = "int  3"
def registerCookieSpec():
    '''public static void registerCookieSpec(final String id, final Class clazz)
    '''
def unregisterCookieSpec():
    '''public static void unregisterCookieSpec(final String id)
    '''
def getCookieSpec():
    '''public static CookieSpec getCookieSpec(final String id)
    '''
def getDefaultPolicy():
    '''public static int getDefaultPolicy()
    '''
def setDefaultPolicy():
    '''public static void setDefaultPolicy(final int policy)
    '''
def getSpecByPolicy():
    '''public static CookieSpec getSpecByPolicy(final int policy)
    '''
def getDefaultSpec():
    '''public static CookieSpec getDefaultSpec()
    '''
def getSpecByVersion():
    '''public static CookieSpec getSpecByVersion(final int ver)
    '''
def getCompatibilitySpec():
    '''public static CookieSpec getCompatibilitySpec()
    '''
def getRegisteredCookieSpecs():
    '''public static String[] getRegisteredCookieSpecs()
    '''
