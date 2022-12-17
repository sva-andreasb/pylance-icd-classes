def ():
    '''returns GetObjectRequest\n\n
    (final String bucketName, final String key)\n
    (final String bucketName, final String key, final String versionId)\n
    (final S3ObjectId s3ObjectId)\n
    (final String bucketName, final String key, final boolean isRequesterPays)\n
    '''
def getBucketName():
    '''returns String\n\n
    getBucketName()\n
    '''
def setBucketName():
    '''returns None\n\n
    setBucketName(final String bucketName)\n
    '''
def withBucketName():
    '''returns GetObjectRequest\n\n
    withBucketName(final String bucketName)\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    '''
def setKey():
    '''returns None\n\n
    setKey(final String key)\n
    '''
def withKey():
    '''returns GetObjectRequest\n\n
    withKey(final String key)\n
    '''
def getVersionId():
    '''returns String\n\n
    getVersionId()\n
    '''
def setVersionId():
    '''returns None\n\n
    setVersionId(final String versionId)\n
    '''
def withVersionId():
    '''returns GetObjectRequest\n\n
    withVersionId(final String versionId)\n
    '''
def getRange():
    '''returns long[]\n\n
    getRange()\n
    '''
def setRange():
    '''returns None\n\n
    setRange(final long start, final long end)\n
    setRange(final long start)\n
    '''
def withRange():
    '''returns GetObjectRequest\n\n
    withRange(final long start, final long end)\n
    withRange(final long start)\n
    '''
def getMatchingETagConstraints():
    '''returns List<String>\n\n
    getMatchingETagConstraints()\n
    '''
def setMatchingETagConstraints():
    '''returns None\n\n
    setMatchingETagConstraints(final List<String> eTagList)\n
    '''
def withMatchingETagConstraint():
    '''returns GetObjectRequest\n\n
    withMatchingETagConstraint(final String eTag)\n
    '''
def getNonmatchingETagConstraints():
    '''returns List<String>\n\n
    getNonmatchingETagConstraints()\n
    '''
def setNonmatchingETagConstraints():
    '''returns None\n\n
    setNonmatchingETagConstraints(final List<String> eTagList)\n
    '''
def withNonmatchingETagConstraint():
    '''returns GetObjectRequest\n\n
    withNonmatchingETagConstraint(final String eTag)\n
    '''
def getUnmodifiedSinceConstraint():
    '''returns Date\n\n
    getUnmodifiedSinceConstraint()\n
    '''
def setUnmodifiedSinceConstraint():
    '''returns None\n\n
    setUnmodifiedSinceConstraint(final Date date)\n
    '''
def withUnmodifiedSinceConstraint():
    '''returns GetObjectRequest\n\n
    withUnmodifiedSinceConstraint(final Date date)\n
    '''
def getModifiedSinceConstraint():
    '''returns Date\n\n
    getModifiedSinceConstraint()\n
    '''
def setModifiedSinceConstraint():
    '''returns None\n\n
    setModifiedSinceConstraint(final Date date)\n
    '''
def withModifiedSinceConstraint():
    '''returns GetObjectRequest\n\n
    withModifiedSinceConstraint(final Date date)\n
    '''
def getResponseHeaders():
    '''returns ResponseHeaderOverrides\n\n
    getResponseHeaders()\n
    '''
def setResponseHeaders():
    '''returns None\n\n
    setResponseHeaders(final ResponseHeaderOverrides responseHeaders)\n
    '''
def withResponseHeaders():
    '''returns GetObjectRequest\n\n
    withResponseHeaders(final ResponseHeaderOverrides responseHeaders)\n
    '''
def setProgressListener():
    '''returns None\n\n
    setProgressListener(final ProgressListener progressListener)\n
    '''
def getProgressListener():
    '''returns ProgressListener\n\n
    getProgressListener()\n
    '''
def withProgressListener():
    '''returns GetObjectRequest\n\n
    withProgressListener(final ProgressListener progressListener)\n
    '''
def isRequesterPays():
    '''returns boolean\n\n
    isRequesterPays()\n
    '''
def setRequesterPays():
    '''returns None\n\n
    setRequesterPays(final boolean isRequesterPays)\n
    '''
def withRequesterPays():
    '''returns GetObjectRequest\n\n
    withRequesterPays(final boolean isRequesterPays)\n
    '''
def getSSECustomerKey():
    '''returns SSECustomerKey\n\n
    getSSECustomerKey()\n
    '''
def setSSECustomerKey():
    '''returns None\n\n
    setSSECustomerKey(final SSECustomerKey sseKey)\n
    '''
def withSSECustomerKey():
    '''returns GetObjectRequest\n\n
    withSSECustomerKey(final SSECustomerKey sseKey)\n
    '''
def getPartNumber():
    '''returns Integer\n\n
    getPartNumber()\n
    '''
def setPartNumber():
    '''returns None\n\n
    setPartNumber(final Integer partNumber)\n
    '''
def withPartNumber():
    '''returns GetObjectRequest\n\n
    withPartNumber(final Integer partNumber)\n
    '''
def getS3ObjectId():
    '''returns S3ObjectId\n\n
    getS3ObjectId()\n
    '''
def setS3ObjectId():
    '''returns None\n\n
    setS3ObjectId(final S3ObjectId s3ObjectId)\n
    '''
def withS3ObjectId():
    '''returns GetObjectRequest\n\n
    withS3ObjectId(final S3ObjectId s3ObjectId)\n
    '''
