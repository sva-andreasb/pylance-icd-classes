S3_SERVICE_NAME = "String  \"s3\""
def AmazonS3Client():
    '''public AmazonS3Client()
    public AmazonS3Client(final AWSCredentials awsCredentials)
    public AmazonS3Client(final AWSCredentials awsCredentials, final ClientConfiguration clientConfiguration)
    public AmazonS3Client(final AWSCredentialsProvider credentialsProvider)
    public AmazonS3Client(final AWSCredentialsProvider credentialsProvider, final ClientConfiguration clientConfiguration)
    public AmazonS3Client(final AWSCredentialsProvider credentialsProvider, final ClientConfiguration clientConfiguration, final RequestMetricCollector requestMetricCollector)
    public AmazonS3Client(final ClientConfiguration clientConfiguration)
    '''
def getCredentials():
    '''public AWSCredentials getCredentials()
    '''
def setEndpoint():
    '''public synchronized void setEndpoint(final String endpoint)
    '''
def setRegion():
    '''public synchronized void setRegion(final Region region)
    '''
def setS3ClientOptions():
    '''public synchronized void setS3ClientOptions(final S3ClientOptions clientOptions)
    '''
def listNextBatchOfVersions():
    '''public VersionListing listNextBatchOfVersions(final VersionListing previousVersionListing)
    public VersionListing listNextBatchOfVersions(final ListNextBatchOfVersionsRequest listNextBatchOfVersionsRequest)
    '''
def listVersions():
    '''public VersionListing listVersions(final String bucketName, final String prefix)
    public VersionListing listVersions(final String bucketName, final String prefix, final String keyMarker, final String versionIdMarker, final String delimiter, final Integer maxKeys)
    public VersionListing listVersions(final ListVersionsRequest listVersionsRequest)
    '''
def listObjects():
    '''public ObjectListing listObjects(final String bucketName)
    public ObjectListing listObjects(final String bucketName, final String prefix)
    public ObjectListing listObjects(final ListObjectsRequest listObjectsRequest)
    '''
def listObjectsV2():
    '''public ListObjectsV2Result listObjectsV2(final String bucketName)
    public ListObjectsV2Result listObjectsV2(final String bucketName, final String prefix)
    public ListObjectsV2Result listObjectsV2(final ListObjectsV2Request listObjectsV2Request)
    '''
def listNextBatchOfObjects():
    '''public ObjectListing listNextBatchOfObjects(final ObjectListing previousObjectListing)
    public ObjectListing listNextBatchOfObjects(final ListNextBatchOfObjectsRequest listNextBatchOfObjectsRequest)
    '''
def getS3AccountOwner():
    '''public Owner getS3AccountOwner()
    public Owner getS3AccountOwner(final GetS3AccountOwnerRequest getS3AccountOwnerRequest)
    '''
def listBuckets():
    '''public List<Bucket> listBuckets(final ListBucketsRequest listBucketsRequest)
    public List<Bucket> listBuckets()
    '''
def getBucketLocation():
    '''public String getBucketLocation(final GetBucketLocationRequest getBucketLocationRequest)
    public String getBucketLocation(final String bucketName)
    '''
def createBucket():
    '''public Bucket createBucket(final String bucketName)
    public Bucket createBucket(final String bucketName, final com.amazonaws.services.s3.model.Region region)
    public Bucket createBucket(final String bucketName, final String region)
    public Bucket createBucket(final CreateBucketRequest createBucketRequest)
    '''
def getObjectAcl():
    '''public AccessControlList getObjectAcl(final String bucketName, final String key)
    public AccessControlList getObjectAcl(final String bucketName, final String key, final String versionId)
    public AccessControlList getObjectAcl(final GetObjectAclRequest getObjectAclRequest)
    '''
def setObjectAcl():
    '''public void setObjectAcl(final String bucketName, final String key, final AccessControlList acl)
    public void setObjectAcl(final String bucketName, final String key, final CannedAccessControlList acl)
    public void setObjectAcl(final String bucketName, final String key, final String versionId, final AccessControlList acl)
    public void setObjectAcl(final String bucketName, final String key, final String versionId, final AccessControlList acl, final RequestMetricCollector requestMetricCollector)
    public void setObjectAcl(final String bucketName, final String key, final String versionId, final CannedAccessControlList acl)
    public void setObjectAcl(final String bucketName, final String key, final String versionId, final CannedAccessControlList acl, final RequestMetricCollector requestMetricCollector)
    public void setObjectAcl(final SetObjectAclRequest setObjectAclRequest)
    '''
