def ():
    '''returns CryptoModuleDispatcher\n\n
    (final AWSKMSClient kms, final S3Direct s3, final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider encryptionMaterialsProvider, CryptoConfiguration cryptoConfig)\n
    '''
def putObjectSecurely():
    '''returns PutObjectResult\n\n
    putObjectSecurely(final PutObjectRequest putObjectRequest)\n
    '''
def getObjectSecurely():
    '''returns ObjectMetadata\n\n
    getObjectSecurely(final GetObjectRequest req)\n
    getObjectSecurely(final GetObjectRequest req, final File destinationFile)\n
    '''
def completeMultipartUploadSecurely():
    '''returns CompleteMultipartUploadResult\n\n
    completeMultipartUploadSecurely(final CompleteMultipartUploadRequest req)\n
    '''
def abortMultipartUploadSecurely():
    '''returns None\n\n
    abortMultipartUploadSecurely(final AbortMultipartUploadRequest req)\n
    '''
def initiateMultipartUploadSecurely():
    '''returns InitiateMultipartUploadResult\n\n
    initiateMultipartUploadSecurely(final InitiateMultipartUploadRequest req)\n
    '''
def uploadPartSecurely():
    '''returns UploadPartResult\n\n
    uploadPartSecurely(final UploadPartRequest req)\n
    '''
def copyPartSecurely():
    '''returns CopyPartResult\n\n
    copyPartSecurely(final CopyPartRequest req)\n
    '''
def putInstructionFileSecurely():
    '''returns PutObjectResult\n\n
    putInstructionFileSecurely(final PutInstructionFileRequest req)\n
    '''
def putLocalObjectSecurely():
    '''returns None\n\n
    putLocalObjectSecurely(final UploadObjectRequest req, final String uploadId, final OutputStream os)\n
    '''
