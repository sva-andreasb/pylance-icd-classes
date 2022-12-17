def ():
    '''returns EncryptionInfo\n\n
    (final POIFSFileSystem fs)\n
    (final OPOIFSFileSystem fs)\n
    (final NPOIFSFileSystem fs)\n
    (final DirectoryNode dir)\n
    (final LittleEndianInput dis, final EncryptionMode preferredEncryptionMode)\n
    (final EncryptionMode encryptionMode)\n
    (final EncryptionMode encryptionMode, final CipherAlgorithm cipherAlgorithm, final HashAlgorithm hashAlgorithm, final int keyBits, final int blockSize, final ChainingMode chainingMode)\n
    '''
def getVersionMajor():
    '''returns int\n\n
    getVersionMajor()\n
    '''
def getVersionMinor():
    '''returns int\n\n
    getVersionMinor()\n
    '''
def getEncryptionFlags():
    '''returns int\n\n
    getEncryptionFlags()\n
    '''
def getHeader():
    '''returns EncryptionHeader\n\n
    getHeader()\n
    '''
def getVerifier():
    '''returns EncryptionVerifier\n\n
    getVerifier()\n
    '''
def getDecryptor():
    '''returns Decryptor\n\n
    getDecryptor()\n
    '''
def getEncryptor():
    '''returns Encryptor\n\n
    getEncryptor()\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final EncryptionHeader header)\n
    '''
def setVerifier():
    '''returns None\n\n
    setVerifier(final EncryptionVerifier verifier)\n
    '''
def setDecryptor():
    '''returns None\n\n
    setDecryptor(final Decryptor decryptor)\n
    '''
def setEncryptor():
    '''returns None\n\n
    setEncryptor(final Encryptor encryptor)\n
    '''
def getEncryptionMode():
    '''returns EncryptionMode\n\n
    getEncryptionMode()\n
    '''
def isDocPropsEncrypted():
    '''returns boolean\n\n
    isDocPropsEncrypted()\n
    '''
def clone():
    '''returns EncryptionInfo\n\n
    clone()\n
    '''
