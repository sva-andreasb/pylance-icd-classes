def createDefaultExecutorService():
'''public static ThreadPoolExecutor createDefaultExecutorService()
'''
pass
def newThread():
'''public Thread newThread(final Runnable r)
'''
pass
def isUploadParallelizable():
'''public static boolean isUploadParallelizable(final PutObjectRequest putObjectRequest, final boolean isUsingEncryption)
'''
pass
def getContentLength():
'''public static long getContentLength(final PutObjectRequest putObjectRequest)
'''
pass
def calculateOptimalPartSize():
'''public static long calculateOptimalPartSize(final PutObjectRequest putObjectRequest, final TransferManagerConfiguration configuration)
'''
pass
def shouldUseMultipartUpload():
'''public static boolean shouldUseMultipartUpload(final PutObjectRequest putObjectRequest, final TransferManagerConfiguration configuration)
'''
pass
def getRequestFile():
'''public static File getRequestFile(final PutObjectRequest putObjectRequest)
'''
pass
def calculateOptimalPartSizeForCopy():
'''public static long calculateOptimalPartSizeForCopy(final CopyObjectRequest copyObjectRequest, final TransferManagerConfiguration configuration, final long contentLengthOfSource)
'''
pass
def determinePauseStatus():
'''public static PauseStatus determinePauseStatus(final Transfer.TransferState transferState, final boolean forceCancel)
'''
pass
def isDownloadParallelizable():
'''public static boolean isDownloadParallelizable(final AmazonS3 s3, final GetObjectRequest getObjectRequest, final Integer partCount)
'''
pass
