def ():
    '''returns OslcRequest\n\n
    (final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost, final List<String> resPath, final String requestURL)\n
    (final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost, final List<String> resPath, final String requestURL, final UserInfo userInfo)\n
    (final HttpServletRequest request)\n
    '''
def setProcessUserInfo():
    '''returns None\n\n
    setProcessUserInfo(final UserInfo processUserInfo)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def setParts():
    '''returns None\n\n
    setParts(final Map<String, MPPartInfo> parts)\n
    '''
def isBranchFilterOn():
    '''returns boolean\n\n
    isBranchFilterOn()\n
    '''
def isIgnoreRowstamp():
    '''returns boolean\n\n
    isIgnoreRowstamp()\n
    '''
def isIgnoreKeyref():
    '''returns boolean\n\n
    isIgnoreKeyref()\n
    '''
def getPart():
    '''returns MPPartInfo\n\n
    getPart(final String partKey)\n
    '''
def isAddSchema():
    '''returns boolean\n\n
    isAddSchema()\n
    '''
def isAddAction():
    '''returns boolean\n\n
    isAddAction()\n
    '''
def isEnableSession():
    '''returns boolean\n\n
    isEnableSession()\n
    '''
def isNewSession():
    '''returns boolean\n\n
    isNewSession()\n
    '''
def isAddLocalizedRep():
    '''returns boolean\n\n
    isAddLocalizedRep()\n
    '''
def getUseView():
    '''returns String\n\n
    getUseView()\n
    '''
def getApiKey():
    '''returns String\n\n
    getApiKey()\n
    '''
def getApps():
    '''returns String\n\n
    getApps()\n
    '''
def isApiCall():
    '''returns boolean\n\n
    isApiCall()\n
    '''
def isClientCertMode():
    '''returns boolean\n\n
    isClientCertMode()\n
    '''
def isBatchError():
    '''returns boolean\n\n
    isBatchError()\n
    '''
def verifyCsrfToken():
    '''returns boolean\n\n
    verifyCsrfToken()\n
    '''
def getCsrfTokenFromRequest():
    '''returns String\n\n
    getCsrfTokenFromRequest()\n
    '''
def getCsrfToken():
    '''returns String\n\n
    getCsrfToken()\n
    '''
def getGuestId():
    '''returns String\n\n
    getGuestId()\n
    '''
def isQueryLocalized():
    '''returns boolean\n\n
    isQueryLocalized()\n
    '''
def isCsrfSession():
    '''returns boolean\n\n
    isCsrfSession()\n
    '''
def isProcessAsSelfReferencing():
    '''returns boolean\n\n
    isProcessAsSelfReferencing()\n
    '''
def isAllowSelfRefDup():
    '''returns boolean\n\n
    isAllowSelfRefDup()\n
    '''
def getProcessAsSelfRefRelName():
    '''returns String\n\n
    getProcessAsSelfRefRelName()\n
    '''
def isLocalizedDate():
    '''returns boolean\n\n
    isLocalizedDate()\n
    '''
def serializeToBytes():
    '''returns byte[]\n\n
    serializeToBytes()\n
    '''
def getTransactionId():
    '''returns String\n\n
    getTransactionId()\n
    '''
def getHttpServletRequest():
    '''returns HttpServletRequest\n\n
    getHttpServletRequest()\n
    '''
def setInteractiveRequest():
    '''returns None\n\n
    setInteractiveRequest()\n
    '''
def isFileLoad():
    '''returns boolean\n\n
    isFileLoad()\n
    '''
def isAsyncRequest():
    '''returns boolean\n\n
    isAsyncRequest()\n
    '''
def isInteractiveRequest():
    '''returns boolean\n\n
    isInteractiveRequest()\n
    '''
def isCheckEsig():
    '''returns boolean\n\n
    isCheckEsig()\n
    '''
def isIgnoreCollectionRef():
    '''returns boolean\n\n
    isIgnoreCollectionRef()\n
    '''
def isInlineDoc():
    '''returns boolean\n\n
    isInlineDoc()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def readRequestBody():
    '''returns byte[]\n\n
    readRequestBody()\n
    '''
def setHttpServletResponse():
    '''returns None\n\n
    setHttpServletResponse(final HttpServletResponse response)\n
    '''
def getHttpServletResponse():
    '''returns HttpServletResponse\n\n
    getHttpServletResponse()\n
    '''
