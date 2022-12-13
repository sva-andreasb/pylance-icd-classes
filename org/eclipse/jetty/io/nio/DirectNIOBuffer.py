def DirectNIOBuffer():
'''public DirectNIOBuffer(final int size)
public DirectNIOBuffer(final ByteBuffer buffer, final boolean immutable)
public DirectNIOBuffer(final File file)
'''
pass
def isDirect():
'''public boolean isDirect()
'''
pass
def array():
'''public byte[] array()
'''
pass
def capacity():
'''public int capacity()
'''
pass
def peek():
'''public byte peek(final int position)
public int peek(final int index, final byte[] b, final int offset, final int length)
'''
pass
def poke():
'''public void poke(final int index, final byte b)
public int poke(final int index, final Buffer src)
public int poke(final int index, final byte[] b, final int offset, int length)
'''
pass
def getByteBuffer():
'''public ByteBuffer getByteBuffer()
'''
pass
def readFrom():
'''public int readFrom(final InputStream in, int max)
'''
pass
def writeTo():
'''public void writeTo(final OutputStream out)
'''
pass
