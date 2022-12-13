def XmlResponsesSaxParser():
    '''    public XmlResponsesSaxParser()
    '''
def parseListBucketObjectsResponse():
    '''    public ListBucketHandler parseListBucketObjectsResponse(final InputStream inputStream, final boolean shouldSDKDecodeResponse)
    '''
def parseListObjectsV2Response():
    '''    public ListObjectsV2Handler parseListObjectsV2Response(final InputStream inputStream, final boolean shouldSDKDecodeResponse)
    '''
def parseListVersionsResponse():
    '''    public ListVersionsHandler parseListVersionsResponse(final InputStream inputStream, final boolean shouldSDKDecodeResponse)
    '''
def parseListMyBucketsResponse():
    '''    public ListAllMyBucketsHandler parseListMyBucketsResponse(final InputStream inputStream)
    '''
def parseAccessControlListResponse():
    '''    public AccessControlListHandler parseAccessControlListResponse(final InputStream inputStream)
    '''
def parseLoggingStatusResponse():
    '''    public BucketLoggingConfigurationHandler parseLoggingStatusResponse(final InputStream inputStream)
    '''
def parseBucketLifecycleConfigurationResponse():
    '''    public BucketLifecycleConfigurationHandler parseBucketLifecycleConfigurationResponse(final InputStream inputStream)
    '''
def parseBucketCrossOriginConfigurationResponse():
    '''    public BucketCrossOriginConfigurationHandler parseBucketCrossOriginConfigurationResponse(final InputStream inputStream)
    '''
def parseBucketLocationResponse():
    '''    public String parseBucketLocationResponse(final InputStream inputStream)
    '''
def parseVersioningConfigurationResponse():
    '''    public BucketVersioningConfigurationHandler parseVersioningConfigurationResponse(final InputStream inputStream)
    '''
def parseWebsiteConfigurationResponse():
    '''    public BucketWebsiteConfigurationHandler parseWebsiteConfigurationResponse(final InputStream inputStream)
    '''
def parseReplicationConfigurationResponse():
    '''    public BucketReplicationConfigurationHandler parseReplicationConfigurationResponse(final InputStream inputStream)
    '''
def parseTaggingConfigurationResponse():
    '''    public BucketTaggingConfigurationHandler parseTaggingConfigurationResponse(final InputStream inputStream)
    '''
def parseAccelerateConfigurationResponse():
    '''    public BucketAccelerateConfigurationHandler parseAccelerateConfigurationResponse(final InputStream inputStream)
    '''
def parseDeletedObjectsResult():
    '''    public DeleteObjectsHandler parseDeletedObjectsResult(final InputStream inputStream)
    '''
def parseCopyObjectResponse():
    '''    public CopyObjectResultHandler parseCopyObjectResponse(final InputStream inputStream)
    '''
def parseCompleteMultipartUploadResponse():
    '''    public CompleteMultipartUploadHandler parseCompleteMultipartUploadResponse(final InputStream inputStream)
    '''
def parseInitiateMultipartUploadResponse():
    '''    public InitiateMultipartUploadHandler parseInitiateMultipartUploadResponse(final InputStream inputStream)
    '''
def parseListMultipartUploadsResponse():
    '''    public ListMultipartUploadsHandler parseListMultipartUploadsResponse(final InputStream inputStream)
    '''
def parseListPartsResponse():
    '''    public ListPartsHandler parseListPartsResponse(final InputStream inputStream)
    '''
def parseRequestPaymentConfigurationResponse():
    '''    public RequestPaymentConfigurationHandler parseRequestPaymentConfigurationResponse(final InputStream inputStream)
    '''
def ListBucketHandler():
    '''    public ListBucketHandler(final boolean shouldSDKDecodeResponse)
    '''
def getObjectListing():
    '''    public ObjectListing getObjectListing()
    '''
def ListObjectsV2Handler():
    '''    public ListObjectsV2Handler(final boolean shouldSDKDecodeResponse)
    '''
def getResult():
    '''    public ListObjectsV2Result getResult()
    '''
def ListAllMyBucketsHandler():
    '''    public ListAllMyBucketsHandler()
    '''
def getBuckets():
    '''    public List<Bucket> getBuckets()
    '''
def getOwner():
    '''    public Owner getOwner()
    '''
def AccessControlListHandler():
    '''    public AccessControlListHandler()
    '''
def getAccessControlList():
    '''    public AccessControlList getAccessControlList()
    '''
def BucketLoggingConfigurationHandler():
    '''    public BucketLoggingConfigurationHandler()
    '''
