ENC_TYPE_RC2_40 = "short  0"
ENC_TYPE_RC2_128 = "short  1"
ENC_ERR_CODE_OK = "int  0"
ENC_ERR_CODE_NOT_INITIALIZED = "int  1"
ENC_ERR_CODE_TOO_WEAK = "int  2"
ENC_ERR_CODE_BAD_ARG = "int  3"
ENC_ERR_CODE_NO_METHOD = "int  4"
def createRequest():
    '''public static int createRequest(final EncData encData)
    '''
def localizeRequest():
    '''public static int localizeRequest(EncLevel encLevel, final EncData encData)
    '''
def localizeReply():
    '''public static int localizeReply(final EncLevel encLevel, final EncData encData)
    '''
def encrypt():
    '''public static byte[] encrypt(final byte[] array, final EncData encData)
    '''
def decrypt():
    '''public static byte[] decrypt(final byte[] array, final EncData encData)
    '''
def getEncMethod():
    '''public static EncMethod getEncMethod(final int n)
    '''
def getEncError():
    '''public static int getEncError()
    '''
