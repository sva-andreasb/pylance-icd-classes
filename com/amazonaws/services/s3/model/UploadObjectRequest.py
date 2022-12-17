def ():
    '''returns UploadObjectRequest\n\n
    (final String bucketName, final String key, final File file)\n
    (final String bucketName, final String key, final InputStream input, final ObjectMetadata metadata)\n
    '''
def getPartSize():
    '''returns long\n\n
    getPartSize()\n
    '''
def withPartSize():
    '''returns UploadObjectRequest\n\n
    withPartSize(final long partSize)\n
    '''
def getDiskLimit():
    '''returns long\n\n
    getDiskLimit()\n
    '''
def withDiskLimit():
    '''returns UploadObjectRequest\n\n
    withDiskLimit(final long diskLimit)\n
    '''
def getExecutorService():
    '''returns ExecutorService\n\n
    getExecutorService()\n
    '''
def withExecutorService():
    '''returns UploadObjectRequest\n\n
    withExecutorService(final ExecutorService executorService)\n
    '''
def getMultiFileOutputStream():
    '''returns MultiFileOutputStream\n\n
    getMultiFileOutputStream()\n
    '''
def withMultiFileOutputStream():
    '''returns UploadObjectRequest\n\n
    withMultiFileOutputStream(final MultiFileOutputStream multiFileOutputStream)\n
    '''
def getUploadObjectObserver():
    '''returns UploadObjectObserver\n\n
    getUploadObjectObserver()\n
    '''
def withUploadObjectObserver():
    '''returns UploadObjectRequest\n\n
    withUploadObjectObserver(final UploadObjectObserver uploadObjectObserver)\n
    '''
def setMaterialsDescription():
    '''returns None\n\n
    setMaterialsDescription(final Map<String, String> materialsDescription)\n
    '''
def withMaterialsDescription():
    '''returns UploadObjectRequest\n\n
    withMaterialsDescription(final Map<String, String> materialsDescription)\n
    '''
def getUploadPartMetadata():
    '''returns ObjectMetadata\n\n
    getUploadPartMetadata()\n
    '''
def setUploadPartMetadata():
    '''returns None\n\n
    setUploadPartMetadata(final ObjectMetadata partUploadMetadata)\n
    '''
def clone():
    '''returns UploadObjectRequest\n\n
    clone()\n
    '''
