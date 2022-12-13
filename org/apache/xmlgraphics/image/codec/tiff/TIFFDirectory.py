def TIFFDirectory():
    '''    public TIFFDirectory(final SeekableStream stream, final int directory)
    public TIFFDirectory(final SeekableStream stream, long ifdOffset, final int directory)
    '''
def getNumEntries():
    '''    public int getNumEntries()
    '''
def getField():
    '''    public TIFFField getField(final int tag)
    '''
def isTagPresent():
    '''    public boolean isTagPresent(final int tag)
    '''
def getTags():
    '''    public int[] getTags()
    '''
def getFields():
    '''    public TIFFField[] getFields()
    '''
def getFieldAsByte():
    '''    public byte getFieldAsByte(final int tag, final int index)
    public byte getFieldAsByte(final int tag)
    '''
def getFieldAsLong():
    '''    public long getFieldAsLong(final int tag, final int index)
    public long getFieldAsLong(final int tag)
    '''
def getFieldAsFloat():
    '''    public float getFieldAsFloat(final int tag, final int index)
    public float getFieldAsFloat(final int tag)
    '''
def getFieldAsDouble():
    '''    public double getFieldAsDouble(final int tag, final int index)
    public double getFieldAsDouble(final int tag)
    '''
def getNumDirectories():
    '''    public static int getNumDirectories(final SeekableStream stream)
    '''
def isBigEndian():
    '''    public boolean isBigEndian()
    '''
def getIFDOffset():
    '''    public long getIFDOffset()
    '''
def getNextIFDOffset():
    '''    public long getNextIFDOffset()
    '''
