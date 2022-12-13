sid = "short  255"
DEFAULT_BUCKET_SIZE = "int  8"
MAX_BUCKETS = "int  128"
ENCODED_SIZE = "int  8"
def ExtSSTRecord():
    '''public ExtSSTRecord()
    public ExtSSTRecord(final RecordInputStream in)
    '''
def setNumStringsPerBucket():
    '''public void setNumStringsPerBucket(final short numStrings)
    '''
def toString():
    '''public String toString()
    '''
def serialize():
    '''public void serialize(final ContinuableRecordOutput out)
    public void serialize(final LittleEndianOutput out)
    '''
def getNumberOfInfoRecsForStrings():
    '''public static final int getNumberOfInfoRecsForStrings(final int numStrings)
    '''
def getRecordSizeForStrings():
    '''public static final int getRecordSizeForStrings(final int numStrings)
    '''
def getSid():
    '''public short getSid()
    '''
def setBucketOffsets():
    '''public void setBucketOffsets(final int[] bucketAbsoluteOffsets, final int[] bucketRelativeOffsets)
    '''
def InfoSubRecord():
    '''public InfoSubRecord(final int streamPos, final int bucketSstOffset)
    public InfoSubRecord(final RecordInputStream in)
    '''
def getStreamPos():
    '''public int getStreamPos()
    '''
def getBucketSSTOffset():
    '''public int getBucketSSTOffset()
    '''
