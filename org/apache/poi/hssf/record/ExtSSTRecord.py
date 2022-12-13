sid = "short  255"
DEFAULT_BUCKET_SIZE = "int  8"
MAX_BUCKETS = "int  128"
ENCODED_SIZE = "int  8"
def ExtSSTRecord():
'''public ExtSSTRecord()
public ExtSSTRecord(final RecordInputStream in)
'''
pass
def setNumStringsPerBucket():
'''public void setNumStringsPerBucket(final short numStrings)
'''
pass
def toString():
'''public String toString()
'''
pass
def serialize():
'''public void serialize(final ContinuableRecordOutput out)
public void serialize(final LittleEndianOutput out)
'''
pass
def getNumberOfInfoRecsForStrings():
'''public static final int getNumberOfInfoRecsForStrings(final int numStrings)
'''
pass
def getRecordSizeForStrings():
'''public static final int getRecordSizeForStrings(final int numStrings)
'''
pass
def getSid():
'''public short getSid()
'''
pass
def setBucketOffsets():
'''public void setBucketOffsets(final int[] bucketAbsoluteOffsets, final int[] bucketRelativeOffsets)
'''
pass
def InfoSubRecord():
'''public InfoSubRecord(final int streamPos, final int bucketSstOffset)
public InfoSubRecord(final RecordInputStream in)
'''
pass
def getStreamPos():
'''public int getStreamPos()
'''
pass
def getBucketSSTOffset():
'''public int getBucketSSTOffset()
'''
pass
