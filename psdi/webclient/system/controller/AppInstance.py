def AppInstance():
    '''    public AppInstance()
    '''
def addMXJSPostEvent():
    '''    public void addMXJSPostEvent(final String id, final String eval)
    '''
def getMXJSPostEvent():
    '''    public String[] getMXJSPostEvent()
    '''
def getTrackInRecents():
    '''    public boolean getTrackInRecents()
    '''
def setSkin():
    '''    public void setSkin(final String skin)
    '''
def getSkin():
    '''    public String getSkin()
    '''
def initialize():
    '''    public AppInstance initialize(final WebClientSession wcs, final AppDescriptor ad)
    '''
def checkMBOShouldBeLocked():
    '''    public void checkMBOShouldBeLocked()
    '''
def createPageInstance():
    '''    public PageInstance createPageInstance(final WebClientSession wcs, final Element el)
    public PageInstance createPageInstance(final WebClientSession wcs, final Element el, final boolean loadDialogEntity)
    '''
def pushPage():
    '''    public void pushPage(final PageInstance page)
    '''
def getOrigId():
    '''    public String getOrigId(final String renderId)
    '''
def addRenderId():
    '''    public void addRenderId(final String renderId, final String origId)
    '''
def removeRenderId():
    '''    public void removeRenderId(final String renderId)
    '''
def generateStaticId():
    '''    public String generateStaticId(final String id)
    '''
def close():
    '''    public void close()
    '''
def popPage():
    '''    public PageInstance popPage(PageInstance page, final boolean removeImmediately)
    public PageInstance popPage()
    public PageInstance popPage(final PageInstance page)
    '''
def cleanupPoppedDialog():
    '''    public void cleanupPoppedDialog()
    '''
def storePageBeans():
    '''    public void storePageBeans(final PageInstance page)
    '''
def clearStoredPageBeans():
    '''    public void clearStoredPageBeans()
    '''
def getAppModule():
    '''    public String getAppModule()
    '''
def getAppDescriptor():
    '''    public AppDescriptor getAppDescriptor()
    '''
def getChildren():
    '''    public List getChildren()
    '''
def getApplicationPage():
    '''    public PageInstance getApplicationPage()
    '''
def getCurrentPage():
    '''    public PageInstance getCurrentPage()
    '''
def getPageStack():
    '''    public Stack<PageInstance> getPageStack()
    '''
def getPoppedDialogs():
    '''    public Vector<PageInstance> getPoppedDialogs()
    '''
def getAppBean():
    '''    public DataBean getAppBean()
    '''
def getAppHandlerInstance():
    '''    public ControlInstance getAppHandlerInstance()
    '''
def getAppHandler():
    '''    public ControlHandler getAppHandler()
    '''
def getDataBean():
    '''    public DataBean getDataBean(final String beanId)
    '''
def getResultsBean():
    '''    public ResultsBean getResultsBean()
    '''
def setAppLinkBean():
    '''    public void setAppLinkBean(final DataBean bean)
    '''
def getAppLinkBean():
    '''    public DataBean getAppLinkBean()
    '''
def onListTab():
    '''    public boolean onListTab()
    '''
def getCurrentPageId():
    '''    public String getCurrentPageId()
    '''
def getApp():
    '''    public String getApp()
    '''
def getAppTitle():
    '''    public String getAppTitle()
    '''
def getAppImage():
    '''    public String getAppImage()
    '''
def getBeanForApp():
    '''    public DataBean getBeanForApp()
    '''
def inAppLinkMode():
    '''    public boolean inAppLinkMode()
    '''
def setAppLinkMode():
    '''    public void setAppLinkMode()
    '''
def getPreviousPage():
    '''    public PageInstance getPreviousPage()
    '''
def isRendered():
    '''    public boolean isRendered()
    '''
def setRendered():
    '''    public void setRendered(final boolean b)
    '''
def hasSaveAccess():
    '''    public boolean hasSaveAccess()
    '''
def getAppQueryOptions():
    '''    public Map<String, Map<String, String>> getAppQueryOptions()
    '''
def refreshQueryMap():
    '''    public void refreshQueryMap()
    '''
def getAppMenuOptions():
    '''    public Map<Integer, Map<String, String>> getAppMenuOptions()
    '''
def getAppActionMenuOptions():
    '''    public Map<Integer, Map<String, String>> getAppActionMenuOptions()
    '''
def showOptionForRL():
    '''    public boolean showOptionForRL(final String sigopt)
    '''
def getAppSearchOptions():
    '''    public Map<String, Map<String, String>> getAppSearchOptions()
    public Map<String, Map<String, String>> getAppSearchOptions(final String position)
    '''
def getAppToolbarOptions():
    '''    public Map<Integer, Map<String, String>> getAppToolbarOptions()
    public Map<Integer, Map<String, String>> getAppToolbarOptions(final boolean filterSavePrerequsite)
    '''
def setStartupWhereClause():
    '''    public void setStartupWhereClause(final String startupWhereClause)
    '''
def getStartupWhereClause():
    '''    public String getStartupWhereClause()
    '''
def setAppStartupQueryName():
    '''    public void setAppStartupQueryName(final String appStartupQueryName)
    '''
def getStartupQueryName():
    '''    public String getStartupQueryName()
    '''
def getUserDefaultQuery():
    '''    public Map<String, String> getUserDefaultQuery()
    '''
def getAppQuickSearchOptions():
    '''    public Map<String, Map<String, String>> getAppQuickSearchOptions()
    '''
def hasBookmarkMenuOption():
    '''    public boolean hasBookmarkMenuOption()
    '''
def applinkreturn():
    '''    public int applinkreturn()
    '''
def render():
    '''    public int render()
    '''
def gototab():
    '''    public int gototab()
    '''
