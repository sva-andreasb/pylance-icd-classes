VIEWER_SCHEDULER = "String  \"SKDViewer\""
VIEWER_GRPASSIGN = "String  \"ASNViewer\""
VIEWER_CREWASSIGN = "String  \"CASNViewer\""
NONE = "String  \"\""
LRE = "String  \"\u202a\""
RLE = "String  \"\u202b\""
PDF = "String  \"\u202c\""
LRM = "String  \"\u200e\""
RLM = "String  \"\u200f\""
def getApplet():
    '''returns SKDViewerApplet\n\n
    getApplet()\n
    '''
def setApplet():
    '''returns None\n\n
    setApplet(final SKDViewerApplet applet)\n
    '''
def setDefaultscenario():
    '''returns None\n\n
    setDefaultscenario(final boolean defaultscenario)\n
    '''
def getDefaultscenario():
    '''returns boolean\n\n
    getDefaultscenario()\n
    '''
def setSnapshot():
    '''returns None\n\n
    setSnapshot(final boolean snapshot)\n
    '''
def getSnapshot():
    '''returns boolean\n\n
    getSnapshot()\n
    '''
def setDailyView():
    '''returns None\n\n
    setDailyView(final boolean dailyview)\n
    '''
def getDailyView():
    '''returns boolean\n\n
    getDailyView()\n
    '''
def getMessages():
    '''returns SKDAppletMessages\n\n
    getMessages()\n
    '''
def getGanttConfigInfo():
    '''returns IGanttConfigInfo\n\n
    getGanttConfigInfo()\n
    '''
def setGanttConfigInfo():
    '''returns None\n\n
    setGanttConfigInfo(final IGanttConfigInfo ganttConfigInfo)\n
    '''
def setSkdActionInfo():
    '''returns None\n\n
    setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)\n
    '''
def setSkdActionUidInfo():
    '''returns None\n\n
    setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)\n
    '''
def getSKDFormat():
    '''returns SKDFormat\n\n
    getSKDFormat()\n
    '''
def setDateFormat():
    '''returns None\n\n
    setDateFormat(final DateFormat dateFormat)\n
    '''
def getUserLocale():
    '''returns Locale\n\n
    getUserLocale()\n
    '''
def getUserTimeZone():
    '''returns TimeZone\n\n
    getUserTimeZone()\n
    '''
def getServerTimeZone():
    '''returns TimeZone\n\n
    getServerTimeZone()\n
    '''
def ():
    '''returns SKDUtility\n\n
    ()\n
    '''
def isDebugMode():
    '''returns boolean\n\n
    isDebugMode()\n
    '''
def setDebugMode():
    '''returns None\n\n
    setDebugMode(final boolean debugMode)\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final String message, final Throwable t)\n
    '''
def logDebugMessage():
    '''returns None\n\n
    logDebugMessage(final Object o)\n
    logDebugMessage(final String message, final Throwable t)\n
    '''
def sendEventAsync():
    '''returns None\n\n
    sendEventAsync(final String event)\n
    sendEventAsync(final String event, final Hashtable<String, String> values)\n
    sendEventAsync(final String event, final String target, final Hashtable<String, String> values)\n
    '''
def sendEvent():
    '''returns None\n\n
    sendEvent(final String event)\n
    sendEvent(final String event, final Hashtable<String, String> values)\n
    sendEvent(final String event, final String target, final Hashtable<String, String> values)\n
    '''
def evalJSResult():
    '''returns Object\n\n
    evalJSResult(final JApplet applet, final String cmdString)\n
    '''
def isFirefox():
    '''returns boolean\n\n
    isFirefox(final JApplet applet)\n
    '''
def callJavascriptEval():
    '''returns None\n\n
    callJavascriptEval(final String eval)\n
    '''
def run():
    '''returns Void\n\n
    run()\n
    run()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final String msgkey)\n
    '''
def getSKDUserLocaleData():
    '''returns SKDUserLocaleData\n\n
    getSKDUserLocaleData()\n
    '''
def getMessageWithPrefix():
    '''returns String\n\n
    getMessageWithPrefix(final String msgkey)\n
    '''
def setSKDUserLocaleData():
    '''returns None\n\n
    setSKDUserLocaleData()\n
    '''
def getResourceString():
    '''returns String\n\n
    getResourceString(final String key)\n
    '''
def getResourceStrings():
    '''returns Hashtable\n\n
    getResourceStrings()\n
    '''
def getDateFormat():
    '''returns DateFormat\n\n
    getDateFormat(final int propDataType)\n
    '''
def getAppletName():
    '''returns String\n\n
    getAppletName()\n
    '''
def getConstraintType():
    '''returns IlvConstraintType\n\n
    getConstraintType(final String num)\n
    '''
def getConstraintTypeInt():
    '''returns Integer\n\n
    getConstraintTypeInt(final IlvConstraintType type)\n
    '''
def getViewerProperty():
    '''returns String\n\n
    getViewerProperty(final String prop, final String defaultValue)\n
    '''
def setViewerProperty():
    '''returns None\n\n
    setViewerProperty(final String key, final String value)\n
    '''
def decodeColor():
    '''returns Color\n\n
    decodeColor(final String hexValue)\n
    '''
def getStatusColors():
    '''returns Color[]\n\n
    getStatusColors(String status, String groupname)\n
    '''
def canShowCurrentTimeIndicatorOnDrag():
    '''returns boolean\n\n
    canShowCurrentTimeIndicatorOnDrag()\n
    '''
def getSnapToGridIntervalMins():
    '''returns int\n\n
    getSnapToGridIntervalMins()\n
    '''
