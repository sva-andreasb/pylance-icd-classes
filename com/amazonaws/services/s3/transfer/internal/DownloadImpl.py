def DownloadImpl():
'''public DownloadImpl(final String description, final TransferProgress transferProgress, final ProgressListenerChain progressListenerChain, final S3Object s3Object, final TransferStateChangeListener listener, final GetObjectRequest getObjectRequest, final File file)
public DownloadImpl(final String description, final TransferProgress transferProgress, final ProgressListenerChain progressListenerChain, final S3Object s3Object, final TransferStateChangeListener listener, final GetObjectRequest getObjectRequest, final File file, final ObjectMetadata objectMetadata, final boolean isDownloadParallel)
'''
pass
def getObjectMetadata():
'''public synchronized ObjectMetadata getObjectMetadata()
'''
pass
def getBucketName():
'''public String getBucketName()
'''
pass
def getKey():
'''public String getKey()
'''
pass
def updatePersistableTransfer():
'''public void updatePersistableTransfer(final Integer lastFullyDownloadedPartNumber)
'''
pass
def getLastFullyDownloadedPartNumber():
'''public synchronized Integer getLastFullyDownloadedPartNumber()
'''
pass
def abort():
'''public synchronized void abort()
'''
pass
def abortWithoutNotifyingStateChangeListener():
'''public synchronized void abortWithoutNotifyingStateChangeListener()
'''
pass
def setS3Object():
'''public synchronized void setS3Object(final S3Object s3Object)
'''
pass
def setState():
'''public void setState(final Transfer.TransferState state)
'''
pass
def pause():
'''public PersistableDownload pause()
'''
pass
