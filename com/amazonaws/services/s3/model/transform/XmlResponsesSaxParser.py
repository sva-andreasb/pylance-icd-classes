def XmlResponsesSaxParser():
'''public XmlResponsesSaxParser()
'''
pass
def parseListBucketObjectsResponse():
'''public ListBucketHandler parseListBucketObjectsResponse(final InputStream inputStream, final boolean shouldSDKDecodeResponse)
'''
pass
def parseListObjectsV2Response():
'''public ListObjectsV2Handler parseListObjectsV2Response(final InputStream inputStream, final boolean shouldSDKDecodeResponse)
'''
pass
def parseListVersionsResponse():
'''public ListVersionsHandler parseListVersionsResponse(final InputStream inputStream, final boolean shouldSDKDecodeResponse)
'''
pass
def parseListMyBucketsResponse():
'''public ListAllMyBucketsHandler parseListMyBucketsResponse(final InputStream inputStream)
'''
pass
def parseAccessControlListResponse():
'''public AccessControlListHandler parseAccessControlListResponse(final InputStream inputStream)
'''
pass
def parseLoggingStatusResponse():
'''public BucketLoggingConfigurationHandler parseLoggingStatusResponse(final InputStream inputStream)
'''
pass
def parseBucketLifecycleConfigurationResponse():
'''public BucketLifecycleConfigurationHandler parseBucketLifecycleConfigurationResponse(final InputStream inputStream)
'''
pass
def parseBucketCrossOriginConfigurationResponse():
'''public BucketCrossOriginConfigurationHandler parseBucketCrossOriginConfigurationResponse(final InputStream inputStream)
'''
pass
def parseBucketLocationResponse():
'''public String parseBucketLocationResponse(final InputStream inputStream)
'''
pass
def parseVersioningConfigurationResponse():
'''public BucketVersioningConfigurationHandler parseVersioningConfigurationResponse(final InputStream inputStream)
'''
pass
def parseWebsiteConfigurationResponse():
'''public BucketWebsiteConfigurationHandler parseWebsiteConfigurationResponse(final InputStream inputStream)
'''
pass
def parseReplicationConfigurationResponse():
'''public BucketReplicationConfigurationHandler parseReplicationConfigurationResponse(final InputStream inputStream)
'''
pass
def parseTaggingConfigurationResponse():
'''public BucketTaggingConfigurationHandler parseTaggingConfigurationResponse(final InputStream inputStream)
'''
pass
def parseAccelerateConfigurationResponse():
'''public BucketAccelerateConfigurationHandler parseAccelerateConfigurationResponse(final InputStream inputStream)
'''
pass
def parseDeletedObjectsResult():
'''public DeleteObjectsHandler parseDeletedObjectsResult(final InputStream inputStream)
'''
pass
def parseCopyObjectResponse():
'''public CopyObjectResultHandler parseCopyObjectResponse(final InputStream inputStream)
'''
pass
def parseCompleteMultipartUploadResponse():
'''public CompleteMultipartUploadHandler parseCompleteMultipartUploadResponse(final InputStream inputStream)
'''
pass
def parseInitiateMultipartUploadResponse():
'''public InitiateMultipartUploadHandler parseInitiateMultipartUploadResponse(final InputStream inputStream)
'''
pass
def parseListMultipartUploadsResponse():
'''public ListMultipartUploadsHandler parseListMultipartUploadsResponse(final InputStream inputStream)
'''
pass
def parseListPartsResponse():
'''public ListPartsHandler parseListPartsResponse(final InputStream inputStream)
'''
pass
def parseRequestPaymentConfigurationResponse():
'''public RequestPaymentConfigurationHandler parseRequestPaymentConfigurationResponse(final InputStream inputStream)
'''
pass
def ListBucketHandler():
'''public ListBucketHandler(final boolean shouldSDKDecodeResponse)
'''
pass
def getObjectListing():
'''public ObjectListing getObjectListing()
'''
pass
def ListObjectsV2Handler():
'''public ListObjectsV2Handler(final boolean shouldSDKDecodeResponse)
'''
pass
def getResult():
'''public ListObjectsV2Result getResult()
'''
pass
def ListAllMyBucketsHandler():
'''public ListAllMyBucketsHandler()
'''
pass
def getBuckets():
'''public List<Bucket> getBuckets()
'''
pass
def getOwner():
'''public Owner getOwner()
'''
pass
def AccessControlListHandler():
'''public AccessControlListHandler()
'''
pass
def getAccessControlList():
'''public AccessControlList getAccessControlList()
'''
pass
def BucketLoggingConfigurationHandler():
'''public BucketLoggingConfigurationHandler()
'''
pass
def getBucketLoggingConfiguration():
'''public BucketLoggingConfiguration getBucketLoggingConfiguration()
'''
pass
def BucketLocationHandler():
'''public BucketLocationHandler()
'''
pass
def getLocation():
'''public String getLocation()
'''
pass
def CopyObjectResultHandler():
'''public CopyObjectResultHandler()
'''
pass
def getLastModified():
'''public Date getLastModified()
'''
pass
def getVersionId():
'''public String getVersionId()
public String getVersionId()
'''
pass
def setVersionId():
'''public void setVersionId(final String versionId)
public void setVersionId(final String versionId)
'''
pass
def getExpirationTime():
'''public Date getExpirationTime()
public Date getExpirationTime()
'''
pass
def setExpirationTime():
'''public void setExpirationTime(final Date expirationTime)
public void setExpirationTime(final Date expirationTime)
'''
pass
def getExpirationTimeRuleId():
'''public String getExpirationTimeRuleId()
public String getExpirationTimeRuleId()
'''
pass
def setExpirationTimeRuleId():
'''public void setExpirationTimeRuleId(final String expirationTimeRuleId)
public void setExpirationTimeRuleId(final String expirationTimeRuleId)
'''
pass
def getETag():
'''public String getETag()
'''
pass
def getErrorCode():
'''public String getErrorCode()
'''
pass
def getErrorHostId():
'''public String getErrorHostId()
'''
pass
def getErrorMessage():
'''public String getErrorMessage()
'''
pass
def getErrorRequestId():
'''public String getErrorRequestId()
'''
pass
def isErrorResponse():
'''public boolean isErrorResponse()
'''
pass
def isRequesterCharged():
'''public boolean isRequesterCharged()
public boolean isRequesterCharged()
'''
pass
def setRequesterCharged():
'''public void setRequesterCharged(final boolean isRequesterCharged)
public void setRequesterCharged(final boolean isRequesterCharged)
'''
pass
def RequestPaymentConfigurationHandler():
'''public RequestPaymentConfigurationHandler()
'''
pass
def getConfiguration():
'''public RequestPaymentConfiguration getConfiguration()
public BucketWebsiteConfiguration getConfiguration()
public BucketVersioningConfiguration getConfiguration()
public BucketAccelerateConfiguration getConfiguration()
public BucketReplicationConfiguration getConfiguration()
public BucketTaggingConfiguration getConfiguration()
public BucketLifecycleConfiguration getConfiguration()
public BucketCrossOriginConfiguration getConfiguration()
'''
pass
def ListVersionsHandler():
'''public ListVersionsHandler(final boolean shouldSDKDecodeResponse)
'''
pass
def getListing():
'''public VersionListing getListing()
'''
pass
def BucketWebsiteConfigurationHandler():
'''public BucketWebsiteConfigurationHandler()
'''
pass
def BucketVersioningConfigurationHandler():
'''public BucketVersioningConfigurationHandler()
'''
pass
def BucketAccelerateConfigurationHandler():
'''public BucketAccelerateConfigurationHandler()
'''
pass
def getCompleteMultipartUploadResult():
'''public CompleteMultipartUploadResult getCompleteMultipartUploadResult()
'''
pass
def getAmazonS3Exception():
'''public AmazonS3Exception getAmazonS3Exception()
'''
pass
def InitiateMultipartUploadHandler():
'''public InitiateMultipartUploadHandler()
'''
pass
def getInitiateMultipartUploadResult():
'''public InitiateMultipartUploadResult getInitiateMultipartUploadResult()
'''
pass
def ListMultipartUploadsHandler():
'''public ListMultipartUploadsHandler()
'''
pass
def getListMultipartUploadsResult():
'''public MultipartUploadListing getListMultipartUploadsResult()
'''
pass
def ListPartsHandler():
'''public ListPartsHandler()
'''
pass
def getListPartsResult():
'''public PartListing getListPartsResult()
'''
pass
def BucketReplicationConfigurationHandler():
'''public BucketReplicationConfigurationHandler()
'''
pass
def BucketTaggingConfigurationHandler():
'''public BucketTaggingConfigurationHandler()
'''
pass
def DeleteObjectsHandler():
'''public DeleteObjectsHandler()
'''
pass
def getDeleteObjectResult():
'''public DeleteObjectsResponse getDeleteObjectResult()
'''
pass
def BucketLifecycleConfigurationHandler():
'''public BucketLifecycleConfigurationHandler()
'''
pass
def BucketCrossOriginConfigurationHandler():
'''public BucketCrossOriginConfigurationHandler()
'''
pass
