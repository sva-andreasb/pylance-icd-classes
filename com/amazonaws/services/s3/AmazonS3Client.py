S3_SERVICE_NAME = "String  s3""
def AmazonS3Client():
'''public AmazonS3Client()
public AmazonS3Client(final AWSCredentials awsCredentials)
public AmazonS3Client(final AWSCredentials awsCredentials, final ClientConfiguration clientConfiguration)
public AmazonS3Client(final AWSCredentialsProvider credentialsProvider)
public AmazonS3Client(final AWSCredentialsProvider credentialsProvider, final ClientConfiguration clientConfiguration)
public AmazonS3Client(final AWSCredentialsProvider credentialsProvider, final ClientConfiguration clientConfiguration, final RequestMetricCollector requestMetricCollector)
public AmazonS3Client(final ClientConfiguration clientConfiguration)
'''
pass
def getCredentials():
'''public AWSCredentials getCredentials()
'''
pass
def setEndpoint():
'''public synchronized void setEndpoint(final String endpoint)
'''
pass
def setRegion():
'''public synchronized void setRegion(final Region region)
'''
pass
def setS3ClientOptions():
'''public synchronized void setS3ClientOptions(final S3ClientOptions clientOptions)
'''
pass
def listNextBatchOfVersions():
'''public VersionListing listNextBatchOfVersions(final VersionListing previousVersionListing)
public VersionListing listNextBatchOfVersions(final ListNextBatchOfVersionsRequest listNextBatchOfVersionsRequest)
'''
pass
def listVersions():
'''public VersionListing listVersions(final String bucketName, final String prefix)
public VersionListing listVersions(final String bucketName, final String prefix, final String keyMarker, final String versionIdMarker, final String delimiter, final Integer maxKeys)
public VersionListing listVersions(final ListVersionsRequest listVersionsRequest)
'''
pass
def listObjects():
'''public ObjectListing listObjects(final String bucketName)
public ObjectListing listObjects(final String bucketName, final String prefix)
public ObjectListing listObjects(final ListObjectsRequest listObjectsRequest)
'''
pass
def listObjectsV2():
'''public ListObjectsV2Result listObjectsV2(final String bucketName)
public ListObjectsV2Result listObjectsV2(final String bucketName, final String prefix)
public ListObjectsV2Result listObjectsV2(final ListObjectsV2Request listObjectsV2Request)
'''
pass
def listNextBatchOfObjects():
'''public ObjectListing listNextBatchOfObjects(final ObjectListing previousObjectListing)
public ObjectListing listNextBatchOfObjects(final ListNextBatchOfObjectsRequest listNextBatchOfObjectsRequest)
'''
pass
def getS3AccountOwner():
'''public Owner getS3AccountOwner()
public Owner getS3AccountOwner(final GetS3AccountOwnerRequest getS3AccountOwnerRequest)
'''
pass
def listBuckets():
'''public List<Bucket> listBuckets(final ListBucketsRequest listBucketsRequest)
public List<Bucket> listBuckets()
'''
pass
def getBucketLocation():
'''public String getBucketLocation(final GetBucketLocationRequest getBucketLocationRequest)
public String getBucketLocation(final String bucketName)
'''
pass
def createBucket():
'''public Bucket createBucket(final String bucketName)
public Bucket createBucket(final String bucketName, final com.amazonaws.services.s3.model.Region region)
public Bucket createBucket(final String bucketName, final String region)
public Bucket createBucket(final CreateBucketRequest createBucketRequest)
'''
pass
def getObjectAcl():
'''public AccessControlList getObjectAcl(final String bucketName, final String key)
public AccessControlList getObjectAcl(final String bucketName, final String key, final String versionId)
public AccessControlList getObjectAcl(final GetObjectAclRequest getObjectAclRequest)
'''
pass
def setObjectAcl():
'''public void setObjectAcl(final String bucketName, final String key, final AccessControlList acl)
public void setObjectAcl(final String bucketName, final String key, final CannedAccessControlList acl)
public void setObjectAcl(final String bucketName, final String key, final String versionId, final AccessControlList acl)
public void setObjectAcl(final String bucketName, final String key, final String versionId, final AccessControlList acl, final RequestMetricCollector requestMetricCollector)
public void setObjectAcl(final String bucketName, final String key, final String versionId, final CannedAccessControlList acl)
public void setObjectAcl(final String bucketName, final String key, final String versionId, final CannedAccessControlList acl, final RequestMetricCollector requestMetricCollector)
public void setObjectAcl(final SetObjectAclRequest setObjectAclRequest)
'''
pass
def getBucketAcl():
'''public AccessControlList getBucketAcl(final String bucketName)
public AccessControlList getBucketAcl(final GetBucketAclRequest getBucketAclRequest)
'''
pass
def setBucketAcl():
'''public void setBucketAcl(final String bucketName, final AccessControlList acl)
public void setBucketAcl(final String bucketName, final AccessControlList acl, final RequestMetricCollector requestMetricCollector)
public void setBucketAcl(final String bucketName, final CannedAccessControlList cannedAcl)
public void setBucketAcl(final String bucketName, final CannedAccessControlList cannedAcl, final RequestMetricCollector requestMetricCollector)
public void setBucketAcl(final SetBucketAclRequest setBucketAclRequest)
'''
pass
def getObjectMetadata():
'''public ObjectMetadata getObjectMetadata(final String bucketName, final String key)
public ObjectMetadata getObjectMetadata(final GetObjectMetadataRequest getObjectMetadataRequest)
'''
pass
def getObject():
'''public S3Object getObject(final String bucketName, final String key)
public S3Object getObject(final GetObjectRequest getObjectRequest)
public ObjectMetadata getObject(final GetObjectRequest getObjectRequest, final File destinationFile)
'''
pass
def doesBucketExist():
'''public boolean doesBucketExist(final String bucketName)
'''
pass
def doesObjectExist():
'''public boolean doesObjectExist(final String bucketName, final String objectName)
'''
pass
def headBucket():
'''public HeadBucketResult headBucket(final HeadBucketRequest headBucketRequest)
'''
pass
def changeObjectStorageClass():
'''public void changeObjectStorageClass(final String bucketName, final String key, final StorageClass newStorageClass)
'''
pass
def setObjectRedirectLocation():
'''public void setObjectRedirectLocation(final String bucketName, final String key, final String newRedirectLocation)
'''
pass
def getS3ObjectStream():
'''public S3Object getS3ObjectStream()
'''
pass
def needIntegrityCheck():
'''public boolean needIntegrityCheck()
'''
pass
def deleteBucket():
'''public void deleteBucket(final String bucketName)
public void deleteBucket(final DeleteBucketRequest deleteBucketRequest)
'''
pass
def putObject():
'''public PutObjectResult putObject(final String bucketName, final String key, final File file)
public PutObjectResult putObject(final String bucketName, final String key, final InputStream input, final ObjectMetadata metadata)
public PutObjectResult putObject(final PutObjectRequest putObjectRequest)
'''
pass
def copyObject():
'''public CopyObjectResult copyObject(final String sourceBucketName, final String sourceKey, final String destinationBucketName, final String destinationKey)
public CopyObjectResult copyObject(final CopyObjectRequest copyObjectRequest)
'''
pass
def copyPart():
'''public CopyPartResult copyPart(final CopyPartRequest copyPartRequest)
'''
pass
def deleteObject():
'''public void deleteObject(final String bucketName, final String key)
public void deleteObject(final DeleteObjectRequest deleteObjectRequest)
'''
pass
def deleteObjects():
'''public DeleteObjectsResult deleteObjects(final DeleteObjectsRequest deleteObjectsRequest)
'''
pass
def deleteVersion():
'''public void deleteVersion(final String bucketName, final String key, final String versionId)
public void deleteVersion(final DeleteVersionRequest deleteVersionRequest)
'''
pass
def setBucketVersioningConfiguration():
'''public void setBucketVersioningConfiguration(final SetBucketVersioningConfigurationRequest setBucketVersioningConfigurationRequest)
'''
pass
def getBucketVersioningConfiguration():
'''public BucketVersioningConfiguration getBucketVersioningConfiguration(final String bucketName)
public BucketVersioningConfiguration getBucketVersioningConfiguration(final GetBucketVersioningConfigurationRequest getBucketVersioningConfigurationRequest)
'''
pass
def getBucketWebsiteConfiguration():
'''public BucketWebsiteConfiguration getBucketWebsiteConfiguration(final String bucketName)
public BucketWebsiteConfiguration getBucketWebsiteConfiguration(final GetBucketWebsiteConfigurationRequest getBucketWebsiteConfigurationRequest)
'''
pass
def getBucketLifecycleConfiguration():
'''public BucketLifecycleConfiguration getBucketLifecycleConfiguration(final String bucketName)
public BucketLifecycleConfiguration getBucketLifecycleConfiguration(final GetBucketLifecycleConfigurationRequest getBucketLifecycleConfigurationRequest)
'''
pass
def setBucketLifecycleConfiguration():
'''public void setBucketLifecycleConfiguration(final String bucketName, final BucketLifecycleConfiguration bucketLifecycleConfiguration)
public void setBucketLifecycleConfiguration(final SetBucketLifecycleConfigurationRequest setBucketLifecycleConfigurationRequest)
'''
pass
def deleteBucketLifecycleConfiguration():
'''public void deleteBucketLifecycleConfiguration(final String bucketName)
public void deleteBucketLifecycleConfiguration(final DeleteBucketLifecycleConfigurationRequest deleteBucketLifecycleConfigurationRequest)
'''
pass
def getBucketCrossOriginConfiguration():
'''public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(final String bucketName)
public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(final GetBucketCrossOriginConfigurationRequest getBucketCrossOriginConfigurationRequest)
'''
pass
def setBucketCrossOriginConfiguration():
'''public void setBucketCrossOriginConfiguration(final String bucketName, final BucketCrossOriginConfiguration bucketCrossOriginConfiguration)
public void setBucketCrossOriginConfiguration(final SetBucketCrossOriginConfigurationRequest setBucketCrossOriginConfigurationRequest)
'''
pass
def deleteBucketCrossOriginConfiguration():
'''public void deleteBucketCrossOriginConfiguration(final String bucketName)
public void deleteBucketCrossOriginConfiguration(final DeleteBucketCrossOriginConfigurationRequest deleteBucketCrossOriginConfigurationRequest)
'''
pass
def getBucketTaggingConfiguration():
'''public BucketTaggingConfiguration getBucketTaggingConfiguration(final String bucketName)
public BucketTaggingConfiguration getBucketTaggingConfiguration(final GetBucketTaggingConfigurationRequest getBucketTaggingConfigurationRequest)
'''
pass
def setBucketTaggingConfiguration():
'''public void setBucketTaggingConfiguration(final String bucketName, final BucketTaggingConfiguration bucketTaggingConfiguration)
public void setBucketTaggingConfiguration(final SetBucketTaggingConfigurationRequest setBucketTaggingConfigurationRequest)
'''
pass
def deleteBucketTaggingConfiguration():
'''public void deleteBucketTaggingConfiguration(final String bucketName)
public void deleteBucketTaggingConfiguration(final DeleteBucketTaggingConfigurationRequest deleteBucketTaggingConfigurationRequest)
'''
pass
def setBucketWebsiteConfiguration():
'''public void setBucketWebsiteConfiguration(final String bucketName, final BucketWebsiteConfiguration configuration)
public void setBucketWebsiteConfiguration(final SetBucketWebsiteConfigurationRequest setBucketWebsiteConfigurationRequest)
'''
pass
def deleteBucketWebsiteConfiguration():
'''public void deleteBucketWebsiteConfiguration(final String bucketName)
public void deleteBucketWebsiteConfiguration(final DeleteBucketWebsiteConfigurationRequest deleteBucketWebsiteConfigurationRequest)
'''
pass
def setBucketNotificationConfiguration():
'''public void setBucketNotificationConfiguration(final String bucketName, final BucketNotificationConfiguration bucketNotificationConfiguration)
public void setBucketNotificationConfiguration(final SetBucketNotificationConfigurationRequest setBucketNotificationConfigurationRequest)
'''
pass
def getBucketNotificationConfiguration():
'''public BucketNotificationConfiguration getBucketNotificationConfiguration(final String bucketName)
public BucketNotificationConfiguration getBucketNotificationConfiguration(final GetBucketNotificationConfigurationRequest getBucketNotificationConfigurationRequest)
'''
pass
def getBucketLoggingConfiguration():
'''public BucketLoggingConfiguration getBucketLoggingConfiguration(final String bucketName)
public BucketLoggingConfiguration getBucketLoggingConfiguration(final GetBucketLoggingConfigurationRequest getBucketLoggingConfigurationRequest)
'''
pass
def setBucketLoggingConfiguration():
'''public void setBucketLoggingConfiguration(final SetBucketLoggingConfigurationRequest setBucketLoggingConfigurationRequest)
'''
pass
def getBucketAccelerateConfiguration():
'''public BucketAccelerateConfiguration getBucketAccelerateConfiguration(final String bucketName)
public BucketAccelerateConfiguration getBucketAccelerateConfiguration(final GetBucketAccelerateConfigurationRequest getBucketAccelerateConfigurationRequest)
'''
pass
def setBucketAccelerateConfiguration():
'''public void setBucketAccelerateConfiguration(final String bucketName, final BucketAccelerateConfiguration accelerateConfiguration)
public void setBucketAccelerateConfiguration(final SetBucketAccelerateConfigurationRequest setBucketAccelerateConfigurationRequest)
'''
pass
def getBucketPolicy():
'''public BucketPolicy getBucketPolicy(final String bucketName)
public BucketPolicy getBucketPolicy(final GetBucketPolicyRequest getBucketPolicyRequest)
'''
pass
def setBucketPolicy():
'''public void setBucketPolicy(final String bucketName, final String policyText)
public void setBucketPolicy(final SetBucketPolicyRequest setBucketPolicyRequest)
'''
pass
def deleteBucketPolicy():
'''public void deleteBucketPolicy(final String bucketName)
public void deleteBucketPolicy(final DeleteBucketPolicyRequest deleteBucketPolicyRequest)
'''
pass
def generatePresignedUrl():
'''public URL generatePresignedUrl(final String bucketName, final String key, final Date expiration)
public URL generatePresignedUrl(final String bucketName, final String key, final Date expiration, final HttpMethod method)
public URL generatePresignedUrl(final GeneratePresignedUrlRequest req)
'''
pass
def abortMultipartUpload():
'''public void abortMultipartUpload(final AbortMultipartUploadRequest abortMultipartUploadRequest)
'''
pass
def completeMultipartUpload():
'''public CompleteMultipartUploadResult completeMultipartUpload(final CompleteMultipartUploadRequest completeMultipartUploadRequest)
'''
pass
def initiateMultipartUpload():
'''public InitiateMultipartUploadResult initiateMultipartUpload(final InitiateMultipartUploadRequest initiateMultipartUploadRequest)
'''
pass
def listMultipartUploads():
'''public MultipartUploadListing listMultipartUploads(final ListMultipartUploadsRequest listMultipartUploadsRequest)
'''
pass
def listParts():
'''public PartListing listParts(final ListPartsRequest listPartsRequest)
'''
pass
def uploadPart():
'''public UploadPartResult uploadPart(final UploadPartRequest uploadPartRequest)
'''
pass
def getCachedResponseMetadata():
'''public S3ResponseMetadata getCachedResponseMetadata(final AmazonWebServiceRequest request)
'''
pass
def restoreObject():
'''public void restoreObject(final RestoreObjectRequest restoreObjectRequest)
public void restoreObject(final String bucketName, final String key, final int expirationInDays)
'''
pass
def getResourceUrl():
'''public String getResourceUrl(final String bucketName, final String key)
'''
pass
def getUrl():
'''public URL getUrl(final String bucketName, final String key)
'''
pass
def enableRequesterPays():
'''public void enableRequesterPays(final String bucketName)
'''
pass
def disableRequesterPays():
'''public void disableRequesterPays(final String bucketName)
'''
pass
def isRequesterPaysEnabled():
'''public boolean isRequesterPaysEnabled(final String bucketName)
'''
pass
def setBucketReplicationConfiguration():
'''public void setBucketReplicationConfiguration(final String bucketName, final BucketReplicationConfiguration configuration)
public void setBucketReplicationConfiguration(final SetBucketReplicationConfigurationRequest setBucketReplicationConfigurationRequest)
'''
pass
def getBucketReplicationConfiguration():
'''public BucketReplicationConfiguration getBucketReplicationConfiguration(final String bucketName)
public BucketReplicationConfiguration getBucketReplicationConfiguration(final GetBucketReplicationConfigurationRequest getBucketReplicationConfigurationRequest)
'''
pass
def deleteBucketReplicationConfiguration():
'''public void deleteBucketReplicationConfiguration(final String bucketName)
public void deleteBucketReplicationConfiguration(final DeleteBucketReplicationConfigurationRequest deleteBucketReplicationConfigurationRequest)
'''
pass
