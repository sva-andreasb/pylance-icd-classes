def TIFFDirectory():
'''public TIFFDirectory(final SeekableStream stream, final int directory)
public TIFFDirectory(final SeekableStream stream, long ifdOffset, final int directory)
'''
pass
def getNumEntries():
'''public int getNumEntries()
'''
pass
def getField():
'''public TIFFField getField(final int tag)
'''
pass
def isTagPresent():
'''public boolean isTagPresent(final int tag)
'''
pass
def getTags():
'''public int[] getTags()
'''
pass
def getFields():
'''public TIFFField[] getFields()
'''
pass
def getFieldAsByte():
'''public byte getFieldAsByte(final int tag, final int index)
public byte getFieldAsByte(final int tag)
'''
pass
def getFieldAsLong():
'''public long getFieldAsLong(final int tag, final int index)
public long getFieldAsLong(final int tag)
'''
pass
def getFieldAsFloat():
'''public float getFieldAsFloat(final int tag, final int index)
public float getFieldAsFloat(final int tag)
'''
pass
def getFieldAsDouble():
'''public double getFieldAsDouble(final int tag, final int index)
public double getFieldAsDouble(final int tag)
'''
pass
def getNumDirectories():
'''public static int getNumDirectories(final SeekableStream stream)
'''
pass
def isBigEndian():
'''public boolean isBigEndian()
'''
pass
def getIFDOffset():
'''public long getIFDOffset()
'''
pass
def getNextIFDOffset():
'''public long getNextIFDOffset()
'''
pass
