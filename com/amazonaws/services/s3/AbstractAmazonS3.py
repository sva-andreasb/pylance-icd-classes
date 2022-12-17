def setEndpoint():
    '''returns None\n\n
    setEndpoint(final String endpoint)\n
    '''
def setRegion():
    '''returns None\n\n
    setRegion(final Region region)\n
    '''
def setS3ClientOptions():
    '''returns None\n\n
    setS3ClientOptions(final S3ClientOptions clientOptions)\n
    '''
def changeObjectStorageClass():
    '''returns None\n\n
    changeObjectStorageClass(final String bucketName, final String key, final StorageClass newStorageClass)\n
    '''
def setObjectRedirectLocation():
    '''returns None\n\n
    setObjectRedirectLocation(final String bucketName, final String key, final String newRedirectLocation)\n
    '''
def listObjects():
    '''returns ObjectListing\n\n
    listObjects(final String bucketName)\n
    listObjects(final String bucketName, final String prefix)\n
    listObjects(final ListObjectsRequest listObjectsRequest)\n
    '''
def listObjectsV2():
    '''returns ListObjectsV2Result\n\n
    listObjectsV2(final String bucketName)\n
    listObjectsV2(final String bucketName, final String prefix)\n
    listObjectsV2(final ListObjectsV2Request listObjectsV2Request)\n
    '''
def listNextBatchOfObjects():
    '''returns ObjectListing\n\n
    listNextBatchOfObjects(final ObjectListing previousObjectListing)\n
    listNextBatchOfObjects(final ListNextBatchOfObjectsRequest listNextBatchOfObjectsRequest)\n
    '''
def listVersions():
    '''returns VersionListing\n\n
    listVersions(final String bucketName, final String prefix)\n
    listVersions(final String bucketName, final String prefix, final String keyMarker, final String versionIdMarker, final String delimiter, final Integer maxResults)\n
    listVersions(final ListVersionsRequest listVersionsRequest)\n
    '''
def listNextBatchOfVersions():
    '''returns VersionListing\n\n
    listNextBatchOfVersions(final VersionListing previousVersionListing)\n
    listNextBatchOfVersions(final ListNextBatchOfVersionsRequest listNextBatchOfVersionsRequest)\n
    '''
def getS3AccountOwner():
    '''returns Owner\n\n
    getS3AccountOwner()\n
    getS3AccountOwner(final GetS3AccountOwnerRequest getS3AccountOwnerRequest)\n
    '''
def doesBucketExist():
    '''returns boolean\n\n
    doesBucketExist(final String bucketName)\n
    '''
def headBucket():
    '''returns HeadBucketResult\n\n
    headBucket(final HeadBucketRequest headBucketRequest)\n
    '''
def listBuckets():
    '''returns List<Bucket>\n\n
    listBuckets()\n
    listBuckets(final ListBucketsRequest listBucketsRequest)\n
    '''
def getBucketLocation():
    '''returns String\n\n
    getBucketLocation(final String bucketName)\n
    getBucketLocation(final GetBucketLocationRequest getBucketLocationRequest)\n
    '''
def createBucket():
    '''returns Bucket\n\n
    createBucket(final CreateBucketRequest createBucketRequest)\n
    createBucket(final String bucketName)\n
    createBucket(final String bucketName, final com.amazonaws.services.s3.model.Region region)\n
    createBucket(final String bucketName, final String region)\n
    '''
def getObjectAcl():
    '''returns AccessControlList\n\n
    getObjectAcl(final String bucketName, final String key)\n
    getObjectAcl(final String bucketName, final String key, final String versionId)\n
    getObjectAcl(final GetObjectAclRequest getObjectAclRequest)\n
    '''
def setObjectAcl():
    '''returns None\n\n
    setObjectAcl(final String bucketName, final String key, final AccessControlList acl)\n
    setObjectAcl(final String bucketName, final String key, final CannedAccessControlList acl)\n
    setObjectAcl(final String bucketName, final String key, final String versionId, final AccessControlList acl)\n
    setObjectAcl(final String bucketName, final String key, final String versionId, final CannedAccessControlList acl)\n
    setObjectAcl(final SetObjectAclRequest setObjectAclRequest)\n
    '''
