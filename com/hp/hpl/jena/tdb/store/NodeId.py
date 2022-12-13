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
'''public static NodeId create(final long value)
public static NodeId create(final byte[] b)
public static NodeId create(final ByteBuffer b)
public static NodeId create(final byte[] b, final int idx)
public static NodeId create(final ByteBuffer b, final int idx)
'''
pass
def NodeId():
'''public NodeId(final long v)
'''
pass
def toByteBuffer():
'''public void toByteBuffer(final ByteBuffer b, final int idx)
'''
pass
def toBytes():
'''public void toBytes(final byte[] b, final int idx)
'''
pass
def isDirect():
'''public boolean isDirect()
'''
pass
def type():
'''public int type()
'''
pass
def getId():
'''public long getId()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def toString():
'''public String toString()
'''
pass
def inline():
'''public static NodeId inline(final Node node)
'''
pass
def extract():
'''public static Node extract(final NodeId nodeId)
'''
pass
def isAny():
'''public static final boolean isAny(final NodeId nodeId)
'''
pass
def doesNotExist():
'''public static final boolean doesNotExist(final NodeId nodeId)
'''
pass
