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
def ():
    '''returns Alignment\n\n
    (final HttpSession httpSession)\n
    (final String langcode)\n
    '''
def isPostTivoli09Skin():
    '''returns boolean\n\n
    isPostTivoli09Skin()\n
    '''
def getSkin():
    '''returns String\n\n
    getSkin()\n
    '''
def getSkinName():
    '''returns String\n\n
    getSkinName()\n
    '''
def getAdaptorInstance():
    '''returns SessionContext\n\n
    getAdaptorInstance()\n
    '''
def getMxSessionConnected():
    '''returns boolean\n\n
    getMxSessionConnected()\n
    '''
def setMxSessionConnected():
    '''returns None\n\n
    setMxSessionConnected(final boolean flag)\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def applySkin():
    '''returns None\n\n
    applySkin()\n
    '''
def isMobileUserAgent():
    '''returns boolean\n\n
    isMobileUserAgent()\n
    '''
def getUserAgentName():
    '''returns String\n\n
    getUserAgentName()\n
    '''
def getUserAgentReplacement():
    '''returns String\n\n
    getUserAgentReplacement()\n
    '''
def getUserAgent():
    '''returns int\n\n
    getUserAgent()\n
    '''
def fixRowForTableDetails():
    '''returns String\n\n
    fixRowForTableDetails(final String compId)\n
    '''
def getProxyRequestContextURL():
    '''returns String\n\n
    getProxyRequestContextURL()\n
    '''
def getProxyBaseURL():
    '''returns String\n\n
    getProxyBaseURL()\n
    '''
def getPortalMsg():
    '''returns String\n\n
    getPortalMsg()\n
    '''
def setPortalMsg():
    '''returns None\n\n
    setPortalMsg(final String aMsg)\n
    '''
def getContextChanged():
    '''returns boolean\n\n
    getContextChanged()\n
    '''
def setContextChanged():
    '''returns None\n\n
    setContextChanged(final boolean aBool)\n
    '''
def showwfinfo():
    '''returns int\n\n
    showwfinfo()\n
    '''
def setErrorFieldFocus():
    '''returns None\n\n
    setErrorFieldFocus(final String currentFocusId, final boolean forceRow)\n
    '''
def printDebugMessage():
    '''returns None\n\n
    printDebugMessage(final int level, final String message)\n
    '''
def handleEvent():
    '''returns int\n\n
    handleEvent(final WebClientEvent event)\n
    '''
def hasWorkflowInfo():
    '''returns boolean\n\n
    hasWorkflowInfo()\n
    '''
def getEventQueue():
    '''returns EventQueue\n\n
    getEventQueue()\n
    '''
def queueEvent():
    '''returns None\n\n
    queueEvent(final WebClientEvent event)\n
    '''
def getCurrentPageId():
    '''returns String\n\n
    getCurrentPageId()\n
    '''
def getCurrentPage():
    '''returns PageInstance\n\n
    getCurrentPage()\n
    '''
def getDataBean():
    '''returns DataBean\n\n
    getDataBean(final String beanId)\n
    '''
def checkForDialogAccess():
    '''returns boolean\n\n
    checkForDialogAccess(final String dialogId, final Element dialog)\n
    '''
def findDialog():
    '''returns PageInstance\n\n
    findDialog(final String dialogId)\n
    '''
def getUniqueId():
    '''returns String\n\n
    getUniqueId()\n
    '''
def findDialogInDesignerApps():
    '''returns ControlInstance\n\n
    findDialogInDesignerApps(final String dialogId)\n
    '''
def setLongOpComponent():
    '''returns None\n\n
    setLongOpComponent(final ComponentInstance longOp)\n
    '''
def getLongOpComponent():
    '''returns ComponentInstance\n\n
    getLongOpComponent()\n
    '''
def loadDialog():
    '''returns int\n\n
    loadDialog(String dialogId)\n
    loadDialog(final String dialogId, final boolean showmessages, final String longOpMessage)\n
    '''
def loadDialogInDesignerApps():
    '''returns int\n\n
    loadDialogInDesignerApps(final String dialogId)\n
    '''
def getControlInstance():
    '''returns ControlInstance\n\n
    getControlInstance(final String id)\n
    getControlInstance(final String id, final boolean tableDownload)\n
    '''
def getCurrentApp():
    '''returns AppInstance\n\n
    getCurrentApp()\n
    '''
def getCurrentAppId():
    '''returns String\n\n
    getCurrentAppId()\n
    '''
def getPreviousApp():
    '''returns AppInstance\n\n
    getPreviousApp()\n
    '''
def getMXSession():
    '''returns MXSession\n\n
    getMXSession()\n
    '''
def getHttpSession():
    '''returns HttpSession\n\n
    getHttpSession()\n
    '''
def setHttpSession():
    '''returns None\n\n
    setHttpSession(final HttpSession https)\n
    '''
def pushApp():
    '''returns None\n\n
    pushApp(final AppInstance ai)\n
    '''
def popApp():
    '''returns AppInstance\n\n
    popApp()\n
    '''
def clearStack():
    '''returns None\n\n
    clearStack()\n
    '''
def getAppStack():
    '''returns Stack<AppInstance>\n\n
    getAppStack()\n
    '''
def setCurrentEvent():
    '''returns None\n\n
    setCurrentEvent(final WebClientEvent event)\n
    '''
def getCurrentEvent():
    '''returns WebClientEvent\n\n
    getCurrentEvent()\n
    '''
def getFirstHandledEvent():
    '''returns WebClientEvent\n\n
    getFirstHandledEvent()\n
    '''
def getOriginalEvent():
    '''returns WebClientEvent\n\n
    getOriginalEvent()\n
    '''
def setEventState():
    '''returns None\n\n
    setEventState(final int state)\n
    '''
def getEventState():
    '''returns int\n\n
    getEventState()\n
    '''
def getCurrentEventHandler():
    '''returns ControlInstance\n\n
    getCurrentEventHandler()\n
    '''
def setCurrentEventHandler():
    '''returns None\n\n
    setCurrentEventHandler(final ControlInstance eventHandler)\n
    '''
def setPerfStat():
    '''returns None\n\n
    setPerfStat(final String flag)\n
    '''
def getPerfStat():
    '''returns boolean\n\n
    getPerfStat()\n
    '''
def getRequest():
    '''returns HttpServletRequest\n\n
    getRequest()\n
    '''
def getRequestType():
    '''returns RequestType\n\n
    getRequestType()\n
    '''
def setRequest():
    '''returns None\n\n
    setRequest(final HttpServletRequest request)\n
    '''
def getResponse():
    '''returns HttpServletResponse\n\n
    getResponse()\n
    '''
def setResponse():
    '''returns None\n\n
    setResponse(final HttpServletResponse response)\n
    '''
def createMXSession():
    '''returns MXSession\n\n
    createMXSession()\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def getWarnings():
    '''returns ArrayList<MXException>\n\n
    getWarnings()\n
    '''
