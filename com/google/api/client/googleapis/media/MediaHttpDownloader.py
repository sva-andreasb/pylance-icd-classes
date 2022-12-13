MAXIMUM_CHUNK_SIZE = "int  33554432"
def MediaHttpDownloader():
    '''    public MediaHttpDownloader(final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)
    '''
def download():
    '''    public void download(final GenericUrl requestUrl, final OutputStream outputStream)
    public void download(final GenericUrl requestUrl, final HttpHeaders requestHeaders, final OutputStream outputStream)
    '''
def setBytesDownloaded():
    '''    public MediaHttpDownloader setBytesDownloaded(final long bytesDownloaded)
    '''
def setContentRange():
    '''    public MediaHttpDownloader setContentRange(final long firstBytePos, final long lastBytePos)
    public MediaHttpDownloader setContentRange(final long firstBytePos, final int lastBytePos)
    '''
def isDirectDownloadEnabled():
    '''    public boolean isDirectDownloadEnabled()
    '''
def setDirectDownloadEnabled():
    '''    public MediaHttpDownloader setDirectDownloadEnabled(final boolean directDownloadEnabled)
    '''
def setProgressListener():
    '''    public MediaHttpDownloader setProgressListener(final MediaHttpDownloaderProgressListener progressListener)
    '''
def getProgressListener():
    '''    public MediaHttpDownloaderProgressListener getProgressListener()
    '''
def getTransport():
    '''    public HttpTransport getTransport()
    '''
def setChunkSize():
    '''    public MediaHttpDownloader setChunkSize(final int chunkSize)
    '''
def getChunkSize():
    '''    public int getChunkSize()
    '''
def getNumBytesDownloaded():
    '''    public long getNumBytesDownloaded()
    '''
def getLastBytePosition():
    '''    public long getLastBytePosition()
    '''
def getDownloadState():
    '''    public DownloadState getDownloadState()
    '''
def getProgress():
    '''    public double getProgress()
    '''
