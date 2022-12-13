CONTENT_LENGTH_HEADER = "String  \"X-Upload-Content-Length\""
CONTENT_TYPE_HEADER = "String  \"X-Upload-Content-Type\""
MINIMUM_CHUNK_SIZE = "int  262144"
DEFAULT_CHUNK_SIZE = "int  10485760"
def MediaHttpUploader():
    '''    public MediaHttpUploader(final AbstractInputStreamContent mediaContent, final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)
    '''
def upload():
    '''    public HttpResponse upload(final GenericUrl initiationRequestUrl)
    '''
def getMetadata():
    '''    public HttpContent getMetadata()
    '''
def setMetadata():
    '''    public MediaHttpUploader setMetadata(final HttpContent metadata)
    '''
def getMediaContent():
    '''    public HttpContent getMediaContent()
    '''
def getTransport():
    '''    public HttpTransport getTransport()
    '''
def setDirectUploadEnabled():
    '''    public MediaHttpUploader setDirectUploadEnabled(final boolean directUploadEnabled)
    '''
def isDirectUploadEnabled():
    '''    public boolean isDirectUploadEnabled()
    '''
def setProgressListener():
    '''    public MediaHttpUploader setProgressListener(final MediaHttpUploaderProgressListener progressListener)
    '''
def getProgressListener():
    '''    public MediaHttpUploaderProgressListener getProgressListener()
    '''
def setChunkSize():
    '''    public MediaHttpUploader setChunkSize(final int chunkSize)
    '''
def getChunkSize():
    '''    public int getChunkSize()
    '''
def getDisableGZipContent():
    '''    public boolean getDisableGZipContent()
    '''
def setDisableGZipContent():
    '''    public MediaHttpUploader setDisableGZipContent(final boolean disableGZipContent)
    '''
def getSleeper():
    '''    public Sleeper getSleeper()
    '''
def setSleeper():
    '''    public MediaHttpUploader setSleeper(final Sleeper sleeper)
    '''
def getInitiationRequestMethod():
    '''    public String getInitiationRequestMethod()
    '''
def setInitiationRequestMethod():
    '''    public MediaHttpUploader setInitiationRequestMethod(final String initiationRequestMethod)
    '''
def setInitiationHeaders():
    '''    public MediaHttpUploader setInitiationHeaders(final HttpHeaders initiationHeaders)
    '''
def getInitiationHeaders():
    '''    public HttpHeaders getInitiationHeaders()
    '''
def getNumBytesUploaded():
    '''    public long getNumBytesUploaded()
    '''
def getUploadState():
    '''    public UploadState getUploadState()
    '''
def getProgress():
    '''    public double getProgress()
    '''