def getDefaultRowHeight():
    '''returns int\n\n
    getDefaultRowHeight()\n
    '''
def getPriorityColors():
    '''returns Color[]\n\n
    getPriorityColors(String priority, String groupname)\n
    '''
def usingStatusColors():
    '''returns boolean\n\n
    usingStatusColors()\n
    '''
def hidingYAxis():
    '''returns boolean\n\n
    hidingYAxis()\n
    '''
def hidingLegend():
    '''returns boolean\n\n
    hidingLegend()\n
    '''
def IlvDurationToDouble():
    '''returns double\n\n
    IlvDurationToDouble(final IlvDuration lv)\n
    '''
def enforceOrientation():
    '''returns None\n\n
    enforceOrientation(final JComponent comp)\n
    '''
def enforceBIDIColumnLayout():
    '''returns None\n\n
    enforceBIDIColumnLayout(final JTable table)\n
    '''
def isGUIMirrored():
    '''returns boolean\n\n
    isGUIMirrored()\n
    '''
def enforceBidiDirection():
    '''returns String\n\n
    enforceBidiDirection(String str, final String bidiDirection)\n
    '''
def setGUIMirrored():
    '''returns None\n\n
    setGUIMirrored(final String langcode)\n
    '''
def isBIDIEnabled():
    '''returns boolean\n\n
    isBIDIEnabled()\n
    '''
def setBIDIEnabled():
    '''returns None\n\n
    setBIDIEnabled(final String value)\n
    '''
def makeTooltipStringBasedOnDirection():
    '''returns String\n\n
    makeTooltipStringBasedOnDirection(final String direction, final String value, final String property)\n
    makeTooltipStringBasedOnDirection(final String direction, final String value)\n
    '''
def fireEscapeKeyDown():
    '''returns None\n\n
    fireEscapeKeyDown()\n
    '''
def todaysDate():
    '''returns Date\n\n
    todaysDate()\n
    '''
def getServerDate():
    '''returns Date\n\n
    getServerDate(Date oldDate)\n
    '''
def getServerDateForUser():
    '''returns Date\n\n
    getServerDateForUser(Date serverDate)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final Locale l, final TimeZone tz, final Date date)\n
    '''
def getFixedTimeIndicatorFromGSheet():
    '''returns IlvFixedTimeIndicator\n\n
    getFixedTimeIndicatorFromGSheet(final IlvGanttSheet gsheet)\n
    '''
def areServerAndUserTZDifferent():
    '''returns boolean\n\n
    areServerAndUserTZDifferent()\n
    '''
def removeTimeIndicator():
    '''returns None\n\n
    removeTimeIndicator(final IlvGanttSheet gSheet)\n
    '''
def refreshActivityTable():
    '''returns None\n\n
    refreshActivityTable()\n
    '''
def getAppName():
    '''returns String\n\n
    getAppName()\n
    '''
def isAssignmentManager():
    '''returns boolean\n\n
    isAssignmentManager()\n
    '''
def setupSnapToGrid():
    '''returns None\n\n
    setupSnapToGrid(final IlvGanttSheet ganttSheet)\n
    '''
def keyPressed():
    '''returns None\n\n
    keyPressed(final KeyEvent e)\n
    '''
def keyReleased():
    '''returns None\n\n
    keyReleased(final KeyEvent e)\n
    '''
def getToolTipPropertyMaxWidth():
    '''returns int\n\n
    getToolTipPropertyMaxWidth()\n
    '''
def getModifiedLabelColorString():
    '''returns String\n\n
    getModifiedLabelColorString()\n
    '''
def getModifiedLabelPrefix():
    '''returns String\n\n
    getModifiedLabelPrefix()\n
    '''
def isComplianceEnabled():
    '''returns boolean\n\n
    isComplianceEnabled()\n
    '''
def setComplianceEnabled():
    '''returns None\n\n
    setComplianceEnabled(final boolean complianceEnabled)\n
    '''
def needSendModelChange():
    '''returns boolean\n\n
    needSendModelChange()\n
    '''
def setSendModelchange():
    '''returns None\n\n
    setSendModelchange(final boolean sendModelchange)\n
    '''
def sendToBeSaved():
    '''returns boolean\n\n
    sendToBeSaved()\n
    '''
def setToBeSaved():
    '''returns None\n\n
    setToBeSaved(final boolean sendtobesaved)\n
    '''
def getColorProperty():
    '''returns Color\n\n
    getColorProperty(final String propName, Color defaultColor)\n
    '''
def isUsingCompressedData():
    '''returns boolean\n\n
    isUsingCompressedData()\n
    '''
def getBooleanProperty():
    '''returns boolean\n\n
    getBooleanProperty(final String propName, final boolean defVal)\n
    '''
def getLongProperty():
    '''returns long\n\n
    getLongProperty(final String propName, final long defVal)\n
    '''
def getIntProperty():
    '''returns int\n\n
    getIntProperty(final String propName, final int defVal)\n
    '''
def setUserOverrideProperties():
    '''returns None\n\n
    setUserOverrideProperties(final Properties props)\n
    '''
def enableHttpOnlyWorkaroundIfNeeded():
    '''returns None\n\n
    enableHttpOnlyWorkaroundIfNeeded(final JApplet applet)\n
    '''
def setDefaultUserTimeZone():
    '''returns boolean\n\n
    setDefaultUserTimeZone(final String userTimeZoneId)\n
    '''
def getReservationLiveUpdateThreshold():
    '''returns long\n\n
    getReservationLiveUpdateThreshold()\n
    '''
def hideDurationCheckEnabled():
    '''returns boolean\n\n
    hideDurationCheckEnabled()\n
    '''
