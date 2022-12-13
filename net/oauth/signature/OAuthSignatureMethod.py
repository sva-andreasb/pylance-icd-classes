_ACCESSOR = "String  \"-Accessor\""
def sign():
    '''    public void sign(final OAuthMessage message)
    '''
def validate():
    '''    public void validate(final OAuthMessage message)
    '''
def getTokenSecret():
    '''    public String getTokenSecret()
    '''
def setTokenSecret():
    '''    public void setTokenSecret(final String tokenSecret)
    '''
def getBaseString():
    '''    public static String getBaseString(final OAuthMessage message)
    '''
def equals():
    '''    public static boolean equals(final String x, final String y)
    public static boolean equals(final byte[] a, final byte[] b)
    '''
def decodeBase64():
    '''    public static byte[] decodeBase64(final String s)
    '''
def base64Encode():
    '''    public static String base64Encode(final byte[] b)
    '''
def newSigner():
    '''    public static OAuthSignatureMethod newSigner(final OAuthMessage message, final OAuthAccessor accessor)
    '''
def newMethod():
    '''    public static OAuthSignatureMethod newMethod(final String name, final OAuthAccessor accessor)
    '''
def registerMethodClass():
    '''    public static void registerMethodClass(final String name, final Class clazz)
    '''
def unregisterMethod():
    '''    public static void unregisterMethod(final String name)
    '''
def compareTo():
    '''    public int compareTo(final ComparableParameter that)
    '''
def toString():
    '''    public String toString()
    '''