def getBucketAcl():
    '''returns AccessControlList\n\n
    getBucketAcl(final String bucketName)\n
    getBucketAcl(final GetBucketAclRequest getBucketAclRequest)\n
    '''
def setBucketAcl():
    '''returns None\n\n
    setBucketAcl(final String bucketName, final AccessControlList acl)\n
    setBucketAcl(final String bucketName, final CannedAccessControlList cannedAcl)\n
    setBucketAcl(final SetBucketAclRequest setBucketAclRequest)\n
    '''
def getObjectMetadata():
    '''returns ObjectMetadata\n\n
    getObjectMetadata(final String bucketName, final String key)\n
    getObjectMetadata(final GetObjectMetadataRequest getObjectMetadataRequest)\n
    '''
def getObject():
    '''returns ObjectMetadata\n\n
    getObject(final String bucketName, final String key)\n
    getObject(final GetObjectRequest getObjectRequest)\n
    getObject(final GetObjectRequest getObjectRequest, final File destinationFile)\n
    '''
def deleteBucket():
    '''returns None\n\n
    deleteBucket(final String bucketName)\n
    deleteBucket(final DeleteBucketRequest deleteBucketRequest)\n
    '''
def putObject():
    '''returns PutObjectResult\n\n
    putObject(final String bucketName, final String key, final File file)\n
    putObject(final String bucketName, final String key, final InputStream input, final ObjectMetadata metadata)\n
    putObject(final PutObjectRequest putObjectRequest)\n
    '''
def copyObject():
    '''returns CopyObjectResult\n\n
    copyObject(final String sourceBucketName, final String sourceKey, final String destinationBucketName, final String destinationKey)\n
    copyObject(final CopyObjectRequest copyObjectRequest)\n
    '''
def copyPart():
    '''returns CopyPartResult\n\n
    copyPart(final CopyPartRequest copyPartRequest)\n
    '''
def deleteObject():
    '''returns None\n\n
    deleteObject(final String bucketName, final String key)\n
    deleteObject(final DeleteObjectRequest deleteObjectRequest)\n
    '''
def deleteObjects():
    '''returns DeleteObjectsResult\n\n
    deleteObjects(final DeleteObjectsRequest deleteObjectsRequest)\n
    '''
def deleteVersion():
    '''returns None\n\n
    deleteVersion(final String bucketName, final String key, final String versionId)\n
    deleteVersion(final DeleteVersionRequest deleteVersionRequest)\n
    '''
def getBucketLoggingConfiguration():
    '''returns BucketLoggingConfiguration\n\n
    getBucketLoggingConfiguration(final String bucketName)\n
    getBucketLoggingConfiguration(final GetBucketLoggingConfigurationRequest getBucketLoggingConfigurationRequest)\n
    '''
def setBucketLoggingConfiguration():
    '''returns None\n\n
    setBucketLoggingConfiguration(final SetBucketLoggingConfigurationRequest setBucketLoggingConfigurationRequest)\n
    '''
def getBucketVersioningConfiguration():
    '''returns BucketVersioningConfiguration\n\n
    getBucketVersioningConfiguration(final String bucketName)\n
    getBucketVersioningConfiguration(final GetBucketVersioningConfigurationRequest getBucketVersioningConfigurationRequest)\n
    '''
def setBucketVersioningConfiguration():
    '''returns None\n\n
    setBucketVersioningConfiguration(final SetBucketVersioningConfigurationRequest setBucketVersioningConfigurationRequest)\n
    '''
def getBucketLifecycleConfiguration():
    '''returns BucketLifecycleConfiguration\n\n
    getBucketLifecycleConfiguration(final String bucketName)\n
    getBucketLifecycleConfiguration(final GetBucketLifecycleConfigurationRequest getBucketLifecycleConfigurationRequest)\n
    '''
def setBucketLifecycleConfiguration():
    '''returns None\n\n
    setBucketLifecycleConfiguration(final String bucketName, final BucketLifecycleConfiguration bucketLifecycleConfiguration)\n
    setBucketLifecycleConfiguration(final SetBucketLifecycleConfigurationRequest setBucketLifecycleConfigurationRequest)\n
    '''
