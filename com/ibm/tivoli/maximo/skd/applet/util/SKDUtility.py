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
    '''    public SKDViewerApplet getApplet()
    '''
def setApplet():
    '''    public void setApplet(final SKDViewerApplet applet)
    '''
def setDefaultscenario():
    '''    public void setDefaultscenario(final boolean defaultscenario)
    '''
def getDefaultscenario():
    '''    public boolean getDefaultscenario()
    '''
def setSnapshot():
    '''    public void setSnapshot(final boolean snapshot)
    '''
def getSnapshot():
    '''    public boolean getSnapshot()
    '''
def setDailyView():
    '''    public void setDailyView(final boolean dailyview)
    '''
def getDailyView():
    '''    public boolean getDailyView()
    '''
def getMessages():
    '''    public SKDAppletMessages getMessages()
    '''
def getGanttConfigInfo():
    '''    public IGanttConfigInfo getGanttConfigInfo()
    '''
def setGanttConfigInfo():
    '''    public void setGanttConfigInfo(final IGanttConfigInfo ganttConfigInfo)
    '''
def setSkdActionInfo():
    '''    public void setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)
    '''
def getSkdActionInfo():
    '''    public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo()
    '''
def setSkdActionUidInfo():
    '''    public void setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)
    '''
def getSkdActionUidInfo():
    '''    public HashMap<Long, SKDActionInfo> getSkdActionUidInfo()
    '''
def getSKDFormat():
    '''    public SKDFormat getSKDFormat()
    '''
def setDateFormat():
    '''    public void setDateFormat(final DateFormat dateFormat)
    '''
def getUserLocale():
    '''    public Locale getUserLocale()
    '''
def getUserTimeZone():
    '''    public TimeZone getUserTimeZone()
    '''
def getServerTimeZone():
    '''    public TimeZone getServerTimeZone()
    '''
def getSKDUtility():
    '''    public static synchronized SKDUtility getSKDUtility()
    '''
def reset():
    '''    public static synchronized void reset()
    '''
def SKDUtility():
    '''    public SKDUtility()
    '''
def isDebugMode():
    '''    public boolean isDebugMode()
    '''
def setDebugMode():
    '''    public void setDebugMode(final boolean debugMode)
    '''
def logMessage():
    '''    public void logMessage(final String message, final Throwable t)
    '''
def logDebugMessage():
    '''    public void logDebugMessage(final Object o)
    public void logDebugMessage(final String message, final Throwable t)
    '''
def sendEventAsync():
    '''    public void sendEventAsync(final String event)
    public void sendEventAsync(final String event, final Hashtable<String, String> values)
    public void sendEventAsync(final String event, final String target, final Hashtable<String, String> values)
    '''
def sendEvent():
    '''    public void sendEvent(final String event)
    public void sendEvent(final String event, final Hashtable<String, String> values)
    public void sendEvent(final String event, final String target, final Hashtable<String, String> values)
    '''
def evalJSResult():
    '''    public Object evalJSResult(final JApplet applet, final String cmdString)
    '''
def isFirefox():
    '''    public boolean isFirefox(final JApplet applet)
    '''
def callJavascriptEval():
    '''    public void callJavascriptEval(final String eval)
    '''
def run():
    '''    public void run()
    public Void run()
    '''
def getMessage():
    '''    public String getMessage(final String msgkey)
    '''
def getSKDUserLocaleData():
    '''    public SKDUserLocaleData getSKDUserLocaleData()
    '''
def getMessageWithPrefix():
    '''    public String getMessageWithPrefix(final String msgkey)
    '''
def setSKDUserLocaleData():
    '''    public void setSKDUserLocaleData()
    '''
def getResourceString():
    '''    public String getResourceString(final String key)
    '''
def getResourceStrings():
    '''    public Hashtable getResourceStrings()
    '''
def getDateFormat():
    '''    public DateFormat getDateFormat(final int propDataType)
    '''
def getAppletName():
    '''    public String getAppletName()
    '''
def getConstraintType():
    '''    public IlvConstraintType getConstraintType(final String num)
    '''
def getConstraintTypeInt():
    '''    public Integer getConstraintTypeInt(final IlvConstraintType type)
    '''
def getViewerProperty():
    '''    public String getViewerProperty(final String prop, final String defaultValue)
    '''
def setViewerProperty():
    '''    public void setViewerProperty(final String key, final String value)
    '''
def decodeColor():
    '''    public Color decodeColor(final String hexValue)
    '''
def getStatusColors():
    '''    public Color[] getStatusColors(String status, String groupname)
    '''
def canShowCurrentTimeIndicatorOnDrag():
    '''    public boolean canShowCurrentTimeIndicatorOnDrag()
    '''
def getSnapToGridIntervalMins():
    '''    public int getSnapToGridIntervalMins()
    '''
def getDefaultRowHeight():
    '''    public int getDefaultRowHeight()
    '''
def getPriorityColors():
    '''    public Color[] getPriorityColors(String priority, String groupname)
    '''
def usingStatusColors():
    '''    public boolean usingStatusColors()
    '''
def hidingYAxis():
    '''    public boolean hidingYAxis()
    '''
