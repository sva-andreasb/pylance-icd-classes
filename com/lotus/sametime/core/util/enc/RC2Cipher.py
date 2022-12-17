RC2_128_KEY_LENGTH = "int  16"
RC2_40_KEY_LENGTH = "int  5"
ENCRYPT_MODE = "int  0"
DECRYPT_MODE = "int  1"
def ():
    '''returns RC2Cipher\n\n
    ()\n
    '''
def getBlockSize():
    '''returns int\n\n
    getBlockSize()\n
    '''
def getOutputSize():
    '''returns int\n\n
    getOutputSize(final int n)\n
    '''
def init():
    '''returns None\n\n
    init(final int cipher_Mode, final byte[] array)\n
    '''
def setIV():
    '''returns None\n\n
    setIV(final byte[] array)\n
    '''
def getIV():
    '''returns byte[]\n\n
    getIV()\n
    '''
def doFinal():
    '''returns byte[]\n\n
    doFinal(final byte[] array)\n
    '''
