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
DISPLAYMETHOD_STATUS = "String  \"STATUS\""
DISPLAYMETHOD_MSGBOX = "String  \"MSGBOX\""
SAVEMODE_ONLOAD = "String  \"ONLOAD\""
SAVEMODE_ONUNLOAD = "String  \"ONUNLOAD\""
SAVEMODE_ONLOADUNLOAD = "String  \"ONLOADUNLOAD\""
REQUESTTYPE = "String  \"requesttype\""
TEMP_TOKEN_PARAM = "String  \"_tt\""
def WebClientSession():
    '''public WebClientSession(final HttpSession httpSession)
    '''
def isPostTivoli09Skin():
    '''public boolean isPostTivoli09Skin()
    '''
def getSkin():
    '''public String getSkin()
    '''
def getSkinName():
    '''public String getSkinName()
    '''
def getAdaptorInstance():
    '''public SessionContext getAdaptorInstance()
    '''
def getMxSessionConnected():
    '''public boolean getMxSessionConnected()
    '''
def setMxSessionConnected():
    '''public void setMxSessionConnected(final boolean flag)
    '''
def isConnected():
    '''public boolean isConnected()
    '''
def applySkin():
    '''public void applySkin()
    '''
def isMobileUserAgent():
    '''public boolean isMobileUserAgent()
    '''
def getUserAgentName():
    '''public String getUserAgentName()
    '''
def getUserAgentReplacement():
    '''public String getUserAgentReplacement()
    '''
def getUserAgent():
    '''public int getUserAgent()
    '''
def handleRequest():
    '''public synchronized void handleRequest(final HttpServletRequest request, final HttpServletResponse response)
    '''
def fixRowForTableDetails():
    '''public String fixRowForTableDetails(final String compId)
    '''
def getProxyRequestContextURL():
    '''public String getProxyRequestContextURL()
    '''
def getProxyBaseURL():
    '''public String getProxyBaseURL()
    '''
def getPortalMsg():
    '''public String getPortalMsg()
    '''
def setPortalMsg():
    '''public void setPortalMsg(final String aMsg)
    '''
def getContextChanged():
    '''public boolean getContextChanged()
    '''
def setContextChanged():
    '''public void setContextChanged(final boolean aBool)
    '''
def showwfinfo():
    '''public int showwfinfo()
    '''
def setErrorFieldFocus():
    '''public void setErrorFieldFocus(final String currentFocusId, final boolean forceRow)
    '''
def printDebugMessage():
    '''public void printDebugMessage(final int level, final String message)
    '''
def handleEvent():
    '''public int handleEvent(final WebClientEvent event)
    '''
def hasWorkflowInfo():
    '''public boolean hasWorkflowInfo()
    '''
def getEventQueue():
    '''public EventQueue getEventQueue()
    '''
def queueEvent():
    '''public void queueEvent(final WebClientEvent event)
    '''
def getCurrentPageId():
    '''public String getCurrentPageId()
    '''
def getCurrentPage():
    '''public PageInstance getCurrentPage()
    '''
def getDataBean():
    '''public DataBean getDataBean(final String beanId)
    '''
def checkForDialogAccess():
    '''public boolean checkForDialogAccess(final String dialogId, final Element dialog)
    '''
def findDialog():
    '''public PageInstance findDialog(final String dialogId)
    '''
def getUniqueId():
    '''public String getUniqueId()
    '''
def findDialogInDesignerApps():
    '''public ControlInstance findDialogInDesignerApps(final String dialogId)
    '''
def setLongOpComponent():
    '''public void setLongOpComponent(final ComponentInstance longOp)
    '''
def getLongOpComponent():
    '''public ComponentInstance getLongOpComponent()
    '''
def loadDialog():
    '''public int loadDialog(String dialogId)
    public int loadDialog(final String dialogId, final boolean showmessages, final String longOpMessage)
    '''
def loadDialogInDesignerApps():
    '''public int loadDialogInDesignerApps(final String dialogId)
    '''
def getControlInstance():
    '''public ControlInstance getControlInstance(final String id)
    public ControlInstance getControlInstance(final String id, final boolean tableDownload)
    '''
def getCurrentApp():
    '''public AppInstance getCurrentApp()
    '''
