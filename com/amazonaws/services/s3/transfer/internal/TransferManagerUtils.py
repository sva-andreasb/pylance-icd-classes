def createDefaultExecutorService():
    '''    public static ThreadPoolExecutor createDefaultExecutorService()
    '''
def newThread():
    '''    public Thread newThread(final Runnable r)
    '''
def isUploadParallelizable():
    '''    public static boolean isUploadParallelizable(final PutObjectRequest putObjectRequest, final boolean isUsingEncryption)
    '''
def getContentLength():
    '''    public static long getContentLength(final PutObjectRequest putObjectRequest)
    '''
def calculateOptimalPartSize():
    '''    public static long calculateOptimalPartSize(final PutObjectRequest putObjectRequest, final TransferManagerConfiguration configuration)
    '''
def shouldUseMultipartUpload():
    '''    public static boolean shouldUseMultipartUpload(final PutObjectRequest putObjectRequest, final TransferManagerConfiguration configuration)
    '''
def getRequestFile():
    '''    public static File getRequestFile(final PutObjectRequest putObjectRequest)
    '''
def calculateOptimalPartSizeForCopy():
    '''    public static long calculateOptimalPartSizeForCopy(final CopyObjectRequest copyObjectRequest, final TransferManagerConfiguration configuration, final long contentLengthOfSource)
    '''
def determinePauseStatus():
    '''    public static PauseStatus determinePauseStatus(final Transfer.TransferState transferState, final boolean forceCancel)
    '''
def isDownloadParallelizable():
    '''    public static boolean isDownloadParallelizable(final AmazonS3 s3, final GetObjectRequest getObjectRequest, final Integer partCount)
    '''
