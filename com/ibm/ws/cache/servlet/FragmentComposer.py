NOT_CACHED = "int  0"
WAS_CACHED = "int  1"
POPULATED_CACHE = "int  2"
SERVLET_REQUEST = "int  1"
PORTLET_CACHE_REQUEST = "int  2"
def FragmentComposer():
    '''public FragmentComposer(final CacheProxyRequest request, final CacheProxyResponse response)
    public FragmentComposer()
    '''
def resetRequestAndResponseOnly():
    '''public void resetRequestAndResponseOnly(final CacheProxyRequest request, final CacheProxyResponse response)
    '''
def reset():
    '''public void reset(final CacheProxyRequest request, final CacheProxyResponse response)
    '''
def addContents():
    '''public void addContents(final Object[] contents)
    '''
def setDoNotConsume():
    '''public void setDoNotConsume(final boolean dnc)
    '''
def getDoNotConsume():
    '''public boolean getDoNotConsume()
    '''
def setConsumeSubfragments():
    '''public void setConsumeSubfragments(final boolean csf)
    '''
def getConsumeSubfragments():
    '''public boolean getConsumeSubfragments()
    '''
def getHasCacheableConsumingParent():
    '''public boolean getHasCacheableConsumingParent()
    '''
def setHasCacheableConsumingParent():
    '''public void setHasCacheableConsumingParent(final boolean hccp)
    '''
def setBufferSize():
    '''public void setBufferSize(final int size)
    '''
def getBufferSize():
    '''public int getBufferSize()
    '''
def resetBuffer():
    '''public void resetBuffer()
    '''
def requestFinished():
    '''public void requestFinished()
    '''
def shouldCacheOutput():
    '''public boolean shouldCacheOutput()
    '''
def isExternallyCached():
    '''public boolean isExternallyCached()
    '''
def setParentExternallyCacheable():
    '''public void setParentExternallyCacheable(final boolean parentExternal)
    '''
def shouldExternalCacheOutput():
    '''public boolean shouldExternalCacheOutput()
    '''
def startChildFragmentComposer():
    '''public void startChildFragmentComposer(final FragmentComposer fragmentComposer)
    '''
def endChildFragmentComposer():
    '''public void endChildFragmentComposer(final FragmentComposer child)
    '''
def saveCachedData():
    '''public void saveCachedData()
    '''
def getOutputStream():
    '''public ServletOutputStream getOutputStream()
    '''
def getPrintWriter():
    '''public PrintWriter getPrintWriter()
    '''
def getMemento():
    '''public FragmentComposerMemento getMemento(final CacheProxyRequest request)
    '''
def copyContentForParents():
    '''public void copyContentForParents()
    '''
def getContextPath():
    '''public String getContextPath()
    '''
def toByteArray():
    '''public byte[] toByteArray(final String charEnc)
    '''
def getCacheType():
    '''public int getCacheType()
    '''
def setCacheType():
    '''public void setCacheType(final int cacheType)
    '''
def getParent():
    '''public FragmentComposer getParent()
    '''
def setParent():
    '''public void setParent(final FragmentComposer fc)
    '''
def isExternalPage():
    '''public boolean isExternalPage()
    '''
def setExternalPage():
    '''public void setExternalPage(final boolean externalPage)
    '''
def setAttributeTableBytes():
    '''public void setAttributeTableBytes(final byte[] attributeTableBytes)
    '''
def getAttributeTableBytes():
    '''public byte[] getAttributeTableBytes()
    '''
def setAttributeTable():
    '''public void setAttributeTable(final CacheProxyRequest.Attribute[] attributeTable)
    '''
def getFragmentInfo():
    '''public FragmentInfo getFragmentInfo()
    '''
def setFragmentInfo():
    '''public void setFragmentInfo(final FragmentInfo fragmentInfo)
    '''
def getURI():
    '''public String getURI()
    '''
def setURI():
    '''public void setURI(final String uri)
    '''
def getServletClassName():
    '''public String getServletClassName()
    '''
def setServletClassName():
    '''public void setServletClassName(final String servletClassName)
    '''
def getInclude():
    '''public boolean getInclude()
    '''
def setInclude():
    '''public void setInclude(final boolean include)
    '''
def getNamedDispatch():
    '''public boolean getNamedDispatch()
    '''
def setNamedDispatch():
    '''public void setNamedDispatch(final boolean namedDispatch)
    '''
def setExpirationTime():
    '''public void setExpirationTime(final long expirationTime)
    '''
def getExpirationTime():
    '''public long getExpirationTime()
    '''
def getTimeStamp():
    '''public long getTimeStamp()
    '''
def setTimeStamp():
    '''public void setTimeStamp(final long timeStamp)
    '''
def getAllInvalidationIds():
    '''public ValueSet getAllInvalidationIds()
    '''
def getAllTemplates():
    '''public ValueSet getAllTemplates()
    '''
def setHeader():
    '''public void setHeader(final String key, final String value, final boolean isSet)
    '''
def sendRedirect():
    '''public void sendRedirect(final String location)
    '''
def addDynamicContentProvider():
    '''public void addDynamicContentProvider(final DynamicContentProvider dynamicContentProvider)
    '''
def addCookie():
    '''public void addCookie(final Cookie cookie)
    '''
def setDateHeader():
    '''public void setDateHeader(final String name, final long value, final boolean isSet)
    '''
def setIntHeader():
    '''public void setIntHeader(final String name, final int value, final boolean isSet)
    '''
def setStatus():
    '''public void setStatus(final int statusCode)
    public void setStatus(final int statusCode, final String comment)
    '''
def setContentLength():
    '''public void setContentLength(final int contentLength)
    '''
def setContentType():
    '''public void setContentType(final String contentType)
    '''
def setCharacterEncoding():
    '''public void setCharacterEncoding(final String charEnc)
    '''
def setLocale():
    '''public void setLocale(final Locale locale)
    '''
def setESIVersion():
    '''public void setESIVersion(final int esiVersion)
    '''
def getESIVersion():
    '''public int getESIVersion()
    '''
def isArdChild():
    '''public boolean isArdChild()
    '''
def setArdChild():
    '''public void setArdChild(final boolean ardChild)
    '''
def isArdParent():
    '''public boolean isArdParent()
    '''
def setArdParent():
    '''public void setArdParent(final boolean ardParent)
    '''
def getNumOfUnprocessedARDChildren():
    '''public synchronized int getNumOfUnprocessedARDChildren()
    '''
def finishedProcessingARDChild():
    '''public synchronized void finishedProcessingARDChild()
    '''
def addARDChildForProcessing():
    '''public synchronized void addARDChildForProcessing()
    '''
def getArdChildID():
    '''public String getArdChildID()
    '''
def setArdChildID():
    '''public void setArdChildID(final String childID)
    '''
def getArdChildren():
    '''public int getArdChildren()
    '''
def isFinishedProcessing():
    '''public boolean isFinishedProcessing()
    '''
def setFinishedProcessing():
    '''public void setFinishedProcessing(final boolean finishedProcessing)
    '''
def getARDChildFragmentComposer():
    '''public FragmentComposer getARDChildFragmentComposer(final String ardID)
    '''
def addChildARDFragmentComposer():
    '''public void addChildARDFragmentComposer(final String ardID, final FragmentComposer fragmentComposer)
    '''
def removeChildARDFragmentComposer():
    '''public FragmentComposer removeChildARDFragmentComposer(final String ardID)
    '''
def isDiscardJSPContent():
    '''public boolean isDiscardJSPContent()
    '''
def setDiscardJSPContent():
    '''public void setDiscardJSPContent(final boolean discardJSPContent)
    '''
