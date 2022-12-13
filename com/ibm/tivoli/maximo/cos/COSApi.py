def COSApi():
'''public COSApi()
public COSApi(final boolean pool)
public COSApi(final String epurl, final String accessKey, final String secretKey)
'''
pass
def createBucket():
'''public void createBucket(final String bucketName)
'''
pass
def doesBucketExist():
'''public boolean doesBucketExist(final String bucketName)
'''
pass
def doesFileExist():
'''public boolean doesFileExist(final String bucketName, final String fileName)
'''
pass
def getAllBuckets():
'''public List<String> getAllBuckets(final String bucketPrefix)
'''
pass
def getAllFiles():
'''public List<String> getAllFiles(final String bucketName)
'''
pass
def getAllS3ObjectsSortedByTime():
'''public List<S3ObjectSummary> getAllS3ObjectsSortedByTime(final String bucketName)
'''
pass
def uploadFile():
'''public String uploadFile(final String bucketName, final String fileName, final String mimeType, final byte[] fileData)
'''
pass
def getFile():
'''public byte[] getFile(final String bucketName, final String fileName)
'''
pass
def getS3Object():
'''public S3Object getS3Object(final String bucketName, final String fileName)
'''
pass
def getS3ObjectContent():
'''public byte[] getS3ObjectContent(final S3Object fileObject)
'''
pass
def getS3ObjectMimeType():
'''public String getS3ObjectMimeType(final S3Object fileObject)
'''
pass
def streamFile():
'''public InputStream streamFile(final String bucketName, final String fileName)
'''
pass
def deleteFile():
'''public void deleteFile(final String bucketName, final String fileName)
'''
pass
def deleteBucket():
'''public void deleteBucket(final String bucketName)
'''
pass
def streamBinaryData():
'''public void streamBinaryData(final InputStream in, final OutputStream out)
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def compare():
'''public int compare(final S3ObjectSummary o1, final S3ObjectSummary o2)
'''
pass
