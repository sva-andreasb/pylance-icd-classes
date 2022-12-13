def DownloadImpl():
    '''    public DownloadImpl(final String description, final TransferProgress transferProgress, final ProgressListenerChain progressListenerChain, final S3Object s3Object, final TransferStateChangeListener listener, final GetObjectRequest getObjectRequest, final File file)
    public DownloadImpl(final String description, final TransferProgress transferProgress, final ProgressListenerChain progressListenerChain, final S3Object s3Object, final TransferStateChangeListener listener, final GetObjectRequest getObjectRequest, final File file, final ObjectMetadata objectMetadata, final boolean isDownloadParallel)
    '''
def getObjectMetadata():
    '''    public synchronized ObjectMetadata getObjectMetadata()
    '''
def getBucketName():
    '''    public String getBucketName()
    '''
def getKey():
    '''    public String getKey()
    '''
def updatePersistableTransfer():
    '''    public void updatePersistableTransfer(final Integer lastFullyDownloadedPartNumber)
    '''
def getLastFullyDownloadedPartNumber():
    '''    public synchronized Integer getLastFullyDownloadedPartNumber()
    '''
def abort():
    '''    public synchronized void abort()
    '''
def abortWithoutNotifyingStateChangeListener():
    '''    public synchronized void abortWithoutNotifyingStateChangeListener()
    '''
def setS3Object():
    '''    public synchronized void setS3Object(final S3Object s3Object)
    '''
def setState():
    '''    public void setState(final Transfer.TransferState state)
    '''
def pause():
    '''    public PersistableDownload pause()
    '''
