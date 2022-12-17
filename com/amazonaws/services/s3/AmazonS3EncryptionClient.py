def ():
    '''returns AmazonS3EncryptionClient\n\n
    (final EncryptionMaterials encryptionMaterials)\n
    (final EncryptionMaterialsProvider encryptionMaterialsProvider)\n
    (final EncryptionMaterials encryptionMaterials, final CryptoConfiguration cryptoConfig)\n
    (final EncryptionMaterialsProvider encryptionMaterialsProvider, final CryptoConfiguration cryptoConfig)\n
    (final AWSCredentials credentials, final EncryptionMaterials encryptionMaterials)\n
    (final AWSCredentials credentials, final EncryptionMaterialsProvider encryptionMaterialsProvider)\n
    (final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider encryptionMaterialsProvider)\n
    (final AWSCredentials credentials, final EncryptionMaterials encryptionMaterials, final CryptoConfiguration cryptoConfig)\n
    (final AWSCredentials credentials, final EncryptionMaterialsProvider encryptionMaterialsProvider, final CryptoConfiguration cryptoConfig)\n
    (final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider encryptionMaterialsProvider, final CryptoConfiguration cryptoConfig)\n
    (final AWSCredentials credentials, final EncryptionMaterials encryptionMaterials, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig)\n
    (final AWSCredentials credentials, final EncryptionMaterialsProvider encryptionMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig)\n
    (final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider kekMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig)\n
    (final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider kekMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig, final RequestMetricCollector requestMetricCollector)\n
    (final AWSKMSClient kms, final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider kekMaterialsProvider, final ClientConfiguration clientConfig, final CryptoConfiguration cryptoConfig, final RequestMetricCollector requestMetricCollector)\n
    '''
def putObject():
    '''returns PutObjectResult\n\n
    putObject(final PutObjectRequest req)\n
    putObject(final PutObjectRequest req)\n
    '''
def getObject():
    '''returns ObjectMetadata\n\n
    getObject(final GetObjectRequest req)\n
    getObject(final GetObjectRequest req, final File dest)\n
    getObject(final GetObjectRequest req)\n
    getObject(final GetObjectRequest req, final File dest)\n
    '''
def deleteObject():
    '''returns None\n\n
    deleteObject(final DeleteObjectRequest req)\n
    '''
def completeMultipartUpload():
    '''returns CompleteMultipartUploadResult\n\n
    completeMultipartUpload(final CompleteMultipartUploadRequest req)\n
    completeMultipartUpload(final CompleteMultipartUploadRequest req)\n
    '''
def initiateMultipartUpload():
    '''returns InitiateMultipartUploadResult\n\n
    initiateMultipartUpload(final InitiateMultipartUploadRequest req)\n
    initiateMultipartUpload(final InitiateMultipartUploadRequest req)\n
    '''
def uploadPart():
    '''returns UploadPartResult\n\n
    uploadPart(final UploadPartRequest uploadPartRequest)\n
    uploadPart(final UploadPartRequest req)\n
    '''
def copyPart():
    '''returns CopyPartResult\n\n
    copyPart(final CopyPartRequest copyPartRequest)\n
    copyPart(final CopyPartRequest req)\n
    '''
def abortMultipartUpload():
    '''returns None\n\n
    abortMultipartUpload(final AbortMultipartUploadRequest req)\n
    abortMultipartUpload(final AbortMultipartUploadRequest req)\n
    '''
def putInstructionFile():
    '''returns PutObjectResult\n\n
    putInstructionFile(final PutInstructionFileRequest req)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def uploadObject():
    '''returns CompleteMultipartUploadResult\n\n
    uploadObject(final UploadObjectRequest req)\n
    '''
