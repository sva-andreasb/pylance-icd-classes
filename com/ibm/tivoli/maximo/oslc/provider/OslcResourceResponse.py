def OslcResourceResponse():
    '''    public OslcResourceResponse()
    public OslcResourceResponse(final JSONArray jsonArray)
    public OslcResourceResponse(final JSONObject jsonObject, final String resourceURI)
    public OslcResourceResponse(final JSONObject jsonObject)
    public OslcResourceResponse(final byte[] resourceData, final String mimeType, final String resourceURI)
    public OslcResourceResponse(final InputStream resourceDataStream, final String mimeType, final String resourceURI, final File fileToDelete)
    public OslcResourceResponse(final byte[] resourceData, final String mimeType, final int maxAge, final String eTag)
    public OslcResourceResponse(final byte[] resourceData, final String mimeType)
    public OslcResourceResponse(final byte[] resourceData, final String mimeType, final String resourceURI, final boolean disableCache, final int maxAge, final String eTag)
    '''
def setMimeTypeJSON():
    '''    public void setMimeTypeJSON()
    '''
def setMaxAge():
    '''    public void setMaxAge(final int age)
    '''
def setETag():
    '''    public void setETag(final String etag)
    '''
def setETagWithVary():
    '''    public void setETagWithVary(final String etag)
    '''
def setMaxAgeWithVary():
    '''    public void setMaxAgeWithVary(final int age)
    '''
def setLocation():
    '''    public void setLocation(final String uri)
    '''
def hasLocationHeader():
    '''    public boolean hasLocationHeader()
    '''
def addCookie():
    '''    public void addCookie(final String cookie, final String value)
    '''
def setCookies():
    '''    public void setCookies(final Map<String, String> respCookies)
    '''
def getCookies():
    '''    public Map<String, String> getCookies()
    '''
def getJSONData():
    '''    public JSONArtifact getJSONData()
    '''
def getHeaders():
    '''    public Map<String, String> getHeaders()
    '''
def setHeaders():
    '''    public void setHeaders(final Map<String, String> headers)
    '''
def getResponseCode():
    '''    public int getResponseCode()
    '''
def setResponseCode():
    '''    public void setResponseCode(final int responseCode)
    '''
def addHeader():
    '''    public void addHeader(final String header, final String value)
    '''
def setResourceNotModifed():
    '''    public void setResourceNotModifed()
    '''
def isResourceModified():
    '''    public boolean isResourceModified()
    '''
def getResourceData():
    '''    public byte[] getResourceData()
    '''
def getResourceStream():
    '''    public InputStream getResourceStream()
    '''
def getMimeType():
    '''    public String getMimeType()
    '''
def getResourceURI():
    '''    public String getResourceURI()
    '''
def isDisableCache():
    '''    public boolean isDisableCache()
    '''
def getETag():
    '''    public String getETag()
    '''
def getMaxAge():
    '''    public int getMaxAge()
    '''
def setContentDisposition():
    '''    public void setContentDisposition(final String disp)
    '''
def getFileToDelete():
    '''    public File getFileToDelete()
    '''
