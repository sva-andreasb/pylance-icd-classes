def ():
    '''returns DownloadImpl\n\n
    (final String description, final TransferProgress transferProgress, final ProgressListenerChain progressListenerChain, final S3Object s3Object, final TransferStateChangeListener listener, final GetObjectRequest getObjectRequest, final File file)\n
    (final String description, final TransferProgress transferProgress, final ProgressListenerChain progressListenerChain, final S3Object s3Object, final TransferStateChangeListener listener, final GetObjectRequest getObjectRequest, final File file, final ObjectMetadata objectMetadata, final boolean isDownloadParallel)\n
    '''
def getBucketName():
    '''returns String\n\n
    getBucketName()\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    '''
def updatePersistableTransfer():
    '''returns None\n\n
    updatePersistableTransfer(final Integer lastFullyDownloadedPartNumber)\n
    '''
def setState():
    '''returns None\n\n
    setState(final Transfer.TransferState state)\n
    '''
def pause():
    '''returns PersistableDownload\n\n
    pause()\n
    '''