def getCurrentAppId():
    '''public String getCurrentAppId()
    '''
def getPreviousApp():
    '''public AppInstance getPreviousApp()
    '''
def getMXSession():
    '''public MXSession getMXSession()
    '''
def getHttpSession():
    '''public HttpSession getHttpSession()
    '''
def setHttpSession():
    '''public void setHttpSession(final HttpSession https)
    '''
def pushApp():
    '''public void pushApp(final AppInstance ai)
    '''
def popApp():
    '''public AppInstance popApp()
    '''
def clearStack():
    '''public void clearStack()
    '''
def getAppStack():
    '''public Stack<AppInstance> getAppStack()
    '''
def setCurrentEvent():
    '''public void setCurrentEvent(final WebClientEvent event)
    '''
def getCurrentEvent():
    '''public WebClientEvent getCurrentEvent()
    '''
def getFirstHandledEvent():
    '''public WebClientEvent getFirstHandledEvent()
    '''
def getOriginalEvent():
    '''public WebClientEvent getOriginalEvent()
    '''
def setEventState():
    '''public void setEventState(final int state)
    '''
def getEventState():
    '''public int getEventState()
    '''
def getCurrentEventHandler():
    '''public ControlInstance getCurrentEventHandler()
    '''
def setCurrentEventHandler():
    '''public void setCurrentEventHandler(final ControlInstance eventHandler)
    '''
def setPerfStat():
    '''public void setPerfStat(final String flag)
    '''
def getPerfStat():
    '''public boolean getPerfStat()
    '''
def getRequest():
    '''public HttpServletRequest getRequest()
    '''
def getRequestType():
    '''public RequestType getRequestType()
    public static RequestType getRequestType(final HttpServletRequest request)
    '''
def setRequest():
    '''public void setRequest(final HttpServletRequest request)
    '''
def getResponse():
    '''public HttpServletResponse getResponse()
    '''
def setResponse():
    '''public void setResponse(final HttpServletResponse response)
    '''
def createMXSession():
    '''public MXSession createMXSession()
    '''
def hasWarnings():
    '''public boolean hasWarnings()
    '''
def getWarnings():
    '''public ArrayList<MXException> getWarnings()
    '''
def addWarning():
    '''public void addWarning(final MXException e)
    '''
def removeWarnings():
    '''public List<MXException> removeWarnings()
    '''
def addWarnings():
    '''public void addWarnings(final List<MXException> warningList)
    '''