def addWarning():
    '''returns None\n\n
    addWarning(final MXException e)\n
    '''
def removeWarnings():
    '''returns List<MXException>\n\n
    removeWarnings()\n
    '''
def addWarnings():
    '''returns None\n\n
    addWarnings(final List<MXException> warningList)\n
    '''
def getLoginEvent():
    '''returns WebClientEvent\n\n
    getLoginEvent()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getAlignment():
    '''returns Alignment\n\n
    getAlignment()\n
    '''
def getHelpLangCode():
    '''returns String\n\n
    getHelpLangCode()\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final String strTimeZone)\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def getUserLanguageCode():
    '''returns String\n\n
    getUserLanguageCode()\n
    '''
def getMaxMessageMboSetRemote():
    '''returns MboSetRemote\n\n
    getMaxMessageMboSetRemote()\n
    '''
def setMaxMessageMboSetRemote():
    '''returns None\n\n
    setMaxMessageMboSetRemote(final MboSetRemote setmboSet)\n
    '''
def getUserApps():
    '''returns Set<String>\n\n
    getUserApps()\n
    '''
def getOriginalApp():
    '''returns String\n\n
    getOriginalApp(final String currentApp)\n
    '''
def getAppDesc():
    '''returns String\n\n
    getAppDesc(String appId)\n
    '''
