CONTENT_LENGTH_HEADER = "String  X-Upload-Content-Length""
CONTENT_TYPE_HEADER = "String  X-Upload-Content-Type""
MINIMUM_CHUNK_SIZE = "int  262144"
DEFAULT_CHUNK_SIZE = "int  10485760"
def MediaHttpUploader():
'''public MediaHttpUploader(final AbstractInputStreamContent mediaContent, final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)
'''
pass
def upload():
'''public HttpResponse upload(final GenericUrl initiationRequestUrl)
'''
pass
def getMetadata():
'''public HttpContent getMetadata()
'''
pass
def setMetadata():
'''public MediaHttpUploader setMetadata(final HttpContent metadata)
'''
pass
def getMediaContent():
'''public HttpContent getMediaContent()
'''
pass
def getTransport():
'''public HttpTransport getTransport()
'''
pass
def setDirectUploadEnabled():
'''public MediaHttpUploader setDirectUploadEnabled(final boolean directUploadEnabled)
'''
pass
def isDirectUploadEnabled():
'''public boolean isDirectUploadEnabled()
'''
pass
def setProgressListener():
'''public MediaHttpUploader setProgressListener(final MediaHttpUploaderProgressListener progressListener)
'''
pass
def getProgressListener():
'''public MediaHttpUploaderProgressListener getProgressListener()
'''
pass
def setChunkSize():
'''public MediaHttpUploader setChunkSize(final int chunkSize)
'''
pass
def getChunkSize():
'''public int getChunkSize()
'''
pass
def getDisableGZipContent():
'''public boolean getDisableGZipContent()
'''
pass
def setDisableGZipContent():
'''public MediaHttpUploader setDisableGZipContent(final boolean disableGZipContent)
'''
pass
def getSleeper():
'''public Sleeper getSleeper()
'''
pass
def setSleeper():
'''public MediaHttpUploader setSleeper(final Sleeper sleeper)
'''
pass
def getInitiationRequestMethod():
'''public String getInitiationRequestMethod()
'''
pass
def setInitiationRequestMethod():
'''public MediaHttpUploader setInitiationRequestMethod(final String initiationRequestMethod)
'''
pass
def setInitiationHeaders():
'''public MediaHttpUploader setInitiationHeaders(final HttpHeaders initiationHeaders)
'''
pass
def getInitiationHeaders():
'''public HttpHeaders getInitiationHeaders()
'''
pass
def getNumBytesUploaded():
'''public long getNumBytesUploaded()
'''
pass
def getUploadState():
'''public UploadState getUploadState()
'''
pass
def getProgress():
'''public double getProgress()
'''
pass