def changetab():
    '''    public int changetab()
    '''
def changetabcond():
    '''    public int changetabcond()
    '''
def setRefreshCanvas():
    '''    public void setRefreshCanvas(final boolean state)
    '''
def getRefreshCanvas():
    '''    public boolean getRefreshCanvas()
    '''
def setReload():
    '''    public void setReload(final boolean state)
    '''
def getReload():
    '''    public boolean getReload()
    '''
def removeDataBean():
    '''    public DataBean removeDataBean(final String beanId)
    '''
def showwfinfo():
    '''    public int showwfinfo()
    '''
def getHotkeys():
    '''    public Hotkeys getHotkeys()
    '''
def cleanup():
    '''    public void cleanup()
    '''
def isSigOptionCheck():
    '''    public Map<String, String> isSigOptionCheck(final WebClientEvent wce)
    public boolean isSigOptionCheck(final String sigoption)
    '''
def openURL():
    '''    public void openURL(final String url, final boolean newWindow, String windowId, final String options)
    public void openURL(final String url, final boolean newWindow)
    '''
def hasSigOptionAccess():
    '''    public boolean hasSigOptionAccess(final String sigoption)
    '''
def isSigOption():
    '''    public boolean isSigOption(final String sigoption)
    '''
def allowPageEdits():
    '''    public boolean allowPageEdits()
    '''
def allowEvent():
    '''    public boolean allowEvent(final WebClientEvent event)
    '''
def getDesignerDialogList():
    '''    public HashMap<String, PageInstance> getDesignerDialogList()
    '''
def getTabManaged():
    '''    public boolean getTabManaged()
    '''
def setQueryCancelMboset():
    '''    public synchronized void setQueryCancelMboset(final MboSetRemote qcMboset)
    '''
def getQueryCancelMboset():
    '''    public synchronized MboSetRemote getQueryCancelMboset()
    '''
def setQueryCancelResultsBean():
    '''    public synchronized void setQueryCancelResultsBean(final DataBean qcDatabean)
    '''
def getQueryCancelResultsBean():
    '''    public synchronized DataBean getQueryCancelResultsBean()
    '''
def isdoclinkweblogic():
    '''    public boolean isdoclinkweblogic()
    '''
def setApphelp():
    '''    public void setApphelp(final String help)
    '''
def getApphelp():
    '''    public String getApphelp()
    '''
def isAsyncEnabled():
    '''    public boolean isAsyncEnabled()
    '''
def isMobile():
    '''    public boolean isMobile()
    '''
def getEntityRelationshipModel():
    '''    public EntityRelationshipModel getEntityRelationshipModel()
    '''
def hasAttributeErrors():
    '''    public boolean hasAttributeErrors()
    '''
def hasAnyErrors():
    '''    public boolean hasAnyErrors()
    '''
def setAttributeErrorList():
    '''    public void setAttributeErrorList(final List<ERMAttributeError> fieldErrorList)
    '''
def stillHasAttributeError():
    '''    public boolean stillHasAttributeError(final ERMAttributeError error)
    '''
def clearErrors():
    '''    public void clearErrors()
    '''
def setRedirectURL():
    '''    public void setRedirectURL(String url)
    '''
def deepRequiredEnabled():
    '''    public boolean deepRequiredEnabled()
    '''
def getWarningType():
    '''    public int getWarningType()
    '''
def getRedirectURL():
    '''    public String getRedirectURL()
    '''
def isReferenceApp():
    '''    public boolean isReferenceApp()
    '''
def addJavaScript():
    '''    public void addJavaScript(final String script)
    '''
def propagateRequiredErrors():
    '''    public MXException propagateRequiredErrors(MXException e, final List<ERMAttributeError> requiredErrorList)
    '''
def propagateRequiredException():
    '''    public MXRequiredFieldException propagateRequiredException(final MXRequiredFieldException e, final List<ERMAttributeError> requireds)
    '''
def getNavigationHistory():
    '''    public NavigationHistoryStack getNavigationHistory()
    '''
def getErrorLevel():
    '''    public int getErrorLevel()
    '''
def setRetryErrorValues():
    '''    public void setRetryErrorValues(final boolean retryErrorValues)
    '''
def hasHandledRequiredFieldException():
    '''    public boolean hasHandledRequiredFieldException()
    '''
def isSigOptionConditional():
    '''    public boolean isSigOptionConditional(String sigOption)
    '''
def addErrorToMasterList():
    '''    public void addErrorToMasterList(final SetValueError setValueError)
    '''
def getErrorFromMasterList():
    '''    public SetValueError getErrorFromMasterList(final ApplicationError appError)
    '''
def removeErrorFromMasterList():
    '''    public void removeErrorFromMasterList(final SetValueError setValueError)
    '''
def getAutoFillForPage():
    '''    public JSONObject getAutoFillForPage(final PageInstance page)
    '''
def getDatastoreSet():
    '''    public DatastoreSet getDatastoreSet()
    '''
def getKeyLabel():
    '''    public String getKeyLabel()
    '''
def setRecHover():
    '''    public void setRecHover(final Element rhElement, final ComponentInstance sourceComponent)
    '''
def getRecHover():
    '''    public RecordHover getRecHover()
    '''
def clearRecHover():
    '''    public void clearRecHover()
    '''
def isMainrecActionMenu():
    '''    public boolean isMainrecActionMenu()
    '''
def setListTableOrderBy():
    '''    public void setListTableOrderBy(final String orderBy)
    '''
def getListTableOrderBy():
    '''    public String getListTableOrderBy()
    '''
def getAppIdList():
    '''    public Hashtable<String, String> getAppIdList()
    '''
def getNextToolbarNumber():
    '''    public int getNextToolbarNumber()
    '''
