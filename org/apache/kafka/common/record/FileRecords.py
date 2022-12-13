def FileRecords():
    '''    public FileRecords(final File file, final FileChannel channel, final int start, final int end, final boolean isSlice)
    '''
def sizeInBytes():
    '''    public int sizeInBytes()
    '''
def file():
    '''    public File file()
    '''
def channel():
    '''    public FileChannel channel()
    '''
def readInto():
    '''    public ByteBuffer readInto(final ByteBuffer buffer, final int position)
    '''
def read():
    '''    public FileRecords read(final int position, final int size)
    '''
def append():
    '''    public int append(final MemoryRecords records)
    '''
def flush():
    '''    public void flush()
    '''
def close():
    '''    public void close()
    '''
def closeHandlers():
    '''    public void closeHandlers()
    '''
def deleteIfExists():
    '''    public boolean deleteIfExists()
    '''
def trim():
    '''    public void trim()
    '''
def setFile():
    '''    public void setFile(final File file)
    '''
def renameTo():
    '''    public void renameTo(final File f)
    '''
def truncateTo():
    '''    public int truncateTo(final int targetSize)
    '''
def writeTo():
    '''    public long writeTo(final GatheringByteChannel destChannel, final long offset, final int length)
    '''
def searchForOffsetWithSize():
    '''    public LogOffsetPosition searchForOffsetWithSize(final long targetOffset, final int startingPosition)
    '''
def searchForTimestamp():
    '''    public TimestampAndOffset searchForTimestamp(final long targetTimestamp, final int startingPosition, final long startingOffset)
    '''
def largestTimestampAfter():
    '''    public TimestampAndOffset largestTimestampAfter(final int startingPosition)
    '''
def open():
    '''    public static FileRecords open(final File file, final boolean mutable, final boolean fileAlreadyExists, final int initFileSize, final boolean preallocate)
    public static FileRecords open(final File file, final boolean fileAlreadyExists, final int initFileSize, final boolean preallocate)
    public static FileRecords open(final File file, final boolean mutable)
    public static FileRecords open(final File file)
    '''
def LogOffsetPosition():
    '''    public LogOffsetPosition(final long offset, final int position, final int size)
    '''
def equals():
    '''    public boolean equals(final Object o)
    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def TimestampAndOffset():
    '''    public TimestampAndOffset(final long timestamp, final long offset)
    '''
