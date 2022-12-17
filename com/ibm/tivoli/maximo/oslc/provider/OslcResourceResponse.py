def ():
    '''returns OslcResourceResponse\n\n
    ()\n
    (final JSONArray jsonArray)\n
    (final JSONObject jsonObject, final String resourceURI)\n
    (final JSONObject jsonObject)\n
    (final byte[] resourceData, final String mimeType, final String resourceURI)\n
    (final InputStream resourceDataStream, final String mimeType, final String resourceURI, final File fileToDelete)\n
    (final byte[] resourceData, final String mimeType, final int maxAge, final String eTag)\n
    (final byte[] resourceData, final String mimeType)\n
    (final byte[] resourceData, final String mimeType, final String resourceURI, final boolean disableCache, final int maxAge, final String eTag)\n
    '''
def setMimeTypeJSON():
    '''returns None\n\n
    setMimeTypeJSON()\n
    '''
def setMaxAge():
    '''returns None\n\n
    setMaxAge(final int age)\n
    '''
def setETag():
    '''returns None\n\n
    setETag(final String etag)\n
    '''
def setETagWithVary():
    '''returns None\n\n
    setETagWithVary(final String etag)\n
    '''
def setMaxAgeWithVary():
    '''returns None\n\n
    setMaxAgeWithVary(final int age)\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final String uri)\n
    '''
def hasLocationHeader():
    '''returns boolean\n\n
    hasLocationHeader()\n
    '''
def addCookie():
    '''returns None\n\n
    addCookie(final String cookie, final String value)\n
    '''
def setCookies():
    '''returns None\n\n
    setCookies(final Map<String, String> respCookies)\n
    '''
def getJSONData():
    '''returns JSONArtifact\n\n
    getJSONData()\n
    '''
def setHeaders():
    '''returns None\n\n
    setHeaders(final Map<String, String> headers)\n
    '''
def getResponseCode():
    '''returns int\n\n
    getResponseCode()\n
    '''
def setResponseCode():
    '''returns None\n\n
    setResponseCode(final int responseCode)\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final String header, final String value)\n
    '''
def setResourceNotModifed():
    '''returns None\n\n
    setResourceNotModifed()\n
    '''
def isResourceModified():
    '''returns boolean\n\n
    isResourceModified()\n
    '''
def getResourceData():
    '''returns byte[]\n\n
    getResourceData()\n
    '''
def getResourceStream():
    '''returns InputStream\n\n
    getResourceStream()\n
    '''
def getMimeType():
    '''returns String\n\n
    getMimeType()\n
    '''
def getResourceURI():
    '''returns String\n\n
    getResourceURI()\n
    '''
def isDisableCache():
    '''returns boolean\n\n
    isDisableCache()\n
    '''
def getETag():
    '''returns String\n\n
    getETag()\n
    '''
def getMaxAge():
    '''returns int\n\n
    getMaxAge()\n
    '''
def setContentDisposition():
    '''returns None\n\n
    setContentDisposition(final String disp)\n
    '''
def getFileToDelete():
    '''returns File\n\n
    getFileToDelete()\n
    '''
