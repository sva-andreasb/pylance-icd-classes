def CryptoModuleDispatcher():
'''public CryptoModuleDispatcher(final AWSKMSClient kms, final S3Direct s3, final AWSCredentialsProvider credentialsProvider, final EncryptionMaterialsProvider encryptionMaterialsProvider, CryptoConfiguration cryptoConfig)
'''
pass
def putObjectSecurely():
'''public PutObjectResult putObjectSecurely(final PutObjectRequest putObjectRequest)
'''
pass
def getObjectSecurely():
'''public S3Object getObjectSecurely(final GetObjectRequest req)
public ObjectMetadata getObjectSecurely(final GetObjectRequest req, final File destinationFile)
'''
pass
def completeMultipartUploadSecurely():
'''public CompleteMultipartUploadResult completeMultipartUploadSecurely(final CompleteMultipartUploadRequest req)
'''
pass
def abortMultipartUploadSecurely():
'''public void abortMultipartUploadSecurely(final AbortMultipartUploadRequest req)
'''
pass
def initiateMultipartUploadSecurely():
'''public InitiateMultipartUploadResult initiateMultipartUploadSecurely(final InitiateMultipartUploadRequest req)
'''
pass
def uploadPartSecurely():
'''public UploadPartResult uploadPartSecurely(final UploadPartRequest req)
'''
pass
def copyPartSecurely():
'''public CopyPartResult copyPartSecurely(final CopyPartRequest req)
'''
pass
def putInstructionFileSecurely():
'''public PutObjectResult putInstructionFileSecurely(final PutInstructionFileRequest req)
'''
pass
def putLocalObjectSecurely():
'''public void putLocalObjectSecurely(final UploadObjectRequest req, final String uploadId, final OutputStream os)
'''
pass
