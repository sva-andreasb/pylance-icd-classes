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
def OmemoElement():
    '''    public OmemoElement(final OmemoHeader header, final byte[] payload)
    '''
def getHeader():
    '''    public OmemoHeader getHeader()
    '''
def getPayload():
    '''    public byte[] getPayload()
    '''
def isKeyTransportElement():
    '''    public boolean isKeyTransportElement()
    '''
def isMessageElement():
    '''    public boolean isMessageElement()
    '''
def OmemoHeader():
    '''    public OmemoHeader(final int sid, final ArrayList<Key> keys, final byte[] iv)
    '''
def getSid():
    '''    public int getSid()
    '''
def getKeys():
    '''    public ArrayList<Key> getKeys()
    '''
def getIv():
    '''    public byte[] getIv()
    '''
def getElementName():
    '''    public String getElementName()
    public String getElementName()
    '''
def toXML():
    '''    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    '''
def Key():
    '''    public Key(final byte[] data, final int id)
    public Key(final byte[] data, final int id, final boolean preKey)
    '''
def getId():
    '''    public int getId()
    '''
def getData():
    '''    public byte[] getData()
    '''
def isPreKey():
    '''    public boolean isPreKey()
    '''
def toString():
    '''    public String toString()
    '''