def deleteBucketLifecycleConfiguration():
    '''returns None\n\n
    deleteBucketLifecycleConfiguration(final String bucketName)\n
    deleteBucketLifecycleConfiguration(final DeleteBucketLifecycleConfigurationRequest deleteBucketLifecycleConfigurationRequest)\n
    '''
def getBucketCrossOriginConfiguration():
    '''returns BucketCrossOriginConfiguration\n\n
    getBucketCrossOriginConfiguration(final String bucketName)\n
    getBucketCrossOriginConfiguration(final GetBucketCrossOriginConfigurationRequest getBucketCrossOriginConfigurationRequest)\n
    '''
def setBucketCrossOriginConfiguration():
    '''returns None\n\n
    setBucketCrossOriginConfiguration(final String bucketName, final BucketCrossOriginConfiguration bucketCrossOriginConfiguration)\n
    setBucketCrossOriginConfiguration(final SetBucketCrossOriginConfigurationRequest setBucketCrossOriginConfigurationRequest)\n
    '''
def deleteBucketCrossOriginConfiguration():
    '''returns None\n\n
    deleteBucketCrossOriginConfiguration(final String bucketName)\n
    deleteBucketCrossOriginConfiguration(final DeleteBucketCrossOriginConfigurationRequest deleteBucketCrossOriginConfigurationRequest)\n
    '''
def getBucketTaggingConfiguration():
    '''returns BucketTaggingConfiguration\n\n
    getBucketTaggingConfiguration(final String bucketName)\n
    getBucketTaggingConfiguration(final GetBucketTaggingConfigurationRequest getBucketTaggingConfigurationRequest)\n
    '''
def setBucketTaggingConfiguration():
    '''returns None\n\n
    setBucketTaggingConfiguration(final String bucketName, final BucketTaggingConfiguration bucketTaggingConfiguration)\n
    setBucketTaggingConfiguration(final SetBucketTaggingConfigurationRequest setBucketTaggingConfigurationRequest)\n
    '''
def deleteBucketTaggingConfiguration():
    '''returns None\n\n
    deleteBucketTaggingConfiguration(final String bucketName)\n
    deleteBucketTaggingConfiguration(final DeleteBucketTaggingConfigurationRequest deleteBucketTaggingConfigurationRequest)\n
    '''
def getBucketNotificationConfiguration():
    '''returns BucketNotificationConfiguration\n\n
    getBucketNotificationConfiguration(final String bucketName)\n
    getBucketNotificationConfiguration(final GetBucketNotificationConfigurationRequest getBucketNotificationConfigurationRequest)\n
    '''
def setBucketNotificationConfiguration():
    '''returns None\n\n
    setBucketNotificationConfiguration(final String bucketName, final BucketNotificationConfiguration bucketNotificationConfiguration)\n
    setBucketNotificationConfiguration(final SetBucketNotificationConfigurationRequest setBucketNotificationConfigurationRequest)\n
    '''
def getBucketWebsiteConfiguration():
    '''returns BucketWebsiteConfiguration\n\n
    getBucketWebsiteConfiguration(final String bucketName)\n
    getBucketWebsiteConfiguration(final GetBucketWebsiteConfigurationRequest getBucketWebsiteConfigurationRequest)\n
    '''
def setBucketWebsiteConfiguration():
    '''returns None\n\n
    setBucketWebsiteConfiguration(final String bucketName, final BucketWebsiteConfiguration configuration)\n
    setBucketWebsiteConfiguration(final SetBucketWebsiteConfigurationRequest setBucketWebsiteConfigurationRequest)\n
    '''
def deleteBucketWebsiteConfiguration():
    '''returns None\n\n
    deleteBucketWebsiteConfiguration(final String bucketName)\n
    deleteBucketWebsiteConfiguration(final DeleteBucketWebsiteConfigurationRequest deleteBucketWebsiteConfigurationRequest)\n
    '''
def getBucketPolicy():
    '''returns BucketPolicy\n\n
    getBucketPolicy(final String bucketName)\n
    getBucketPolicy(final GetBucketPolicyRequest getBucketPolicyRequest)\n
    '''
