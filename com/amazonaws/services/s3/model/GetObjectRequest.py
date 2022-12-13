def GetObjectRequest():
    '''public GetObjectRequest(final String bucketName, final String key)
    public GetObjectRequest(final String bucketName, final String key, final String versionId)
    public GetObjectRequest(final S3ObjectId s3ObjectId)
    public GetObjectRequest(final String bucketName, final String key, final boolean isRequesterPays)
    '''
def getBucketName():
    '''public String getBucketName()
    '''
def setBucketName():
    '''public void setBucketName(final String bucketName)
    '''
def withBucketName():
    '''public GetObjectRequest withBucketName(final String bucketName)
    '''
def getKey():
    '''public String getKey()
    '''
def setKey():
    '''public void setKey(final String key)
    '''
def withKey():
    '''public GetObjectRequest withKey(final String key)
    '''
def getVersionId():
    '''public String getVersionId()
    '''
def setVersionId():
    '''public void setVersionId(final String versionId)
    '''
def withVersionId():
    '''public GetObjectRequest withVersionId(final String versionId)
    '''
def getRange():
    '''public long[] getRange()
    '''
def setRange():
    '''public void setRange(final long start, final long end)
    public void setRange(final long start)
    '''
def withRange():
    '''public GetObjectRequest withRange(final long start, final long end)
    public GetObjectRequest withRange(final long start)
    '''
def getMatchingETagConstraints():
    '''public List<String> getMatchingETagConstraints()
    '''
def setMatchingETagConstraints():
    '''public void setMatchingETagConstraints(final List<String> eTagList)
    '''
def withMatchingETagConstraint():
    '''public GetObjectRequest withMatchingETagConstraint(final String eTag)
    '''
def getNonmatchingETagConstraints():
    '''public List<String> getNonmatchingETagConstraints()
    '''
def setNonmatchingETagConstraints():
    '''public void setNonmatchingETagConstraints(final List<String> eTagList)
    '''
def withNonmatchingETagConstraint():
    '''public GetObjectRequest withNonmatchingETagConstraint(final String eTag)
    '''
def getUnmodifiedSinceConstraint():
    '''public Date getUnmodifiedSinceConstraint()
    '''
def setUnmodifiedSinceConstraint():
    '''public void setUnmodifiedSinceConstraint(final Date date)
    '''
def withUnmodifiedSinceConstraint():
    '''public GetObjectRequest withUnmodifiedSinceConstraint(final Date date)
    '''
def getModifiedSinceConstraint():
    '''public Date getModifiedSinceConstraint()
    '''
def setModifiedSinceConstraint():
    '''public void setModifiedSinceConstraint(final Date date)
    '''
def withModifiedSinceConstraint():
    '''public GetObjectRequest withModifiedSinceConstraint(final Date date)
    '''
def getResponseHeaders():
    '''public ResponseHeaderOverrides getResponseHeaders()
    '''
def setResponseHeaders():
    '''public void setResponseHeaders(final ResponseHeaderOverrides responseHeaders)
    '''
def withResponseHeaders():
    '''public GetObjectRequest withResponseHeaders(final ResponseHeaderOverrides responseHeaders)
    '''
def setProgressListener():
    '''public void setProgressListener(final ProgressListener progressListener)
    '''
def getProgressListener():
    '''public ProgressListener getProgressListener()
    '''
def withProgressListener():
    '''public GetObjectRequest withProgressListener(final ProgressListener progressListener)
    '''
def isRequesterPays():
    '''public boolean isRequesterPays()
    '''
def setRequesterPays():
    '''public void setRequesterPays(final boolean isRequesterPays)
    '''
def withRequesterPays():
    '''public GetObjectRequest withRequesterPays(final boolean isRequesterPays)
    '''
def getSSECustomerKey():
    '''public SSECustomerKey getSSECustomerKey()
    '''
def setSSECustomerKey():
    '''public void setSSECustomerKey(final SSECustomerKey sseKey)
    '''
def withSSECustomerKey():
    '''public GetObjectRequest withSSECustomerKey(final SSECustomerKey sseKey)
    '''
def getPartNumber():
    '''public Integer getPartNumber()
    '''
def setPartNumber():
    '''public void setPartNumber(final Integer partNumber)
    '''
def withPartNumber():
    '''public GetObjectRequest withPartNumber(final Integer partNumber)
    '''
def getS3ObjectId():
    '''public S3ObjectId getS3ObjectId()
    '''
def setS3ObjectId():
    '''public void setS3ObjectId(final S3ObjectId s3ObjectId)
    '''
def withS3ObjectId():
    '''public GetObjectRequest withS3ObjectId(final S3ObjectId s3ObjectId)
    '''
