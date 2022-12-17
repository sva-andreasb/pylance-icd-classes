def ():
    '''returns PdfEncryption\n\n
    ()\n
    '''
def setupAllKeys():
    '''returns None\n\n
    setupAllKeys(final byte[] userPassword, byte[] ownerPassword, int permissions, final boolean strength128Bits)\n
    '''
def setupByUserPassword():
    '''returns None\n\n
    setupByUserPassword(final byte[] documentID, final byte[] userPassword, final byte[] ownerKey, final int permissions, final boolean strength128Bits)\n
    '''
def setupByOwnerPassword():
    '''returns None\n\n
    setupByOwnerPassword(final byte[] documentID, final byte[] ownerPassword, final byte[] userKey, final byte[] ownerKey, final int permissions, final boolean strength128Bits)\n
    '''
def prepareKey():
    '''returns None\n\n
    prepareKey()\n
    '''
def setHashKey():
    '''returns None\n\n
    setHashKey(final int number, final int generation)\n
    '''
def getEncryptionDictionary():
    '''returns PdfDictionary\n\n
    getEncryptionDictionary()\n
    '''
def prepareRC4Key():
    '''returns None\n\n
    prepareRC4Key(final byte[] key)\n
    prepareRC4Key(final byte[] key, final int off, final int len)\n
    '''
def encryptRC4():
    '''returns None\n\n
    encryptRC4(final byte[] dataIn, final int off, final int len, final byte[] dataOut)\n
    encryptRC4(final byte[] data, final int off, final int len)\n
    encryptRC4(final byte[] dataIn, final byte[] dataOut)\n
    encryptRC4(final byte[] data)\n
    '''
def getFileID():
    '''returns PdfObject\n\n
    getFileID()\n
    '''
