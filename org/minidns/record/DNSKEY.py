FLAG_SECURE_ENTRY_POINT = "short  1"
FLAG_REVOKE = "short  128"
FLAG_ZONE = "short  256"
PROTOCOL_RFC4034 = "byte  3"
def parse():
'''public static DNSKEY parse(final DataInputStream dis, final int length)
'''
pass
def DNSKEY():
'''public DNSKEY(final short flags, final byte protocol, final byte algorithm, final byte[] key)
public DNSKEY(final short flags, final byte protocol, final DnssecConstants.SignatureAlgorithm algorithm, final byte[] key)
'''
pass
def getKeyTag():
'''public int getKeyTag()
'''
pass
def serialize():
'''public void serialize(final DataOutputStream dos)
'''
pass
def toString():
'''public String toString()
'''
pass
def getKeyLength():
'''public int getKeyLength()
'''
pass
def getKey():
'''public byte[] getKey()
'''
pass
def getKeyBase64():
'''public String getKeyBase64()
'''
pass
def keyEquals():
'''public boolean keyEquals(final byte[] otherKey)
'''
pass
def isSecureEntryPoint():
'''public boolean isSecureEntryPoint()
'''
pass