def setInMemorySort():
    '''returns None\n\n
    setInMemorySort(final boolean inmemsort)\n
    '''
def isInMemorySort():
    '''returns boolean\n\n
    isInMemorySort()\n
    '''
def invlaidateSession():
    '''returns None\n\n
    invlaidateSession()\n
    '''
def bindMboToSession():
    '''returns String\n\n
    bindMboToSession(final String osName, final MboRemote mbo)\n
    '''
def unbindMboFromSession():
    '''returns MboRemote\n\n
    unbindMboFromSession(final MboRemote mbo)\n
    '''
def getHeader():
    '''returns String\n\n
    getHeader(final String headerName)\n
    '''
def copy():
    '''returns OslcRequest\n\n
    copy(final Map<String, List<String>> bulkHeaders, final Map<String, String[]> bulkQueryParams)\n
    '''
def isRelatedRef():
    '''returns boolean\n\n
    isRelatedRef()\n
    '''
def isLocalRef():
    '''returns boolean\n\n
    isLocalRef()\n
    '''
def getAbsoluteURI():
    '''returns String\n\n
    getAbsoluteURI()\n
    '''
def getDistinctClause():
    '''returns String\n\n
    getDistinctClause()\n
    '''
def isDistinct():
    '''returns boolean\n\n
    isDistinct()\n
    '''
def isAction():
    '''returns boolean\n\n
    isAction()\n
    '''
def isMaxSSO():
    '''returns boolean\n\n
    isMaxSSO()\n
    '''
def isCollectionCount():
    '''returns boolean\n\n
    isCollectionCount()\n
    '''
def getAction():
    '''returns String\n\n
    getAction()\n
    '''
def getTemplate():
    '''returns String\n\n
    getTemplate()\n
    '''
def isBulkOperation():
    '''returns boolean\n\n
    isBulkOperation()\n
    '''
def setResourcePath():
    '''returns None\n\n
    setResourcePath(final List<String> resPath)\n
    '''
def addIDToURI():
    '''returns None\n\n
    addIDToURI(final String id)\n
    '''
def replaceIDToURI():
    '''returns None\n\n
    replaceIDToURI(final String id)\n
    '''
def getAbsolutePath():
    '''returns List<String>\n\n
    getAbsolutePath()\n
    '''
def truncateAbsolutePath():
    '''returns None\n\n
    truncateAbsolutePath(final int num)\n
    '''
def getRequestPublicURI():
    '''returns String\n\n
    getRequestPublicURI()\n
    '''
def isAllowEvents():
    '''returns boolean\n\n
    isAllowEvents()\n
    '''
def isListTemplate():
    '''returns boolean\n\n
    isListTemplate()\n
    '''
def isChangePasswordSession():
    '''returns boolean\n\n
    isChangePasswordSession()\n
    '''
def isRegUserSession():
    '''returns boolean\n\n
    isRegUserSession()\n
    '''
def getResourcePath():
    '''returns List<String>\n\n
    getResourcePath()\n
    '''
def getRequestURL():
    '''returns String\n\n
    getRequestURL()\n
    '''
def isLeanJSON():
    '''returns boolean\n\n
    isLeanJSON()\n
    '''
def getAttachmentDocType():
    '''returns String[]\n\n
    getAttachmentDocType()\n
    '''
def getLinkHeader():
    '''returns String\n\n
    getLinkHeader()\n
    '''
def getContentLocationHeader():
    '''returns String\n\n
    getContentLocationHeader()\n
    '''
def getAttachmentDescription():
    '''returns String\n\n
    getAttachmentDescription()\n
    '''
def getAttachmentEncDescription():
    '''returns String\n\n
    getAttachmentEncDescription()\n
    '''
def getAttachmentExternalID():
    '''returns String\n\n
    getAttachmentExternalID()\n
    '''
def isEditMode():
    '''returns boolean\n\n
    isEditMode()\n
    '''
def isSetValueMode():
    '''returns boolean\n\n
    isSetValueMode()\n
    '''
def getSelfRef():
    '''returns String\n\n
    getSelfRef()\n
    '''
def isShowHidden():
    '''returns boolean\n\n
    isShowHidden()\n
    '''
def isDropNulls():
    '''returns boolean\n\n
    isDropNulls()\n
    '''
def isSubmitSession():
    '''returns boolean\n\n
    isSubmitSession()\n
    '''
def isInitiateStablePaging():
    '''returns boolean\n\n
    isInitiateStablePaging()\n
    '''
