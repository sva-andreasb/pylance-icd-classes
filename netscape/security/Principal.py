CODEBASE_EXACT = "int  1"
CODEBASE_REGEXP = "int  2"
CERT = "int  3"
CERT_FINGERPRINT = "int  4"
CERT_KEY = "int  5"
def Principal():
    '''    public Principal()
    public Principal(final URL url)
    public Principal(final int type, final String s)
    public Principal(final int type, final byte[] array)
    public Principal(final int type, final byte[] array, final Class clazz)
    '''
def isCodebase():
    '''    public boolean isCodebase()
    '''
def isCodebaseExact():
    '''    public boolean isCodebaseExact()
    '''
def isCodebaseRegexp():
    '''    public boolean isCodebaseRegexp()
    '''
def isCert():
    '''    public boolean isCert()
    '''
def isCertFingerprint():
    '''    public boolean isCertFingerprint()
    '''
def toVerboseString():
    '''    public String toVerboseString()
    '''
def getVendor():
    '''    public String getVendor()
    '''
def toVerboseHtml():
    '''    public String toVerboseHtml()
    '''
def getNickname():
    '''    public String getNickname()
    '''
def isSystemPrincipal():
    '''    public boolean isSystemPrincipal()
    '''
def getZigPtr():
    '''    public static int getZigPtr(final Class clazz)
    '''