def getBucketAcl():
    '''public AccessControlList getBucketAcl(final String bucketName)
    public AccessControlList getBucketAcl(final GetBucketAclRequest getBucketAclRequest)
    '''
def setBucketAcl():
    '''public void setBucketAcl(final String bucketName, final AccessControlList acl)
    public void setBucketAcl(final String bucketName, final AccessControlList acl, final RequestMetricCollector requestMetricCollector)
    public void setBucketAcl(final String bucketName, final CannedAccessControlList cannedAcl)
    public void setBucketAcl(final String bucketName, final CannedAccessControlList cannedAcl, final RequestMetricCollector requestMetricCollector)
    public void setBucketAcl(final SetBucketAclRequest setBucketAclRequest)
    '''
def getObjectMetadata():
    '''public ObjectMetadata getObjectMetadata(final String bucketName, final String key)
    public ObjectMetadata getObjectMetadata(final GetObjectMetadataRequest getObjectMetadataRequest)
    '''
def getObject():
    '''public S3Object getObject(final String bucketName, final String key)
    public S3Object getObject(final GetObjectRequest getObjectRequest)
    public ObjectMetadata getObject(final GetObjectRequest getObjectRequest, final File destinationFile)
    '''
def doesBucketExist():
    '''public boolean doesBucketExist(final String bucketName)
    '''
def doesObjectExist():
    '''public boolean doesObjectExist(final String bucketName, final String objectName)
    '''
def headBucket():
    '''public HeadBucketResult headBucket(final HeadBucketRequest headBucketRequest)
    '''
def changeObjectStorageClass():
    '''public void changeObjectStorageClass(final String bucketName, final String key, final StorageClass newStorageClass)
    '''
def setObjectRedirectLocation():
    '''public void setObjectRedirectLocation(final String bucketName, final String key, final String newRedirectLocation)
    '''
def getS3ObjectStream():
    '''public S3Object getS3ObjectStream()
    '''
def needIntegrityCheck():
    '''public boolean needIntegrityCheck()
    '''
def deleteBucket():
    '''public void deleteBucket(final String bucketName)
    public void deleteBucket(final DeleteBucketRequest deleteBucketRequest)
    '''
def putObject():
    '''public PutObjectResult putObject(final String bucketName, final String key, final File file)
    public PutObjectResult putObject(final String bucketName, final String key, final InputStream input, final ObjectMetadata metadata)
    public PutObjectResult putObject(final PutObjectRequest putObjectRequest)
    '''
def copyObject():
    '''public CopyObjectResult copyObject(final String sourceBucketName, final String sourceKey, final String destinationBucketName, final String destinationKey)
    public CopyObjectResult copyObject(final CopyObjectRequest copyObjectRequest)
    '''
def copyPart():
    '''public CopyPartResult copyPart(final CopyPartRequest copyPartRequest)
    '''
def deleteObject():
    '''public void deleteObject(final String bucketName, final String key)
    public void deleteObject(final DeleteObjectRequest deleteObjectRequest)
    '''
def deleteObjects():
    '''public DeleteObjectsResult deleteObjects(final DeleteObjectsRequest deleteObjectsRequest)
    '''
def deleteVersion():
    '''public void deleteVersion(final String bucketName, final String key, final String versionId)
    public void deleteVersion(final DeleteVersionRequest deleteVersionRequest)
    '''
def setBucketVersioningConfiguration():
    '''public void setBucketVersioningConfiguration(final SetBucketVersioningConfigurationRequest setBucketVersioningConfigurationRequest)
    '''
def getBucketVersioningConfiguration():
    '''public BucketVersioningConfiguration getBucketVersioningConfiguration(final String bucketName)
    public BucketVersioningConfiguration getBucketVersioningConfiguration(final GetBucketVersioningConfigurationRequest getBucketVersioningConfigurationRequest)
    '''
def getBucketWebsiteConfiguration():
    '''public BucketWebsiteConfiguration getBucketWebsiteConfiguration(final String bucketName)
    public BucketWebsiteConfiguration getBucketWebsiteConfiguration(final GetBucketWebsiteConfigurationRequest getBucketWebsiteConfigurationRequest)
    '''
