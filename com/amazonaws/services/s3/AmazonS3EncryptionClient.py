def AmazonS3EncryptionClient():
    '''public AmazonS3EncryptionClient(final EncryptionMaterials encryptionMaterials)
    public AmazonS3EncryptionClient(final EncryptionMaterialsProvider encryptionMaterialsProvider)
    public AmazonS3EncryptionClient(final EncryptionMaterials encryptionMaterials, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final EncryptionMaterialsProvider encryptionMaterialsProvider, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final AWSCredentials credentials, final EncryptionMaterials encryptionMaterials)
    public AmazonS3EncryptionClient(final AWSCredentials credentials, final EncryptionMaterialsProvider encryptionMaterialsProvider)
    public AmazonS3EncryptionClient(final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider encryptionMaterialsProvider)
    public AmazonS3EncryptionClient(final AWSCredentials credentials, final EncryptionMaterials encryptionMaterials, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final AWSCredentials credentials, final EncryptionMaterialsProvider encryptionMaterialsProvider, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider encryptionMaterialsProvider, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final AWSCredentials credentials, final EncryptionMaterials encryptionMaterials, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final AWSCredentials credentials, final EncryptionMaterialsProvider encryptionMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider kekMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig)
    public AmazonS3EncryptionClient(final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider kekMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig, final RequestMetricCollector requestMetricCollector)
    public AmazonS3EncryptionClient(final AWSKMSClient kms, final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider kekMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig, final RequestMetricCollector requestMetricCollector)
    '''
def putObject():
    '''public PutObjectResult putObject(final PutObjectRequest req)
    public PutObjectResult putObject(final PutObjectRequest req)
    '''
def getObject():
    '''public S3Object getObject(final GetObjectRequest req)
    public ObjectMetadata getObject(final GetObjectRequest req, final File dest)
    public S3Object getObject(final GetObjectRequest req)
    public ObjectMetadata getObject(final GetObjectRequest req, final File dest)
    '''
def deleteObject():
    '''public void deleteObject(final DeleteObjectRequest req)
    '''
def completeMultipartUpload():
    '''public CompleteMultipartUploadResult completeMultipartUpload(final CompleteMultipartUploadRequest req)
    public CompleteMultipartUploadResult completeMultipartUpload(final CompleteMultipartUploadRequest req)
    '''
def initiateMultipartUpload():
    '''public InitiateMultipartUploadResult initiateMultipartUpload(final InitiateMultipartUploadRequest req)
    public InitiateMultipartUploadResult initiateMultipartUpload(final InitiateMultipartUploadRequest req)
    '''
def uploadPart():
    '''public UploadPartResult uploadPart(final UploadPartRequest uploadPartRequest)
    public UploadPartResult uploadPart(final UploadPartRequest req)
    '''
def copyPart():
    '''public CopyPartResult copyPart(final CopyPartRequest copyPartRequest)
    public CopyPartResult copyPart(final CopyPartRequest req)
    '''
def abortMultipartUpload():
    '''public void abortMultipartUpload(final AbortMultipartUploadRequest req)
    public void abortMultipartUpload(final AbortMultipartUploadRequest req)
    '''
def putInstructionFile():
    '''public PutObjectResult putInstructionFile(final PutInstructionFileRequest req)
    '''
def shutdown():
    '''public void shutdown()
    '''
def uploadObject():
    '''public CompleteMultipartUploadResult uploadObject(final UploadObjectRequest req)
    '''
