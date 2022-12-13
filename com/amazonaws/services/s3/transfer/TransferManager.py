def TransferManager():
    '''    public TransferManager()
    public TransferManager(final AWSCredentialsProvider credentialsProvider)
    public TransferManager(final AWSCredentials credentials)
    public TransferManager(final AmazonS3 s3)
    public TransferManager(final AmazonS3 s3, final ExecutorService executorService)
    public TransferManager(final AmazonS3 s3, final ExecutorService executorService, final boolean shutDownThreadPools)
    '''
def setConfiguration():
    '''    public void setConfiguration(final TransferManagerConfiguration configuration)
    '''
def getConfiguration():
    '''    public TransferManagerConfiguration getConfiguration()
    '''
def getAmazonS3Client():
    '''    public AmazonS3 getAmazonS3Client()
    '''
def upload():
    '''    public Upload upload(final String bucketName, final String key, final InputStream input, final ObjectMetadata objectMetadata)
    public Upload upload(final String bucketName, final String key, final File file)
    public Upload upload(final PutObjectRequest putObjectRequest)
    public Upload upload(final PutObjectRequest putObjectRequest, final S3ProgressListener progressListener)
    '''
def download():
    '''    public Download download(final String bucket, final String key, final File file)
    public Download download(final String bucket, final String key, final File file, final long timeoutMillis)
    public Download download(final GetObjectRequest getObjectRequest, final File file)
    public Download download(final GetObjectRequest getObjectRequest, final File file, final long timeoutMillis)
    public Download download(final GetObjectRequest getObjectRequest, final File file, final S3ProgressListener progressListener)
    public Download download(final GetObjectRequest getObjectRequest, final File file, final S3ProgressListener progressListener, final long timeoutMillis)
    '''
def downloadDirectory():
    '''    public MultipleFileDownload downloadDirectory(final String bucketName, String keyPrefix, final File destinationDirectory)
    '''
def uploadDirectory():
    '''    public MultipleFileUpload uploadDirectory(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final boolean includeSubdirectories)
    public MultipleFileUpload uploadDirectory(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final boolean includeSubdirectories, final ObjectMetadataProvider metadataProvider)
    '''
def uploadFileList():
    '''    public MultipleFileUpload uploadFileList(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final List<File> files)
    public MultipleFileUpload uploadFileList(final String bucketName, String virtualDirectoryKeyPrefix, final File directory, final List<File> files, final ObjectMetadataProvider metadataProvider)
    '''
def abortMultipartUploads():
    '''    public void abortMultipartUploads(final String bucketName, final Date date)
    '''
def shutdownNow():
    '''    public void shutdownNow()
    public void shutdownNow(final boolean shutDownS3Client)
    '''
def appendSingleObjectUserAgent():
    '''    public static <X extends AmazonWebServiceRequest> X appendSingleObjectUserAgent(final X request)
    '''
def appendMultipartUserAgent():
    '''    public static <X extends AmazonWebServiceRequest> X appendMultipartUserAgent(final X request)
    '''
def copy():
    '''    public Copy copy(final String sourceBucketName, final String sourceKey, final String destinationBucketName, final String destinationKey)
    public Copy copy(final CopyObjectRequest copyObjectRequest)
    public Copy copy(final CopyObjectRequest copyObjectRequest, final TransferStateChangeListener stateChangeListener)
    '''
def resumeUpload():
    '''    public Upload resumeUpload(final PersistableUpload persistableUpload)
    '''
def resumeDownload():
    '''    public Download resumeDownload(final PersistableDownload persistableDownload)
    '''
def newThread():
    '''    public Thread newThread(final Runnable r)
    '''
