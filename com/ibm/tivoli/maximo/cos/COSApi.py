def ():
    '''returns COSApi\n\n
    ()\n
    (final boolean pool)\n
    (final String epurl, final String accessKey, final String secretKey)\n
    '''
def createBucket():
    '''returns None\n\n
    createBucket(final String bucketName)\n
    '''
def doesBucketExist():
    '''returns boolean\n\n
    doesBucketExist(final String bucketName)\n
    '''
def doesFileExist():
    '''returns boolean\n\n
    doesFileExist(final String bucketName, final String fileName)\n
    '''
def getAllBuckets():
    '''returns List<String>\n\n
    getAllBuckets(final String bucketPrefix)\n
    '''
def getAllFiles():
    '''returns List<String>\n\n
    getAllFiles(final String bucketName)\n
    '''
def getAllS3ObjectsSortedByTime():
    '''returns List<S3ObjectSummary>\n\n
    getAllS3ObjectsSortedByTime(final String bucketName)\n
    '''
def uploadFile():
    '''returns String\n\n
    uploadFile(final String bucketName, final String fileName, final String mimeType, final byte[] fileData)\n
    '''
def getFile():
    '''returns byte[]\n\n
    getFile(final String bucketName, final String fileName)\n
    '''
def getS3Object():
    '''returns S3Object\n\n
    getS3Object(final String bucketName, final String fileName)\n
    '''
def getS3ObjectContent():
    '''returns byte[]\n\n
    getS3ObjectContent(final S3Object fileObject)\n
    '''
def getS3ObjectMimeType():
    '''returns String\n\n
    getS3ObjectMimeType(final S3Object fileObject)\n
    '''
def streamFile():
    '''returns InputStream\n\n
    streamFile(final String bucketName, final String fileName)\n
    '''
def deleteFile():
    '''returns None\n\n
    deleteFile(final String bucketName, final String fileName)\n
    '''
def deleteBucket():
    '''returns None\n\n
    deleteBucket(final String bucketName)\n
    '''
def streamBinaryData():
    '''returns None\n\n
    streamBinaryData(final InputStream in, final OutputStream out)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def compare():
    '''returns int\n\n
    compare(final S3ObjectSummary o1, final S3ObjectSummary o2)\n
    '''