def isCount():
    '''returns boolean\n\n
    isCount()\n
    '''
def isAllowedActions():
    '''returns boolean\n\n
    isAllowedActions()\n
    '''
def getSavedQuery():
    '''returns String\n\n
    getSavedQuery()\n
    '''
def getOslcResourceURI():
    '''returns String\n\n
    getOslcResourceURI()\n
    '''
def getOslcRequestURI():
    '''returns String\n\n
    getOslcRequestURI()\n
    '''
def getOslcQuery():
    '''returns OslcQuery\n\n
    getOslcQuery()\n
    '''
def isGETByPOST():
    '''returns boolean\n\n
    isGETByPOST()\n
    '''
def getDefaultFormat():
    '''returns String\n\n
    getDefaultFormat()\n
    '''
def getStableResourceId():
    '''returns String\n\n
    getStableResourceId()\n
    '''
def useFetchLimit():
    '''returns boolean\n\n
    useFetchLimit()\n
    '''
def getGBFilter():
    '''returns String\n\n
    getGBFilter()\n
    '''
def getGroupByAttributes():
    '''returns String\n\n
    getGroupByAttributes()\n
    '''
def getGroupBySortOrder():
    '''returns String\n\n
    getGroupBySortOrder()\n
    '''
def getGroupByRelations():
    '''returns String\n\n
    getGroupByRelations()\n
    '''
def getGroupByRelationProperties():
    '''returns String\n\n
    getGroupByRelationProperties()\n
    '''
def getGroupByTemplate():
    '''returns String\n\n
    getGroupByTemplate()\n
    '''
def getGroupByRange():
    '''returns String\n\n
    getGroupByRange()\n
    '''
def getQueryTemplate():
    '''returns String\n\n
    getQueryTemplate()\n
    '''
def getSchemaSearchTerm():
    '''returns String\n\n
    getSchemaSearchTerm()\n
    '''
def getSchemaOrderBy():
    '''returns String\n\n
    getSchemaOrderBy()\n
    '''
def isGroupBy():
    '''returns boolean\n\n
    isGroupBy()\n
    '''
def isQueryTemplate():
    '''returns boolean\n\n
    isQueryTemplate()\n
    '''
def internalValues():
    '''returns boolean\n\n
    internalValues()\n
    '''
def invalidateSession():
    '''returns None\n\n
    invalidateSession()\n
    '''
def getQueryString():
    '''returns Object\n\n
    getQueryString()\n
    '''
def getTimeLineAttribute():
    '''returns String\n\n
    getTimeLineAttribute()\n
    '''
def getTimeLineRange():
    '''returns String\n\n
    getTimeLineRange()\n
    '''
def isSetLocalizedRep():
    '''returns boolean\n\n
    isSetLocalizedRep()\n
    '''
def getUserWhere():
    '''returns String\n\n
    getUserWhere()\n
    '''
def getMaxRowStamp():
    '''returns Long\n\n
    getMaxRowStamp()\n
    '''
def isFetchModeDelta():
    '''returns boolean\n\n
    isFetchModeDelta()\n
    '''
def isAddQueryMeta():
    '''returns boolean\n\n
    isAddQueryMeta()\n
    '''
def getNpFilter():
    '''returns String\n\n
    getNpFilter()\n
    '''
def isAddID():
    '''returns boolean\n\n
    isAddID()\n
    '''
def getTimeLineFilter():
    '''returns String\n\n
    getTimeLineFilter()\n
    '''
def isResourceMeta():
    '''returns boolean\n\n
    isResourceMeta()\n
    '''
def isContentLocalized():
    '''returns boolean\n\n
    isContentLocalized()\n
    '''
def getQbeFilter():
    '''returns String\n\n
    getQbeFilter()\n
    '''
def isAddDomainMeta():
    '''returns boolean\n\n
    isAddDomainMeta()\n
    '''
def getCanChangeExternalStatus():
    '''returns String[]\n\n
    getCanChangeExternalStatus(final String objectName)\n
    '''
def getCanChangeMaxStatus():
    '''returns String[]\n\n
    getCanChangeMaxStatus(final String objectName)\n
    '''
def isWhoAmIApi():
    '''returns boolean\n\n
    isWhoAmIApi()\n
    '''
def isTlModeDate():
    '''returns boolean\n\n
    isTlModeDate()\n
    '''
def isStrictSchema():
    '''returns boolean\n\n
    isStrictSchema()\n
    '''
