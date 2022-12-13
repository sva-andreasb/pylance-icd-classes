TYPE_OMEMO_PREKEY_MESSAGE = "int  1"
TYPE_OMEMO_MESSAGE = "int  0"
ENCRYPTED = "String  encrypted""
HEADER = "String  header""
SID = "String  sid""
KEY = "String  key""
RID = "String  rid""
PREKEY = "String  prekey""
IV = "String  iv""
PAYLOAD = "String  payload""
def OmemoElement():
'''public OmemoElement(final OmemoHeader header, final byte[] payload)
'''
pass
def getHeader():
'''public OmemoHeader getHeader()
'''
pass
def getPayload():
'''public byte[] getPayload()
'''
pass
def isKeyTransportElement():
'''public boolean isKeyTransportElement()
'''
pass
def isMessageElement():
'''public boolean isMessageElement()
'''
pass
def OmemoHeader():
'''public OmemoHeader(final int sid, final ArrayList<Key> keys, final byte[] iv)
'''
pass
def getSid():
'''public int getSid()
'''
pass
def getKeys():
'''public ArrayList<Key> getKeys()
'''
pass
def getIv():
'''public byte[] getIv()
'''
pass
def getElementName():
'''public String getElementName()
public String getElementName()
'''
pass
def toXML():
'''public CharSequence toXML(final String enclosingNamespace)
public CharSequence toXML(final String enclosingNamespace)
'''
pass
def Key():
'''public Key(final byte[] data, final int id)
public Key(final byte[] data, final int id, final boolean preKey)
'''
pass
def getId():
'''public int getId()
'''
pass
def getData():
'''public byte[] getData()
'''
pass
def isPreKey():
'''public boolean isPreKey()
'''
pass
def toString():
'''public String toString()
'''
pass
