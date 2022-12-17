NOT_CACHED = "int  0"
WAS_CACHED = "int  1"
POPULATED_CACHE = "int  2"
SERVLET_REQUEST = "int  1"
PORTLET_CACHE_REQUEST = "int  2"
def ():
    '''returns FragmentComposer\n\n
    (final CacheProxyRequest request, final CacheProxyResponse response)\n
    ()\n
    '''
def resetRequestAndResponseOnly():
    '''returns None\n\n
    resetRequestAndResponseOnly(final CacheProxyRequest request, final CacheProxyResponse response)\n
    '''
def reset():
    '''returns None\n\n
    reset(final CacheProxyRequest request, final CacheProxyResponse response)\n
    '''
def addContents():
    '''returns None\n\n
    addContents(final Object[] contents)\n
    '''
def setDoNotConsume():
    '''returns None\n\n
    setDoNotConsume(final boolean dnc)\n
    '''
def getDoNotConsume():
    '''returns boolean\n\n
    getDoNotConsume()\n
    '''
def setConsumeSubfragments():
    '''returns None\n\n
    setConsumeSubfragments(final boolean csf)\n
    '''
def getConsumeSubfragments():
    '''returns boolean\n\n
    getConsumeSubfragments()\n
    '''
def getHasCacheableConsumingParent():
    '''returns boolean\n\n
    getHasCacheableConsumingParent()\n
    '''
def setHasCacheableConsumingParent():
    '''returns None\n\n
    setHasCacheableConsumingParent(final boolean hccp)\n
    '''
def setBufferSize():
    '''returns None\n\n
    setBufferSize(final int size)\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def resetBuffer():
    '''returns None\n\n
    resetBuffer()\n
    '''
def requestFinished():
    '''returns None\n\n
    requestFinished()\n
    '''
def shouldCacheOutput():
    '''returns boolean\n\n
    shouldCacheOutput()\n
    '''
def isExternallyCached():
    '''returns boolean\n\n
    isExternallyCached()\n
    '''
def setParentExternallyCacheable():
    '''returns None\n\n
    setParentExternallyCacheable(final boolean parentExternal)\n
    '''
def shouldExternalCacheOutput():
    '''returns boolean\n\n
    shouldExternalCacheOutput()\n
    '''
def startChildFragmentComposer():
    '''returns None\n\n
    startChildFragmentComposer(final FragmentComposer fragmentComposer)\n
    '''
def endChildFragmentComposer():
    '''returns None\n\n
    endChildFragmentComposer(final FragmentComposer child)\n
    '''
def saveCachedData():
    '''returns None\n\n
    saveCachedData()\n
    '''
def getOutputStream():
    '''returns ServletOutputStream\n\n
    getOutputStream()\n
    '''
def getPrintWriter():
    '''returns PrintWriter\n\n
    getPrintWriter()\n
    '''
def getMemento():
    '''returns FragmentComposerMemento\n\n
    getMemento(final CacheProxyRequest request)\n
    '''
def copyContentForParents():
    '''returns None\n\n
    copyContentForParents()\n
    '''
def getContextPath():
    '''returns String\n\n
    getContextPath()\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray(final String charEnc)\n
    '''
def getCacheType():
    '''returns int\n\n
    getCacheType()\n
    '''
def setCacheType():
    '''returns None\n\n
    setCacheType(final int cacheType)\n
    '''
def getParent():
    '''returns FragmentComposer\n\n
    getParent()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final FragmentComposer fc)\n
    '''
def isExternalPage():
    '''returns boolean\n\n
    isExternalPage()\n
    '''
def setExternalPage():
    '''returns None\n\n
    setExternalPage(final boolean externalPage)\n
    '''
def setAttributeTableBytes():
    '''returns None\n\n
    setAttributeTableBytes(final byte[] attributeTableBytes)\n
    '''
def getAttributeTableBytes():
    '''returns byte[]\n\n
    getAttributeTableBytes()\n
    '''
def setAttributeTable():
    '''returns None\n\n
    setAttributeTable(final CacheProxyRequest.Attribute[] attributeTable)\n
    '''
def getFragmentInfo():
    '''returns FragmentInfo\n\n
    getFragmentInfo()\n
    '''
def setFragmentInfo():
    '''returns None\n\n
    setFragmentInfo(final FragmentInfo fragmentInfo)\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def setURI():
    '''returns None\n\n
    setURI(final String uri)\n
    '''
