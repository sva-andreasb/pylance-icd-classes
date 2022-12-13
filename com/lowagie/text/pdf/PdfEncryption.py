def PdfEncryption():
    '''public PdfEncryption()
    '''
def setupAllKeys():
    '''public void setupAllKeys(final byte[] userPassword, byte[] ownerPassword, int permissions, final boolean strength128Bits)
    '''
def createDocumentId():
    '''public static byte[] createDocumentId()
    '''
def setupByUserPassword():
    '''public void setupByUserPassword(final byte[] documentID, final byte[] userPassword, final byte[] ownerKey, final int permissions, final boolean strength128Bits)
    '''
def setupByOwnerPassword():
    '''public void setupByOwnerPassword(final byte[] documentID, final byte[] ownerPassword, final byte[] userKey, final byte[] ownerKey, final int permissions, final boolean strength128Bits)
    '''
def prepareKey():
    '''public void prepareKey()
    '''
def setHashKey():
    '''public void setHashKey(final int number, final int generation)
    '''
def createInfoId():
    '''public static PdfObject createInfoId(final byte[] id)
    '''
def getEncryptionDictionary():
    '''public PdfDictionary getEncryptionDictionary()
    '''
def prepareRC4Key():
    '''public void prepareRC4Key(final byte[] key)
    public void prepareRC4Key(final byte[] key, final int off, final int len)
    '''
def encryptRC4():
    '''public void encryptRC4(final byte[] dataIn, final int off, final int len, final byte[] dataOut)
    public void encryptRC4(final byte[] data, final int off, final int len)
    public void encryptRC4(final byte[] dataIn, final byte[] dataOut)
    public void encryptRC4(final byte[] data)
    '''
def getFileID():
    '''public PdfObject getFileID()
    '''