def getClonedApps():
    '''returns Set<String>\n\n
    getClonedApps(final String originalApp)\n
    '''
def getOriginalApps():
    '''returns Set<String>\n\n
    getOriginalApps(String currentApp)\n
    '''
def getAppMainTable():
    '''returns String\n\n
    getAppMainTable(final String currentApp)\n
    '''
def getSpellSessionAdapter():
    '''returns SpellingSessionAdapter\n\n
    getSpellSessionAdapter()\n
    '''
def setSpellSessionAdapter():
    '''returns None\n\n
    setSpellSessionAdapter(final SpellingSessionAdapter spellSessionAdapter)\n
    '''
def pauseQueue():
    '''returns None\n\n
    pauseQueue()\n
    '''
def isQueuePaused():
    '''returns boolean\n\n
    isQueuePaused()\n
    '''
def unPauseQueue():
    '''returns None\n\n
    unPauseQueue()\n
    '''
def runLongOp():
    '''returns boolean\n\n
    runLongOp(final DataBean dataSrc, final WebClientEvent event)\n
    runLongOp(final DataBean dataSrc, final WebClientEvent event, boolean showMessages, final String longOpMessage)\n
    runLongOp(final DataBean dataSrc, final String method)\n
    runLongOp(final DataBean dataSrc, final String method, boolean showMessages, final String longOpMessage)\n
    '''
def runLongOpQuery():
    '''returns boolean\n\n
    runLongOpQuery(final DataBean dataSrc, final String method, boolean showMessages, final String longOpMessage)\n
    '''
def stopLongOpQuery():
    '''returns None\n\n
    stopLongOpQuery()\n
    '''
def getLongOpStatus():
    '''returns int\n\n
    getLongOpStatus()\n
    '''
def hasLongOpStarted():
    '''returns boolean\n\n
    hasLongOpStarted()\n
    '''
def setLongOpChecked():
    '''returns None\n\n
    setLongOpChecked(final boolean longopChecked)\n
    '''
def hasLongOpCompleted():
    '''returns boolean\n\n
    hasLongOpCompleted()\n
    '''
def hasQueryLongOpCompleted():
    '''returns boolean\n\n
    hasQueryLongOpCompleted()\n
    '''
def getLongOpEvent():
    '''returns WebClientEvent\n\n
    getLongOpEvent()\n
    '''
def getLongOpMethod():
    '''returns String\n\n
    getLongOpMethod()\n
    '''
def finishLongOpEvent():
    '''returns None\n\n
    finishLongOpEvent()\n
    '''
def longOpCleanup():
    '''returns None\n\n
    longOpCleanup()\n
    '''
def longOpQueryCleanup():
    '''returns None\n\n
    longOpQueryCleanup()\n
    '''
def getWorkflowDirector():
    '''returns WorkflowDirector\n\n
    getWorkflowDirector()\n
    '''
def getSettingsProperty():
    '''returns String\n\n
    getSettingsProperty(final String prop)\n
    getSettingsProperty(final String prop, final String[] params)\n
    '''
def getMaxMessage():
    '''returns MaxMessage\n\n
    getMaxMessage(final MXException mxe)\n
    getMaxMessage(final RemoteException e)\n
    getMaxMessage(final String group, final String key)\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final MXException mxe)\n
    getMessage(final String group, final String key)\n
    getMessage(final String group, final String key, final String[] params)\n
    '''
def getMessages():
    '''returns String[]\n\n
    getMessages(final String group, final String[] key)\n
    '''
def getClientSideMessage():
    '''returns String\n\n
    getClientSideMessage(final String group, final String key)\n
    '''