def getBucketLifecycleConfiguration():
    '''public BucketLifecycleConfiguration getBucketLifecycleConfiguration(final String bucketName)
    public BucketLifecycleConfiguration getBucketLifecycleConfiguration(final GetBucketLifecycleConfigurationRequest getBucketLifecycleConfigurationRequest)
    '''
def setBucketLifecycleConfiguration():
    '''public void setBucketLifecycleConfiguration(final String bucketName, final BucketLifecycleConfiguration bucketLifecycleConfiguration)
    public void setBucketLifecycleConfiguration(final SetBucketLifecycleConfigurationRequest setBucketLifecycleConfigurationRequest)
    '''
def deleteBucketLifecycleConfiguration():
    '''public void deleteBucketLifecycleConfiguration(final String bucketName)
    public void deleteBucketLifecycleConfiguration(final DeleteBucketLifecycleConfigurationRequest deleteBucketLifecycleConfigurationRequest)
    '''
def getBucketCrossOriginConfiguration():
    '''public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(final String bucketName)
    public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(final GetBucketCrossOriginConfigurationRequest getBucketCrossOriginConfigurationRequest)
    '''
def setBucketCrossOriginConfiguration():
    '''public void setBucketCrossOriginConfiguration(final String bucketName, final BucketCrossOriginConfiguration bucketCrossOriginConfiguration)
    public void setBucketCrossOriginConfiguration(final SetBucketCrossOriginConfigurationRequest setBucketCrossOriginConfigurationRequest)
    '''
def deleteBucketCrossOriginConfiguration():
    '''public void deleteBucketCrossOriginConfiguration(final String bucketName)
    public void deleteBucketCrossOriginConfiguration(final DeleteBucketCrossOriginConfigurationRequest deleteBucketCrossOriginConfigurationRequest)
    '''
def getBucketTaggingConfiguration():
    '''public BucketTaggingConfiguration getBucketTaggingConfiguration(final String bucketName)
    public BucketTaggingConfiguration getBucketTaggingConfiguration(final GetBucketTaggingConfigurationRequest getBucketTaggingConfigurationRequest)
    '''
def setBucketTaggingConfiguration():
    '''public void setBucketTaggingConfiguration(final String bucketName, final BucketTaggingConfiguration bucketTaggingConfiguration)
    public void setBucketTaggingConfiguration(final SetBucketTaggingConfigurationRequest setBucketTaggingConfigurationRequest)
    '''
def deleteBucketTaggingConfiguration():
    '''public void deleteBucketTaggingConfiguration(final String bucketName)
    public void deleteBucketTaggingConfiguration(final DeleteBucketTaggingConfigurationRequest deleteBucketTaggingConfigurationRequest)
    '''
def setBucketWebsiteConfiguration():
    '''public void setBucketWebsiteConfiguration(final String bucketName, final BucketWebsiteConfiguration configuration)
    public void setBucketWebsiteConfiguration(final SetBucketWebsiteConfigurationRequest setBucketWebsiteConfigurationRequest)
    '''
def deleteBucketWebsiteConfiguration():
    '''public void deleteBucketWebsiteConfiguration(final String bucketName)
    public void deleteBucketWebsiteConfiguration(final DeleteBucketWebsiteConfigurationRequest deleteBucketWebsiteConfigurationRequest)
    '''
def setBucketNotificationConfiguration():
    '''public void setBucketNotificationConfiguration(final String bucketName, final BucketNotificationConfiguration bucketNotificationConfiguration)
    public void setBucketNotificationConfiguration(final SetBucketNotificationConfigurationRequest setBucketNotificationConfigurationRequest)
    '''
def getBucketNotificationConfiguration():
    '''public BucketNotificationConfiguration getBucketNotificationConfiguration(final String bucketName)
    public BucketNotificationConfiguration getBucketNotificationConfiguration(final GetBucketNotificationConfigurationRequest getBucketNotificationConfigurationRequest)
    '''
def getBucketLoggingConfiguration():
    '''public BucketLoggingConfiguration getBucketLoggingConfiguration(final String bucketName)
    public BucketLoggingConfiguration getBucketLoggingConfiguration(final GetBucketLoggingConfigurationRequest getBucketLoggingConfigurationRequest)
    '''
