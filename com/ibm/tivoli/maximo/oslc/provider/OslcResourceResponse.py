def OslcResourceResponse():
'''public OslcResourceResponse()
public OslcResourceResponse(final JSONArray jsonArray)
public OslcResourceResponse(final JSONObject jsonObject, final String resourceURI)
public OslcResourceResponse(final JSONObject jsonObject)
public OslcResourceResponse(final byte[] resourceData, final String mimeType, final String resourceURI)
public OslcResourceResponse(final InputStream resourceDataStream, final String mimeType, final String resourceURI, final File fileToDelete)
public OslcResourceResponse(final byte[] resourceData, final String mimeType, final int maxAge, final String eTag)
public OslcResourceResponse(final byte[] resourceData, final String mimeType)
public OslcResourceResponse(final byte[] resourceData, final String mimeType, final String resourceURI, final boolean disableCache, final int maxAge, final String eTag)
'''
pass
def setMimeTypeJSON():
'''public void setMimeTypeJSON()
'''
pass
def setMaxAge():
'''public void setMaxAge(final int age)
'''
pass
def setETag():
'''public void setETag(final String etag)
'''
pass
def setETagWithVary():
'''public void setETagWithVary(final String etag)
'''
pass
def setMaxAgeWithVary():
'''public void setMaxAgeWithVary(final int age)
'''
pass
def setLocation():
'''public void setLocation(final String uri)
'''
pass
def hasLocationHeader():
'''public boolean hasLocationHeader()
'''
pass
def addCookie():
'''public void addCookie(final String cookie, final String value)
'''
pass
def setCookies():
'''public void setCookies(final Map<String, String> respCookies)
'''
pass
def getCookies():
'''public Map<String, String> getCookies()
'''
pass
def getJSONData():
'''public JSONArtifact getJSONData()
'''
pass
def getHeaders():
'''public Map<String, String> getHeaders()
'''
pass
def setHeaders():
'''public void setHeaders(final Map<String, String> headers)
'''
pass
def getResponseCode():
'''public int getResponseCode()
'''
pass
def setResponseCode():
'''public void setResponseCode(final int responseCode)
'''
pass
def addHeader():
'''public void addHeader(final String header, final String value)
'''
pass
def setResourceNotModifed():
'''public void setResourceNotModifed()
'''
pass
def isResourceModified():
'''public boolean isResourceModified()
'''
pass
def getResourceData():
'''public byte[] getResourceData()
'''
pass
def getResourceStream():
'''public InputStream getResourceStream()
'''
pass
def getMimeType():
'''public String getMimeType()
'''
pass
def getResourceURI():
'''public String getResourceURI()
'''
pass
def isDisableCache():
'''public boolean isDisableCache()
'''
pass
def getETag():
'''public String getETag()
'''
pass
def getMaxAge():
'''public int getMaxAge()
'''
pass
def setContentDisposition():
'''public void setContentDisposition(final String disp)
'''
pass
def getFileToDelete():
'''public File getFileToDelete()
'''
pass