def setBucketPolicy():
    '''returns None\n\n
    setBucketPolicy(final String bucketName, final String policyText)\n
    setBucketPolicy(final SetBucketPolicyRequest setBucketPolicyRequest)\n
    '''
def deleteBucketPolicy():
    '''returns None\n\n
    deleteBucketPolicy(final String bucketName)\n
    deleteBucketPolicy(final DeleteBucketPolicyRequest deleteBucketPolicyRequest)\n
    '''
def generatePresignedUrl():
    '''returns URL\n\n
    generatePresignedUrl(final String bucketName, final String key, final Date expiration)\n
    generatePresignedUrl(final String bucketName, final String key, final Date expiration, final HttpMethod method)\n
    generatePresignedUrl(final GeneratePresignedUrlRequest generatePresignedUrlRequest)\n
    '''
def initiateMultipartUpload():
    '''returns InitiateMultipartUploadResult\n\n
    initiateMultipartUpload(final InitiateMultipartUploadRequest request)\n
    '''
def uploadPart():
    '''returns UploadPartResult\n\n
    uploadPart(final UploadPartRequest request)\n
    '''
def listParts():
    '''returns PartListing\n\n
    listParts(final ListPartsRequest request)\n
    '''
def abortMultipartUpload():
    '''returns None\n\n
    abortMultipartUpload(final AbortMultipartUploadRequest request)\n
    '''
def completeMultipartUpload():
    '''returns CompleteMultipartUploadResult\n\n
    completeMultipartUpload(final CompleteMultipartUploadRequest request)\n
    '''
def listMultipartUploads():
    '''returns MultipartUploadListing\n\n
    listMultipartUploads(final ListMultipartUploadsRequest request)\n
    '''
def getCachedResponseMetadata():
    '''returns S3ResponseMetadata\n\n
    getCachedResponseMetadata(final AmazonWebServiceRequest request)\n
    '''
def restoreObject():
    '''returns None\n\n
    restoreObject(final String bucketName, final String key, final int expirationInDays)\n
    restoreObject(final RestoreObjectRequest request)\n
    '''
def enableRequesterPays():
    '''returns None\n\n
    enableRequesterPays(final String bucketName)\n
    '''
def disableRequesterPays():
    '''returns None\n\n
    disableRequesterPays(final String bucketName)\n
    '''
def isRequesterPaysEnabled():
    '''returns boolean\n\n
    isRequesterPaysEnabled(final String bucketName)\n
    '''
def setBucketReplicationConfiguration():
    '''returns None\n\n
    setBucketReplicationConfiguration(final String bucketName, final BucketReplicationConfiguration configuration)\n
    setBucketReplicationConfiguration(final SetBucketReplicationConfigurationRequest setBucketReplicationConfigurationRequest)\n
    '''
def getBucketReplicationConfiguration():
    '''returns BucketReplicationConfiguration\n\n
    getBucketReplicationConfiguration(final String bucketName)\n
    getBucketReplicationConfiguration(final GetBucketReplicationConfigurationRequest getBucketReplicationConfigurationRequest)\n
    '''
def deleteBucketReplicationConfiguration():
    '''returns None\n\n
    deleteBucketReplicationConfiguration(final String bucketName)\n
    deleteBucketReplicationConfiguration(final DeleteBucketReplicationConfigurationRequest request)\n
    '''
def doesObjectExist():
    '''returns boolean\n\n
    doesObjectExist(final String bucketName, final String objectName)\n
    '''
def getBucketAccelerateConfiguration():
    '''returns BucketAccelerateConfiguration\n\n
    getBucketAccelerateConfiguration(final String bucketName)\n
    getBucketAccelerateConfiguration(final GetBucketAccelerateConfigurationRequest getBucketAccelerateConfigurationRequest)\n
    '''
def setBucketAccelerateConfiguration():
    '''returns None\n\n
    setBucketAccelerateConfiguration(final String bucketName, final BucketAccelerateConfiguration accelerateConfiguration)\n
    setBucketAccelerateConfiguration(final SetBucketAccelerateConfigurationRequest setBucketAccelerateConfigurationRequest)\n
    '''
def getUrl():
    '''returns URL\n\n
    getUrl(final String bucketName, final String key)\n
    '''
