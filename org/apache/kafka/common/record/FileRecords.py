def FileRecords():
'''public FileRecords(final File file, final FileChannel channel, final int start, final int end, final boolean isSlice)
'''
pass
def sizeInBytes():
'''public int sizeInBytes()
'''
pass
def file():
'''public File file()
'''
pass
def channel():
'''public FileChannel channel()
'''
pass
def readInto():
'''public ByteBuffer readInto(final ByteBuffer buffer, final int position)
'''
pass
def read():
'''public FileRecords read(final int position, final int size)
'''
pass
def append():
'''public int append(final MemoryRecords records)
'''
pass
def flush():
'''public void flush()
'''
pass
def close():
'''public void close()
'''
pass
def closeHandlers():
'''public void closeHandlers()
'''
pass
def deleteIfExists():
'''public boolean deleteIfExists()
'''
pass
def trim():
'''public void trim()
'''
pass
def setFile():
'''public void setFile(final File file)
'''
pass
def renameTo():
'''public void renameTo(final File f)
'''
pass
def truncateTo():
'''public int truncateTo(final int targetSize)
'''
pass
def writeTo():
'''public long writeTo(final GatheringByteChannel destChannel, final long offset, final int length)
'''
pass
def searchForOffsetWithSize():
'''public LogOffsetPosition searchForOffsetWithSize(final long targetOffset, final int startingPosition)
'''
pass
def searchForTimestamp():
'''public TimestampAndOffset searchForTimestamp(final long targetTimestamp, final int startingPosition, final long startingOffset)
'''
pass
def largestTimestampAfter():
'''public TimestampAndOffset largestTimestampAfter(final int startingPosition)
'''
pass
def open():
'''public static FileRecords open(final File file, final boolean mutable, final boolean fileAlreadyExists, final int initFileSize, final boolean preallocate)
public static FileRecords open(final File file, final boolean fileAlreadyExists, final int initFileSize, final boolean preallocate)
public static FileRecords open(final File file, final boolean mutable)
public static FileRecords open(final File file)
'''
pass
def LogOffsetPosition():
'''public LogOffsetPosition(final long offset, final int position, final int size)
'''
pass
def equals():
'''public boolean equals(final Object o)
public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def TimestampAndOffset():
'''public TimestampAndOffset(final long timestamp, final long offset)
'''
pass
