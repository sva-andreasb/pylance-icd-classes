TESTIDS_ENABLED_PROPERTY = "String  mxe.skd.automationids.enabled""
SKD_BUILD_ID = "String  20200715-0100""
SCHEDULER_MSG_GROUP = "String  scheduler""
def AbstractTreeGridMiniAppBean():
'''public AbstractTreeGridMiniAppBean()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def addQuickSearch():
'''public void addQuickSearch(final UIOptions opts)
'''
pass
def addToggleDependencies():
'''public void addToggleDependencies(final UIOptions opts, final boolean create)
'''
pass
def addLinkToWorkViewFilter():
'''public void addLinkToWorkViewFilter(final UIOptions opts, final boolean create, final boolean initialState)
'''
pass
def addFilterToggle():
'''public void addFilterToggle(final UIOptions opts)
'''
pass
def onReset():
'''public void onReset()
'''
pass
def getCurrentProjectId():
'''public String getCurrentProjectId()
'''
pass
def isGUIMirrored():
'''public boolean isGUIMirrored()
'''
pass
def setGridTitleInUIOptions():
'''public void setGridTitleInUIOptions(final UIOptions opts, final boolean readOnly)
'''
pass
def async_export_echo():
'''public void async_export_echo(final WebClientSession sess)
'''
pass
def getLastKnownState():
'''public String getLastKnownState()
'''
pass
def async_upload_state():
'''public JSONObject async_upload_state(final WebClientSession sess, @MXEventParam("cfgid") final String cfgid, @MXEventParam("cookie") final String cookie)
'''
pass
def async_load_text():
'''public JSONObject async_load_text(final WebClientSession sess)
'''
pass
def loadSKDUIInfo():
'''public SKDUIInfo loadSKDUIInfo()
'''
pass
def async_get_table_context_menu():
'''public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value)
'''
pass
def on_handle_applink_menu_item():
'''public Object on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values)
'''
pass
def callMethod():
'''public Object callMethod(final String methodName, final Class<?>[] paramTypes, final Object[] params)
'''
pass
def callBeanMethod():
'''public Object callBeanMethod(final String method, final Class<?>[] paramTypes, final Object[] params)
'''
pass
def async_upload_changes():
'''public ReplyBuilder async_upload_changes(final WebClientSession sess)
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def getAppName():
'''public String getAppName()
'''
pass
def getTooltipForPoint():
'''public DynamicTooltip getTooltipForPoint(@MXEventParam("id") final String id, @MXEventParam("point_index") final int pointIndex)
'''
pass
def async_push_client_message():
'''public void async_push_client_message()
'''
pass
def sendEventToTreeGrid():
'''public void sendEventToTreeGrid(final String eventId, final String eventArg)
'''
pass
def getPresentationOptions():
'''public JSONObject getPresentationOptions()
'''
pass
def isShowingWeather():
'''public boolean isShowingWeather()
'''
pass
def label():
'''public String label(final String key)
public String label(final String key, final String def)
'''
pass
def sortSKDAction():
'''public HashMap<String, SKDActionInfo> sortSKDAction(final HashMap<String, SKDActionInfo> skdActivityActions, final String frame)
'''
pass
def appendCss():
'''public void appendCss(final StringBuilder sb, final String key, final String value)
'''
pass
def filterCss():
'''public String filterCss(String css, final MiniAppControl control)
'''
pass
def getBaseImageUrl():
'''public String getBaseImageUrl()
'''
pass
def loadMiniAppResource():
'''public String loadMiniAppResource(final String path)
'''
pass
def getSchedulerProperties():
'''public Properties getSchedulerProperties()
'''
pass
def loadTemplate():
'''public String loadTemplate(final String id)
'''
pass
def loadTooltip():
'''public String loadTooltip(final String id)
'''
pass
def getSKDAppServiceBean():
'''public SKDAppServiceBeanRemote getSKDAppServiceBean()
public static SKDAppServiceBeanRemote getSKDAppServiceBean(final WebClientSession wcs)
'''
pass
def isAiviationLicensePresent():
'''public static boolean isAiviationLicensePresent(final WebClientSession sess)
'''
pass
def isAiviationMROLicensePresent():
'''public static boolean isAiviationMROLicensePresent(final WebClientSession sess)
'''
pass
def isLicensePresent():
'''public static boolean isLicensePresent(final WebClientSession sess, final String lic)
public static boolean isLicensePresent(final String lic)
'''
pass
def resolveTemplate():
'''public String resolveTemplate(final String templateName, final MboRemote projectMbo)
'''
pass
def setupBean():
'''public void setupBean(final WebClientSession wcs)
'''
pass
def initializeProjectData():
'''public void initializeProjectData()
'''
pass
def getUIOptions():
'''public UIOptions getUIOptions()
'''
pass
def setSerializationHelper():
'''public void setSerializationHelper(final MXSerializationHelper mxSerializationHelper)
'''
pass
def clearSavedState():
'''public void clearSavedState()
'''
pass
def getApplicationResource():
'''public String getApplicationResource(final String path)
'''
pass
def getShiftWorkPeriodInfoForDate():
'''public List<ShiftInfo> getShiftWorkPeriodInfoForDate(final IMXGanttModel sched, final Properties props, final Date d)
public ShiftInfo getShiftWorkPeriodInfoForDate(final IMXGanttModel model, final Date d)
public ShiftInfo getShiftWorkPeriodInfoForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)
'''
pass
def getTooltipForDateInSchedule():
'''public DynamicTooltip getTooltipForDateInSchedule(final IMXGanttModel schedule, final Properties props, final long date)
'''
pass
def getClientSession():
'''public WebClientSession getClientSession()
'''
pass
def beanSupplier():
'''public Supplier<AbstractTreeGridMiniAppBean> beanSupplier()
'''
pass
def uiOptionsSupplier():
'''public Supplier<UIOptions> uiOptionsSupplier()
'''
pass
def get():
'''public UIOptions get()
'''
pass
def getModAvailForDate():
'''public IMXActivity getModAvailForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)
'''
pass
def getShiftBreakInfoForDate():
'''public ShiftInfo getShiftBreakInfoForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)
'''
pass
def updateDateTimeProperty():
'''public void updateDateTimeProperty(final String prop, final JSONObject obj, final IMXActivity act)
'''
pass
def updateStringProperty():
'''public void updateStringProperty(final String prop, final JSONObject obj, final IMXActivity act, final boolean acceptEmptyString)
'''
pass
def updateIntProperty():
'''public boolean updateIntProperty(final String prop, final JSONObject obj, final IMXActivity act)
'''
pass
def updateBooleanProperty():
'''public void updateBooleanProperty(final String prop, final JSONObject obj, final IMXActivity act)
'''
pass
def CfgId():
'''public static String CfgId(final String base)
'''
pass
def getProjectMbo():
'''public MboRemote getProjectMbo()
'''
pass
def getShiftWorkTime():
'''public SKDShiftWorkTime getShiftWorkTime()
'''
pass
def setShiftWorkTime():
'''public void setShiftWorkTime(final SKDShiftWorkTime shiftWorkTime)
'''
pass
def getStart():
'''public Date getStart()
'''
pass
def setStart():
'''public void setStart(final Date start)
'''
pass
def getEnd():
'''public Date getEnd()
'''
pass
def setEnd():
'''public void setEnd(final Date end)
'''
pass
def getColor():
'''public String getColor()
'''
pass
def setColor():
'''public void setColor(final String color)
'''
pass
