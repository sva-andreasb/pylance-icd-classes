TESTIDS_ENABLED_PROPERTY = "String  \"mxe.skd.automationids.enabled\""
SKD_BUILD_ID = "String  \"20200715-0100\""
SCHEDULER_MSG_GROUP = "String  \"scheduler\""
def AbstractTreeGridMiniAppBean():
    '''    public AbstractTreeGridMiniAppBean()
    '''
def getUserInfo():
    '''    public UserInfo getUserInfo()
    '''
def addQuickSearch():
    '''    public void addQuickSearch(final UIOptions opts)
    '''
def addToggleDependencies():
    '''    public void addToggleDependencies(final UIOptions opts, final boolean create)
    '''
def addLinkToWorkViewFilter():
    '''    public void addLinkToWorkViewFilter(final UIOptions opts, final boolean create, final boolean initialState)
    '''
def addFilterToggle():
    '''    public void addFilterToggle(final UIOptions opts)
    '''
def onReset():
    '''    public void onReset()
    '''
def getCurrentProjectId():
    '''    public String getCurrentProjectId()
    '''
def isGUIMirrored():
    '''    public boolean isGUIMirrored()
    '''
def setGridTitleInUIOptions():
    '''    public void setGridTitleInUIOptions(final UIOptions opts, final boolean readOnly)
    '''
def async_export_echo():
    '''    public void async_export_echo(final WebClientSession sess)
    '''
def getLastKnownState():
    '''    public String getLastKnownState()
    '''
def async_upload_state():
    '''    public JSONObject async_upload_state(final WebClientSession sess, @MXEventParam("cfgid") final String cfgid, @MXEventParam("cookie") final String cookie)
    '''
def async_load_text():
    '''    public JSONObject async_load_text(final WebClientSession sess)
    '''
def loadSKDUIInfo():
    '''    public SKDUIInfo loadSKDUIInfo()
    '''
def async_get_table_context_menu():
    '''    public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value)
    '''
def on_handle_applink_menu_item():
    '''    public Object on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values)
    '''
def callMethod():
    '''    public Object callMethod(final String methodName, final Class<?>[] paramTypes, final Object[] params)
    '''
def callBeanMethod():
    '''    public Object callBeanMethod(final String method, final Class<?>[] paramTypes, final Object[] params)
    '''
def async_upload_changes():
    '''    public ReplyBuilder async_upload_changes(final WebClientSession sess)
    '''
def getTimeZone():
    '''    public TimeZone getTimeZone()
    '''
def getAppName():
    '''    public String getAppName()
    '''
def getTooltipForPoint():
    '''    public DynamicTooltip getTooltipForPoint(@MXEventParam("id") final String id, @MXEventParam("point_index") final int pointIndex)
    '''
def async_push_client_message():
    '''    public void async_push_client_message()
    '''
def sendEventToTreeGrid():
    '''    public void sendEventToTreeGrid(final String eventId, final String eventArg)
    '''
def getPresentationOptions():
    '''    public JSONObject getPresentationOptions()
    '''
def isShowingWeather():
    '''    public boolean isShowingWeather()
    '''
def label():
    '''    public String label(final String key)
    public String label(final String key, final String def)
    '''
def sortSKDAction():
    '''    public HashMap<String, SKDActionInfo> sortSKDAction(final HashMap<String, SKDActionInfo> skdActivityActions, final String frame)
    '''
def appendCss():
    '''    public void appendCss(final StringBuilder sb, final String key, final String value)
    '''
def filterCss():
    '''    public String filterCss(String css, final MiniAppControl control)
    '''
def getBaseImageUrl():
    '''    public String getBaseImageUrl()
    '''
def loadMiniAppResource():
    '''    public String loadMiniAppResource(final String path)
    '''
def getSchedulerProperties():
    '''    public Properties getSchedulerProperties()
    '''
def loadTemplate():
    '''    public String loadTemplate(final String id)
    '''
