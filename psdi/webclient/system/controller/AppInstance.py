def ():
    '''returns AppInstance\n\n
    ()\n
    '''
def addMXJSPostEvent():
    '''returns None\n\n
    addMXJSPostEvent(final String id, final String eval)\n
    '''
def getMXJSPostEvent():
    '''returns String[]\n\n
    getMXJSPostEvent()\n
    '''
def getTrackInRecents():
    '''returns boolean\n\n
    getTrackInRecents()\n
    '''
def setSkin():
    '''returns None\n\n
    setSkin(final String skin)\n
    '''
def getSkin():
    '''returns String\n\n
    getSkin()\n
    '''
def initialize():
    '''returns AppInstance\n\n
    initialize(final WebClientSession wcs, final AppDescriptor ad)\n
    '''
def checkMBOShouldBeLocked():
    '''returns None\n\n
    checkMBOShouldBeLocked()\n
    '''
def createPageInstance():
    '''returns PageInstance\n\n
    createPageInstance(final WebClientSession wcs, final Element el)\n
    createPageInstance(final WebClientSession wcs, final Element el, final boolean loadDialogEntity)\n
    '''
def pushPage():
    '''returns None\n\n
    pushPage(final PageInstance page)\n
    '''
def getOrigId():
    '''returns String\n\n
    getOrigId(final String renderId)\n
    '''
def addRenderId():
    '''returns None\n\n
    addRenderId(final String renderId, final String origId)\n
    '''
def removeRenderId():
    '''returns None\n\n
    removeRenderId(final String renderId)\n
    '''
def generateStaticId():
    '''returns String\n\n
    generateStaticId(final String id)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def popPage():
    '''returns PageInstance\n\n
    popPage(PageInstance page, final boolean removeImmediately)\n
    popPage()\n
    popPage(final PageInstance page)\n
    '''
def cleanupPoppedDialog():
    '''returns None\n\n
    cleanupPoppedDialog()\n
    '''
def storePageBeans():
    '''returns None\n\n
    storePageBeans(final PageInstance page)\n
    '''
def clearStoredPageBeans():
    '''returns None\n\n
    clearStoredPageBeans()\n
    '''
def getAppModule():
    '''returns String\n\n
    getAppModule()\n
    '''
def getAppDescriptor():
    '''returns AppDescriptor\n\n
    getAppDescriptor()\n
    '''
def getChildren():
    '''returns List\n\n
    getChildren()\n
    '''
def getApplicationPage():
    '''returns PageInstance\n\n
    getApplicationPage()\n
    '''
def getCurrentPage():
    '''returns PageInstance\n\n
    getCurrentPage()\n
    '''
def getPageStack():
    '''returns Stack<PageInstance>\n\n
    getPageStack()\n
    '''
def getPoppedDialogs():
    '''returns Vector<PageInstance>\n\n
    getPoppedDialogs()\n
    '''
def getAppBean():
    '''returns DataBean\n\n
    getAppBean()\n
    '''
def getAppHandlerInstance():
    '''returns ControlInstance\n\n
    getAppHandlerInstance()\n
    '''
def getAppHandler():
    '''returns ControlHandler\n\n
    getAppHandler()\n
    '''
def getDataBean():
    '''returns DataBean\n\n
    getDataBean(final String beanId)\n
    '''
def getResultsBean():
    '''returns ResultsBean\n\n
    getResultsBean()\n
    '''
def setAppLinkBean():
    '''returns None\n\n
    setAppLinkBean(final DataBean bean)\n
    '''
def getAppLinkBean():
    '''returns DataBean\n\n
    getAppLinkBean()\n
    '''
def onListTab():
    '''returns boolean\n\n
    onListTab()\n
    '''
def getCurrentPageId():
    '''returns String\n\n
    getCurrentPageId()\n
    '''
def getApp():
    '''returns String\n\n
    getApp()\n
    '''
def getAppTitle():
    '''returns String\n\n
    getAppTitle()\n
    '''
def getAppImage():
    '''returns String\n\n
    getAppImage()\n
    '''
def getBeanForApp():
    '''returns DataBean\n\n
    getBeanForApp()\n
    '''
def inAppLinkMode():
    '''returns boolean\n\n
    inAppLinkMode()\n
    '''
def setAppLinkMode():
    '''returns None\n\n
    setAppLinkMode()\n
    '''
def getPreviousPage():
    '''returns PageInstance\n\n
    getPreviousPage()\n
    '''
def isRendered():
    '''returns boolean\n\n
    isRendered()\n
    '''
def setRendered():
    '''returns None\n\n
    setRendered(final boolean b)\n
    '''
def hasSaveAccess():
    '''returns boolean\n\n
    hasSaveAccess()\n
    '''
def refreshQueryMap():
    '''returns None\n\n
    refreshQueryMap()\n
    '''
def showOptionForRL():
    '''returns boolean\n\n
    showOptionForRL(final String sigopt)\n
    '''
def setStartupWhereClause():
    '''returns None\n\n
    setStartupWhereClause(final String startupWhereClause)\n
    '''
def getStartupWhereClause():
    '''returns String\n\n
    getStartupWhereClause()\n
    '''
def setAppStartupQueryName():
    '''returns None\n\n
    setAppStartupQueryName(final String appStartupQueryName)\n
    '''
def getStartupQueryName():
    '''returns String\n\n
    getStartupQueryName()\n
    '''
def hasBookmarkMenuOption():
    '''returns boolean\n\n
    hasBookmarkMenuOption()\n
    '''
def applinkreturn():
    '''returns int\n\n
    applinkreturn()\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def gototab():
    '''returns int\n\n
    gototab()\n
    '''
