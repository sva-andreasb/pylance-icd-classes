def UploadObjectObserver():
'''public UploadObjectObserver()
'''
pass
def init():
'''public UploadObjectObserver init(final UploadObjectRequest req, final S3DirectSpi s3direct, final AmazonS3 s3, final ExecutorService es)
'''
pass
def onUploadInitiation():
'''public String onUploadInitiation(final UploadObjectRequest req)
'''
pass
def onPartCreate():
'''public void onPartCreate(final PartCreationEvent event)
'''
pass
def call():
'''public UploadPartResult call()
'''
pass
def onCompletion():
'''public CompleteMultipartUploadResult onCompletion(final List<PartETag> partETags)
'''
pass
def onAbort():
'''public void onAbort()
'''
pass
def getFutures():
'''public List<Future<UploadPartResult>> getFutures()
'''
pass
