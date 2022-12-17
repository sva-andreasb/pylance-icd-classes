FLAG_SECURE_ENTRY_POINT = "short  1"
FLAG_REVOKE = "short  128"
FLAG_ZONE = "short  256"
PROTOCOL_RFC4034 = "byte  3"
def ():
    '''returns DNSKEY\n\n
    (final short flags, final byte protocol, final byte algorithm, final byte[] key)\n
    (final short flags, final byte protocol, final DnssecConstants.SignatureAlgorithm algorithm, final byte[] key)\n
    '''
def getKeyTag():
    '''returns int\n\n
    getKeyTag()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final DataOutputStream dos)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getKeyLength():
    '''returns int\n\n
    getKeyLength()\n
    '''
def getKey():
    '''returns byte[]\n\n
    getKey()\n
    '''
def getKeyBase64():
    '''returns String\n\n
    getKeyBase64()\n
    '''
def keyEquals():
    '''returns boolean\n\n
    keyEquals(final byte[] otherKey)\n
    '''
def isSecureEntryPoint():
    '''returns boolean\n\n
    isSecureEntryPoint()\n
    '''
