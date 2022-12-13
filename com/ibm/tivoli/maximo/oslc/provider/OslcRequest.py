def OslcRequest():
    '''    public OslcRequest(final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost, final List<String> resPath, final String requestURL)
    public OslcRequest(final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost, final List<String> resPath, final String requestURL, final UserInfo userInfo)
    public OslcRequest(final HttpServletRequest request)
    '''
def setProcessUserInfo():
    '''    public void setProcessUserInfo(final UserInfo processUserInfo)
    '''
def getInputStream():
    '''    public InputStream getInputStream()
    '''
def setParts():
    '''    public void setParts(final Map<String, MPPartInfo> parts)
    '''
def isBranchFilterOn():
    '''    public boolean isBranchFilterOn()
    '''
def isIgnoreRowstamp():
    '''    public boolean isIgnoreRowstamp()
    '''
def isIgnoreKeyref():
    '''    public boolean isIgnoreKeyref()
    '''
def getPart():
    '''    public MPPartInfo getPart(final String partKey)
    '''
def isAddSchema():
    '''    public boolean isAddSchema()
    '''
def isAddAction():
    '''    public boolean isAddAction()
    '''
def isEnableSession():
    '''    public boolean isEnableSession()
    '''
def isNewSession():
    '''    public boolean isNewSession()
    '''
def isAddLocalizedRep():
    '''    public boolean isAddLocalizedRep()
    '''
def getUseView():
    '''    public String getUseView()
    '''
def getApiKey():
    '''    public String getApiKey()
    '''
def getApps():
    '''    public String getApps()
    '''
def isApiCall():
    '''    public boolean isApiCall()
    '''
def isClientCertMode():
    '''    public boolean isClientCertMode()
    '''
def isBatchError():
    '''    public boolean isBatchError()
    '''
def verifyCsrfToken():
    '''    public boolean verifyCsrfToken()
    '''
def getCsrfTokenFromRequest():
    '''    public String getCsrfTokenFromRequest()
    '''
def getCsrfToken():
    '''    public String getCsrfToken()
    '''
def getGuestId():
    '''    public String getGuestId()
    '''
def isQueryLocalized():
    '''    public boolean isQueryLocalized()
    '''
def isCsrfSession():
    '''    public boolean isCsrfSession()
    '''
def isProcessAsSelfReferencing():
    '''    public boolean isProcessAsSelfReferencing()
    '''
def isAllowSelfRefDup():
    '''    public boolean isAllowSelfRefDup()
    '''
def getProcessAsSelfRefRelName():
    '''    public String getProcessAsSelfRefRelName()
    '''
def isLocalizedDate():
    '''    public boolean isLocalizedDate()
    '''
def getResponseCookiesToSet():
    '''    public Map<String, String> getResponseCookiesToSet()
    '''
def serializeToBytes():
    '''    public byte[] serializeToBytes()
    '''
def getTransactionId():
    '''    public String getTransactionId()
    '''
def resurrectRequest():
    '''    public static OslcRequest resurrectRequest(final byte[] reqBytes)
    '''
def getHttpServletRequest():
    '''    public HttpServletRequest getHttpServletRequest()
    '''
def setInteractiveRequest():
    '''    public void setInteractiveRequest()
    '''
def isFileLoad():
    '''    public boolean isFileLoad()
    '''
def isAsyncRequest():
    '''    public boolean isAsyncRequest()
    '''
def isInteractiveRequest():
    '''    public boolean isInteractiveRequest()
    '''
def isCheckEsig():
    '''    public boolean isCheckEsig()
    '''
def isIgnoreCollectionRef():
    '''    public boolean isIgnoreCollectionRef()
    '''
def isInlineDoc():
    '''    public boolean isInlineDoc()
    '''
def getUserInfo():
    '''    public UserInfo getUserInfo()
    '''
def readRequestBody():
    '''    public byte[] readRequestBody()
    '''
def setHttpServletResponse():
    '''    public void setHttpServletResponse(final HttpServletResponse response)
    '''
