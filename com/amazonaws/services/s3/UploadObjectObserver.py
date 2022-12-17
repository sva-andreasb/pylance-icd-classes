def ():
    '''returns UploadObjectObserver\n\n
    ()\n
    '''
def init():
    '''returns UploadObjectObserver\n\n
    init(final UploadObjectRequest req, final S3DirectSpi s3direct, final AmazonS3 s3, final ExecutorService es)\n
    '''
def onUploadInitiation():
    '''returns String\n\n
    onUploadInitiation(final UploadObjectRequest req)\n
    '''
def onPartCreate():
    '''returns None\n\n
    onPartCreate(final PartCreationEvent event)\n
    '''
def call():
    '''returns UploadPartResult\n\n
    call()\n
    '''
def onCompletion():
    '''returns CompleteMultipartUploadResult\n\n
    onCompletion(final List<PartETag> partETags)\n
    '''
def onAbort():
    '''returns None\n\n
    onAbort()\n
    '''
def getFutures():
    '''returns List<Future<UploadPartResult>>\n\n
    getFutures()\n
    '''
