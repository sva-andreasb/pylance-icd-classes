NOT_CACHED = "int  0"
WAS_CACHED = "int  1"
POPULATED_CACHE = "int  2"
SERVLET_REQUEST = "int  1"
PORTLET_CACHE_REQUEST = "int  2"
def FragmentComposer():
'''public FragmentComposer(final CacheProxyRequest request, final CacheProxyResponse response)
public FragmentComposer()
'''
pass
def resetRequestAndResponseOnly():
'''public void resetRequestAndResponseOnly(final CacheProxyRequest request, final CacheProxyResponse response)
'''
pass
def reset():
'''public void reset(final CacheProxyRequest request, final CacheProxyResponse response)
'''
pass
def addContents():
'''public void addContents(final Object[] contents)
'''
pass
def setDoNotConsume():
'''public void setDoNotConsume(final boolean dnc)
'''
pass
def getDoNotConsume():
'''public boolean getDoNotConsume()
'''
pass
def setConsumeSubfragments():
'''public void setConsumeSubfragments(final boolean csf)
'''
pass
def getConsumeSubfragments():
'''public boolean getConsumeSubfragments()
'''
pass
def getHasCacheableConsumingParent():
'''public boolean getHasCacheableConsumingParent()
'''
pass
def setHasCacheableConsumingParent():
'''public void setHasCacheableConsumingParent(final boolean hccp)
'''
pass
def setBufferSize():
'''public void setBufferSize(final int size)
'''
pass
def getBufferSize():
'''public int getBufferSize()
'''
pass
def resetBuffer():
'''public void resetBuffer()
'''
pass
def requestFinished():
'''public void requestFinished()
'''
pass
def shouldCacheOutput():
'''public boolean shouldCacheOutput()
'''
pass
def isExternallyCached():
'''public boolean isExternallyCached()
'''
pass
def setParentExternallyCacheable():
'''public void setParentExternallyCacheable(final boolean parentExternal)
'''
pass
def shouldExternalCacheOutput():
'''public boolean shouldExternalCacheOutput()
'''
pass
def startChildFragmentComposer():
'''public void startChildFragmentComposer(final FragmentComposer fragmentComposer)
'''
pass
def endChildFragmentComposer():
'''public void endChildFragmentComposer(final FragmentComposer child)
'''
pass
def saveCachedData():
'''public void saveCachedData()
'''
pass
def getOutputStream():
'''public ServletOutputStream getOutputStream()
'''
pass
def getPrintWriter():
'''public PrintWriter getPrintWriter()
'''
pass
def getMemento():
'''public FragmentComposerMemento getMemento(final CacheProxyRequest request)
'''
pass
def copyContentForParents():
'''public void copyContentForParents()
'''
pass
def getContextPath():
'''public String getContextPath()
'''
pass
def toByteArray():
'''public byte[] toByteArray(final String charEnc)
'''
pass
def getCacheType():
'''public int getCacheType()
'''
pass
def setCacheType():
'''public void setCacheType(final int cacheType)
'''
pass
def getParent():
'''public FragmentComposer getParent()
'''
pass
def setParent():
'''public void setParent(final FragmentComposer fc)
'''
pass
def isExternalPage():
'''public boolean isExternalPage()
'''
pass
def setExternalPage():
'''public void setExternalPage(final boolean externalPage)
'''
pass
def setAttributeTableBytes():
'''public void setAttributeTableBytes(final byte[] attributeTableBytes)
'''
pass
def getAttributeTableBytes():
'''public byte[] getAttributeTableBytes()
'''
pass
def setAttributeTable():
'''public void setAttributeTable(final CacheProxyRequest.Attribute[] attributeTable)
'''
pass
def getFragmentInfo():
'''public FragmentInfo getFragmentInfo()
'''
pass
def setFragmentInfo():
'''public void setFragmentInfo(final FragmentInfo fragmentInfo)
'''
pass
def getURI():
'''public String getURI()
'''
pass
def setURI():
'''public void setURI(final String uri)
'''
pass
def getServletClassName():
'''public String getServletClassName()
'''
pass
def setServletClassName():
'''public void setServletClassName(final String servletClassName)
'''
pass
def getInclude():
'''public boolean getInclude()
'''
pass
def setInclude():
'''public void setInclude(final boolean include)
'''
pass
def getNamedDispatch():
'''public boolean getNamedDispatch()
'''
pass
def setNamedDispatch():
'''public void setNamedDispatch(final boolean namedDispatch)
'''
pass
def setExpirationTime():
'''public void setExpirationTime(final long expirationTime)
'''
pass
def getExpirationTime():
'''public long getExpirationTime()
'''
pass
def getTimeStamp():
'''public long getTimeStamp()
'''
pass
def setTimeStamp():
'''public void setTimeStamp(final long timeStamp)
'''
pass
def getAllInvalidationIds():
'''public ValueSet getAllInvalidationIds()
'''
pass
def getAllTemplates():
'''public ValueSet getAllTemplates()
'''
pass
def setHeader():
'''public void setHeader(final String key, final String value, final boolean isSet)
'''
pass
def sendRedirect():
'''public void sendRedirect(final String location)
'''
pass
def addDynamicContentProvider():
'''public void addDynamicContentProvider(final DynamicContentProvider dynamicContentProvider)
'''
pass
def addCookie():
'''public void addCookie(final Cookie cookie)
'''
pass
def setDateHeader():
'''public void setDateHeader(final String name, final long value, final boolean isSet)
'''
pass
def setIntHeader():
'''public void setIntHeader(final String name, final int value, final boolean isSet)
'''
pass
def setStatus():
'''public void setStatus(final int statusCode)
public void setStatus(final int statusCode, final String comment)
'''
pass
def setContentLength():
'''public void setContentLength(final int contentLength)
'''
pass
def setContentType():
'''public void setContentType(final String contentType)
'''
pass
def setCharacterEncoding():
'''public void setCharacterEncoding(final String charEnc)
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
'''
pass
def setESIVersion():
'''public void setESIVersion(final int esiVersion)
'''
pass
def getESIVersion():
'''public int getESIVersion()
'''
pass
def isArdChild():
'''public boolean isArdChild()
'''
pass
def setArdChild():
'''public void setArdChild(final boolean ardChild)
'''
pass
def isArdParent():
'''public boolean isArdParent()
'''
pass
def setArdParent():
'''public void setArdParent(final boolean ardParent)
'''
pass
def getNumOfUnprocessedARDChildren():
'''public synchronized int getNumOfUnprocessedARDChildren()
'''
pass
def finishedProcessingARDChild():
'''public synchronized void finishedProcessingARDChild()
'''
pass
def addARDChildForProcessing():
'''public synchronized void addARDChildForProcessing()
'''
pass
def getArdChildID():
'''public String getArdChildID()
'''
pass
def setArdChildID():
'''public void setArdChildID(final String childID)
'''
pass
def getArdChildren():
'''public int getArdChildren()
'''
pass
def isFinishedProcessing():
'''public boolean isFinishedProcessing()
'''
pass
def setFinishedProcessing():
'''public void setFinishedProcessing(final boolean finishedProcessing)
'''
pass
def getARDChildFragmentComposer():
'''public FragmentComposer getARDChildFragmentComposer(final String ardID)
'''
pass
def addChildARDFragmentComposer():
'''public void addChildARDFragmentComposer(final String ardID, final FragmentComposer fragmentComposer)
'''
pass
def removeChildARDFragmentComposer():
'''public FragmentComposer removeChildARDFragmentComposer(final String ardID)
'''
pass
def isDiscardJSPContent():
'''public boolean isDiscardJSPContent()
'''
pass
def setDiscardJSPContent():
'''public void setDiscardJSPContent(final boolean discardJSPContent)
'''
pass