def showMessageBox():
    '''returns None\n\n
    showMessageBox(final WebClientEvent srcEvent, final String title, final String warnings, final int flags)\n
    showMessageBox(final WebClientEvent srcEvent, final String messageFile, final String key, final String[] params)\n
    showMessageBox(final WebClientEvent srcEvent, final String messageFile, final String key, final Object[] params)\n
    showMessageBox(final String messageFile, final String key, final String[] params)\n
    showMessageBox(final WebClientEvent srcEvent, final MXException mxe)\n
    showMessageBox(final WebClientEvent srcEvent, final RemoteException re)\n
    showMessageBox(final MXException mxe)\n
    '''
def generateMessageBoxForTable():
    '''returns None\n\n
    generateMessageBoxForTable(final Hashtable<String, String> messageInfo)\n
    '''
def showEsigLoginDialog():
    '''returns None\n\n
    showEsigLoginDialog(final ESigLoginException srcExcept)\n
    '''
def addMXWarnings():
    '''returns boolean\n\n
    addMXWarnings(final MXException[] warnings)\n
    '''
def handleMXWarnings():
    '''returns boolean\n\n
    handleMXWarnings()\n
    handleMXWarnings(final boolean showMultipleWarningsSeparately)\n
    '''
def setUserInput():
    '''returns None\n\n
    setUserInput(final MXException mxe, final int msgReturn)\n
    '''
def clearUserInput():
    '''returns None\n\n
    clearUserInput()\n
    '''
def showLongopDialog():
    '''returns None\n\n
    showLongopDialog(final String datasrc)\n
    '''
def gotoApplink():
    '''returns None\n\n
    gotoApplink(String url)\n
    '''
def handleDialogOK():
    '''returns boolean\n\n
    handleDialogOK(final boolean advancedLongOp)\n
    handleDialogOK(final boolean advancedLongOp, final String longOpMessage)\n
    '''
def findControl():
    '''returns ControlInstance\n\n
    findControl(final String controlId)\n
    '''
def processProfiles():
    '''returns int\n\n
    processProfiles(final String profileName)\n
    '''
def clearModuleMap():
    '''returns None\n\n
    clearModuleMap()\n
    '''
def getSystemProperty():
    '''returns String[]\n\n
    getSystemProperty(final String propertyName)\n
    '''
def isPermanentLicense():
    '''returns boolean\n\n
    isPermanentLicense()\n
    '''
def getEvalDaysRemaining():
    '''returns String\n\n
    getEvalDaysRemaining()\n
    '''
def invalidate():
    '''returns None\n\n
    invalidate()\n
    '''
def useLeftContextInterval():
    '''returns None\n\n
    useLeftContextInterval(final boolean use)\n
    '''
def usingContextInterval():
    '''returns boolean\n\n
    usingContextInterval()\n
    '''
