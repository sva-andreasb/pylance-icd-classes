sid = "short  255"
DEFAULT_BUCKET_SIZE = "int  8"
MAX_BUCKETS = "int  128"
ENCODED_SIZE = "int  8"
def ():
    '''returns InfoSubRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    (final int streamPos, final int bucketSstOffset)\n
    (final RecordInputStream in)\n
    '''
def setNumStringsPerBucket():
    '''returns None\n\n
    setNumStringsPerBucket(final short numStrings)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final ContinuableRecordOutput out)\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def setBucketOffsets():
    '''returns None\n\n
    setBucketOffsets(final int[] bucketAbsoluteOffsets, final int[] bucketRelativeOffsets)\n
    '''
def getStreamPos():
    '''returns int\n\n
    getStreamPos()\n
    '''
def getBucketSSTOffset():
    '''returns int\n\n
    getBucketSSTOffset()\n
    '''