def changetab():
    '''returns int\n\n
    changetab()\n
    '''
def changetabcond():
    '''returns int\n\n
    changetabcond()\n
    '''
def setRefreshCanvas():
    '''returns None\n\n
    setRefreshCanvas(final boolean state)\n
    '''
def getRefreshCanvas():
    '''returns boolean\n\n
    getRefreshCanvas()\n
    '''
def setReload():
    '''returns None\n\n
    setReload(final boolean state)\n
    '''
def getReload():
    '''returns boolean\n\n
    getReload()\n
    '''
def removeDataBean():
    '''returns DataBean\n\n
    removeDataBean(final String beanId)\n
    '''
def showwfinfo():
    '''returns int\n\n
    showwfinfo()\n
    '''
def getHotkeys():
    '''returns Hotkeys\n\n
    getHotkeys()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def isSigOptionCheck():
    '''returns boolean\n\n
    isSigOptionCheck(final String sigoption)\n
    '''
def openURL():
    '''returns None\n\n
    openURL(final String url, final boolean newWindow, String windowId, final String options)\n
    openURL(final String url, final boolean newWindow)\n
    '''
def hasSigOptionAccess():
    '''returns boolean\n\n
    hasSigOptionAccess(final String sigoption)\n
    '''
def isSigOption():
    '''returns boolean\n\n
    isSigOption(final String sigoption)\n
    '''
def allowPageEdits():
    '''returns boolean\n\n
    allowPageEdits()\n
    '''
def allowEvent():
    '''returns boolean\n\n
    allowEvent(final WebClientEvent event)\n
    '''
def getTabManaged():
    '''returns boolean\n\n
    getTabManaged()\n
    '''
def isdoclinkweblogic():
    '''returns boolean\n\n
    isdoclinkweblogic()\n
    '''
def setApphelp():
    '''returns None\n\n
    setApphelp(final String help)\n
    '''
def getApphelp():
    '''returns String\n\n
    getApphelp()\n
    '''
def isAsyncEnabled():
    '''returns boolean\n\n
    isAsyncEnabled()\n
    '''
def isMobile():
    '''returns boolean\n\n
    isMobile()\n
    '''
def getEntityRelationshipModel():
    '''returns EntityRelationshipModel\n\n
    getEntityRelationshipModel()\n
    '''
def hasAttributeErrors():
    '''returns boolean\n\n
    hasAttributeErrors()\n
    '''
def hasAnyErrors():
    '''returns boolean\n\n
    hasAnyErrors()\n
    '''
def setAttributeErrorList():
    '''returns None\n\n
    setAttributeErrorList(final List<ERMAttributeError> fieldErrorList)\n
    '''
def stillHasAttributeError():
    '''returns boolean\n\n
    stillHasAttributeError(final ERMAttributeError error)\n
    '''
def clearErrors():
    '''returns None\n\n
    clearErrors()\n
    '''
def setRedirectURL():
    '''returns None\n\n
    setRedirectURL(String url)\n
    '''
def deepRequiredEnabled():
    '''returns boolean\n\n
    deepRequiredEnabled()\n
    '''
def getWarningType():
    '''returns int\n\n
    getWarningType()\n
    '''
def getRedirectURL():
    '''returns String\n\n
    getRedirectURL()\n
    '''
def isReferenceApp():
    '''returns boolean\n\n
    isReferenceApp()\n
    '''
def addJavaScript():
    '''returns None\n\n
    addJavaScript(final String script)\n
    '''
def propagateRequiredErrors():
    '''returns MXException\n\n
    propagateRequiredErrors(MXException e, final List<ERMAttributeError> requiredErrorList)\n
    '''
def propagateRequiredException():
    '''returns MXRequiredFieldException\n\n
    propagateRequiredException(final MXRequiredFieldException e, final List<ERMAttributeError> requireds)\n
    '''
def getNavigationHistory():
    '''returns NavigationHistoryStack\n\n
    getNavigationHistory()\n
    '''
def getErrorLevel():
    '''returns int\n\n
    getErrorLevel()\n
    '''
def setRetryErrorValues():
    '''returns None\n\n
    setRetryErrorValues(final boolean retryErrorValues)\n
    '''
def hasHandledRequiredFieldException():
    '''returns boolean\n\n
    hasHandledRequiredFieldException()\n
    '''
def isSigOptionConditional():
    '''returns boolean\n\n
    isSigOptionConditional(String sigOption)\n
    '''
def addErrorToMasterList():
    '''returns None\n\n
    addErrorToMasterList(final SetValueError setValueError)\n
    '''
def getErrorFromMasterList():
    '''returns SetValueError\n\n
    getErrorFromMasterList(final ApplicationError appError)\n
    '''
def removeErrorFromMasterList():
    '''returns None\n\n
    removeErrorFromMasterList(final SetValueError setValueError)\n
    '''
def getAutoFillForPage():
    '''returns JSONObject\n\n
    getAutoFillForPage(final PageInstance page)\n
    '''
def getDatastoreSet():
    '''returns DatastoreSet\n\n
    getDatastoreSet()\n
    '''
def getKeyLabel():
    '''returns String\n\n
    getKeyLabel()\n
    '''
def setRecHover():
    '''returns None\n\n
    setRecHover(final Element rhElement, final ComponentInstance sourceComponent)\n
    '''
def getRecHover():
    '''returns RecordHover\n\n
    getRecHover()\n
    '''
def clearRecHover():
    '''returns None\n\n
    clearRecHover()\n
    '''
def isMainrecActionMenu():
    '''returns boolean\n\n
    isMainrecActionMenu()\n
    '''
def setListTableOrderBy():
    '''returns None\n\n
    setListTableOrderBy(final String orderBy)\n
    '''
def getListTableOrderBy():
    '''returns String\n\n
    getListTableOrderBy()\n
    '''
def getNextToolbarNumber():
    '''returns int\n\n
    getNextToolbarNumber()\n
    '''
