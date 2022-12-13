def TransferManager():
'''public TransferManager()
public TransferManager(final AWSCredentialsProvider credentialsProvider)
public TransferManager(final AWSCredentials credentials)
public TransferManager(final AmazonS3 s3)
public TransferManager(final AmazonS3 s3, final ExecutorService executorService)
public TransferManager(final AmazonS3 s3, final ExecutorService executorService, final boolean shutDownThreadPools)
'''
pass
def setConfiguration():
'''public void setConfiguration(final TransferManagerConfiguration configuration)
'''
pass
def getConfiguration():
'''public TransferManagerConfiguration getConfiguration()
'''
pass
def getAmazonS3Client():
'''public AmazonS3 getAmazonS3Client()
'''
pass
def upload():
'''public Upload upload(final String bucketName, final String key, final InputStream input, final ObjectMetadata objectMetadata)
public Upload upload(final String bucketName, final String key, final File file)
public Upload upload(final PutObjectRequest putObjectRequest)
public Upload upload(final PutObjectRequest putObjectRequest, final S3ProgressListener progressListener)
'''
pass
def download():
'''public Download download(final String bucket, final String key, final File file)
public Download download(final String bucket, final String key, final File file, final long timeoutMillis)
public Download download(final GetObjectRequest getObjectRequest, final File file)
public Download download(final GetObjectRequest getObjectRequest, final File file, final long timeoutMillis)
public Download download(final GetObjectRequest getObjectRequest, final File file, final S3ProgressListener progressListener)
public Download download(final GetObjectRequest getObjectRequest, final File file, final S3ProgressListener progressListener, final long timeoutMillis)
'''
pass
def downloadDirectory():
'''public MultipleFileDownload downloadDirectory(final String bucketName, String keyPrefix, final File destinationDirectory)
'''
pass
def uploadDirectory():
'''public MultipleFileUpload uploadDirectory(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final boolean includeSubdirectories)
public MultipleFileUpload uploadDirectory(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final boolean includeSubdirectories, final ObjectMetadataProvider metadataProvider)
'''
pass
def uploadFileList():
'''public MultipleFileUpload uploadFileList(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final List<File> files)
public MultipleFileUpload uploadFileList(final String bucketName, String virtualDirectoryKeyPrefix, final File directory, final List<File> files, final ObjectMetadataProvider metadataProvider)
'''
pass
def abortMultipartUploads():
'''public void abortMultipartUploads(final String bucketName, final Date date)
'''
pass
def shutdownNow():
'''public void shutdownNow()
public void shutdownNow(final boolean shutDownS3Client)
'''
pass
def appendSingleObjectUserAgent():
'''public static <X extends AmazonWebServiceRequest> X appendSingleObjectUserAgent(final X request)
'''
pass
def appendMultipartUserAgent():
'''public static <X extends AmazonWebServiceRequest> X appendMultipartUserAgent(final X request)
'''
pass
def copy():
'''public Copy copy(final String sourceBucketName, final String sourceKey, final String destinationBucketName, final String destinationKey)
public Copy copy(final CopyObjectRequest copyObjectRequest)
public Copy copy(final CopyObjectRequest copyObjectRequest, final TransferStateChangeListener stateChangeListener)
'''
pass
def resumeUpload():
'''public Upload resumeUpload(final PersistableUpload persistableUpload)
'''
pass
def resumeDownload():
'''public Download resumeDownload(final PersistableDownload persistableDownload)
'''
pass
def newThread():
'''public Thread newThread(final Runnable r)
'''
pass
