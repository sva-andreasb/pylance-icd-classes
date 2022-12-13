def AppInstance():
'''public AppInstance()
'''
pass
def addMXJSPostEvent():
'''public void addMXJSPostEvent(final String id, final String eval)
'''
pass
def getMXJSPostEvent():
'''public String[] getMXJSPostEvent()
'''
pass
def getTrackInRecents():
'''public boolean getTrackInRecents()
'''
pass
def setSkin():
'''public void setSkin(final String skin)
'''
pass
def getSkin():
'''public String getSkin()
'''
pass
def initialize():
'''public AppInstance initialize(final WebClientSession wcs, final AppDescriptor ad)
'''
pass
def checkMBOShouldBeLocked():
'''public void checkMBOShouldBeLocked()
'''
pass
def createPageInstance():
'''public PageInstance createPageInstance(final WebClientSession wcs, final Element el)
public PageInstance createPageInstance(final WebClientSession wcs, final Element el, final boolean loadDialogEntity)
'''
pass
def pushPage():
'''public void pushPage(final PageInstance page)
'''
pass
def getOrigId():
'''public String getOrigId(final String renderId)
'''
pass
def addRenderId():
'''public void addRenderId(final String renderId, final String origId)
'''
pass
def removeRenderId():
'''public void removeRenderId(final String renderId)
'''
pass
def generateStaticId():
'''public String generateStaticId(final String id)
'''
pass
def close():
'''public void close()
'''
pass
def popPage():
'''public PageInstance popPage(PageInstance page, final boolean removeImmediately)
public PageInstance popPage()
public PageInstance popPage(final PageInstance page)
'''
pass
def cleanupPoppedDialog():
'''public void cleanupPoppedDialog()
'''
pass
def storePageBeans():
'''public void storePageBeans(final PageInstance page)
'''
pass
def clearStoredPageBeans():
'''public void clearStoredPageBeans()
'''
pass
def getAppModule():
'''public String getAppModule()
'''
pass
def getAppDescriptor():
'''public AppDescriptor getAppDescriptor()
'''
pass
def getChildren():
'''public List getChildren()
'''
pass
def getApplicationPage():
'''public PageInstance getApplicationPage()
'''
pass
def getCurrentPage():
'''public PageInstance getCurrentPage()
'''
pass
def getPageStack():
'''public Stack<PageInstance> getPageStack()
'''
pass
def getPoppedDialogs():
'''public Vector<PageInstance> getPoppedDialogs()
'''
pass
def getAppBean():
'''public DataBean getAppBean()
'''
pass
def getAppHandlerInstance():
'''public ControlInstance getAppHandlerInstance()
'''
pass
def getAppHandler():
'''public ControlHandler getAppHandler()
'''
pass
def getDataBean():
'''public DataBean getDataBean(final String beanId)
'''
pass
def getResultsBean():
'''public ResultsBean getResultsBean()
'''
pass
def setAppLinkBean():
'''public void setAppLinkBean(final DataBean bean)
'''
pass
def getAppLinkBean():
'''public DataBean getAppLinkBean()
'''
pass
def onListTab():
'''public boolean onListTab()
'''
pass
def getCurrentPageId():
'''public String getCurrentPageId()
'''
pass
def getApp():
'''public String getApp()
'''
pass
def getAppTitle():
'''public String getAppTitle()
'''
pass
def getAppImage():
'''public String getAppImage()
'''
pass
def getBeanForApp():
'''public DataBean getBeanForApp()
'''
pass
def inAppLinkMode():
'''public boolean inAppLinkMode()
'''
pass
def setAppLinkMode():
'''public void setAppLinkMode()
'''
pass
def getPreviousPage():
'''public PageInstance getPreviousPage()
'''
pass
def isRendered():
'''public boolean isRendered()
'''
pass
def setRendered():
'''public void setRendered(final boolean b)
'''
pass
def hasSaveAccess():
'''public boolean hasSaveAccess()
'''
pass
def getAppQueryOptions():
'''public Map<String, Map<String, String>> getAppQueryOptions()
'''
pass
def refreshQueryMap():
'''public void refreshQueryMap()
'''
pass
def getAppMenuOptions():
'''public Map<Integer, Map<String, String>> getAppMenuOptions()
'''
pass
def getAppActionMenuOptions():
'''public Map<Integer, Map<String, String>> getAppActionMenuOptions()
'''
pass
def showOptionForRL():
'''public boolean showOptionForRL(final String sigopt)
'''
pass
def getAppSearchOptions():
'''public Map<String, Map<String, String>> getAppSearchOptions()
public Map<String, Map<String, String>> getAppSearchOptions(final String position)
'''
pass
def getAppToolbarOptions():
'''public Map<Integer, Map<String, String>> getAppToolbarOptions()
public Map<Integer, Map<String, String>> getAppToolbarOptions(final boolean filterSavePrerequsite)
'''
pass
def setStartupWhereClause():
'''public void setStartupWhereClause(final String startupWhereClause)
'''
pass
def getStartupWhereClause():
'''public String getStartupWhereClause()
'''
pass
def setAppStartupQueryName():
'''public void setAppStartupQueryName(final String appStartupQueryName)
'''
pass
def getStartupQueryName():
'''public String getStartupQueryName()
'''
pass
def getUserDefaultQuery():
'''public Map<String, String> getUserDefaultQuery()
'''
pass
def getAppQuickSearchOptions():
'''public Map<String, Map<String, String>> getAppQuickSearchOptions()
'''
pass
def hasBookmarkMenuOption():
'''public boolean hasBookmarkMenuOption()
'''
pass
def applinkreturn():
'''public int applinkreturn()
'''
pass
def render():
'''public int render()
'''
pass
def gototab():
'''public int gototab()
'''
pass
def changetab():
'''public int changetab()
'''
pass
def changetabcond():
'''public int changetabcond()
'''
pass
def setRefreshCanvas():
'''public void setRefreshCanvas(final boolean state)
'''
pass
def getRefreshCanvas():
'''public boolean getRefreshCanvas()
'''
pass
def setReload():
'''public void setReload(final boolean state)
'''
pass
def getReload():
'''public boolean getReload()
'''
pass
def removeDataBean():
'''public DataBean removeDataBean(final String beanId)
'''
pass
def showwfinfo():
'''public int showwfinfo()
'''
pass
def getHotkeys():
'''public Hotkeys getHotkeys()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def isSigOptionCheck():
'''public Map<String, String> isSigOptionCheck(final WebClientEvent wce)
public boolean isSigOptionCheck(final String sigoption)
'''
pass
def openURL():
'''public void openURL(final String url, final boolean newWindow, String windowId, final String options)
public void openURL(final String url, final boolean newWindow)
'''
pass
def hasSigOptionAccess():
'''public boolean hasSigOptionAccess(final String sigoption)
'''
pass
def isSigOption():
'''public boolean isSigOption(final String sigoption)
'''
pass
def allowPageEdits():
'''public boolean allowPageEdits()
'''
pass
def allowEvent():
'''public boolean allowEvent(final WebClientEvent event)
'''
pass
def getDesignerDialogList():
'''public HashMap<String, PageInstance> getDesignerDialogList()
'''
pass
def getTabManaged():
'''public boolean getTabManaged()
'''
pass
def setQueryCancelMboset():
'''public synchronized void setQueryCancelMboset(final MboSetRemote qcMboset)
'''
pass
def getQueryCancelMboset():
'''public synchronized MboSetRemote getQueryCancelMboset()
'''
pass
def setQueryCancelResultsBean():
'''public synchronized void setQueryCancelResultsBean(final DataBean qcDatabean)
'''
pass
def getQueryCancelResultsBean():
'''public synchronized DataBean getQueryCancelResultsBean()
'''
pass
def isdoclinkweblogic():
'''public boolean isdoclinkweblogic()
'''
pass
def setApphelp():
'''public void setApphelp(final String help)
'''
pass
def getApphelp():
'''public String getApphelp()
'''
pass
def isAsyncEnabled():
'''public boolean isAsyncEnabled()
'''
pass
def isMobile():
'''public boolean isMobile()
'''
pass
def getEntityRelationshipModel():
'''public EntityRelationshipModel getEntityRelationshipModel()
'''
pass
def hasAttributeErrors():
'''public boolean hasAttributeErrors()
'''
pass
def hasAnyErrors():
'''public boolean hasAnyErrors()
'''
pass
def setAttributeErrorList():
'''public void setAttributeErrorList(final List<ERMAttributeError> fieldErrorList)
'''
pass
def stillHasAttributeError():
'''public boolean stillHasAttributeError(final ERMAttributeError error)
'''
pass
def clearErrors():
'''public void clearErrors()
'''
pass
def setRedirectURL():
'''public void setRedirectURL(String url)
'''
pass
def deepRequiredEnabled():
'''public boolean deepRequiredEnabled()
'''
pass
def getWarningType():
'''public int getWarningType()
'''
pass
def getRedirectURL():
'''public String getRedirectURL()
'''
pass
def isReferenceApp():
'''public boolean isReferenceApp()
'''
pass
def addJavaScript():
'''public void addJavaScript(final String script)
'''
pass
def propagateRequiredErrors():
'''public MXException propagateRequiredErrors(MXException e, final List<ERMAttributeError> requiredErrorList)
'''
pass
def propagateRequiredException():
'''public MXRequiredFieldException propagateRequiredException(final MXRequiredFieldException e, final List<ERMAttributeError> requireds)
'''
pass
def getNavigationHistory():
'''public NavigationHistoryStack getNavigationHistory()
'''
pass
def getErrorLevel():
'''public int getErrorLevel()
'''
pass
def setRetryErrorValues():
'''public void setRetryErrorValues(final boolean retryErrorValues)
'''
pass
def hasHandledRequiredFieldException():
'''public boolean hasHandledRequiredFieldException()
'''
pass
def isSigOptionConditional():
'''public boolean isSigOptionConditional(String sigOption)
'''
pass
def addErrorToMasterList():
'''public void addErrorToMasterList(final SetValueError setValueError)
'''
pass
def getErrorFromMasterList():
'''public SetValueError getErrorFromMasterList(final ApplicationError appError)
'''
pass
def removeErrorFromMasterList():
'''public void removeErrorFromMasterList(final SetValueError setValueError)
'''
pass
def getAutoFillForPage():
'''public JSONObject getAutoFillForPage(final PageInstance page)
'''
pass
def getDatastoreSet():
'''public DatastoreSet getDatastoreSet()
'''
pass
def getKeyLabel():
'''public String getKeyLabel()
'''
pass
def setRecHover():
'''public void setRecHover(final Element rhElement, final ComponentInstance sourceComponent)
'''
pass
def getRecHover():
'''public RecordHover getRecHover()
'''
pass
def clearRecHover():
'''public void clearRecHover()
'''
pass
def isMainrecActionMenu():
'''public boolean isMainrecActionMenu()
'''
pass
def setListTableOrderBy():
'''public void setListTableOrderBy(final String orderBy)
'''
pass
def getListTableOrderBy():
'''public String getListTableOrderBy()
'''
pass
def getAppIdList():
'''public Hashtable<String, String> getAppIdList()
'''
pass
def getNextToolbarNumber():
'''public int getNextToolbarNumber()
'''
pass
