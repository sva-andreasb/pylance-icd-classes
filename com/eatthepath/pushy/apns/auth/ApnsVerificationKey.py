def ApnsVerificationKey():
    '''public ApnsVerificationKey(final String keyId, final String teamId, final ECPublicKey key)
    '''
def getKey():
    '''public ECPublicKey getKey()
    '''
def getAlgorithm():
    '''public String getAlgorithm()
    '''
def getFormat():
    '''public String getFormat()
    '''
def getEncoded():
    '''public byte[] getEncoded()
    '''
def getW():
    '''public ECPoint getW()
    '''
def loadFromPkcs8File():
    '''public static ApnsVerificationKey loadFromPkcs8File(final File pkcs8File, final String teamId, final String keyId)
    '''
def loadFromInputStream():
    '''public static ApnsVerificationKey loadFromInputStream(final InputStream inputStream, final String teamId, final String keyId)
    '''
