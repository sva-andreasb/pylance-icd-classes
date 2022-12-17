def ():
    '''returns PutObjectRequest\n\n
    (final String bucketName, final String key, final File file)\n
    (final String bucketName, final String key, final String redirectLocation)\n
    (final String bucketName, final String key, final InputStream input, final ObjectMetadata metadata)\n
    '''
def clone():
    '''returns PutObjectRequest\n\n
    clone()\n
    '''
def withBucketName():
    '''returns PutObjectRequest\n\n
    withBucketName(final String bucketName)\n
    '''
def withKey():
    '''returns PutObjectRequest\n\n
    withKey(final String key)\n
    '''
def withStorageClass():
    '''returns PutObjectRequest\n\n
    withStorageClass(final String storageClass)\n
    withStorageClass(final StorageClass storageClass)\n
    '''
def withFile():
    '''returns PutObjectRequest\n\n
    withFile(final File file)\n
    '''
def withMetadata():
    '''returns PutObjectRequest\n\n
    withMetadata(final ObjectMetadata metadata)\n
    '''
def withCannedAcl():
    '''returns PutObjectRequest\n\n
    withCannedAcl(final CannedAccessControlList cannedAcl)\n
    '''
def withAccessControlList():
    '''returns PutObjectRequest\n\n
    withAccessControlList(final AccessControlList accessControlList)\n
    '''
def withInputStream():
    '''returns PutObjectRequest\n\n
    withInputStream(final InputStream inputStream)\n
    '''
def withRedirectLocation():
    '''returns PutObjectRequest\n\n
    withRedirectLocation(final String redirectLocation)\n
    '''
def withSSECustomerKey():
    '''returns PutObjectRequest\n\n
    withSSECustomerKey(final SSECustomerKey sseKey)\n
    '''
def withProgressListener():
    '''returns PutObjectRequest\n\n
    withProgressListener(final ProgressListener progressListener)\n
    '''
def withSSEAwsKeyManagementParams():
    '''returns PutObjectRequest\n\n
    withSSEAwsKeyManagementParams(final SSEAwsKeyManagementParams sseAwsKeyManagementParams)\n
    '''
def isRequesterPays():
    '''returns boolean\n\n
    isRequesterPays()\n
    '''
def setRequesterPays():
    '''returns None\n\n
    setRequesterPays(final boolean isRequesterPays)\n
    '''
def withRequesterPays():
    '''returns PutObjectRequest\n\n
    withRequesterPays(final boolean isRequesterPays)\n
    '''
