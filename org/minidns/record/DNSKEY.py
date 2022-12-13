FLAG_SECURE_ENTRY_POINT = "short  1"
FLAG_REVOKE = "short  128"
FLAG_ZONE = "short  256"
PROTOCOL_RFC4034 = "byte  3"
def parse():
    '''public static DNSKEY parse(final DataInputStream dis, final int length)
    '''
def DNSKEY():
    '''public DNSKEY(final short flags, final byte protocol, final byte algorithm, final byte[] key)
    public DNSKEY(final short flags, final byte protocol, final DnssecConstants.SignatureAlgorithm algorithm, final byte[] key)
    '''
def getKeyTag():
    '''public int getKeyTag()
    '''
def serialize():
    '''public void serialize(final DataOutputStream dos)
    '''
def toString():
    '''public String toString()
    '''
def getKeyLength():
    '''public int getKeyLength()
    '''
def getKey():
    '''public byte[] getKey()
    '''
def getKeyBase64():
    '''public String getKeyBase64()
    '''
def keyEquals():
    '''public boolean keyEquals(final byte[] otherKey)
    '''
def isSecureEntryPoint():
    '''public boolean isSecureEntryPoint()
    '''
