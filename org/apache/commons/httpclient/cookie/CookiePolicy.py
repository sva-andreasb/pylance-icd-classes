BROWSER_COMPATIBILITY = "String  compatibility""
NETSCAPE = "String  netscape""
RFC_2109 = "String  rfc2109""
RFC_2965 = "String  rfc2965""
IGNORE_COOKIES = "String  ignoreCookies""
DEFAULT = "String  default""
COMPATIBILITY = "int  0"
NETSCAPE_DRAFT = "int  1"
RFC2109 = "int  2"
RFC2965 = "int  3"
def registerCookieSpec():
'''public static void registerCookieSpec(final String id, final Class clazz)
'''
pass
def unregisterCookieSpec():
'''public static void unregisterCookieSpec(final String id)
'''
pass
def getCookieSpec():
'''public static CookieSpec getCookieSpec(final String id)
'''
pass
def getDefaultPolicy():
'''public static int getDefaultPolicy()
'''
pass
def setDefaultPolicy():
'''public static void setDefaultPolicy(final int policy)
'''
pass
def getSpecByPolicy():
'''public static CookieSpec getSpecByPolicy(final int policy)
'''
pass
def getDefaultSpec():
'''public static CookieSpec getDefaultSpec()
'''
pass
def getSpecByVersion():
'''public static CookieSpec getSpecByVersion(final int ver)
'''
pass
def getCompatibilitySpec():
'''public static CookieSpec getCompatibilitySpec()
'''
pass
def getRegisteredCookieSpecs():
'''public static String[] getRegisteredCookieSpecs()
'''
pass
