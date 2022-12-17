DEFAULT_PASSWORD = "String  \"VelvetSweatshop\""
DEFAULT_POIFS_ENTRY = "String  \"EncryptedPackage\""
def getDataStream():
    '''returns InputStream\n\n
    getDataStream(final InputStream stream, final int size, final int initialPos)\n
    getDataStream(final NPOIFSFileSystem fs)\n
    getDataStream(final OPOIFSFileSystem fs)\n
    getDataStream(final POIFSFileSystem fs)\n
    '''
def setChunkSize():
    '''returns None\n\n
    setChunkSize(final int chunkSize)\n
    '''
def initCipherForBlock():
    '''returns Cipher\n\n
    initCipherForBlock(final Cipher cipher, final int block)\n
    '''
def getVerifier():
    '''returns byte[]\n\n
    getVerifier()\n
    '''
def getSecretKey():
    '''returns SecretKey\n\n
    getSecretKey()\n
    '''
def getIntegrityHmacKey():
    '''returns byte[]\n\n
    getIntegrityHmacKey()\n
    '''
def getIntegrityHmacValue():
    '''returns byte[]\n\n
    getIntegrityHmacValue()\n
    '''
def getEncryptionInfo():
    '''returns EncryptionInfo\n\n
    getEncryptionInfo()\n
    '''
def setEncryptionInfo():
    '''returns None\n\n
    setEncryptionInfo(final EncryptionInfo encryptionInfo)\n
    '''
def clone():
    '''returns Decryptor\n\n
    clone()\n
    '''
