def PNGChunk():
'''public PNGChunk(final int length, final int type, final byte[] data, final int crc)
'''
pass
def getLength():
'''public int getLength()
'''
pass
def getType():
'''public int getType()
'''
pass
def getTypeString():
'''public String getTypeString()
'''
pass
def getData():
'''public byte[] getData()
'''
pass
def getByte():
'''public byte getByte(final int offset)
'''
pass
def getInt1():
'''public int getInt1(final int offset)
'''
pass
def getInt2():
'''public int getInt2(final int offset)
'''
pass
def getInt4():
'''public int getInt4(final int offset)
'''
pass
def getString4():
'''public String getString4(final int offset)
'''
pass
def isType():
'''public boolean isType(final String typeName)
'''
pass
def readChunk():
'''public static PNGChunk readChunk(final DataInputStream distream)
'''
pass
def getChunkType():
'''public static String getChunkType(final DataInputStream distream)
'''
pass
def skipChunk():
'''public static boolean skipChunk(final DataInputStream distream)
'''
pass
