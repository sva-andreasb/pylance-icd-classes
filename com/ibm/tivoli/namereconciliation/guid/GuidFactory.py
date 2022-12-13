GUID_VERSION_3 = "byte  48"
GUID_VERSION_1_MASK = "byte  -1"
GUID_VERSION_MASK = "byte  15"
GUID_VERSION_3_ALGORITHM = "String  MD5""
CHARACTER_SET = "String  UTF-8""
GUID_RESERVED = "byte  Byte.MIN_VALUE"
GUID_RESERVED_MASK = "byte  63"
VALID_HEX_CHARACTERS = "String  0123456789abcdefABCDEF""
def GuidFactory():
'''public GuidFactory(final byte[] namespaceGUID)
'''
pass
def createGuid():
'''public Guid createGuid(final byte[] guidByteArray)
public Guid createGuid(final String name)
'''
pass
def createGuidFromHex():
'''public Guid createGuidFromHex(final String guidHexString)
'''
pass
def createGuidFromDB():
'''public Guid createGuidFromDB(final String guidHexString)
'''
pass
def createNullGuid():
'''public Guid createNullGuid()
'''
pass
def getDefaultGuidFactory():
'''public static GuidFactory getDefaultGuidFactory()
'''
pass
def setDefaultGuidFactory():
'''public static void setDefaultGuidFactory(final GuidFactory defaultGuidFactory)
'''
pass
def getNamespaceGuid():
'''public Guid getNamespaceGuid()
'''
pass
