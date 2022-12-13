def Base64():
    '''    public Base64()
    public Base64(final boolean urlSafe)
    public Base64(final int lineLength)
    public Base64(final int lineLength, final byte[] lineSeparator)
    public Base64(final int lineLength, final byte[] lineSeparator, final boolean urlSafe)
    '''
def isUrlSafe():
    '''    public boolean isUrlSafe()
    '''
def isArrayByteBase64():
    '''    public static boolean isArrayByteBase64(final byte[] arrayOctet)
    '''
def isBase64():
    '''    public static boolean isBase64(final byte octet)
    public static boolean isBase64(final String base64)
    public static boolean isBase64(final byte[] arrayOctet)
    '''
def encodeBase64():
    '''    public static byte[] encodeBase64(final byte[] binaryData)
    public static byte[] encodeBase64(final byte[] binaryData, final boolean isChunked)
    public static byte[] encodeBase64(final byte[] binaryData, final boolean isChunked, final boolean urlSafe)
    public static byte[] encodeBase64(final byte[] binaryData, final boolean isChunked, final boolean urlSafe, final int maxResultSize)
    '''
def encodeBase64String():
    '''    public static String encodeBase64String(final byte[] binaryData)
    '''
def encodeBase64URLSafe():
    '''    public static byte[] encodeBase64URLSafe(final byte[] binaryData)
    '''
def encodeBase64URLSafeString():
    '''    public static String encodeBase64URLSafeString(final byte[] binaryData)
    '''
def encodeBase64Chunked():
    '''    public static byte[] encodeBase64Chunked(final byte[] binaryData)
    '''
def decodeBase64():
    '''    public static byte[] decodeBase64(final String base64String)
    public static byte[] decodeBase64(final byte[] base64Data)
    '''
def decodeInteger():
    '''    public static BigInteger decodeInteger(final byte[] pArray)
    '''
def encodeInteger():
    '''    public static byte[] encodeInteger(final BigInteger bigInt)
    '''