def getBucketLoggingConfiguration():
    '''    public BucketLoggingConfiguration getBucketLoggingConfiguration()
    '''
def BucketLocationHandler():
    '''    public BucketLocationHandler()
    '''
def getLocation():
    '''    public String getLocation()
    '''
def CopyObjectResultHandler():
    '''    public CopyObjectResultHandler()
    '''
def getLastModified():
    '''    public Date getLastModified()
    '''
def getVersionId():
    '''    public String getVersionId()
    public String getVersionId()
    '''
def setVersionId():
    '''    public void setVersionId(final String versionId)
    public void setVersionId(final String versionId)
    '''
def getExpirationTime():
    '''    public Date getExpirationTime()
    public Date getExpirationTime()
    '''
def setExpirationTime():
    '''    public void setExpirationTime(final Date expirationTime)
    public void setExpirationTime(final Date expirationTime)
    '''
def getExpirationTimeRuleId():
    '''    public String getExpirationTimeRuleId()
    public String getExpirationTimeRuleId()
    '''
def setExpirationTimeRuleId():
    '''    public void setExpirationTimeRuleId(final String expirationTimeRuleId)
    public void setExpirationTimeRuleId(final String expirationTimeRuleId)
    '''
def getETag():
    '''    public String getETag()
    '''
def getErrorCode():
    '''    public String getErrorCode()
    '''
def getErrorHostId():
    '''    public String getErrorHostId()
    '''
def getErrorMessage():
    '''    public String getErrorMessage()
    '''
def getErrorRequestId():
    '''    public String getErrorRequestId()
    '''
def isErrorResponse():
    '''    public boolean isErrorResponse()
    '''
def isRequesterCharged():
    '''    public boolean isRequesterCharged()
    public boolean isRequesterCharged()
    '''
def setRequesterCharged():
    '''    public void setRequesterCharged(final boolean isRequesterCharged)
    public void setRequesterCharged(final boolean isRequesterCharged)
    '''
def RequestPaymentConfigurationHandler():
    '''    public RequestPaymentConfigurationHandler()
    '''
def getConfiguration():
    '''    public RequestPaymentConfiguration getConfiguration()
    public BucketWebsiteConfiguration getConfiguration()
    public BucketVersioningConfiguration getConfiguration()
    public BucketAccelerateConfiguration getConfiguration()
    public BucketReplicationConfiguration getConfiguration()
    public BucketTaggingConfiguration getConfiguration()
    public BucketLifecycleConfiguration getConfiguration()
    public BucketCrossOriginConfiguration getConfiguration()
    '''
def ListVersionsHandler():
    '''    public ListVersionsHandler(final boolean shouldSDKDecodeResponse)
    '''
def getListing():
    '''    public VersionListing getListing()
    '''
def BucketWebsiteConfigurationHandler():
    '''    public BucketWebsiteConfigurationHandler()
    '''
def BucketVersioningConfigurationHandler():
    '''    public BucketVersioningConfigurationHandler()
    '''
def BucketAccelerateConfigurationHandler():
    '''    public BucketAccelerateConfigurationHandler()
    '''
def getCompleteMultipartUploadResult():
    '''    public CompleteMultipartUploadResult getCompleteMultipartUploadResult()
    '''
def getAmazonS3Exception():
    '''    public AmazonS3Exception getAmazonS3Exception()
    '''
def InitiateMultipartUploadHandler():
    '''    public InitiateMultipartUploadHandler()
    '''
def getInitiateMultipartUploadResult():
    '''    public InitiateMultipartUploadResult getInitiateMultipartUploadResult()
    '''
def ListMultipartUploadsHandler():
    '''    public ListMultipartUploadsHandler()
    '''
def getListMultipartUploadsResult():
    '''    public MultipartUploadListing getListMultipartUploadsResult()
    '''
def ListPartsHandler():
    '''    public ListPartsHandler()
    '''
def getListPartsResult():
    '''    public PartListing getListPartsResult()
    '''
def BucketReplicationConfigurationHandler():
    '''    public BucketReplicationConfigurationHandler()
    '''
def BucketTaggingConfigurationHandler():
    '''    public BucketTaggingConfigurationHandler()
    '''
def DeleteObjectsHandler():
    '''    public DeleteObjectsHandler()
    '''
def getDeleteObjectResult():
    '''    public DeleteObjectsResponse getDeleteObjectResult()
    '''
def BucketLifecycleConfigurationHandler():
    '''    public BucketLifecycleConfigurationHandler()
    '''
def BucketCrossOriginConfigurationHandler():
    '''    public BucketCrossOriginConfigurationHandler()
    '''
