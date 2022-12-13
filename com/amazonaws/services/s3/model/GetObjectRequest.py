def GetObjectRequest():
'''public GetObjectRequest(final String bucketName, final String key)
public GetObjectRequest(final String bucketName, final String key, final String versionId)
public GetObjectRequest(final S3ObjectId s3ObjectId)
public GetObjectRequest(final String bucketName, final String key, final boolean isRequesterPays)
'''
pass
def getBucketName():
'''public String getBucketName()
'''
pass
def setBucketName():
'''public void setBucketName(final String bucketName)
'''
pass
def withBucketName():
'''public GetObjectRequest withBucketName(final String bucketName)
'''
pass
def getKey():
'''public String getKey()
'''
pass
def setKey():
'''public void setKey(final String key)
'''
pass
def withKey():
'''public GetObjectRequest withKey(final String key)
'''
pass
def getVersionId():
'''public String getVersionId()
'''
pass
def setVersionId():
'''public void setVersionId(final String versionId)
'''
pass
def withVersionId():
'''public GetObjectRequest withVersionId(final String versionId)
'''
pass
def getRange():
'''public long[] getRange()
'''
pass
def setRange():
'''public void setRange(final long start, final long end)
public void setRange(final long start)
'''
pass
def withRange():
'''public GetObjectRequest withRange(final long start, final long end)
public GetObjectRequest withRange(final long start)
'''
pass
def getMatchingETagConstraints():
'''public List<String> getMatchingETagConstraints()
'''
pass
def setMatchingETagConstraints():
'''public void setMatchingETagConstraints(final List<String> eTagList)
'''
pass
def withMatchingETagConstraint():
'''public GetObjectRequest withMatchingETagConstraint(final String eTag)
'''
pass
def getNonmatchingETagConstraints():
'''public List<String> getNonmatchingETagConstraints()
'''
pass
def setNonmatchingETagConstraints():
'''public void setNonmatchingETagConstraints(final List<String> eTagList)
'''
pass
def withNonmatchingETagConstraint():
'''public GetObjectRequest withNonmatchingETagConstraint(final String eTag)
'''
pass
def getUnmodifiedSinceConstraint():
'''public Date getUnmodifiedSinceConstraint()
'''
pass
def setUnmodifiedSinceConstraint():
'''public void setUnmodifiedSinceConstraint(final Date date)
'''
pass
def withUnmodifiedSinceConstraint():
'''public GetObjectRequest withUnmodifiedSinceConstraint(final Date date)
'''
pass
def getModifiedSinceConstraint():
'''public Date getModifiedSinceConstraint()
'''
pass
def setModifiedSinceConstraint():
'''public void setModifiedSinceConstraint(final Date date)
'''
pass
def withModifiedSinceConstraint():
'''public GetObjectRequest withModifiedSinceConstraint(final Date date)
'''
pass
def getResponseHeaders():
'''public ResponseHeaderOverrides getResponseHeaders()
'''
pass
def setResponseHeaders():
'''public void setResponseHeaders(final ResponseHeaderOverrides responseHeaders)
'''
pass
def withResponseHeaders():
'''public GetObjectRequest withResponseHeaders(final ResponseHeaderOverrides responseHeaders)
'''
pass
def setProgressListener():
'''public void setProgressListener(final ProgressListener progressListener)
'''
pass
def getProgressListener():
'''public ProgressListener getProgressListener()
'''
pass
def withProgressListener():
'''public GetObjectRequest withProgressListener(final ProgressListener progressListener)
'''
pass
def isRequesterPays():
'''public boolean isRequesterPays()
'''
pass
def setRequesterPays():
'''public void setRequesterPays(final boolean isRequesterPays)
'''
pass
def withRequesterPays():
'''public GetObjectRequest withRequesterPays(final boolean isRequesterPays)
'''
pass
def getSSECustomerKey():
'''public SSECustomerKey getSSECustomerKey()
'''
pass
def setSSECustomerKey():
'''public void setSSECustomerKey(final SSECustomerKey sseKey)
'''
pass
def withSSECustomerKey():
'''public GetObjectRequest withSSECustomerKey(final SSECustomerKey sseKey)
'''
pass
def getPartNumber():
'''public Integer getPartNumber()
'''
pass
def setPartNumber():
'''public void setPartNumber(final Integer partNumber)
'''
pass
def withPartNumber():
'''public GetObjectRequest withPartNumber(final Integer partNumber)
'''
pass
def getS3ObjectId():
'''public S3ObjectId getS3ObjectId()
'''
pass
def setS3ObjectId():
'''public void setS3ObjectId(final S3ObjectId s3ObjectId)
'''
pass
def withS3ObjectId():
'''public GetObjectRequest withS3ObjectId(final S3ObjectId s3ObjectId)
'''
pass
