CONTENT_LENGTH_HEADER = "String  \"X-Upload-Content-Length\""
CONTENT_TYPE_HEADER = "String  \"X-Upload-Content-Type\""
MINIMUM_CHUNK_SIZE = "int  262144"
DEFAULT_CHUNK_SIZE = "int  10485760"
def ():
    '''returns MediaHttpUploader\n\n
    (final AbstractInputStreamContent mediaContent, final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)\n
    '''
def upload():
    '''returns HttpResponse\n\n
    upload(final GenericUrl initiationRequestUrl)\n
    '''
def getMetadata():
    '''returns HttpContent\n\n
    getMetadata()\n
    '''
def setMetadata():
    '''returns MediaHttpUploader\n\n
    setMetadata(final HttpContent metadata)\n
    '''
def getMediaContent():
    '''returns HttpContent\n\n
    getMediaContent()\n
    '''
def getTransport():
    '''returns HttpTransport\n\n
    getTransport()\n
    '''
def setDirectUploadEnabled():
    '''returns MediaHttpUploader\n\n
    setDirectUploadEnabled(final boolean directUploadEnabled)\n
    '''
def isDirectUploadEnabled():
    '''returns boolean\n\n
    isDirectUploadEnabled()\n
    '''
def setProgressListener():
    '''returns MediaHttpUploader\n\n
    setProgressListener(final MediaHttpUploaderProgressListener progressListener)\n
    '''
def getProgressListener():
    '''returns MediaHttpUploaderProgressListener\n\n
    getProgressListener()\n
    '''
def setChunkSize():
    '''returns MediaHttpUploader\n\n
    setChunkSize(final int chunkSize)\n
    '''
def getChunkSize():
    '''returns int\n\n
    getChunkSize()\n
    '''
def getDisableGZipContent():
    '''returns boolean\n\n
    getDisableGZipContent()\n
    '''
def setDisableGZipContent():
    '''returns MediaHttpUploader\n\n
    setDisableGZipContent(final boolean disableGZipContent)\n
    '''
def getSleeper():
    '''returns Sleeper\n\n
    getSleeper()\n
    '''
def setSleeper():
    '''returns MediaHttpUploader\n\n
    setSleeper(final Sleeper sleeper)\n
    '''
def getInitiationRequestMethod():
    '''returns String\n\n
    getInitiationRequestMethod()\n
    '''
def setInitiationRequestMethod():
    '''returns MediaHttpUploader\n\n
    setInitiationRequestMethod(final String initiationRequestMethod)\n
    '''
def setInitiationHeaders():
    '''returns MediaHttpUploader\n\n
    setInitiationHeaders(final HttpHeaders initiationHeaders)\n
    '''
def getInitiationHeaders():
    '''returns HttpHeaders\n\n
    getInitiationHeaders()\n
    '''
def getNumBytesUploaded():
    '''returns long\n\n
    getNumBytesUploaded()\n
    '''
def getUploadState():
    '''returns UploadState\n\n
    getUploadState()\n
    '''
def getProgress():
    '''returns double\n\n
    getProgress()\n
    '''
