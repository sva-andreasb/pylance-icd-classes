def setEndpoint():
'''public void setEndpoint(final String endpoint)
'''
pass
def setRegion():
'''public void setRegion(final Region region)
'''
pass
def setS3ClientOptions():
'''public void setS3ClientOptions(final S3ClientOptions clientOptions)
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
def listVersions():
'''public VersionListing listVersions(final String bucketName, final String prefix)
public VersionListing listVersions(final String bucketName, final String prefix, final String keyMarker, final String versionIdMarker, final String delimiter, final Integer maxResults)
public VersionListing listVersions(final ListVersionsRequest listVersionsRequest)
'''
pass
def listNextBatchOfVersions():
'''public VersionListing listNextBatchOfVersions(final VersionListing previousVersionListing)
public VersionListing listNextBatchOfVersions(final ListNextBatchOfVersionsRequest listNextBatchOfVersionsRequest)
'''
pass
def getS3AccountOwner():
'''public Owner getS3AccountOwner()
public Owner getS3AccountOwner(final GetS3AccountOwnerRequest getS3AccountOwnerRequest)
'''
pass
def doesBucketExist():
'''public boolean doesBucketExist(final String bucketName)
'''
pass
def headBucket():
'''public HeadBucketResult headBucket(final HeadBucketRequest headBucketRequest)
'''
pass
def listBuckets():
'''public List<Bucket> listBuckets()
public List<Bucket> listBuckets(final ListBucketsRequest listBucketsRequest)
'''
pass
def getBucketLocation():
'''public String getBucketLocation(final String bucketName)
public String getBucketLocation(final GetBucketLocationRequest getBucketLocationRequest)
'''
pass
def createBucket():
'''public Bucket createBucket(final CreateBucketRequest createBucketRequest)
public Bucket createBucket(final String bucketName)
public Bucket createBucket(final String bucketName, final com.amazonaws.services.s3.model.Region region)
public Bucket createBucket(final String bucketName, final String region)
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
public void setObjectAcl(final String bucketName, final String key, final String versionId, final CannedAccessControlList acl)
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
public void setBucketAcl(final String bucketName, final CannedAccessControlList cannedAcl)
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
def getBucketLoggingConfiguration():
'''public BucketLoggingConfiguration getBucketLoggingConfiguration(final String bucketName)
public BucketLoggingConfiguration getBucketLoggingConfiguration(final GetBucketLoggingConfigurationRequest getBucketLoggingConfigurationRequest)
'''
pass
def setBucketLoggingConfiguration():
'''public void setBucketLoggingConfiguration(final SetBucketLoggingConfigurationRequest setBucketLoggingConfigurationRequest)
'''
pass
def getBucketVersioningConfiguration():
'''public BucketVersioningConfiguration getBucketVersioningConfiguration(final String bucketName)
public BucketVersioningConfiguration getBucketVersioningConfiguration(final GetBucketVersioningConfigurationRequest getBucketVersioningConfigurationRequest)
'''
pass
def setBucketVersioningConfiguration():
'''public void setBucketVersioningConfiguration(final SetBucketVersioningConfigurationRequest setBucketVersioningConfigurationRequest)
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
def getBucketNotificationConfiguration():
'''public BucketNotificationConfiguration getBucketNotificationConfiguration(final String bucketName)
public BucketNotificationConfiguration getBucketNotificationConfiguration(final GetBucketNotificationConfigurationRequest getBucketNotificationConfigurationRequest)
'''
pass
def setBucketNotificationConfiguration():
'''public void setBucketNotificationConfiguration(final String bucketName, final BucketNotificationConfiguration bucketNotificationConfiguration)
public void setBucketNotificationConfiguration(final SetBucketNotificationConfigurationRequest setBucketNotificationConfigurationRequest)
'''
pass
def getBucketWebsiteConfiguration():
'''public BucketWebsiteConfiguration getBucketWebsiteConfiguration(final String bucketName)
public BucketWebsiteConfiguration getBucketWebsiteConfiguration(final GetBucketWebsiteConfigurationRequest getBucketWebsiteConfigurationRequest)
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
public URL generatePresignedUrl(final GeneratePresignedUrlRequest generatePresignedUrlRequest)
'''
pass
def initiateMultipartUpload():
'''public InitiateMultipartUploadResult initiateMultipartUpload(final InitiateMultipartUploadRequest request)
'''
pass
def uploadPart():
'''public UploadPartResult uploadPart(final UploadPartRequest request)
'''
pass
def listParts():
'''public PartListing listParts(final ListPartsRequest request)
'''
pass
def abortMultipartUpload():
'''public void abortMultipartUpload(final AbortMultipartUploadRequest request)
'''
pass
def completeMultipartUpload():
'''public CompleteMultipartUploadResult completeMultipartUpload(final CompleteMultipartUploadRequest request)
'''
pass
def listMultipartUploads():
'''public MultipartUploadListing listMultipartUploads(final ListMultipartUploadsRequest request)
'''
pass
def getCachedResponseMetadata():
'''public S3ResponseMetadata getCachedResponseMetadata(final AmazonWebServiceRequest request)
'''
pass
def restoreObject():
'''public void restoreObject(final String bucketName, final String key, final int expirationInDays)
public void restoreObject(final RestoreObjectRequest request)
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
public void deleteBucketReplicationConfiguration(final DeleteBucketReplicationConfigurationRequest request)
'''
pass
def doesObjectExist():
'''public boolean doesObjectExist(final String bucketName, final String objectName)
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
def getUrl():
'''public URL getUrl(final String bucketName, final String key)
'''
pass
