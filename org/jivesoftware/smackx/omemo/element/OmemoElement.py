TYPE_OMEMO_PREKEY_MESSAGE = "int  1"
TYPE_OMEMO_MESSAGE = "int  0"
ENCRYPTED = "String  \"encrypted\""
HEADER = "String  \"header\""
SID = "String  \"sid\""
KEY = "String  \"key\""
RID = "String  \"rid\""
PREKEY = "String  \"prekey\""
IV = "String  \"iv\""
PAYLOAD = "String  \"payload\""
def ():
    '''returns Key\n\n
    (final OmemoHeader header, final byte[] payload)\n
    (final int sid, final ArrayList<Key> keys, final byte[] iv)\n
    (final byte[] data, final int id)\n
    (final byte[] data, final int id, final boolean preKey)\n
    '''
def getHeader():
    '''returns OmemoHeader\n\n
    getHeader()\n
    '''
def getPayload():
    '''returns byte[]\n\n
    getPayload()\n
    '''
def isKeyTransportElement():
    '''returns boolean\n\n
    isKeyTransportElement()\n
    '''
def isMessageElement():
    '''returns boolean\n\n
    isMessageElement()\n
    '''
def getSid():
    '''returns int\n\n
    getSid()\n
    '''
def getKeys():
    '''returns ArrayList<Key>\n\n
    getKeys()\n
    '''
def getIv():
    '''returns byte[]\n\n
    getIv()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    getElementName()\n
    '''
def toXML():
    '''returns CharSequence\n\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    '''
def getId():
    '''returns int\n\n
    getId()\n
    '''
def getData():
    '''returns byte[]\n\n
    getData()\n
    '''
def isPreKey():
    '''returns boolean\n\n
    isPreKey()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