def hasTimedOut():
    '''returns boolean\n\n
    hasTimedOut()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def getRequestParameter():
    '''returns String\n\n
    getRequestParameter(final String key)\n
    '''
def setLightningPortalMode():
    '''returns None\n\n
    setLightningPortalMode(final boolean portalmode)\n
    '''
def setPortalMode():
    '''returns None\n\n
    setPortalMode(final boolean portalmode)\n
    '''
def getLightningPortalMode():
    '''returns boolean\n\n
    getLightningPortalMode()\n
    '''
def getPortalMode():
    '''returns boolean\n\n
    getPortalMode()\n
    '''
def setTipPortalMode():
    '''returns None\n\n
    setTipPortalMode(final boolean tipportalmode)\n
    '''
def getTipPortalMode():
    '''returns boolean\n\n
    getTipPortalMode()\n
    '''
def getDesignModeWebClientSession():
    '''returns WebClientSession\n\n
    getDesignModeWebClientSession()\n
    '''
def hasDesignModeWebClientSession():
    '''returns boolean\n\n
    hasDesignModeWebClientSession()\n
    '''
def setDesignModeWebClientSession():
    '''returns None\n\n
    setDesignModeWebClientSession(final WebClientSession wcs)\n
    '''
def setOriginalSession():
    '''returns None\n\n
    setOriginalSession(final WebClientSession wcs)\n
    '''
def getOriginalSession():
    '''returns WebClientSession\n\n
    getOriginalSession()\n
    '''
def getContextPath():
    '''returns String\n\n
    getContextPath()\n
    '''
def setDesignmode():
    '''returns None\n\n
    setDesignmode(final boolean flag)\n
    '''
def getDesignmode():
    '''returns boolean\n\n
    getDesignmode()\n
    '''
def getMobile():
    '''returns boolean\n\n
    getMobile()\n
    '''
def setMobile():
    '''returns None\n\n
    setMobile(final boolean setValue)\n
    '''
def setLockMboOnEntry():
    '''returns None\n\n
    setLockMboOnEntry(final boolean checkrecordlock)\n
    '''
def lockMboOnEntry():
    '''returns boolean\n\n
    lockMboOnEntry()\n
    '''
def setPerformanceDataHASH():
    '''returns None\n\n
    setPerformanceDataHASH(final String keyName, final String value)\n
    setPerformanceDataHASH(final String keyName, long sInputValue)\n
    '''
def clearPerformanceDataHASH():
    '''returns None\n\n
    clearPerformanceDataHASH(final String appname)\n
    '''
def clearAllTracking():
    '''returns None\n\n
    clearAllTracking()\n
    '''
def getUISessionID():
    '''returns String\n\n
    getUISessionID()\n
    '''
def getUISessionUrlParameter():
    '''returns String\n\n
    getUISessionUrlParameter()\n
    '''
def setUISessionID():
    '''returns None\n\n
    setUISessionID(final String uiSessionID)\n
    '''
def setSessionFound():
    '''returns None\n\n
    setSessionFound(final boolean flag)\n
    '''
def isSessionFound():
    '''returns boolean\n\n
    isSessionFound()\n
    '''
def valueBound():
    '''returns None\n\n
    valueBound(final HttpSessionBindingEvent arg0)\n
    '''
def valueUnbound():
    '''returns None\n\n
    valueUnbound(final HttpSessionBindingEvent arg0)\n
    '''
def isWebReplayEnabled():
    '''returns boolean\n\n
    isWebReplayEnabled()\n
    '''
def setShowWebReplay():
    '''returns None\n\n
    setShowWebReplay(final boolean show)\n
    '''
def getShowWebReplay():
    '''returns boolean\n\n
    getShowWebReplay()\n
    '''
def showWebReplay():
    '''returns boolean\n\n
    showWebReplay(final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def hideWebReplay():
    '''returns None\n\n
    hideWebReplay(final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def getDebug():
    '''returns boolean\n\n
    getDebug()\n
    '''
def getDebugLevel():
    '''returns int\n\n
    getDebugLevel()\n
    '''
def getEventLog():
    '''returns String\n\n
    getEventLog()\n
    '''
def setDebugDock():
    '''returns None\n\n
    setDebugDock(final String left, final String top)\n
    '''
def setAccessibilityMode():
    '''returns None\n\n
    setAccessibilityMode(final boolean mode)\n
    '''
def getAccessibilityMode():
    '''returns boolean\n\n
    getAccessibilityMode()\n
    '''
def getSystemEventHandler():
    '''returns EventHandlerInterface\n\n
    getSystemEventHandler()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def getImagePath():
    '''returns String\n\n
    getImagePath()\n
    '''
def getCssPath():
    '''returns String\n\n
    getCssPath()\n
    '''
def getWebClientURL():
    '''returns String\n\n
    getWebClientURL()\n
    '''
def getImageURL():
    '''returns String\n\n
    getImageURL()\n
    '''
def getCssURL():
    '''returns String\n\n
    getCssURL()\n
    '''
def setImagePath():
    '''returns None\n\n
    setImagePath(final String path)\n
    '''
def setCssPath():
    '''returns None\n\n
    setCssPath(final String path)\n
    '''
def isCombinedSetValue():
    '''returns boolean\n\n
    isCombinedSetValue()\n
    '''
def subFrameAllowed():
    '''returns boolean\n\n
    subFrameAllowed()\n
    '''
def forceMessagesToMainPage():
    '''returns None\n\n
    forceMessagesToMainPage(final boolean forceMain)\n
    '''
def getForceMessagesToMainPage():
    '''returns boolean\n\n
    getForceMessagesToMainPage()\n
    '''
def setAdvancedLongOp():
    '''returns None\n\n
    setAdvancedLongOp(final boolean advanced)\n
    '''
def isAutomationOn():
    '''returns boolean\n\n
    isAutomationOn()\n
    '''
def turnAutomationOn():
    '''returns None\n\n
    turnAutomationOn()\n
    '''
def replaceQbeclearButton():
    '''returns Element\n\n
    replaceQbeclearButton(final Element dialogElement)\n
    '''
def addMoreinfoButton():
    '''returns Element\n\n
    addMoreinfoButton(final Element dialogElement, final String value)\n
    '''
def isMaximoOrTivoliBrand():
    '''returns boolean\n\n
    isMaximoOrTivoliBrand()\n
    '''
def killPopup():
    '''returns None\n\n
    killPopup(final boolean killIt)\n
    killPopup(final WebClientEvent event)\n
    '''
def wasPopupKilled():
    '''returns boolean\n\n
    wasPopupKilled()\n
    '''
def getMaximoRequestURI():
    '''returns String\n\n
    getMaximoRequestURI()\n
    '''
def getMaximoRequestURL():
    '''returns String\n\n
    getMaximoRequestURL()\n
    '''
def getMaximoRequestContextURL():
    '''returns String\n\n
    getMaximoRequestContextURL()\n
    '''
def getMaximoBaseURL():
    '''returns String\n\n
    getMaximoBaseURL()\n
    '''
def getDefautlFormat():
    '''returns String\n\n
    getDefautlFormat()\n
    '''
def setDefautlFormat():
    '''returns None\n\n
    setDefautlFormat(final String defaultFormat)\n
    '''
def wereImagesPreLoaded():
    '''returns boolean\n\n
    wereImagesPreLoaded()\n
    '''
def setImagesPreLoaded():
    '''returns None\n\n
    setImagesPreLoaded(final boolean pre)\n
    '''
def lastAccessed():
    '''returns Date\n\n
    lastAccessed()\n
    '''
def stamp():
    '''returns None\n\n
    stamp()\n
    '''
def getFactoryId():
    '''returns String\n\n
    getFactoryId()\n
    '''
def getStartCenterCache():
    '''returns Object\n\n
    getStartCenterCache(final String key)\n
    '''
def setStartCenterCache():
    '''returns None\n\n
    setStartCenterCache(final String key, final Object obj)\n
    '''
def resetStartCenterCache():
    '''returns None\n\n
    resetStartCenterCache()\n
    '''
def resetPortletCaches():
    '''returns None\n\n
    resetPortletCaches()\n
    '''
def clearPortletCacheSelectively():
    '''returns None\n\n
    clearPortletCacheSelectively(final String prefix)\n
    '''
def clearPortletCacheOnKPIChange():
    '''returns None\n\n
    clearPortletCacheOnKPIChange(final String kpiName)\n
    '''
def clearPortletCacheOnReportChange():
    '''returns None\n\n
    clearPortletCacheOnReportChange(final String reportId)\n
    '''
def clearStartCenterCache():
    '''returns None\n\n
    clearStartCenterCache(final String key)\n
    '''
def hasStartCenterCache():
    '''returns boolean\n\n
    hasStartCenterCache(final String key)\n
    '''
def isAsyncEnabled():
    '''returns boolean\n\n
    isAsyncEnabled()\n
    '''
def getAsyncRequestManager():
    '''returns AsyncRequestManager\n\n
    getAsyncRequestManager()\n
    '''
def performApplink():
    '''returns None\n\n
    performApplink(final boolean canApplink)\n
    '''
def canPerformApplink():
    '''returns boolean\n\n
    canPerformApplink()\n
    '''
def processRender():
    '''returns None\n\n
    processRender()\n
    '''
def getDebugDockLeft():
    '''returns int\n\n
    getDebugDockLeft()\n
    '''
def getDebugDockTop():
    '''returns int\n\n
    getDebugDockTop()\n
    '''
def getIEVersion():
    '''returns double\n\n
    getIEVersion()\n
    '''
def setInFrameset():
    '''returns None\n\n
    setInFrameset(final boolean isInFrameset)\n
    '''
def isInFrameset():
    '''returns boolean\n\n
    isInFrameset()\n
    '''
def canUseStaticIds():
    '''returns boolean\n\n
    canUseStaticIds()\n
    '''
def getImageSourcePath():
    '''returns String\n\n
    getImageSourcePath()\n
    '''
def getDialogIcon():
    '''returns String\n\n
    getDialogIcon(final String suffix)\n
    '''
def getWarningInfo():
    '''returns ContainerErrorInfo\n\n
    getWarningInfo()\n
    '''
def getSmartFillExceptionInfo():
    '''returns ContainerErrorInfo\n\n
    getSmartFillExceptionInfo()\n
    '''
def getExceptionInfo():
    '''returns ContainerErrorInfo\n\n
    getExceptionInfo()\n
    '''
def getQuestionInfo():
    '''returns ContainerErrorInfo\n\n
    getQuestionInfo()\n
    '''
def getContainerErrorIconJSON():
    '''returns JSONObject\n\n
    getContainerErrorIconJSON()\n
    '''
def getConditionalUIHelper():
    '''returns ConditionalUIHelper\n\n
    getConditionalUIHelper()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getDefaultStartApp():
    '''returns String\n\n
    getDefaultStartApp()\n
    '''
def getRegexPattern():
    '''returns String\n\n
    getRegexPattern(final int dataType)\n
    '''
def setMenusCached():
    '''returns None\n\n
    setMenusCached(final boolean cached)\n
    '''
def getMenusCached():
    '''returns boolean\n\n
    getMenusCached()\n
    '''
def hasPausedEvents():
    '''returns boolean\n\n
    hasPausedEvents()\n
    '''
def getDesignerAsyncRequestManager():
    '''returns AsyncRequestManager\n\n
    getDesignerAsyncRequestManager()\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String attributeName, final Object value)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String attributeName)\n
    '''
def attachUOM():
    '''returns String\n\n
    attachUOM(String size)\n
    '''
def removeUOM():
    '''returns String\n\n
    removeUOM(String size)\n
    '''
def useVerticalLabels():
    '''returns boolean\n\n
    useVerticalLabels()\n
    '''
def generateOneTimeCSRFTokenParameter():
    '''returns String\n\n
    generateOneTimeCSRFTokenParameter()\n
    '''
def generateRetryCSRFTokenParameter():
    '''returns String\n\n
    generateRetryCSRFTokenParameter()\n
    '''
def isTempTokenValid():
    '''returns boolean\n\n
    isTempTokenValid(final String oneTimeToken)\n
    '''
def getCSRFToken():
    '''returns String\n\n
    getCSRFToken()\n
    '''
def getCSRFTokenParameter():
    '''returns String\n\n
    getCSRFTokenParameter()\n
    '''
def showSystemNavBar():
    '''returns boolean\n\n
    showSystemNavBar(final PageInstance page)\n
    '''
def getFeaturePack():
    '''returns String\n\n
    getFeaturePack()\n
    '''
def supportsLocalStorage():
    '''returns boolean\n\n
    supportsLocalStorage()\n
    '''
def setLeftNavWidth():
    '''returns None\n\n
    setLeftNavWidth(final String width)\n
    '''
def getLeftNavWidth():
    '''returns String\n\n
    getLeftNavWidth(final PageInstance page)\n
    '''
def reverse():
    '''returns String\n\n
    reverse(final String align)\n
    '''