def getServletClassName():
    '''returns String\n\n
    getServletClassName()\n
    '''
def setServletClassName():
    '''returns None\n\n
    setServletClassName(final String servletClassName)\n
    '''
def getInclude():
    '''returns boolean\n\n
    getInclude()\n
    '''
def setInclude():
    '''returns None\n\n
    setInclude(final boolean include)\n
    '''
def getNamedDispatch():
    '''returns boolean\n\n
    getNamedDispatch()\n
    '''
def setNamedDispatch():
    '''returns None\n\n
    setNamedDispatch(final boolean namedDispatch)\n
    '''
def setExpirationTime():
    '''returns None\n\n
    setExpirationTime(final long expirationTime)\n
    '''
def getExpirationTime():
    '''returns long\n\n
    getExpirationTime()\n
    '''
def getTimeStamp():
    '''returns long\n\n
    getTimeStamp()\n
    '''
def setTimeStamp():
    '''returns None\n\n
    setTimeStamp(final long timeStamp)\n
    '''
def getAllInvalidationIds():
    '''returns ValueSet\n\n
    getAllInvalidationIds()\n
    '''
def getAllTemplates():
    '''returns ValueSet\n\n
    getAllTemplates()\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final String key, final String value, final boolean isSet)\n
    '''
def sendRedirect():
    '''returns None\n\n
    sendRedirect(final String location)\n
    '''
def addDynamicContentProvider():
    '''returns None\n\n
    addDynamicContentProvider(final DynamicContentProvider dynamicContentProvider)\n
    '''
def addCookie():
    '''returns None\n\n
    addCookie(final Cookie cookie)\n
    '''
def setDateHeader():
    '''returns None\n\n
    setDateHeader(final String name, final long value, final boolean isSet)\n
    '''
def setIntHeader():
    '''returns None\n\n
    setIntHeader(final String name, final int value, final boolean isSet)\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final int statusCode)\n
    setStatus(final int statusCode, final String comment)\n
    '''
def setContentLength():
    '''returns None\n\n
    setContentLength(final int contentLength)\n
    '''
def setContentType():
    '''returns None\n\n
    setContentType(final String contentType)\n
    '''
def setCharacterEncoding():
    '''returns None\n\n
    setCharacterEncoding(final String charEnc)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def setESIVersion():
    '''returns None\n\n
    setESIVersion(final int esiVersion)\n
    '''
def getESIVersion():
    '''returns int\n\n
    getESIVersion()\n
    '''
def isArdChild():
    '''returns boolean\n\n
    isArdChild()\n
    '''
def setArdChild():
    '''returns None\n\n
    setArdChild(final boolean ardChild)\n
    '''
def isArdParent():
    '''returns boolean\n\n
    isArdParent()\n
    '''
def setArdParent():
    '''returns None\n\n
    setArdParent(final boolean ardParent)\n
    '''
def getArdChildID():
    '''returns String\n\n
    getArdChildID()\n
    '''
def setArdChildID():
    '''returns None\n\n
    setArdChildID(final String childID)\n
    '''
def getArdChildren():
    '''returns int\n\n
    getArdChildren()\n
    '''
def isFinishedProcessing():
    '''returns boolean\n\n
    isFinishedProcessing()\n
    '''
def setFinishedProcessing():
    '''returns None\n\n
    setFinishedProcessing(final boolean finishedProcessing)\n
    '''
def getARDChildFragmentComposer():
    '''returns FragmentComposer\n\n
    getARDChildFragmentComposer(final String ardID)\n
    '''
def addChildARDFragmentComposer():
    '''returns None\n\n
    addChildARDFragmentComposer(final String ardID, final FragmentComposer fragmentComposer)\n
    '''
def removeChildARDFragmentComposer():
    '''returns FragmentComposer\n\n
    removeChildARDFragmentComposer(final String ardID)\n
    '''
def isDiscardJSPContent():
    '''returns boolean\n\n
    isDiscardJSPContent()\n
    '''
def setDiscardJSPContent():
    '''returns None\n\n
    setDiscardJSPContent(final boolean discardJSPContent)\n
    '''