def loadTooltip():
    '''    public String loadTooltip(final String id)
    '''
def getSKDAppServiceBean():
    '''    public SKDAppServiceBeanRemote getSKDAppServiceBean()
    public static SKDAppServiceBeanRemote getSKDAppServiceBean(final WebClientSession wcs)
    '''
def isAiviationLicensePresent():
    '''    public static boolean isAiviationLicensePresent(final WebClientSession sess)
    '''
def isAiviationMROLicensePresent():
    '''    public static boolean isAiviationMROLicensePresent(final WebClientSession sess)
    '''
def isLicensePresent():
    '''    public static boolean isLicensePresent(final WebClientSession sess, final String lic)
    public static boolean isLicensePresent(final String lic)
    '''
def resolveTemplate():
    '''    public String resolveTemplate(final String templateName, final MboRemote projectMbo)
    '''
def setupBean():
    '''    public void setupBean(final WebClientSession wcs)
    '''
def initializeProjectData():
    '''    public void initializeProjectData()
    '''
def getUIOptions():
    '''    public UIOptions getUIOptions()
    '''
def setSerializationHelper():
    '''    public void setSerializationHelper(final MXSerializationHelper mxSerializationHelper)
    '''
def clearSavedState():
    '''    public void clearSavedState()
    '''
def getApplicationResource():
    '''    public String getApplicationResource(final String path)
    '''
def getShiftWorkPeriodInfoForDate():
    '''    public List<ShiftInfo> getShiftWorkPeriodInfoForDate(final IMXGanttModel sched, final Properties props, final Date d)
    public ShiftInfo getShiftWorkPeriodInfoForDate(final IMXGanttModel model, final Date d)
    public ShiftInfo getShiftWorkPeriodInfoForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)
    '''
def getTooltipForDateInSchedule():
    '''    public DynamicTooltip getTooltipForDateInSchedule(final IMXGanttModel schedule, final Properties props, final long date)
    '''
def getClientSession():
    '''    public WebClientSession getClientSession()
    '''
def beanSupplier():
    '''    public Supplier<AbstractTreeGridMiniAppBean> beanSupplier()
    '''
def uiOptionsSupplier():
    '''    public Supplier<UIOptions> uiOptionsSupplier()
    '''
def get():
    '''    public UIOptions get()
    '''
def getModAvailForDate():
    '''    public IMXActivity getModAvailForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)
    '''
def getShiftBreakInfoForDate():
    '''    public ShiftInfo getShiftBreakInfoForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)
    '''
def updateDateTimeProperty():
    '''    public void updateDateTimeProperty(final String prop, final JSONObject obj, final IMXActivity act)
    '''
def updateStringProperty():
    '''    public void updateStringProperty(final String prop, final JSONObject obj, final IMXActivity act, final boolean acceptEmptyString)
    '''
def updateIntProperty():
    '''    public boolean updateIntProperty(final String prop, final JSONObject obj, final IMXActivity act)
    '''
def updateBooleanProperty():
    '''    public void updateBooleanProperty(final String prop, final JSONObject obj, final IMXActivity act)
    '''
def CfgId():
    '''    public static String CfgId(final String base)
    '''
def getProjectMbo():
    '''    public MboRemote getProjectMbo()
    '''
def getShiftWorkTime():
    '''    public SKDShiftWorkTime getShiftWorkTime()
    '''
def setShiftWorkTime():
    '''    public void setShiftWorkTime(final SKDShiftWorkTime shiftWorkTime)
    '''
def getStart():
    '''    public Date getStart()
    '''
def setStart():
    '''    public void setStart(final Date start)
    '''
def getEnd():
    '''    public Date getEnd()
    '''
def setEnd():
    '''    public void setEnd(final Date end)
    '''
def getColor():
    '''    public String getColor()
    '''
def setColor():
    '''    public void setColor(final String color)
    '''
