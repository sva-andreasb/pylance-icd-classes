def OslcRequest():
'''public OslcRequest(final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost, final List<String> resPath, final String requestURL)
public OslcRequest(final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost, final List<String> resPath, final String requestURL, final UserInfo userInfo)
public OslcRequest(final HttpServletRequest request)
'''
pass
def setProcessUserInfo():
'''public void setProcessUserInfo(final UserInfo processUserInfo)
'''
pass
def getInputStream():
'''public InputStream getInputStream()
'''
pass
def setParts():
'''public void setParts(final Map<String, MPPartInfo> parts)
'''
pass
def isBranchFilterOn():
'''public boolean isBranchFilterOn()
'''
pass
def isIgnoreRowstamp():
'''public boolean isIgnoreRowstamp()
'''
pass
def isIgnoreKeyref():
'''public boolean isIgnoreKeyref()
'''
pass
def getPart():
'''public MPPartInfo getPart(final String partKey)
'''
pass
def isAddSchema():
'''public boolean isAddSchema()
'''
pass
def isAddAction():
'''public boolean isAddAction()
'''
pass
def isEnableSession():
'''public boolean isEnableSession()
'''
pass
def isNewSession():
'''public boolean isNewSession()
'''
pass
def isAddLocalizedRep():
'''public boolean isAddLocalizedRep()
'''
pass
def getUseView():
'''public String getUseView()
'''
pass
def getApiKey():
'''public String getApiKey()
'''
pass
def getApps():
'''public String getApps()
'''
pass
def isApiCall():
'''public boolean isApiCall()
'''
pass
def isClientCertMode():
'''public boolean isClientCertMode()
'''
pass
def isBatchError():
'''public boolean isBatchError()
'''
pass
def verifyCsrfToken():
'''public boolean verifyCsrfToken()
'''
pass
def getCsrfTokenFromRequest():
'''public String getCsrfTokenFromRequest()
'''
pass
def getCsrfToken():
'''public String getCsrfToken()
'''
pass
def getGuestId():
'''public String getGuestId()
'''
pass
def isQueryLocalized():
'''public boolean isQueryLocalized()
'''
pass
def isCsrfSession():
'''public boolean isCsrfSession()
'''
pass
def isProcessAsSelfReferencing():
'''public boolean isProcessAsSelfReferencing()
'''
pass
def isAllowSelfRefDup():
'''public boolean isAllowSelfRefDup()
'''
pass
def getProcessAsSelfRefRelName():
'''public String getProcessAsSelfRefRelName()
'''
pass
def isLocalizedDate():
'''public boolean isLocalizedDate()
'''
pass
def getResponseCookiesToSet():
'''public Map<String, String> getResponseCookiesToSet()
'''
pass
def serializeToBytes():
'''public byte[] serializeToBytes()
'''
pass
def getTransactionId():
'''public String getTransactionId()
'''
pass
def resurrectRequest():
'''public static OslcRequest resurrectRequest(final byte[] reqBytes)
'''
pass
def getHttpServletRequest():
'''public HttpServletRequest getHttpServletRequest()
'''
pass
def setInteractiveRequest():
'''public void setInteractiveRequest()
'''
pass
def isFileLoad():
'''public boolean isFileLoad()
'''
pass
def isAsyncRequest():
'''public boolean isAsyncRequest()
'''
pass
def isInteractiveRequest():
'''public boolean isInteractiveRequest()
'''
pass
def isCheckEsig():
'''public boolean isCheckEsig()
'''
pass
def isIgnoreCollectionRef():
'''public boolean isIgnoreCollectionRef()
'''
pass
def isInlineDoc():
'''public boolean isInlineDoc()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def readRequestBody():
'''public byte[] readRequestBody()
'''
pass
def setHttpServletResponse():
'''public void setHttpServletResponse(final HttpServletResponse response)
'''
pass
def getHttpServletResponse():
'''public HttpServletResponse getHttpServletResponse()
'''
pass
def setInMemorySort():
'''public void setInMemorySort(final boolean inmemsort)
'''
pass
def isInMemorySort():
'''public boolean isInMemorySort()
'''
pass
def invlaidateSession():
'''public void invlaidateSession()
'''
pass
def bindMboToSession():
'''public String bindMboToSession(final String osName, final MboRemote mbo)
'''
pass
def unbindMboFromSession():
'''public MboRemote unbindMboFromSession(final MboRemote mbo)
'''
pass
def getHeader():
'''public String getHeader(final String headerName)
'''
pass
def copy():
'''public OslcRequest copy(final Map<String, List<String>> bulkHeaders, final Map<String, String[]> bulkQueryParams)
'''
pass
def isRelatedRef():
'''public boolean isRelatedRef()
'''
pass
def isLocalRef():
'''public boolean isLocalRef()
'''
pass
def getAbsoluteURI():
'''public String getAbsoluteURI()
'''
pass
def getDistinctClause():
'''public String getDistinctClause()
'''
pass
def isDistinct():
'''public boolean isDistinct()
'''
pass
def isAction():
'''public boolean isAction()
'''
pass
def isMaxSSO():
'''public boolean isMaxSSO()
'''
pass
def isCollectionCount():
'''public boolean isCollectionCount()
'''
pass
def getAction():
'''public String getAction()
'''
pass
def getTemplate():
'''public String getTemplate()
'''
pass
def isBulkOperation():
'''public boolean isBulkOperation()
'''
pass
def setResourcePath():
'''public void setResourcePath(final List<String> resPath)
'''
pass
def addIDToURI():
'''public void addIDToURI(final String id)
'''
pass
def replaceIDToURI():
'''public void replaceIDToURI(final String id)
'''
pass
def getAbsolutePath():
'''public List<String> getAbsolutePath()
'''
pass
def truncateAbsolutePath():
'''public void truncateAbsolutePath(final int num)
'''
pass
def getRequestPublicURI():
'''public String getRequestPublicURI()
'''
pass
def isAllowEvents():
'''public boolean isAllowEvents()
'''
pass
def isListTemplate():
'''public boolean isListTemplate()
'''
pass
def isChangePasswordSession():
'''public boolean isChangePasswordSession()
'''
pass
def isRegUserSession():
'''public boolean isRegUserSession()
'''
pass
def getResourcePath():
'''public List<String> getResourcePath()
'''
pass
def getRequestURL():
'''public String getRequestURL()
'''
pass
def isLeanJSON():
'''public boolean isLeanJSON()
'''
pass
def getAttachmentDocType():
'''public String[] getAttachmentDocType()
'''
pass
def getLinkHeader():
'''public String getLinkHeader()
'''
pass
def getContentLocationHeader():
'''public String getContentLocationHeader()
'''
pass
def getAttachmentDescription():
'''public String getAttachmentDescription()
'''
pass
def getAttachmentEncDescription():
'''public String getAttachmentEncDescription()
'''
pass
def getAttachmentExternalID():
'''public String getAttachmentExternalID()
'''
pass
def isEditMode():
'''public boolean isEditMode()
'''
pass
def isSetValueMode():
'''public boolean isSetValueMode()
'''
pass
def getSelfRef():
'''public String getSelfRef()
'''
pass
def isShowHidden():
'''public boolean isShowHidden()
'''
pass
def isDropNulls():
'''public boolean isDropNulls()
'''
pass
def getSavedQueryParams():
'''public Map<String, String> getSavedQueryParams()
'''
pass
def isSubmitSession():
'''public boolean isSubmitSession()
'''
pass
def isInitiateStablePaging():
'''public boolean isInitiateStablePaging()
'''
pass
def isCount():
'''public boolean isCount()
'''
pass
def isAllowedActions():
'''public boolean isAllowedActions()
'''
pass
def getSavedQuery():
'''public String getSavedQuery()
'''
pass
def getOslcResourceURI():
'''public String getOslcResourceURI()
'''
pass
def getOslcRequestURI():
'''public String getOslcRequestURI()
'''
pass
def getOslcQuery():
'''public OslcQuery getOslcQuery()
'''
pass
def getResourceQBE():
'''public Map<String, String> getResourceQBE()
'''
pass
def isGETByPOST():
'''public boolean isGETByPOST()
'''
pass
def getResponseFormatMimeTypeMap():
'''public Map<String, String> getResponseFormatMimeTypeMap()
'''
pass
def getRequestFormatMimeTypeMap():
'''public Map<String, String> getRequestFormatMimeTypeMap()
'''
pass
def getDefaultFormat():
'''public String getDefaultFormat()
'''
pass
def getStableResourceId():
'''public String getStableResourceId()
'''
pass
def useFetchLimit():
'''public boolean useFetchLimit()
'''
pass
def getGBFilter():
'''public String getGBFilter()
'''
pass
def getGroupByAttributes():
'''public String getGroupByAttributes()
'''
pass
def getGroupBySortOrder():
'''public String getGroupBySortOrder()
'''
pass
def getGroupByRelations():
'''public String getGroupByRelations()
'''
pass
def getGroupByRelationProperties():
'''public String getGroupByRelationProperties()
'''
pass
def getGroupByTemplate():
'''public String getGroupByTemplate()
'''
pass
def getGroupByRange():
'''public String getGroupByRange()
'''
pass
def getQueryTemplate():
'''public String getQueryTemplate()
'''
pass
def getSchemaSearchTerm():
'''public String getSchemaSearchTerm()
'''
pass
def getSchemaOrderBy():
'''public String getSchemaOrderBy()
'''
pass
def isGroupBy():
'''public boolean isGroupBy()
'''
pass
def isQueryTemplate():
'''public boolean isQueryTemplate()
'''
pass
def internalValues():
'''public boolean internalValues()
'''
pass
def getDependentSubSelects():
'''public Map<String, String> getDependentSubSelects()
'''
pass
def getSubSelectRefs():
'''public Map<String, String[]> getSubSelectRefs()
'''
pass
def invalidateSession():
'''public void invalidateSession()
'''
pass
def getQueryString():
'''public Object getQueryString()
'''
pass
def getTimeLineAttribute():
'''public String getTimeLineAttribute()
'''
pass
def getTimeLineRange():
'''public String getTimeLineRange()
'''
pass
def isSetLocalizedRep():
'''public boolean isSetLocalizedRep()
'''
pass
def getUserWhere():
'''public String getUserWhere()
'''
pass
def getMaxRowStamp():
'''public Long getMaxRowStamp()
'''
pass
def isFetchModeDelta():
'''public boolean isFetchModeDelta()
'''
pass
def isAddQueryMeta():
'''public boolean isAddQueryMeta()
'''
pass
def getNpFilter():
'''public String getNpFilter()
'''
pass
def isAddID():
'''public boolean isAddID()
'''
pass
def getTimeLineFilter():
'''public String getTimeLineFilter()
'''
pass
def isResourceMeta():
'''public boolean isResourceMeta()
'''
pass
def isContentLocalized():
'''public boolean isContentLocalized()
'''
pass
def getQbeFilter():
'''public String getQbeFilter()
'''
pass
def isAddDomainMeta():
'''public boolean isAddDomainMeta()
'''
pass
def getCanChangeExternalStatus():
'''public String[] getCanChangeExternalStatus(final String objectName)
'''
pass
def getCanChangeMaxStatus():
'''public String[] getCanChangeMaxStatus(final String objectName)
'''
pass
def isWhoAmIApi():
'''public boolean isWhoAmIApi()
'''
pass
def getSetValueEvalChild():
'''public Map<String, Set<String>> getSetValueEvalChild()
'''
pass
def isTlModeDate():
'''public boolean isTlModeDate()
'''
pass
def isStrictSchema():
'''public boolean isStrictSchema()
'''
pass