def getLoginEvent():
    '''public WebClientEvent getLoginEvent()
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def getAlignment():
    '''public Alignment getAlignment()
    '''
def getHelpLangCode():
    '''public String getHelpLangCode()
    '''
def getTimeZone():
    '''public TimeZone getTimeZone()
    '''
def setTimeZone():
    '''public void setTimeZone(final String strTimeZone)
    '''
def getUserInfo():
    '''public UserInfo getUserInfo()
    '''
def getUserLanguageCode():
    '''public String getUserLanguageCode()
    '''
def getMaxMessageMboSetRemote():
    '''public MboSetRemote getMaxMessageMboSetRemote()
    '''
def setMaxMessageMboSetRemote():
    '''public void setMaxMessageMboSetRemote(final MboSetRemote setmboSet)
    '''
def getUserApps():
    '''public Set<String> getUserApps()
    '''
def getOriginalApp():
    '''public String getOriginalApp(final String currentApp)
    '''
def getAppDesc():
    '''public String getAppDesc(String appId)
    '''
def getClonedApps():
    '''public Set<String> getClonedApps(final String originalApp)
    '''
def getOriginalApps():
    '''public Set<String> getOriginalApps(String currentApp)
    '''
def getAppMainTable():
    '''public String getAppMainTable(final String currentApp)
    '''
def getSpellSessionAdapter():
    '''public SpellingSessionAdapter getSpellSessionAdapter()
    '''
def setSpellSessionAdapter():
    '''public void setSpellSessionAdapter(final SpellingSessionAdapter spellSessionAdapter)
    '''
def pauseQueue():
    '''public void pauseQueue()
    '''
def isQueuePaused():
    '''public boolean isQueuePaused()
    '''
def unPauseQueue():
    '''public void unPauseQueue()
    '''
def runLongOp():
    '''public boolean runLongOp(final DataBean dataSrc, final WebClientEvent event)
    public boolean runLongOp(final DataBean dataSrc, final WebClientEvent event, boolean showMessages, final String longOpMessage)
    public boolean runLongOp(final DataBean dataSrc, final String method)
    public boolean runLongOp(final DataBean dataSrc, final String method, boolean showMessages, final String longOpMessage)
    '''
def runLongOpQuery():
    '''public boolean runLongOpQuery(final DataBean dataSrc, final String method, boolean showMessages, final String longOpMessage)
    '''
def stopLongOpQuery():
    '''public void stopLongOpQuery()
    '''
def getLongOpStatus():
    '''public int getLongOpStatus()
    '''
def hasLongOpStarted():
    '''public boolean hasLongOpStarted()
    '''
def setLongOpChecked():
    '''public void setLongOpChecked(final boolean longopChecked)
    '''
def hasLongOpCompleted():
    '''public boolean hasLongOpCompleted()
    '''
def hasQueryLongOpCompleted():
    '''public boolean hasQueryLongOpCompleted()
    '''
def getLongOpEvent():
    '''public WebClientEvent getLongOpEvent()
    '''
def getLongOpMethod():
    '''public String getLongOpMethod()
    '''
def finishLongOpEvent():
    '''public void finishLongOpEvent()
    '''
def longOpCleanup():
    '''public void longOpCleanup()
    '''
def longOpQueryCleanup():
    '''public void longOpQueryCleanup()
    '''
def getWorkflowDirector():
    '''public WorkflowDirector getWorkflowDirector()
    '''
def getSettingsProperty():
    '''public String getSettingsProperty(final String prop)
    public String getSettingsProperty(final String prop, final String[] params)
    '''
def getMaxMessage():
    '''public MaxMessage getMaxMessage(final MXException mxe)
    public MaxMessage getMaxMessage(final RemoteException e)
    public MaxMessage getMaxMessage(final String group, final String key)
    '''
def getMessage():
    '''public String getMessage(final MXException mxe)
    public String getMessage(final String group, final String key)
    public String getMessage(final String group, final String key, final String[] params)
    '''
def getMessages():
    '''public String[] getMessages(final String group, final String[] key)
    '''
def getClientSideMessage():
    '''public String getClientSideMessage(final String group, final String key)
    '''
def showMessageBox():
    '''public void showMessageBox(final WebClientEvent srcEvent, final String title, final String warnings, final int flags)
    public void showMessageBox(final WebClientEvent srcEvent, final String messageFile, final String key, final String[] params)
    public void showMessageBox(final WebClientEvent srcEvent, final String messageFile, final String key, final Object[] params)
    public void showMessageBox(final String messageFile, final String key, final String[] params)
    public void showMessageBox(final WebClientEvent srcEvent, final MXException mxe)
    public void showMessageBox(final WebClientEvent srcEvent, final RemoteException re)
    public void showMessageBox(final MXException mxe)
    '''
def generateMessageBoxForTable():
    '''public void generateMessageBoxForTable(final Hashtable<String, String> messageInfo)
    '''
def getMessageInfoForTable():
    '''public Hashtable<String, String> getMessageInfoForTable(final MaxMessage message, final MXException mxe)
    public Hashtable<String, String> getMessageInfoForTable(final MaxMessage message, final Object[] params)
    '''
def showEsigLoginDialog():
    '''public void showEsigLoginDialog(final ESigLoginException srcExcept)
    '''
def addMXWarnings():
    '''public boolean addMXWarnings(final MXException[] warnings)
    '''
def handleMXWarnings():
    '''public boolean handleMXWarnings()
    public boolean handleMXWarnings(final boolean showMultipleWarningsSeparately)
    '''
def setUserInput():
    '''public void setUserInput(final MXException mxe, final int msgReturn)
    '''
def clearUserInput():
    '''public void clearUserInput()
    '''
def showLongopDialog():
    '''public void showLongopDialog(final String datasrc)
    '''
def gotoApplink():
    '''public void gotoApplink(String url)
    '''
def handleDialogOK():
    '''public boolean handleDialogOK(final boolean advancedLongOp)
    public boolean handleDialogOK(final boolean advancedLongOp, final String longOpMessage)
    '''
def findControl():
    '''public ControlInstance findControl(final String controlId)
    '''
def processProfiles():
    '''public int processProfiles(final String profileName)
    '''
def getSystemOptionMap():
    '''public Map<Integer, Map<String, String>> getSystemOptionMap()
    '''
def clearModuleMap():
    '''public void clearModuleMap()
    '''
def getModuleMap():
    '''public Map<Integer, Hashtable<String, String>> getModuleMap()
    '''
def getReportsMap():
    '''public Map<Integer, Map<String, String>> getReportsMap()
    '''
def getSystemProperty():
    '''public String[] getSystemProperty(final String propertyName)
    '''
def isPermanentLicense():
    '''public boolean isPermanentLicense()
    '''
def getEvalDaysRemaining():
    '''public String getEvalDaysRemaining()
    '''
def invalidate():
    '''public void invalidate()
    '''
def useLeftContextInterval():
    '''public void useLeftContextInterval(final boolean use)
    '''
def usingContextInterval():
    '''public boolean usingContextInterval()
    '''
def hasTimedOut():
    '''public boolean hasTimedOut()
    '''
def isValid():
    '''public boolean isValid()
    '''
def getRequestParameter():
    '''public String getRequestParameter(final String key)
    '''
def setLightningPortalMode():
    '''public void setLightningPortalMode(final boolean portalmode)
    '''
def setPortalMode():
    '''public void setPortalMode(final boolean portalmode)
    '''
def getLightningPortalMode():
    '''public boolean getLightningPortalMode()
    '''
def getPortalMode():
    '''public boolean getPortalMode()
    '''
def setTipPortalMode():
    '''public void setTipPortalMode(final boolean tipportalmode)
    '''
def getTipPortalMode():
    '''public boolean getTipPortalMode()
    '''
def getDesignModeWebClientSession():
    '''public WebClientSession getDesignModeWebClientSession()
    '''
def hasDesignModeWebClientSession():
    '''public boolean hasDesignModeWebClientSession()
    '''
def setDesignModeWebClientSession():
    '''public void setDesignModeWebClientSession(final WebClientSession wcs)
    '''
def setOriginalSession():
    '''public void setOriginalSession(final WebClientSession wcs)
    '''
def getOriginalSession():
    '''public WebClientSession getOriginalSession()
    '''
def getContextPath():
    '''public String getContextPath()
    '''
def setDesignmode():
    '''public void setDesignmode(final boolean flag)
    '''
def getDesignmode():
    '''public boolean getDesignmode()
    '''
def getMobile():
    '''public boolean getMobile()
    '''
def setMobile():
    '''public void setMobile(final boolean setValue)
    '''
def setLockMboOnEntry():
    '''public void setLockMboOnEntry(final boolean checkrecordlock)
    '''
def lockMboOnEntry():
    '''public boolean lockMboOnEntry()
    '''
def setPerformanceDataHASH():
    '''public void setPerformanceDataHASH(final String keyName, final String value)
    public void setPerformanceDataHASH(final String keyName, long sInputValue)
    '''
def clearPerformanceDataHASH():
    '''public void clearPerformanceDataHASH(final String appname)
    '''
def clearAllTracking():
    '''public void clearAllTracking()
    '''
def getUISessionID():
    '''public String getUISessionID()
    '''
def getUISessionUrlParameter():
    '''public String getUISessionUrlParameter()
    '''
def setUISessionID():
    '''public void setUISessionID(final String uiSessionID)
    '''
def setSessionFound():
    '''public void setSessionFound(final boolean flag)
    '''
def isSessionFound():
    '''public boolean isSessionFound()
    '''
def valueBound():
    '''public void valueBound(final HttpSessionBindingEvent arg0)
    '''
def valueUnbound():
    '''public void valueUnbound(final HttpSessionBindingEvent arg0)
    '''
def isWebReplayEnabled():
    '''public boolean isWebReplayEnabled()
    '''
def setShowWebReplay():
    '''public void setShowWebReplay(final boolean show)
    '''
def getShowWebReplay():
    '''public boolean getShowWebReplay()
    '''
def showWebReplay():
    '''public boolean showWebReplay(final HttpServletRequest request, final HttpServletResponse response)
    '''
def hideWebReplay():
    '''public void hideWebReplay(final HttpServletRequest request, final HttpServletResponse response)
    '''
def getDebug():
    '''public boolean getDebug()
    '''
def getDebugLevel():
    '''public int getDebugLevel()
    '''
def getEventLog():
    '''public String getEventLog()
    '''
def setDebugDock():
    '''public void setDebugDock(final String left, final String top)
    '''
def setAccessibilityMode():
    '''public void setAccessibilityMode(final boolean mode)
    '''
def getAccessibilityMode():
    '''public boolean getAccessibilityMode()
    '''
def getSystemEventHandler():
    '''public EventHandlerInterface getSystemEventHandler()
    '''
def cleanup():
    '''public void cleanup()
    '''
def getImagePath():
    '''public String getImagePath()
    '''
def getCssPath():
    '''public String getCssPath()
    '''
def getWebClientURL():
    '''public String getWebClientURL()
    '''
def getImageURL():
    '''public String getImageURL()
    '''
def getCssURL():
    '''public String getCssURL()
    '''
def setImagePath():
    '''public void setImagePath(final String path)
    '''
def setCssPath():
    '''public void setCssPath(final String path)
    '''
def isCombinedSetValue():
    '''public boolean isCombinedSetValue()
    '''
def subFrameAllowed():
    '''public boolean subFrameAllowed()
    '''
def forceMessagesToMainPage():
    '''public void forceMessagesToMainPage(final boolean forceMain)
    '''
def getForceMessagesToMainPage():
    '''public boolean getForceMessagesToMainPage()
    '''
def setAdvancedLongOp():
    '''public void setAdvancedLongOp(final boolean advanced)
    '''
def isAutomationOn():
    '''public boolean isAutomationOn()
    '''
def turnAutomationOn():
    '''public void turnAutomationOn()
    '''
def checkResults():
    '''public static void checkResults(final DataBean results, final WebClientSession clientSession, final AppInstance app)
    '''
def replaceQbeclearButton():
    '''public Element replaceQbeclearButton(final Element dialogElement)
    '''
def addMoreinfoButton():
    '''public Element addMoreinfoButton(final Element dialogElement, final String value)
    '''
def isMaximoOrTivoliBrand():
    '''public boolean isMaximoOrTivoliBrand()
    '''
def killPopup():
    '''public void killPopup(final boolean killIt)
    public void killPopup(final WebClientEvent event)
    '''
def wasPopupKilled():
    '''public boolean wasPopupKilled()
    '''
def getMaximoRequestURI():
    '''public String getMaximoRequestURI()
    '''
def getMaximoRequestURL():
    '''public String getMaximoRequestURL()
    '''
def getMaximoRequestContextURL():
    '''public String getMaximoRequestContextURL()
    '''
def getMaximoBaseURL():
    '''public String getMaximoBaseURL()
    '''
def getDefautlFormat():
    '''public String getDefautlFormat()
    '''
def setDefautlFormat():
    '''public void setDefautlFormat(final String defaultFormat)
    '''
def wereImagesPreLoaded():
    '''public boolean wereImagesPreLoaded()
    '''
def setImagesPreLoaded():
    '''public void setImagesPreLoaded(final boolean pre)
    '''
def lastAccessed():
    '''public Date lastAccessed()
    '''
def stamp():
    '''public void stamp()
    '''
def getFactoryId():
    '''public String getFactoryId()
    '''
def getStartCenterCache():
    '''public Object getStartCenterCache(final String key)
    '''
def setStartCenterCache():
    '''public void setStartCenterCache(final String key, final Object obj)
    '''
def resetStartCenterCache():
    '''public void resetStartCenterCache()
    '''
def resetPortletCaches():
    '''public void resetPortletCaches()
    '''
def clearPortletCacheSelectively():
    '''public void clearPortletCacheSelectively(final String prefix)
    '''
def clearPortletCacheOnKPIChange():
    '''public void clearPortletCacheOnKPIChange(final String kpiName)
    '''
def clearPortletCacheOnReportChange():
    '''public void clearPortletCacheOnReportChange(final String reportId)
    '''
def clearStartCenterCache():
    '''public void clearStartCenterCache(final String key)
    '''
def hasStartCenterCache():
    '''public boolean hasStartCenterCache(final String key)
    '''
def isAsyncEnabled():
    '''public boolean isAsyncEnabled()
    '''
def getAsyncRequestManager():
    '''public AsyncRequestManager getAsyncRequestManager()
    '''
def performApplink():
    '''public void performApplink(final boolean canApplink)
    '''
def canPerformApplink():
    '''public boolean canPerformApplink()
    '''
def processRender():
    '''public void processRender()
    '''
def getDebugDockLeft():
    '''public int getDebugDockLeft()
    '''
def getDebugDockTop():
    '''public int getDebugDockTop()
    '''
def getIEVersion():
    '''public double getIEVersion()
    '''
def setInFrameset():
    '''public void setInFrameset(final boolean isInFrameset)
    '''
def isInFrameset():
    '''public boolean isInFrameset()
    '''
def canUseStaticIds():
    '''public boolean canUseStaticIds()
    '''
def getImageSourcePath():
    '''public String getImageSourcePath()
    '''
def getDialogIcon():
    '''public String getDialogIcon(final String suffix)
    '''
def getWarningInfo():
    '''public ContainerErrorInfo getWarningInfo()
    '''
def getSmartFillExceptionInfo():
    '''public ContainerErrorInfo getSmartFillExceptionInfo()
    '''
def getExceptionInfo():
    '''public ContainerErrorInfo getExceptionInfo()
    '''
def getQuestionInfo():
    '''public ContainerErrorInfo getQuestionInfo()
    '''
def getContainerErrorIconJSON():
    '''public JSONObject getContainerErrorIconJSON()
    '''
def getConditionalUIHelper():
    '''public ConditionalUIHelper getConditionalUIHelper()
    '''
def toString():
    '''public String toString()
    '''
def getDefaultStartApp():
    '''public String getDefaultStartApp()
    '''
def getRegexPattern():
    '''public String getRegexPattern(final int dataType)
    '''
def setMenusCached():
    '''public void setMenusCached(final boolean cached)
    '''
def getMenusCached():
    '''public boolean getMenusCached()
    '''
def hasPausedEvents():
    '''public boolean hasPausedEvents()
    '''
def getDesignerAsyncRequestManager():
    '''public AsyncRequestManager getDesignerAsyncRequestManager()
    '''
def setAttribute():
    '''public void setAttribute(final String attributeName, final Object value)
    '''
def getAttribute():
    '''public Object getAttribute(final String attributeName)
    '''
def attachUOM():
    '''public String attachUOM(String size)
    '''
def removeUOM():
    '''public String removeUOM(String size)
    '''
def useVerticalLabels():
    '''public boolean useVerticalLabels()
    '''
def generateOneTimeCSRFTokenParameter():
    '''public String generateOneTimeCSRFTokenParameter()
    '''
def generateRetryCSRFTokenParameter():
    '''public String generateRetryCSRFTokenParameter()
    '''
def isTempTokenValid():
    '''public boolean isTempTokenValid(final String oneTimeToken)
    '''
def getCSRFToken():
    '''public String getCSRFToken()
    '''
def getCSRFTokenParameter():
    '''public String getCSRFTokenParameter()
    '''
def showSystemNavBar():
    '''public boolean showSystemNavBar(final PageInstance page)
    '''
def getMessageBoxQueue():
    '''public Queue<Map<String, String>> getMessageBoxQueue()
    '''
def getFeaturePack():
    '''public String getFeaturePack()
    '''
def supportsLocalStorage():
    '''public boolean supportsLocalStorage()
    '''
def setLeftNavWidth():
    '''public void setLeftNavWidth(final String width)
    '''
def getLeftNavWidth():
    '''public String getLeftNavWidth(final PageInstance page)
    '''
def valueFor():
    '''public static RequestType valueFor(final String type)
    '''
def Alignment():
    '''public Alignment(final String langcode)
    '''
def reverse():
    '''public String reverse(final String align)
    '''
