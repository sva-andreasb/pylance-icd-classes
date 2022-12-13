def COSApi():
    '''    public COSApi()
    public COSApi(final boolean pool)
    public COSApi(final String epurl, final String accessKey, final String secretKey)
    '''
def createBucket():
    '''    public void createBucket(final String bucketName)
    '''
def doesBucketExist():
    '''    public boolean doesBucketExist(final String bucketName)
    '''
def doesFileExist():
    '''    public boolean doesFileExist(final String bucketName, final String fileName)
    '''
def getAllBuckets():
    '''    public List<String> getAllBuckets(final String bucketPrefix)
    '''
def getAllFiles():
    '''    public List<String> getAllFiles(final String bucketName)
    '''
def getAllS3ObjectsSortedByTime():
    '''    public List<S3ObjectSummary> getAllS3ObjectsSortedByTime(final String bucketName)
    '''
def uploadFile():
    '''    public String uploadFile(final String bucketName, final String fileName, final String mimeType, final byte[] fileData)
    '''
def getFile():
    '''    public byte[] getFile(final String bucketName, final String fileName)
    '''
def getS3Object():
    '''    public S3Object getS3Object(final String bucketName, final String fileName)
    '''
def getS3ObjectContent():
    '''    public byte[] getS3ObjectContent(final S3Object fileObject)
    '''
def getS3ObjectMimeType():
    '''    public String getS3ObjectMimeType(final S3Object fileObject)
    '''
def streamFile():
    '''    public InputStream streamFile(final String bucketName, final String fileName)
    '''
def deleteFile():
    '''    public void deleteFile(final String bucketName, final String fileName)
    '''
def deleteBucket():
    '''    public void deleteBucket(final String bucketName)
    '''
def streamBinaryData():
    '''    public void streamBinaryData(final InputStream in, final OutputStream out)
    '''
def cleanup():
    '''    public void cleanup()
    '''
def compare():
    '''    public int compare(final S3ObjectSummary o1, final S3ObjectSummary o2)
    '''
