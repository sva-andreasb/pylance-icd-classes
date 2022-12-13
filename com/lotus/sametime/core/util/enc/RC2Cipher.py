RC2_128_KEY_LENGTH = "int  16"
RC2_40_KEY_LENGTH = "int  5"
ENCRYPT_MODE = "int  0"
DECRYPT_MODE = "int  1"
def getInstance():
    '''    public static RC2Cipher getInstance(final String s)
    '''
def RC2Cipher():
    '''    public RC2Cipher()
    '''
def getBlockSize():
    '''    public int getBlockSize()
    '''
def getOutputSize():
    '''    public int getOutputSize(final int n)
    '''
def init():
    '''    public void init(final int cipher_Mode, final byte[] array)
    '''
def setIV():
    '''    public void setIV(final byte[] array)
    '''
def getIV():
    '''    public byte[] getIV()
    '''
def doFinal():
    '''    public byte[] doFinal(final byte[] array)
    '''
def encryptOT():
    '''    public static byte[] encryptOT(final byte[] array, final byte[] array2, final int n)
    '''
def decryptOT():
    '''    public static byte[] decryptOT(final byte[] array, final byte[] array2, final int n)
    '''
