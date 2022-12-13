SIZE = "int  8"
NONE = "int  0"
INTEGER = "int  1"
DECIMAL = "int  2"
DATE = "int  3"
DATETIME = "int  4"
BOOLEAN = "int  5"
SHORT_STRING = "int  6"
SPECIAL = "int  255"
def create():
    '''    public static NodeId create(final long value)
    public static NodeId create(final byte[] b)
    public static NodeId create(final ByteBuffer b)
    public static NodeId create(final byte[] b, final int idx)
    public static NodeId create(final ByteBuffer b, final int idx)
    '''
def NodeId():
    '''    public NodeId(final long v)
    '''
def toByteBuffer():
    '''    public void toByteBuffer(final ByteBuffer b, final int idx)
    '''
def toBytes():
    '''    public void toBytes(final byte[] b, final int idx)
    '''
def isDirect():
    '''    public boolean isDirect()
    '''
def type():
    '''    public int type()
    '''
def getId():
    '''    public long getId()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def toString():
    '''    public String toString()
    '''
def inline():
    '''    public static NodeId inline(final Node node)
    '''
def extract():
    '''    public static Node extract(final NodeId nodeId)
    '''
def isAny():
    '''    public static final boolean isAny(final NodeId nodeId)
    '''
def doesNotExist():
    '''    public static final boolean doesNotExist(final NodeId nodeId)
    '''
