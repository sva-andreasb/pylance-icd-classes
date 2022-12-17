CODEBASE_EXACT = "int  1"
CODEBASE_REGEXP = "int  2"
CERT = "int  3"
CERT_FINGERPRINT = "int  4"
CERT_KEY = "int  5"
def ():
    '''returns Principal\n\n
    ()\n
    (final URL url)\n
    (final int type, final String s)\n
    (final int type, final byte[] array)\n
    (final int type, final byte[] array, final Class clazz)\n
    '''
def isCodebase():
    '''returns boolean\n\n
    isCodebase()\n
    '''
def isCodebaseExact():
    '''returns boolean\n\n
    isCodebaseExact()\n
    '''
def isCodebaseRegexp():
    '''returns boolean\n\n
    isCodebaseRegexp()\n
    '''
def isCert():
    '''returns boolean\n\n
    isCert()\n
    '''
def isCertFingerprint():
    '''returns boolean\n\n
    isCertFingerprint()\n
    '''
def toVerboseString():
    '''returns String\n\n
    toVerboseString()\n
    '''
def getVendor():
    '''returns String\n\n
    getVendor()\n
    '''
def toVerboseHtml():
    '''returns String\n\n
    toVerboseHtml()\n
    '''
def getNickname():
    '''returns String\n\n
    getNickname()\n
    '''
def isSystemPrincipal():
    '''returns boolean\n\n
    isSystemPrincipal()\n
    '''