def getHttpServletResponse():
    '''    public HttpServletResponse getHttpServletResponse()
    '''
def setInMemorySort():
    '''    public void setInMemorySort(final boolean inmemsort)
    '''
def isInMemorySort():
    '''    public boolean isInMemorySort()
    '''
def invlaidateSession():
    '''    public void invlaidateSession()
    '''
def bindMboToSession():
    '''    public String bindMboToSession(final String osName, final MboRemote mbo)
    '''
def unbindMboFromSession():
    '''    public MboRemote unbindMboFromSession(final MboRemote mbo)
    '''
def getHeader():
    '''    public String getHeader(final String headerName)
    '''
def copy():
    '''    public OslcRequest copy(final Map<String, List<String>> bulkHeaders, final Map<String, String[]> bulkQueryParams)
    '''
def isRelatedRef():
    '''    public boolean isRelatedRef()
    '''
def isLocalRef():
    '''    public boolean isLocalRef()
    '''
def getAbsoluteURI():
    '''    public String getAbsoluteURI()
    '''
def getDistinctClause():
    '''    public String getDistinctClause()
    '''
def isDistinct():
    '''    public boolean isDistinct()
    '''
def isAction():
    '''    public boolean isAction()
    '''
def isMaxSSO():
    '''    public boolean isMaxSSO()
    '''
def isCollectionCount():
    '''    public boolean isCollectionCount()
    '''
def getAction():
    '''    public String getAction()
    '''
def getTemplate():
    '''    public String getTemplate()
    '''
def isBulkOperation():
    '''    public boolean isBulkOperation()
    '''
def setResourcePath():
    '''    public void setResourcePath(final List<String> resPath)
    '''
def addIDToURI():
    '''    public void addIDToURI(final String id)
    '''
def replaceIDToURI():
    '''    public void replaceIDToURI(final String id)
    '''
def getAbsolutePath():
    '''    public List<String> getAbsolutePath()
    '''
def truncateAbsolutePath():
    '''    public void truncateAbsolutePath(final int num)
    '''
def getRequestPublicURI():
    '''    public String getRequestPublicURI()
    '''
def isAllowEvents():
    '''    public boolean isAllowEvents()
    '''
def isListTemplate():
    '''    public boolean isListTemplate()
    '''
def isChangePasswordSession():
    '''    public boolean isChangePasswordSession()
    '''
def isRegUserSession():
    '''    public boolean isRegUserSession()
    '''
def getResourcePath():
    '''    public List<String> getResourcePath()
    '''
def getRequestURL():
    '''    public String getRequestURL()
    '''
def isLeanJSON():
    '''    public boolean isLeanJSON()
    '''
def getAttachmentDocType():
    '''    public String[] getAttachmentDocType()
    '''
def getLinkHeader():
    '''    public String getLinkHeader()
    '''
def getContentLocationHeader():
    '''    public String getContentLocationHeader()
    '''
def getAttachmentDescription():
    '''    public String getAttachmentDescription()
    '''
def getAttachmentEncDescription():
    '''    public String getAttachmentEncDescription()
    '''
def getAttachmentExternalID():
    '''    public String getAttachmentExternalID()
    '''
def isEditMode():
    '''    public boolean isEditMode()
    '''
def isSetValueMode():
    '''    public boolean isSetValueMode()
    '''
def getSelfRef():
    '''    public String getSelfRef()
    '''
def isShowHidden():
    '''    public boolean isShowHidden()
    '''
def isDropNulls():
    '''    public boolean isDropNulls()
    '''
def getSavedQueryParams():
    '''    public Map<String, String> getSavedQueryParams()
    '''
def isSubmitSession():
    '''    public boolean isSubmitSession()
    '''
def isInitiateStablePaging():
    '''    public boolean isInitiateStablePaging()
    '''
def isCount():
    '''    public boolean isCount()
    '''
def isAllowedActions():
    '''    public boolean isAllowedActions()
    '''
def getSavedQuery():
    '''    public String getSavedQuery()
    '''
