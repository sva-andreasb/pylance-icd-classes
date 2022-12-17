MAXIMUM_CHUNK_SIZE = "int  33554432"
def ():
    '''returns MediaHttpDownloader\n\n
    (final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)\n
    '''
def download():
    '''returns None\n\n
    download(final GenericUrl requestUrl, final OutputStream outputStream)\n
    download(final GenericUrl requestUrl, final HttpHeaders requestHeaders, final OutputStream outputStream)\n
    '''
def setBytesDownloaded():
    '''returns MediaHttpDownloader\n\n
    setBytesDownloaded(final long bytesDownloaded)\n
    '''
def setContentRange():
    '''returns MediaHttpDownloader\n\n
    setContentRange(final long firstBytePos, final long lastBytePos)\n
    setContentRange(final long firstBytePos, final int lastBytePos)\n
    '''
def isDirectDownloadEnabled():
    '''returns boolean\n\n
    isDirectDownloadEnabled()\n
    '''
def setDirectDownloadEnabled():
    '''returns MediaHttpDownloader\n\n
    setDirectDownloadEnabled(final boolean directDownloadEnabled)\n
    '''
def setProgressListener():
    '''returns MediaHttpDownloader\n\n
    setProgressListener(final MediaHttpDownloaderProgressListener progressListener)\n
    '''
def getProgressListener():
    '''returns MediaHttpDownloaderProgressListener\n\n
    getProgressListener()\n
    '''
def getTransport():
    '''returns HttpTransport\n\n
    getTransport()\n
    '''
def setChunkSize():
    '''returns MediaHttpDownloader\n\n
    setChunkSize(final int chunkSize)\n
    '''
def getChunkSize():
    '''returns int\n\n
    getChunkSize()\n
    '''
def getNumBytesDownloaded():
    '''returns long\n\n
    getNumBytesDownloaded()\n
    '''
def getLastBytePosition():
    '''returns long\n\n
    getLastBytePosition()\n
    '''
def getDownloadState():
    '''returns DownloadState\n\n
    getDownloadState()\n
    '''
def getProgress():
    '''returns double\n\n
    getProgress()\n
    '''
