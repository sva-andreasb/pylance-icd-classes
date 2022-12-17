MAGIC_OFFSET = "int  0"
VERSION_OFFSET = "int  4"
REFTYPE_OFFSET = "int  5"
HASH_OFFSET = "int  6"
NAME_LENGTH_OFFSET_V1 = "int  6"
NAME_LENGTH_OFFSET_V2 = "int  10"
NAME_OFFSET_V1 = "int  7"
NAME_OFFSET_V2 = "int  11"
NAME_LENGTH_SIZE = "int  1"
OA_NAME_LENGTH_SIZE = "int  1"
SERVANT_NAME_LENGTH_SIZE = "int  4"
PLAIN_REF = "byte  0"
SGAWARE_REF = "byte  1"
MAGIC = "int  1229277776"
VERSION_1 = "byte  1"
VERSION_2 = "byte  2"
def ():
    '''returns UserKey\n\n
    (final String rootName, final boolean sgAware, final byte[] oaPrefix, final byte[] objKey)\n
    (final byte[] rootKey, final boolean sgAware, final byte[] oaPrefix, final byte[] objKey)\n
    (final byte[] rootKey, final boolean sgAware, final byte[] oaPrefix, final ByteArray objKey)\n
    (byte[] key)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getOAKey():
    '''returns byte[]\n\n
    getOAKey()\n
    '''
def getServantKey():
    '''returns byte[]\n\n
    getServantKey()\n
    '''
def getMagicNumber():
    '''returns int\n\n
    getMagicNumber()\n
    '''
def getVersionNumber():
    '''returns byte\n\n
    getVersionNumber()\n
    '''
def getWLMObjectRefType():
    '''returns byte\n\n
    getWLMObjectRefType()\n
    '''
def getHashValue():
    '''returns int\n\n
    getHashValue()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getOAName():
    '''returns String\n\n
    getOAName()\n
    '''
def setPlainRef():
    '''returns None\n\n
    setPlainRef(final String name)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    '''