def hidingLegend():
    '''    public boolean hidingLegend()
    '''
def IlvDurationToDouble():
    '''    public double IlvDurationToDouble(final IlvDuration lv)
    '''
def enforceOrientation():
    '''    public void enforceOrientation(final JComponent comp)
    '''
def enforceBIDIColumnLayout():
    '''    public void enforceBIDIColumnLayout(final JTable table)
    '''
def isGUIMirrored():
    '''    public boolean isGUIMirrored()
    '''
def enforceBidiDirection():
    '''    public String enforceBidiDirection(String str, final String bidiDirection)
    '''
def removeMarkersForApplink():
    '''    public static String removeMarkersForApplink(final String str)
    '''
def setGUIMirrored():
    '''    public void setGUIMirrored(final String langcode)
    '''
def isBIDIEnabled():
    '''    public boolean isBIDIEnabled()
    '''
def setBIDIEnabled():
    '''    public void setBIDIEnabled(final String value)
    '''
def replaceString():
    '''    public static String replaceString(String str, final String pattern, final String replacement)
    '''
def makeTooltipStringBasedOnDirection():
    '''    public String makeTooltipStringBasedOnDirection(final String direction, final String value, final String property)
    public String makeTooltipStringBasedOnDirection(final String direction, final String value)
    '''
def removeMarkers():
    '''    public static String removeMarkers(final String str)
    '''
def isBiDiString():
    '''    public static boolean isBiDiString(final String str)
    '''
def fireEscapeKeyDown():
    '''    public void fireEscapeKeyDown()
    '''
def todaysDate():
    '''    public Date todaysDate()
    '''
def getServerDate():
    '''    public Date getServerDate(Date oldDate)
    '''
def getServerDateForUser():
    '''    public Date getServerDateForUser(Date serverDate)
    '''
def getDate():
    '''    public Date getDate(final Locale l, final TimeZone tz, final Date date)
    '''
def getFixedTimeIndicatorFromGSheet():
    '''    public IlvFixedTimeIndicator getFixedTimeIndicatorFromGSheet(final IlvGanttSheet gsheet)
    '''
def areServerAndUserTZDifferent():
    '''    public boolean areServerAndUserTZDifferent()
    '''
def removeTimeIndicator():
    '''    public void removeTimeIndicator(final IlvGanttSheet gSheet)
    '''
def refreshActivityTable():
    '''    public void refreshActivityTable()
    '''
def getAppName():
    '''    public String getAppName()
    '''
def isAssignmentManager():
    '''    public boolean isAssignmentManager()
    '''
def setupSnapToGrid():
    '''    public void setupSnapToGrid(final IlvGanttSheet ganttSheet)
    '''
def keyPressed():
    '''    public void keyPressed(final KeyEvent e)
    '''
def keyReleased():
    '''    public void keyReleased(final KeyEvent e)
    '''
def getToolTipPropertyMaxWidth():
    '''    public int getToolTipPropertyMaxWidth()
    '''
def getModifiedLabelColorString():
    '''    public String getModifiedLabelColorString()
    '''
def getModifiedLabelPrefix():
    '''    public String getModifiedLabelPrefix()
    '''
def isComplianceEnabled():
    '''    public boolean isComplianceEnabled()
    '''
def setComplianceEnabled():
    '''    public void setComplianceEnabled(final boolean complianceEnabled)
    '''
def needSendModelChange():
    '''    public boolean needSendModelChange()
    '''
def setSendModelchange():
    '''    public void setSendModelchange(final boolean sendModelchange)
    '''
def sendToBeSaved():
    '''    public boolean sendToBeSaved()
    '''
def setToBeSaved():
    '''    public void setToBeSaved(final boolean sendtobesaved)
    '''
def getColorProperty():
    '''    public Color getColorProperty(final String propName, Color defaultColor)
    '''
def isUsingCompressedData():
    '''    public boolean isUsingCompressedData()
    '''
def getLegendColors():
    '''    public static IlvStyle[] getLegendColors()
    '''
def getLegendColorsforResourceHourView():
    '''    public static IlvStyle[] getLegendColorsforResourceHourView()
    '''
def getBooleanProperty():
    '''    public boolean getBooleanProperty(final String propName, final boolean defVal)
    '''
def getLongProperty():
    '''    public long getLongProperty(final String propName, final long defVal)
    '''
def getIntProperty():
    '''    public int getIntProperty(final String propName, final int defVal)
    '''
def setUserOverrideProperties():
    '''    public void setUserOverrideProperties(final Properties props)
    '''
def isEmpty():
    '''    public static boolean isEmpty(final String text)
    '''
def enableHttpOnlyWorkaroundIfNeeded():
    '''    public void enableHttpOnlyWorkaroundIfNeeded(final JApplet applet)
    '''
def setDefaultUserTimeZone():
    '''    public boolean setDefaultUserTimeZone(final String userTimeZoneId)
    '''
def getReservationLiveUpdateThreshold():
    '''    public long getReservationLiveUpdateThreshold()
    '''
def hideDurationCheckEnabled():
    '''    public boolean hideDurationCheckEnabled()
    '''
