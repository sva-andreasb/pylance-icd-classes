def BOMInputStream():
'''public BOMInputStream(final InputStream delegate)
public BOMInputStream(final InputStream delegate, final boolean include)
public BOMInputStream(final InputStream delegate, final ByteOrderMark... boms)
public BOMInputStream(final InputStream delegate, final boolean include, final ByteOrderMark... boms)
'''
pass
def hasBOM():
'''public boolean hasBOM()
public boolean hasBOM(final ByteOrderMark bom)
'''
pass
def getBOM():
'''public ByteOrderMark getBOM()
'''
pass
def getBOMCharsetName():
'''public String getBOMCharsetName()
'''
pass
def read():
'''public int read()
public int read(final byte[] buf, int off, int len)
public int read(final byte[] buf)
'''
pass
def mark():
'''public synchronized void mark(final int readlimit)
'''
pass
def reset():
'''public synchronized void reset()
'''
pass
def skip():
'''public long skip(final long n)
'''
pass
def compare():
'''public int compare(final ByteOrderMark bom1, final ByteOrderMark bom2)
'''
pass
