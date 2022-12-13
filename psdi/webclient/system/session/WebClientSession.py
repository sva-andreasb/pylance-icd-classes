MSG_BTNCLOSE = "int  1"
MSG_BTNOK = "int  2"
MSG_BTNCANCEL = "int  4"
MSG_BTNYES = "int  8"
MSG_BTNNO = "int  16"
AGENT_IE = "int  0"
AGENT_FIREFOX = "int  1"
AGENT_CHROME = "int  2"
AGENT_SAFARI = "int  3"
AGENT_OPERA = "int  4"
LEFTNAV_INHERIT = "int  0"
LEFTNAV_OPEN = "int  1"
LEFTNAV_CLOSE = "int  2"
DISPLAYMETHOD_STATUS = "String  STATUS""
DISPLAYMETHOD_MSGBOX = "String  MSGBOX""
SAVEMODE_ONLOAD = "String  ONLOAD""
SAVEMODE_ONUNLOAD = "String  ONUNLOAD""
SAVEMODE_ONLOADUNLOAD = "String  ONLOADUNLOAD""
REQUESTTYPE = "String  requesttype""
TEMP_TOKEN_PARAM = "String  _tt""
def WebClientSession():
'''public WebClientSession(final HttpSession httpSession)
'''
pass
def isPostTivoli09Skin():
'''public boolean isPostTivoli09Skin()
'''
pass
def getSkin():
'''public String getSkin()
'''
pass
def getSkinName():
'''public String getSkinName()
'''
pass
def getAdaptorInstance():
'''public SessionContext getAdaptorInstance()
'''
pass
def getMxSessionConnected():
'''public boolean getMxSessionConnected()
'''
pass
def setMxSessionConnected():
'''public void setMxSessionConnected(final boolean flag)
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def applySkin():
'''public void applySkin()
'''
pass
def isMobileUserAgent():
'''public boolean isMobileUserAgent()
'''
pass
def getUserAgentName():
'''public String getUserAgentName()
'''
pass
def getUserAgentReplacement():
'''public String getUserAgentReplacement()
'''
pass
def getUserAgent():
'''public int getUserAgent()
'''
pass
def handleRequest():
'''public synchronized void handleRequest(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
def fixRowForTableDetails():
'''public String fixRowForTableDetails(final String compId)
'''
pass
def getProxyRequestContextURL():
'''public String getProxyRequestContextURL()
'''
pass
def getProxyBaseURL():
'''public String getProxyBaseURL()
'''
pass
def getPortalMsg():
'''public String getPortalMsg()
'''
pass
def setPortalMsg():
'''public void setPortalMsg(final String aMsg)
'''
pass
def getContextChanged():
'''public boolean getContextChanged()
'''
pass
def setContextChanged():
'''public void setContextChanged(final boolean aBool)
'''
pass
def showwfinfo():
'''public int showwfinfo()
'''
pass
def setErrorFieldFocus():
'''public void setErrorFieldFocus(final String currentFocusId, final boolean forceRow)
'''
pass
def printDebugMessage():
'''public void printDebugMessage(final int level, final String message)
'''
pass
def handleEvent():
'''public int handleEvent(final WebClientEvent event)
'''
pass
def hasWorkflowInfo():
'''public boolean hasWorkflowInfo()
'''
pass
def getEventQueue():
'''public EventQueue getEventQueue()
'''
pass
def queueEvent():
'''public void queueEvent(final WebClientEvent event)
'''
pass
def getCurrentPageId():
'''public String getCurrentPageId()
'''
pass
def getCurrentPage():
'''public PageInstance getCurrentPage()
'''
pass
def getDataBean():
'''public DataBean getDataBean(final String beanId)
'''
pass
def checkForDialogAccess():
'''public boolean checkForDialogAccess(final String dialogId, final Element dialog)
'''
pass
def findDialog():
'''public PageInstance findDialog(final String dialogId)
'''
pass
def getUniqueId():
'''public String getUniqueId()
'''
pass
def findDialogInDesignerApps():
'''public ControlInstance findDialogInDesignerApps(final String dialogId)
'''
pass
def setLongOpComponent():
'''public void setLongOpComponent(final ComponentInstance longOp)
'''
pass
def getLongOpComponent():
'''public ComponentInstance getLongOpComponent()
'''
pass
def loadDialog():
'''public int loadDialog(String dialogId)
public int loadDialog(final String dialogId, final boolean showmessages, final String longOpMessage)
'''
pass
def loadDialogInDesignerApps():
'''public int loadDialogInDesignerApps(final String dialogId)
'''
pass
def getControlInstance():
'''public ControlInstance getControlInstance(final String id)
public ControlInstance getControlInstance(final String id, final boolean tableDownload)
'''
pass
def getCurrentApp():
'''public AppInstance getCurrentApp()
'''
pass
def getCurrentAppId():
'''public String getCurrentAppId()
'''
pass
def getPreviousApp():
'''public AppInstance getPreviousApp()
'''
pass
def getMXSession():
'''public MXSession getMXSession()
'''
pass
def getHttpSession():
'''public HttpSession getHttpSession()
'''
pass
def setHttpSession():
'''public void setHttpSession(final HttpSession https)
'''
pass
def pushApp():
'''public void pushApp(final AppInstance ai)
'''
pass
def popApp():
'''public AppInstance popApp()
'''
pass
def clearStack():
'''public void clearStack()
'''
pass
def getAppStack():
'''public Stack<AppInstance> getAppStack()
'''
pass
def setCurrentEvent():
'''public void setCurrentEvent(final WebClientEvent event)
'''
pass
def getCurrentEvent():
'''public WebClientEvent getCurrentEvent()
'''
pass
def getFirstHandledEvent():
'''public WebClientEvent getFirstHandledEvent()
'''
pass
def getOriginalEvent():
'''public WebClientEvent getOriginalEvent()
'''
pass
def setEventState():
'''public void setEventState(final int state)
'''
pass
def getEventState():
'''public int getEventState()
'''
pass
def getCurrentEventHandler():
'''public ControlInstance getCurrentEventHandler()
'''
pass
def setCurrentEventHandler():
'''public void setCurrentEventHandler(final ControlInstance eventHandler)
'''
pass
def setPerfStat():
'''public void setPerfStat(final String flag)
'''
pass
def getPerfStat():
'''public boolean getPerfStat()
'''
pass
def getRequest():
'''public HttpServletRequest getRequest()
'''
pass
def getRequestType():
'''public RequestType getRequestType()
public static RequestType getRequestType(final HttpServletRequest request)
'''
pass
def setRequest():
'''public void setRequest(final HttpServletRequest request)
'''
pass
def getResponse():
'''public HttpServletResponse getResponse()
'''
pass
def setResponse():
'''public void setResponse(final HttpServletResponse response)
'''
pass
def createMXSession():
'''public MXSession createMXSession()
'''
pass
def hasWarnings():
'''public boolean hasWarnings()
'''
pass
def getWarnings():
'''public ArrayList<MXException> getWarnings()
'''
pass
def addWarning():
'''public void addWarning(final MXException e)
'''
pass
def removeWarnings():
'''public List<MXException> removeWarnings()
'''
pass
def addWarnings():
'''public void addWarnings(final List<MXException> warningList)
'''
pass
def getLoginEvent():
'''public WebClientEvent getLoginEvent()
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getAlignment():
'''public Alignment getAlignment()
'''
pass
def getHelpLangCode():
'''public String getHelpLangCode()
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def setTimeZone():
'''public void setTimeZone(final String strTimeZone)
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def getUserLanguageCode():
'''public String getUserLanguageCode()
'''
pass
def getMaxMessageMboSetRemote():
'''public MboSetRemote getMaxMessageMboSetRemote()
'''
pass
def setMaxMessageMboSetRemote():
'''public void setMaxMessageMboSetRemote(final MboSetRemote setmboSet)
'''
pass
def getUserApps():
'''public Set<String> getUserApps()
'''
pass
def getOriginalApp():
'''public String getOriginalApp(final String currentApp)
'''
pass
def getAppDesc():
'''public String getAppDesc(String appId)
'''
pass
def getClonedApps():
'''public Set<String> getClonedApps(final String originalApp)
'''
pass
def getOriginalApps():
'''public Set<String> getOriginalApps(String currentApp)
'''
pass
def getAppMainTable():
'''public String getAppMainTable(final String currentApp)
'''
pass
def getSpellSessionAdapter():
'''public SpellingSessionAdapter getSpellSessionAdapter()
'''
pass
def setSpellSessionAdapter():
'''public void setSpellSessionAdapter(final SpellingSessionAdapter spellSessionAdapter)
'''
pass
def pauseQueue():
'''public void pauseQueue()
'''
pass
def isQueuePaused():
'''public boolean isQueuePaused()
'''
pass
def unPauseQueue():
'''public void unPauseQueue()
'''
pass
def runLongOp():
'''public boolean runLongOp(final DataBean dataSrc, final WebClientEvent event)
public boolean runLongOp(final DataBean dataSrc, final WebClientEvent event, boolean showMessages, final String longOpMessage)
public boolean runLongOp(final DataBean dataSrc, final String method)
public boolean runLongOp(final DataBean dataSrc, final String method, boolean showMessages, final String longOpMessage)
'''
pass
def runLongOpQuery():
'''public boolean runLongOpQuery(final DataBean dataSrc, final String method, boolean showMessages, final String longOpMessage)
'''
pass
def stopLongOpQuery():
'''public void stopLongOpQuery()
'''
pass
def getLongOpStatus():
'''public int getLongOpStatus()
'''
pass
def hasLongOpStarted():
'''public boolean hasLongOpStarted()
'''
pass
def setLongOpChecked():
'''public void setLongOpChecked(final boolean longopChecked)
'''
pass
def hasLongOpCompleted():
'''public boolean hasLongOpCompleted()
'''
pass
def hasQueryLongOpCompleted():
'''public boolean hasQueryLongOpCompleted()
'''
pass
def getLongOpEvent():
'''public WebClientEvent getLongOpEvent()
'''
pass
def getLongOpMethod():
'''public String getLongOpMethod()
'''
pass
def finishLongOpEvent():
'''public void finishLongOpEvent()
'''
pass
def longOpCleanup():
'''public void longOpCleanup()
'''
pass
def longOpQueryCleanup():
'''public void longOpQueryCleanup()
'''
pass
def getWorkflowDirector():
'''public WorkflowDirector getWorkflowDirector()
'''
pass
def getSettingsProperty():
'''public String getSettingsProperty(final String prop)
public String getSettingsProperty(final String prop, final String[] params)
'''
pass
def getMaxMessage():
'''public MaxMessage getMaxMessage(final MXException mxe)
public MaxMessage getMaxMessage(final RemoteException e)
public MaxMessage getMaxMessage(final String group, final String key)
'''
pass
def getMessage():
'''public String getMessage(final MXException mxe)
public String getMessage(final String group, final String key)
public String getMessage(final String group, final String key, final String[] params)
'''
pass
def getMessages():
'''public String[] getMessages(final String group, final String[] key)
'''
pass
def getClientSideMessage():
'''public String getClientSideMessage(final String group, final String key)
'''
pass
def showMessageBox():
'''public void showMessageBox(final WebClientEvent srcEvent, final String title, final String warnings, final int flags)
public void showMessageBox(final WebClientEvent srcEvent, final String messageFile, final String key, final String[] params)
public void showMessageBox(final WebClientEvent srcEvent, final String messageFile, final String key, final Object[] params)
public void showMessageBox(final String messageFile, final String key, final String[] params)
public void showMessageBox(final WebClientEvent srcEvent, final MXException mxe)
public void showMessageBox(final WebClientEvent srcEvent, final RemoteException re)
public void showMessageBox(final MXException mxe)
'''
pass
def generateMessageBoxForTable():
'''public void generateMessageBoxForTable(final Hashtable<String, String> messageInfo)
'''
pass
def getMessageInfoForTable():
'''public Hashtable<String, String> getMessageInfoForTable(final MaxMessage message, final MXException mxe)
public Hashtable<String, String> getMessageInfoForTable(final MaxMessage message, final Object[] params)
'''
pass
def showEsigLoginDialog():
'''public void showEsigLoginDialog(final ESigLoginException srcExcept)
'''
pass
def addMXWarnings():
'''public boolean addMXWarnings(final MXException[] warnings)
'''
pass
def handleMXWarnings():
'''public boolean handleMXWarnings()
public boolean handleMXWarnings(final boolean showMultipleWarningsSeparately)
'''
pass
def setUserInput():
'''public void setUserInput(final MXException mxe, final int msgReturn)
'''
pass
def clearUserInput():
'''public void clearUserInput()
'''
pass
def showLongopDialog():
'''public void showLongopDialog(final String datasrc)
'''
pass
def gotoApplink():
'''public void gotoApplink(String url)
'''
pass
def handleDialogOK():
'''public boolean handleDialogOK(final boolean advancedLongOp)
public boolean handleDialogOK(final boolean advancedLongOp, final String longOpMessage)
'''
pass
def findControl():
'''public ControlInstance findControl(final String controlId)
'''
pass
def processProfiles():
'''public int processProfiles(final String profileName)
'''
pass
def getSystemOptionMap():
'''public Map<Integer, Map<String, String>> getSystemOptionMap()
'''
pass
def clearModuleMap():
'''public void clearModuleMap()
'''
pass
def getModuleMap():
'''public Map<Integer, Hashtable<String, String>> getModuleMap()
'''
pass
def getReportsMap():
'''public Map<Integer, Map<String, String>> getReportsMap()
'''
pass
def getSystemProperty():
'''public String[] getSystemProperty(final String propertyName)
'''
pass
def isPermanentLicense():
'''public boolean isPermanentLicense()
'''
pass
def getEvalDaysRemaining():
'''public String getEvalDaysRemaining()
'''
pass
def invalidate():
'''public void invalidate()
'''
pass
def useLeftContextInterval():
'''public void useLeftContextInterval(final boolean use)
'''
pass
def usingContextInterval():
'''public boolean usingContextInterval()
'''
pass
def hasTimedOut():
'''public boolean hasTimedOut()
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def getRequestParameter():
'''public String getRequestParameter(final String key)
'''
pass
def setLightningPortalMode():
'''public void setLightningPortalMode(final boolean portalmode)
'''
pass
def setPortalMode():
'''public void setPortalMode(final boolean portalmode)
'''
pass
def getLightningPortalMode():
'''public boolean getLightningPortalMode()
'''
pass
def getPortalMode():
'''public boolean getPortalMode()
'''
pass
def setTipPortalMode():
'''public void setTipPortalMode(final boolean tipportalmode)
'''
pass
def getTipPortalMode():
'''public boolean getTipPortalMode()
'''
pass
def getDesignModeWebClientSession():
'''public WebClientSession getDesignModeWebClientSession()
'''
pass
def hasDesignModeWebClientSession():
'''public boolean hasDesignModeWebClientSession()
'''
pass
def setDesignModeWebClientSession():
'''public void setDesignModeWebClientSession(final WebClientSession wcs)
'''
pass
def setOriginalSession():
'''public void setOriginalSession(final WebClientSession wcs)
'''
pass
def getOriginalSession():
'''public WebClientSession getOriginalSession()
'''
pass
def getContextPath():
'''public String getContextPath()
'''
pass
def setDesignmode():
'''public void setDesignmode(final boolean flag)
'''
pass
def getDesignmode():
'''public boolean getDesignmode()
'''
pass
def getMobile():
'''public boolean getMobile()
'''
pass
def setMobile():
'''public void setMobile(final boolean setValue)
'''
pass
def setLockMboOnEntry():
'''public void setLockMboOnEntry(final boolean checkrecordlock)
'''
pass
def lockMboOnEntry():
'''public boolean lockMboOnEntry()
'''
pass
def setPerformanceDataHASH():
'''public void setPerformanceDataHASH(final String keyName, final String value)
public void setPerformanceDataHASH(final String keyName, long sInputValue)
'''
pass
def clearPerformanceDataHASH():
'''public void clearPerformanceDataHASH(final String appname)
'''
pass
def clearAllTracking():
'''public void clearAllTracking()
'''
pass
def getUISessionID():
'''public String getUISessionID()
'''
pass
def getUISessionUrlParameter():
'''public String getUISessionUrlParameter()
'''
pass
def setUISessionID():
'''public void setUISessionID(final String uiSessionID)
'''
pass
def setSessionFound():
'''public void setSessionFound(final boolean flag)
'''
pass
def isSessionFound():
'''public boolean isSessionFound()
'''
pass
def valueBound():
'''public void valueBound(final HttpSessionBindingEvent arg0)
'''
pass
def valueUnbound():
'''public void valueUnbound(final HttpSessionBindingEvent arg0)
'''
pass
def isWebReplayEnabled():
'''public boolean isWebReplayEnabled()
'''
pass
def setShowWebReplay():
'''public void setShowWebReplay(final boolean show)
'''
pass
def getShowWebReplay():
'''public boolean getShowWebReplay()
'''
pass
def showWebReplay():
'''public boolean showWebReplay(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
def hideWebReplay():
'''public void hideWebReplay(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
def getDebug():
'''public boolean getDebug()
'''
pass
def getDebugLevel():
'''public int getDebugLevel()
'''
pass
def getEventLog():
'''public String getEventLog()
'''
pass
def setDebugDock():
'''public void setDebugDock(final String left, final String top)
'''
pass
def setAccessibilityMode():
'''public void setAccessibilityMode(final boolean mode)
'''
pass
def getAccessibilityMode():
'''public boolean getAccessibilityMode()
'''
pass
def getSystemEventHandler():
'''public EventHandlerInterface getSystemEventHandler()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def getImagePath():
'''public String getImagePath()
'''
pass
def getCssPath():
'''public String getCssPath()
'''
pass
def getWebClientURL():
'''public String getWebClientURL()
'''
pass
def getImageURL():
'''public String getImageURL()
'''
pass
def getCssURL():
'''public String getCssURL()
'''
pass
def setImagePath():
'''public void setImagePath(final String path)
'''
pass
def setCssPath():
'''public void setCssPath(final String path)
'''
pass
def isCombinedSetValue():
'''public boolean isCombinedSetValue()
'''
pass
def subFrameAllowed():
'''public boolean subFrameAllowed()
'''
pass
def forceMessagesToMainPage():
'''public void forceMessagesToMainPage(final boolean forceMain)
'''
pass
def getForceMessagesToMainPage():
'''public boolean getForceMessagesToMainPage()
'''
pass
def setAdvancedLongOp():
'''public void setAdvancedLongOp(final boolean advanced)
'''
pass
def isAutomationOn():
'''public boolean isAutomationOn()
'''
pass
def turnAutomationOn():
'''public void turnAutomationOn()
'''
pass
def checkResults():
'''public static void checkResults(final DataBean results, final WebClientSession clientSession, final AppInstance app)
'''
pass
def replaceQbeclearButton():
'''public Element replaceQbeclearButton(final Element dialogElement)
'''
pass
def addMoreinfoButton():
'''public Element addMoreinfoButton(final Element dialogElement, final String value)
'''
pass
def isMaximoOrTivoliBrand():
'''public boolean isMaximoOrTivoliBrand()
'''
pass
def killPopup():
'''public void killPopup(final boolean killIt)
public void killPopup(final WebClientEvent event)
'''
pass
def wasPopupKilled():
'''public boolean wasPopupKilled()
'''
pass
def getMaximoRequestURI():
'''public String getMaximoRequestURI()
'''
pass
def getMaximoRequestURL():
'''public String getMaximoRequestURL()
'''
pass
def getMaximoRequestContextURL():
'''public String getMaximoRequestContextURL()
'''
pass
def getMaximoBaseURL():
'''public String getMaximoBaseURL()
'''
pass
def getDefautlFormat():
'''public String getDefautlFormat()
'''
pass
def setDefautlFormat():
'''public void setDefautlFormat(final String defaultFormat)
'''
pass
def wereImagesPreLoaded():
'''public boolean wereImagesPreLoaded()
'''
pass
def setImagesPreLoaded():
'''public void setImagesPreLoaded(final boolean pre)
'''
pass
def lastAccessed():
'''public Date lastAccessed()
'''
pass
def stamp():
'''public void stamp()
'''
pass
def getFactoryId():
'''public String getFactoryId()
'''
pass
def getStartCenterCache():
'''public Object getStartCenterCache(final String key)
'''
pass
def setStartCenterCache():
'''public void setStartCenterCache(final String key, final Object obj)
'''
pass
def resetStartCenterCache():
'''public void resetStartCenterCache()
'''
pass
def resetPortletCaches():
'''public void resetPortletCaches()
'''
pass
def clearPortletCacheSelectively():
'''public void clearPortletCacheSelectively(final String prefix)
'''
pass
def clearPortletCacheOnKPIChange():
'''public void clearPortletCacheOnKPIChange(final String kpiName)
'''
pass
def clearPortletCacheOnReportChange():
'''public void clearPortletCacheOnReportChange(final String reportId)
'''
pass
def clearStartCenterCache():
'''public void clearStartCenterCache(final String key)
'''
pass
def hasStartCenterCache():
'''public boolean hasStartCenterCache(final String key)
'''
pass
def isAsyncEnabled():
'''public boolean isAsyncEnabled()
'''
pass
def getAsyncRequestManager():
'''public AsyncRequestManager getAsyncRequestManager()
'''
pass
def performApplink():
'''public void performApplink(final boolean canApplink)
'''
pass
def canPerformApplink():
'''public boolean canPerformApplink()
'''
pass
def processRender():
'''public void processRender()
'''
pass
def getDebugDockLeft():
'''public int getDebugDockLeft()
'''
pass
def getDebugDockTop():
'''public int getDebugDockTop()
'''
pass
def getIEVersion():
'''public double getIEVersion()
'''
pass
def setInFrameset():
'''public void setInFrameset(final boolean isInFrameset)
'''
pass
def isInFrameset():
'''public boolean isInFrameset()
'''
pass
def canUseStaticIds():
'''public boolean canUseStaticIds()
'''
pass
def getImageSourcePath():
'''public String getImageSourcePath()
'''
pass
def getDialogIcon():
'''public String getDialogIcon(final String suffix)
'''
pass
def getWarningInfo():
'''public ContainerErrorInfo getWarningInfo()
'''
pass
def getSmartFillExceptionInfo():
'''public ContainerErrorInfo getSmartFillExceptionInfo()
'''
pass
def getExceptionInfo():
'''public ContainerErrorInfo getExceptionInfo()
'''
pass
def getQuestionInfo():
'''public ContainerErrorInfo getQuestionInfo()
'''
pass
def getContainerErrorIconJSON():
'''public JSONObject getContainerErrorIconJSON()
'''
pass
def getConditionalUIHelper():
'''public ConditionalUIHelper getConditionalUIHelper()
'''
pass
def toString():
'''public String toString()
'''
pass
def getDefaultStartApp():
'''public String getDefaultStartApp()
'''
pass
def getRegexPattern():
'''public String getRegexPattern(final int dataType)
'''
pass
def setMenusCached():
'''public void setMenusCached(final boolean cached)
'''
pass
def getMenusCached():
'''public boolean getMenusCached()
'''
pass
def hasPausedEvents():
'''public boolean hasPausedEvents()
'''
pass
def getDesignerAsyncRequestManager():
'''public AsyncRequestManager getDesignerAsyncRequestManager()
'''
pass
def setAttribute():
'''public void setAttribute(final String attributeName, final Object value)
'''
pass
def getAttribute():
'''public Object getAttribute(final String attributeName)
'''
pass
def attachUOM():
'''public String attachUOM(String size)
'''
pass
def removeUOM():
'''public String removeUOM(String size)
'''
pass
def useVerticalLabels():
'''public boolean useVerticalLabels()
'''
pass
def generateOneTimeCSRFTokenParameter():
'''public String generateOneTimeCSRFTokenParameter()
'''
pass
def generateRetryCSRFTokenParameter():
'''public String generateRetryCSRFTokenParameter()
'''
pass
def isTempTokenValid():
'''public boolean isTempTokenValid(final String oneTimeToken)
'''
pass
def getCSRFToken():
'''public String getCSRFToken()
'''
pass
def getCSRFTokenParameter():
'''public String getCSRFTokenParameter()
'''
pass
def showSystemNavBar():
'''public boolean showSystemNavBar(final PageInstance page)
'''
pass
def getMessageBoxQueue():
'''public Queue<Map<String, String>> getMessageBoxQueue()
'''
pass
def getFeaturePack():
'''public String getFeaturePack()
'''
pass
def supportsLocalStorage():
'''public boolean supportsLocalStorage()
'''
pass
def setLeftNavWidth():
'''public void setLeftNavWidth(final String width)
'''
pass
def getLeftNavWidth():
'''public String getLeftNavWidth(final PageInstance page)
'''
pass
def valueFor():
'''public static RequestType valueFor(final String type)
'''
pass
def Alignment():
'''public Alignment(final String langcode)
'''
pass
def reverse():
'''public String reverse(final String align)
'''
pass
