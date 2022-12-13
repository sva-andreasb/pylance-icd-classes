def CryptoModuleDispatcher():
    '''public CryptoModuleDispatcher(final AWSKMSClient kms, final S3Direct s3, final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider encryptionMaterialsProvider, CryptoConfiguration cryptoConfig)
    '''
def putObjectSecurely():
    '''public PutObjectResult putObjectSecurely(final PutObjectRequest putObjectRequest)
    '''
def getObjectSecurely():
    '''public S3Object getObjectSecurely(final GetObjectRequest req)
    public ObjectMetadata getObjectSecurely(final GetObjectRequest req, final File destinationFile)
    '''
def completeMultipartUploadSecurely():
    '''public CompleteMultipartUploadResult completeMultipartUploadSecurely(final CompleteMultipartUploadRequest req)
    '''
def abortMultipartUploadSecurely():
    '''public void abortMultipartUploadSecurely(final AbortMultipartUploadRequest req)
    '''
def initiateMultipartUploadSecurely():
    '''public InitiateMultipartUploadResult initiateMultipartUploadSecurely(final InitiateMultipartUploadRequest req)
    '''
def uploadPartSecurely():
    '''public UploadPartResult uploadPartSecurely(final UploadPartRequest req)
    '''
def copyPartSecurely():
    '''public CopyPartResult copyPartSecurely(final CopyPartRequest req)
    '''
def putInstructionFileSecurely():
    '''public PutObjectResult putInstructionFileSecurely(final PutInstructionFileRequest req)
    '''
def putLocalObjectSecurely():
    '''public void putLocalObjectSecurely(final UploadObjectRequest req, final String uploadId, final OutputStream os)
    '''
