MAXIMUM_CHUNK_SIZE = "int  33554432"
def MediaHttpDownloader():
'''public MediaHttpDownloader(final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)
'''
pass
def download():
'''public void download(final GenericUrl requestUrl, final OutputStream outputStream)
public void download(final GenericUrl requestUrl, final HttpHeaders requestHeaders, final OutputStream outputStream)
'''
pass
def setBytesDownloaded():
'''public MediaHttpDownloader setBytesDownloaded(final long bytesDownloaded)
'''
pass
def setContentRange():
'''public MediaHttpDownloader setContentRange(final long firstBytePos, final long lastBytePos)
public MediaHttpDownloader setContentRange(final long firstBytePos, final int lastBytePos)
'''
pass
def isDirectDownloadEnabled():
'''public boolean isDirectDownloadEnabled()
'''
pass
def setDirectDownloadEnabled():
'''public MediaHttpDownloader setDirectDownloadEnabled(final boolean directDownloadEnabled)
'''
pass
def setProgressListener():
'''public MediaHttpDownloader setProgressListener(final MediaHttpDownloaderProgressListener progressListener)
'''
pass
def getProgressListener():
'''public MediaHttpDownloaderProgressListener getProgressListener()
'''
pass
def getTransport():
'''public HttpTransport getTransport()
'''
pass
def setChunkSize():
'''public MediaHttpDownloader setChunkSize(final int chunkSize)
'''
pass
def getChunkSize():
'''public int getChunkSize()
'''
pass
def getNumBytesDownloaded():
'''public long getNumBytesDownloaded()
'''
pass
def getLastBytePosition():
'''public long getLastBytePosition()
'''
pass
def getDownloadState():
'''public DownloadState getDownloadState()
'''
pass
def getProgress():
'''public double getProgress()
'''
pass
