NAMESPACE_V1 = "String  \"urn:xmpp:jingle:transports:ibb:1\""
ATTR_BLOCK_SIZE = "String  \"block-size\""
ATTR_SID = "String  \"sid\""
DEFAULT_BLOCK_SIZE = "short  4096"
def ():
    '''returns JingleIBBTransport\n\n
    ()\n
    (final String sid)\n
    (final short blockSize)\n
    (final short blockSize, final String sid)\n
    '''
def getSessionId():
    '''returns String\n\n
    getSessionId()\n
    '''
def getBlockSize():
    '''returns short\n\n
    getBlockSize()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
