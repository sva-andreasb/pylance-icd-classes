GUID_VERSION_3 = "byte  48"
GUID_VERSION_1_MASK = "byte  -1"
GUID_VERSION_MASK = "byte  15"
GUID_VERSION_3_ALGORITHM = "String  \"MD5\""
CHARACTER_SET = "String  \"UTF-8\""
GUID_RESERVED = "byte  Byte.MIN_VALUE"
GUID_RESERVED_MASK = "byte  63"
VALID_HEX_CHARACTERS = "String  \"0123456789abcdefABCDEF\""
def ():
    '''returns GuidFactory\n\n
    (final byte[] namespaceGUID)\n
    '''
def createGuid():
    '''returns Guid\n\n
    createGuid(final byte[] guidByteArray)\n
    createGuid(final String name)\n
    '''
def createGuidFromHex():
    '''returns Guid\n\n
    createGuidFromHex(final String guidHexString)\n
    '''
def createGuidFromDB():
    '''returns Guid\n\n
    createGuidFromDB(final String guidHexString)\n
    '''
def createNullGuid():
    '''returns Guid\n\n
    createNullGuid()\n
    '''
def getNamespaceGuid():
    '''returns Guid\n\n
    getNamespaceGuid()\n
    '''
