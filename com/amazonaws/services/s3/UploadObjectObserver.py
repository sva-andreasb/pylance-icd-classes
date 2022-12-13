def UploadObjectObserver():
    '''public UploadObjectObserver()
    '''
def init():
    '''public UploadObjectObserver init(final UploadObjectRequest req, final S3DirectSpi s3direct, final AmazonS3 s3, final ExecutorService es)
    '''
def onUploadInitiation():
    '''public String onUploadInitiation(final UploadObjectRequest req)
    '''
def onPartCreate():
    '''public void onPartCreate(final PartCreationEvent event)
    '''
def call():
    '''public UploadPartResult call()
    '''
def onCompletion():
    '''public CompleteMultipartUploadResult onCompletion(final List<PartETag> partETags)
    '''
def onAbort():
    '''public void onAbort()
    '''
def getFutures():
    '''public List<Future<UploadPartResult>> getFutures()
    '''
