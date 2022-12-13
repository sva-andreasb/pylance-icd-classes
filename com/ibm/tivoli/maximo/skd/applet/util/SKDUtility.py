VIEWER_SCHEDULER = "String  SKDViewer""
VIEWER_GRPASSIGN = "String  ASNViewer""
VIEWER_CREWASSIGN = "String  CASNViewer""
NONE = "String  "
LRE = "String  \u202a""
RLE = "String  \u202b""
PDF = "String  \u202c""
LRM = "String  \u200e""
RLM = "String  \u200f""
def getApplet():
'''public SKDViewerApplet getApplet()
'''
pass
def setApplet():
'''public void setApplet(final SKDViewerApplet applet)
'''
pass
def setDefaultscenario():
'''public void setDefaultscenario(final boolean defaultscenario)
'''
pass
def getDefaultscenario():
'''public boolean getDefaultscenario()
'''
pass
def setSnapshot():
'''public void setSnapshot(final boolean snapshot)
'''
pass
def getSnapshot():
'''public boolean getSnapshot()
'''
pass
def setDailyView():
'''public void setDailyView(final boolean dailyview)
'''
pass
def getDailyView():
'''public boolean getDailyView()
'''
pass
def getMessages():
'''public SKDAppletMessages getMessages()
'''
pass
def getGanttConfigInfo():
'''public IGanttConfigInfo getGanttConfigInfo()
'''
pass
def setGanttConfigInfo():
'''public void setGanttConfigInfo(final IGanttConfigInfo ganttConfigInfo)
'''
pass
def setSkdActionInfo():
'''public void setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)
'''
pass
def getSkdActionInfo():
'''public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo()
'''
pass
def setSkdActionUidInfo():
'''public void setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)
'''
pass
def getSkdActionUidInfo():
'''public HashMap<Long, SKDActionInfo> getSkdActionUidInfo()
'''
pass
def getSKDFormat():
'''public SKDFormat getSKDFormat()
'''
pass
def setDateFormat():
'''public void setDateFormat(final DateFormat dateFormat)
'''
pass
def getUserLocale():
'''public Locale getUserLocale()
'''
pass
def getUserTimeZone():
'''public TimeZone getUserTimeZone()
'''
pass
def getServerTimeZone():
'''public TimeZone getServerTimeZone()
'''
pass
def getSKDUtility():
'''public static synchronized SKDUtility getSKDUtility()
'''
pass
def reset():
'''public static synchronized void reset()
'''
pass
def SKDUtility():
'''public SKDUtility()
'''
pass
def isDebugMode():
'''public boolean isDebugMode()
'''
pass
def setDebugMode():
'''public void setDebugMode(final boolean debugMode)
'''
pass
def logMessage():
'''public void logMessage(final String message, final Throwable t)
'''
pass
def logDebugMessage():
'''public void logDebugMessage(final Object o)
public void logDebugMessage(final String message, final Throwable t)
'''
pass
def sendEventAsync():
'''public void sendEventAsync(final String event)
public void sendEventAsync(final String event, final Hashtable<String, String> values)
public void sendEventAsync(final String event, final String target, final Hashtable<String, String> values)
'''
pass
def sendEvent():
'''public void sendEvent(final String event)
public void sendEvent(final String event, final Hashtable<String, String> values)
public void sendEvent(final String event, final String target, final Hashtable<String, String> values)
'''
pass
def evalJSResult():
'''public Object evalJSResult(final JApplet applet, final String cmdString)
'''
pass
def isFirefox():
'''public boolean isFirefox(final JApplet applet)
'''
pass
def callJavascriptEval():
'''public void callJavascriptEval(final String eval)
'''
pass
def run():
'''public void run()
public Void run()
'''
pass
def getMessage():
'''public String getMessage(final String msgkey)
'''
pass
def getSKDUserLocaleData():
'''public SKDUserLocaleData getSKDUserLocaleData()
'''
pass
def getMessageWithPrefix():
'''public String getMessageWithPrefix(final String msgkey)
'''
pass
def setSKDUserLocaleData():
'''public void setSKDUserLocaleData()
'''
pass
def getResourceString():
'''public String getResourceString(final String key)
'''
pass
def getResourceStrings():
'''public Hashtable getResourceStrings()
'''
pass
def getDateFormat():
'''public DateFormat getDateFormat(final int propDataType)
'''
pass
def getAppletName():
'''public String getAppletName()
'''
pass
def getConstraintType():
'''public IlvConstraintType getConstraintType(final String num)
'''
pass
def getConstraintTypeInt():
'''public Integer getConstraintTypeInt(final IlvConstraintType type)
'''
pass
def getViewerProperty():
'''public String getViewerProperty(final String prop, final String defaultValue)
'''
pass
def setViewerProperty():
'''public void setViewerProperty(final String key, final String value)
'''
pass
def decodeColor():
'''public Color decodeColor(final String hexValue)
'''
pass
def getStatusColors():
'''public Color[] getStatusColors(String status, String groupname)
'''
pass
def canShowCurrentTimeIndicatorOnDrag():
'''public boolean canShowCurrentTimeIndicatorOnDrag()
'''
pass
def getSnapToGridIntervalMins():
'''public int getSnapToGridIntervalMins()
'''
pass
def getDefaultRowHeight():
'''public int getDefaultRowHeight()
'''
pass
def getPriorityColors():
'''public Color[] getPriorityColors(String priority, String groupname)
'''
pass
def usingStatusColors():
'''public boolean usingStatusColors()
'''
pass
def hidingYAxis():
'''public boolean hidingYAxis()
'''
pass
def hidingLegend():
'''public boolean hidingLegend()
'''
pass
def IlvDurationToDouble():
'''public double IlvDurationToDouble(final IlvDuration lv)
'''
pass
def enforceOrientation():
'''public void enforceOrientation(final JComponent comp)
'''
pass
def enforceBIDIColumnLayout():
'''public void enforceBIDIColumnLayout(final JTable table)
'''
pass
def isGUIMirrored():
'''public boolean isGUIMirrored()
'''
pass
def enforceBidiDirection():
'''public String enforceBidiDirection(String str, final String bidiDirection)
'''
pass
def removeMarkersForApplink():
'''public static String removeMarkersForApplink(final String str)
'''
pass
def setGUIMirrored():
'''public void setGUIMirrored(final String langcode)
'''
pass
def isBIDIEnabled():
'''public boolean isBIDIEnabled()
'''
pass
def setBIDIEnabled():
'''public void setBIDIEnabled(final String value)
'''
pass
def replaceString():
'''public static String replaceString(String str, final String pattern, final String replacement)
'''
pass
def makeTooltipStringBasedOnDirection():
'''public String makeTooltipStringBasedOnDirection(final String direction, final String value, final String property)
public String makeTooltipStringBasedOnDirection(final String direction, final String value)
'''
pass
def removeMarkers():
'''public static String removeMarkers(final String str)
'''
pass
def isBiDiString():
'''public static boolean isBiDiString(final String str)
'''
pass
def fireEscapeKeyDown():
'''public void fireEscapeKeyDown()
'''
pass
def todaysDate():
'''public Date todaysDate()
'''
pass
def getServerDate():
'''public Date getServerDate(Date oldDate)
'''
pass
def getServerDateForUser():
'''public Date getServerDateForUser(Date serverDate)
'''
pass
def getDate():
'''public Date getDate(final Locale l, final TimeZone tz, final Date date)
'''
pass
def getFixedTimeIndicatorFromGSheet():
'''public IlvFixedTimeIndicator getFixedTimeIndicatorFromGSheet(final IlvGanttSheet gsheet)
'''
pass
def areServerAndUserTZDifferent():
'''public boolean areServerAndUserTZDifferent()
'''
pass
def removeTimeIndicator():
'''public void removeTimeIndicator(final IlvGanttSheet gSheet)
'''
pass
def refreshActivityTable():
'''public void refreshActivityTable()
'''
pass
def getAppName():
'''public String getAppName()
'''
pass
def isAssignmentManager():
'''public boolean isAssignmentManager()
'''
pass
def setupSnapToGrid():
'''public void setupSnapToGrid(final IlvGanttSheet ganttSheet)
'''
pass
def keyPressed():
'''public void keyPressed(final KeyEvent e)
'''
pass
def keyReleased():
'''public void keyReleased(final KeyEvent e)
'''
pass
def getToolTipPropertyMaxWidth():
'''public int getToolTipPropertyMaxWidth()
'''
pass
def getModifiedLabelColorString():
'''public String getModifiedLabelColorString()
'''
pass
def getModifiedLabelPrefix():
'''public String getModifiedLabelPrefix()
'''
pass
def isComplianceEnabled():
'''public boolean isComplianceEnabled()
'''
pass
def setComplianceEnabled():
'''public void setComplianceEnabled(final boolean complianceEnabled)
'''
pass
def needSendModelChange():
'''public boolean needSendModelChange()
'''
pass
def setSendModelchange():
'''public void setSendModelchange(final boolean sendModelchange)
'''
pass
def sendToBeSaved():
'''public boolean sendToBeSaved()
'''
pass
def setToBeSaved():
'''public void setToBeSaved(final boolean sendtobesaved)
'''
pass
def getColorProperty():
'''public Color getColorProperty(final String propName, Color defaultColor)
'''
pass
def isUsingCompressedData():
'''public boolean isUsingCompressedData()
'''
pass
def getLegendColors():
'''public static IlvStyle[] getLegendColors()
'''
pass
def getLegendColorsforResourceHourView():
'''public static IlvStyle[] getLegendColorsforResourceHourView()
'''
pass
def getBooleanProperty():
'''public boolean getBooleanProperty(final String propName, final boolean defVal)
'''
pass
def getLongProperty():
'''public long getLongProperty(final String propName, final long defVal)
'''
pass
def getIntProperty():
'''public int getIntProperty(final String propName, final int defVal)
'''
pass
def setUserOverrideProperties():
'''public void setUserOverrideProperties(final Properties props)
'''
pass
def isEmpty():
'''public static boolean isEmpty(final String text)
'''
pass
def enableHttpOnlyWorkaroundIfNeeded():
'''public void enableHttpOnlyWorkaroundIfNeeded(final JApplet applet)
'''
pass
def setDefaultUserTimeZone():
'''public boolean setDefaultUserTimeZone(final String userTimeZoneId)
'''
pass
def getReservationLiveUpdateThreshold():
'''public long getReservationLiveUpdateThreshold()
'''
pass
def hideDurationCheckEnabled():
'''public boolean hideDurationCheckEnabled()
'''
pass
