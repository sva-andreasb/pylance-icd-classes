def ():
    '''returns TransferManager\n\n
    ()\n
    (final AWSCredentialsProvider credentialsProvider)\n
    (final AWSCredentials credentials)\n
    (final AmazonS3 s3)\n
    (final AmazonS3 s3, final ExecutorService executorService)\n
    (final AmazonS3 s3, final ExecutorService executorService, final boolean shutDownThreadPools)\n
    '''
def setConfiguration():
    '''returns None\n\n
    setConfiguration(final TransferManagerConfiguration configuration)\n
    '''
def getConfiguration():
    '''returns TransferManagerConfiguration\n\n
    getConfiguration()\n
    '''
def getAmazonS3Client():
    '''returns AmazonS3\n\n
    getAmazonS3Client()\n
    '''
def upload():
    '''returns Upload\n\n
    upload(final String bucketName, final String key, final InputStream input, final ObjectMetadata objectMetadata)\n
    upload(final String bucketName, final String key, final File file)\n
    upload(final PutObjectRequest putObjectRequest)\n
    upload(final PutObjectRequest putObjectRequest, final S3ProgressListener progressListener)\n
    '''
def download():
    '''returns Download\n\n
    download(final String bucket, final String key, final File file)\n
    download(final String bucket, final String key, final File file, final long timeoutMillis)\n
    download(final GetObjectRequest getObjectRequest, final File file)\n
    download(final GetObjectRequest getObjectRequest, final File file, final long timeoutMillis)\n
    download(final GetObjectRequest getObjectRequest, final File file, final S3ProgressListener progressListener)\n
    download(final GetObjectRequest getObjectRequest, final File file, final S3ProgressListener progressListener, final long timeoutMillis)\n
    '''
def downloadDirectory():
    '''returns MultipleFileDownload\n\n
    downloadDirectory(final String bucketName, String keyPrefix, final File destinationDirectory)\n
    '''
def uploadDirectory():
    '''returns MultipleFileUpload\n\n
    uploadDirectory(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final boolean includeSubdirectories)\n
    uploadDirectory(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final boolean includeSubdirectories, final ObjectMetadataProvider metadataProvider)\n
    '''
def uploadFileList():
    '''returns MultipleFileUpload\n\n
    uploadFileList(final String bucketName, final String virtualDirectoryKeyPrefix, final File directory, final List<File> files)\n
    uploadFileList(final String bucketName, String virtualDirectoryKeyPrefix, final File directory, final List<File> files, final ObjectMetadataProvider metadataProvider)\n
    '''
def abortMultipartUploads():
    '''returns None\n\n
    abortMultipartUploads(final String bucketName, final Date date)\n
    '''
def shutdownNow():
    '''returns None\n\n
    shutdownNow()\n
    shutdownNow(final boolean shutDownS3Client)\n
    '''
def copy():
    '''returns Copy\n\n
    copy(final String sourceBucketName, final String sourceKey, final String destinationBucketName, final String destinationKey)\n
    copy(final CopyObjectRequest copyObjectRequest)\n
    copy(final CopyObjectRequest copyObjectRequest, final TransferStateChangeListener stateChangeListener)\n
    '''
def resumeUpload():
    '''returns Upload\n\n
    resumeUpload(final PersistableUpload persistableUpload)\n
    '''
def resumeDownload():
    '''returns Download\n\n
    resumeDownload(final PersistableDownload persistableDownload)\n
    '''
def newThread():
    '''returns Thread\n\n
    newThread(final Runnable r)\n
    '''