def setBucketLoggingConfiguration():
    '''public void setBucketLoggingConfiguration(final SetBucketLoggingConfigurationRequest setBucketLoggingConfigurationRequest)
    '''
def getBucketAccelerateConfiguration():
    '''public BucketAccelerateConfiguration getBucketAccelerateConfiguration(final String bucketName)
    public BucketAccelerateConfiguration getBucketAccelerateConfiguration(final GetBucketAccelerateConfigurationRequest getBucketAccelerateConfigurationRequest)
    '''
def setBucketAccelerateConfiguration():
    '''public void setBucketAccelerateConfiguration(final String bucketName, final BucketAccelerateConfiguration accelerateConfiguration)
    public void setBucketAccelerateConfiguration(final SetBucketAccelerateConfigurationRequest setBucketAccelerateConfigurationRequest)
    '''
def getBucketPolicy():
    '''public BucketPolicy getBucketPolicy(final String bucketName)
    public BucketPolicy getBucketPolicy(final GetBucketPolicyRequest getBucketPolicyRequest)
    '''
def setBucketPolicy():
    '''public void setBucketPolicy(final String bucketName, final String policyText)
    public void setBucketPolicy(final SetBucketPolicyRequest setBucketPolicyRequest)
    '''
def deleteBucketPolicy():
    '''public void deleteBucketPolicy(final String bucketName)
    public void deleteBucketPolicy(final DeleteBucketPolicyRequest deleteBucketPolicyRequest)
    '''
def generatePresignedUrl():
    '''public URL generatePresignedUrl(final String bucketName, final String key, final Date expiration)
    public URL generatePresignedUrl(final String bucketName, final String key, final Date expiration, final HttpMethod method)
    public URL generatePresignedUrl(final GeneratePresignedUrlRequest req)
    '''
def abortMultipartUpload():
    '''public void abortMultipartUpload(final AbortMultipartUploadRequest abortMultipartUploadRequest)
    '''
def completeMultipartUpload():
    '''public CompleteMultipartUploadResult completeMultipartUpload(final CompleteMultipartUploadRequest completeMultipartUploadRequest)
    '''
def initiateMultipartUpload():
    '''public InitiateMultipartUploadResult initiateMultipartUpload(final InitiateMultipartUploadRequest initiateMultipartUploadRequest)
    '''
def listMultipartUploads():
    '''public MultipartUploadListing listMultipartUploads(final ListMultipartUploadsRequest listMultipartUploadsRequest)
    '''
def listParts():
    '''public PartListing listParts(final ListPartsRequest listPartsRequest)
    '''
def uploadPart():
    '''public UploadPartResult uploadPart(final UploadPartRequest uploadPartRequest)
    '''
def getCachedResponseMetadata():
    '''public S3ResponseMetadata getCachedResponseMetadata(final AmazonWebServiceRequest request)
    '''
def restoreObject():
    '''public void restoreObject(final RestoreObjectRequest restoreObjectRequest)
    public void restoreObject(final String bucketName, final String key, final int expirationInDays)
    '''
def getResourceUrl():
    '''public String getResourceUrl(final String bucketName, final String key)
    '''
def getUrl():
    '''public URL getUrl(final String bucketName, final String key)
    '''
def enableRequesterPays():
    '''public void enableRequesterPays(final String bucketName)
    '''
def disableRequesterPays():
    '''public void disableRequesterPays(final String bucketName)
    '''
def isRequesterPaysEnabled():
    '''public boolean isRequesterPaysEnabled(final String bucketName)
    '''
def setBucketReplicationConfiguration():
    '''public void setBucketReplicationConfiguration(final String bucketName, final BucketReplicationConfiguration configuration)
    public void setBucketReplicationConfiguration(final SetBucketReplicationConfigurationRequest setBucketReplicationConfigurationRequest)
    '''
def getBucketReplicationConfiguration():
    '''public BucketReplicationConfiguration getBucketReplicationConfiguration(final String bucketName)
    public BucketReplicationConfiguration getBucketReplicationConfiguration(final GetBucketReplicationConfigurationRequest getBucketReplicationConfigurationRequest)
    '''
def deleteBucketReplicationConfiguration():
    '''public void deleteBucketReplicationConfiguration(final String bucketName)
    public void deleteBucketReplicationConfiguration(final DeleteBucketReplicationConfigurationRequest deleteBucketReplicationConfigurationRequest)
    '''
