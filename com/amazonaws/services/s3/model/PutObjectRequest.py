def PutObjectRequest():
    '''    public PutObjectRequest(final String bucketName, final String key, final File file)
    public PutObjectRequest(final String bucketName, final String key, final String redirectLocation)
    public PutObjectRequest(final String bucketName, final String key, final InputStream input, final ObjectMetadata metadata)
    '''
def clone():
    '''    public PutObjectRequest clone()
    '''
def withBucketName():
    '''    public PutObjectRequest withBucketName(final String bucketName)
    '''
def withKey():
    '''    public PutObjectRequest withKey(final String key)
    '''
def withStorageClass():
    '''    public PutObjectRequest withStorageClass(final String storageClass)
    public PutObjectRequest withStorageClass(final StorageClass storageClass)
    '''
def withFile():
    '''    public PutObjectRequest withFile(final File file)
    '''
def withMetadata():
    '''    public PutObjectRequest withMetadata(final ObjectMetadata metadata)
    '''
def withCannedAcl():
    '''    public PutObjectRequest withCannedAcl(final CannedAccessControlList cannedAcl)
    '''
def withAccessControlList():
    '''    public PutObjectRequest withAccessControlList(final AccessControlList accessControlList)
    '''
def withInputStream():
    '''    public PutObjectRequest withInputStream(final InputStream inputStream)
    '''
def withRedirectLocation():
    '''    public PutObjectRequest withRedirectLocation(final String redirectLocation)
    '''
def withSSECustomerKey():
    '''    public PutObjectRequest withSSECustomerKey(final SSECustomerKey sseKey)
    '''
def withProgressListener():
    '''    public PutObjectRequest withProgressListener(final ProgressListener progressListener)
    '''
def withSSEAwsKeyManagementParams():
    '''    public PutObjectRequest withSSEAwsKeyManagementParams(final SSEAwsKeyManagementParams sseAwsKeyManagementParams)
    '''
def isRequesterPays():
    '''    public boolean isRequesterPays()
    '''
def setRequesterPays():
    '''    public void setRequesterPays(final boolean isRequesterPays)
    '''
def withRequesterPays():
    '''    public PutObjectRequest withRequesterPays(final boolean isRequesterPays)
    '''