def getOslcResourceURI():
    '''    public String getOslcResourceURI()
    '''
def getOslcRequestURI():
    '''    public String getOslcRequestURI()
    '''
def getOslcQuery():
    '''    public OslcQuery getOslcQuery()
    '''
def getResourceQBE():
    '''    public Map<String, String> getResourceQBE()
    '''
def isGETByPOST():
    '''    public boolean isGETByPOST()
    '''
def getResponseFormatMimeTypeMap():
    '''    public Map<String, String> getResponseFormatMimeTypeMap()
    '''
def getRequestFormatMimeTypeMap():
    '''    public Map<String, String> getRequestFormatMimeTypeMap()
    '''
def getDefaultFormat():
    '''    public String getDefaultFormat()
    '''
def getStableResourceId():
    '''    public String getStableResourceId()
    '''
def useFetchLimit():
    '''    public boolean useFetchLimit()
    '''
def getGBFilter():
    '''    public String getGBFilter()
    '''
def getGroupByAttributes():
    '''    public String getGroupByAttributes()
    '''
def getGroupBySortOrder():
    '''    public String getGroupBySortOrder()
    '''
def getGroupByRelations():
    '''    public String getGroupByRelations()
    '''
def getGroupByRelationProperties():
    '''    public String getGroupByRelationProperties()
    '''
def getGroupByTemplate():
    '''    public String getGroupByTemplate()
    '''
def getGroupByRange():
    '''    public String getGroupByRange()
    '''
def getQueryTemplate():
    '''    public String getQueryTemplate()
    '''
def getSchemaSearchTerm():
    '''    public String getSchemaSearchTerm()
    '''
def getSchemaOrderBy():
    '''    public String getSchemaOrderBy()
    '''
def isGroupBy():
    '''    public boolean isGroupBy()
    '''
def isQueryTemplate():
    '''    public boolean isQueryTemplate()
    '''
def internalValues():
    '''    public boolean internalValues()
    '''
def getDependentSubSelects():
    '''    public Map<String, String> getDependentSubSelects()
    '''
def getSubSelectRefs():
    '''    public Map<String, String[]> getSubSelectRefs()
    '''
def invalidateSession():
    '''    public void invalidateSession()
    '''
def getQueryString():
    '''    public Object getQueryString()
    '''
def getTimeLineAttribute():
    '''    public String getTimeLineAttribute()
    '''
def getTimeLineRange():
    '''    public String getTimeLineRange()
    '''
def isSetLocalizedRep():
    '''    public boolean isSetLocalizedRep()
    '''
def getUserWhere():
    '''    public String getUserWhere()
    '''
def getMaxRowStamp():
    '''    public Long getMaxRowStamp()
    '''
def isFetchModeDelta():
    '''    public boolean isFetchModeDelta()
    '''
def isAddQueryMeta():
    '''    public boolean isAddQueryMeta()
    '''
def getNpFilter():
    '''    public String getNpFilter()
    '''
def isAddID():
    '''    public boolean isAddID()
    '''
def getTimeLineFilter():
    '''    public String getTimeLineFilter()
    '''
def isResourceMeta():
    '''    public boolean isResourceMeta()
    '''
def isContentLocalized():
    '''    public boolean isContentLocalized()
    '''
def getQbeFilter():
    '''    public String getQbeFilter()
    '''
def isAddDomainMeta():
    '''    public boolean isAddDomainMeta()
    '''
def getCanChangeExternalStatus():
    '''    public String[] getCanChangeExternalStatus(final String objectName)
    '''
def getCanChangeMaxStatus():
    '''    public String[] getCanChangeMaxStatus(final String objectName)
    '''
def isWhoAmIApi():
    '''    public boolean isWhoAmIApi()
    '''
def getSetValueEvalChild():
    '''    public Map<String, Set<String>> getSetValueEvalChild()
    '''
def isTlModeDate():
    '''    public boolean isTlModeDate()
    '''
def isStrictSchema():
    '''    public boolean isStrictSchema()
    '''
