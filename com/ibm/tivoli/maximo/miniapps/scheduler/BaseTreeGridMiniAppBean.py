def onReset():
    '''public void onReset()
    '''
def async_get_table_context_menu():
    '''public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value)
    '''
def on_handle_applink_menu_item():
    '''public Object on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values, @MXEventParam("selection") final JSONObject selection)
    '''
def getGanttConfigInfo():
    '''public GanttConfigInfo getGanttConfigInfo(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
    '''
def async_upload_changes():
    '''public ReplyBuilder async_upload_changes(final WebClientSession sess)
    '''
def updateStartEndTimes():
    '''public int updateStartEndTimes(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final MXActivity mxa)
    '''
def updateDuration():
    '''public void updateDuration(final MXGanttModel model, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final MXActivity mxa)
    '''
def loadSKDUIInfo():
    '''public SKDUIInfo loadSKDUIInfo()
    '''
def getTooltip():
    '''public DynamicTooltip getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)
    '''
def getTooltipForCPM():
    '''public DynamicTooltip getTooltipForCPM(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("fromid") final String fromId, @MXEventParam("toid") final String toId)
    '''
def getTooltipForDate():
    '''public DynamicTooltip getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)
    '''
def getTooltipForPoint():
    '''public DynamicTooltip getTooltipForPoint(@MXEventParam("id") final String id, @MXEventParam("point_index") final int pointIndex)
    '''
def loadProject():
    '''public synchronized Future<MXGanttModel> loadProject(final JSONObject projectOptions)
    '''
def getActivitites():
    '''public List<MXActivity> getActivitites(final String[] ids, final Future<MXGanttModel> model)
    '''
def addActionMenuItems():
    '''public void addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final Future<MXGanttModel> modelFutre, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)
    '''
def addModelChange():
    '''public void addModelChange(final MXGanttModel model, final MXActivity currentActivity, final WebClientSession session)
    public void addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final WebClientSession session)
    '''
def getSKDPMUtility():
    '''public SKDPMUtility getSKDPMUtility(final MXGanttModel model)
    '''
def addGotoToolbarOptions():
    '''public void addGotoToolbarOptions(final UIOptions opts)
    '''
def addZoomToToolbarOptions():
    '''public void addZoomToToolbarOptions(final UIOptions opts)
    '''
def addLockDurationIcon():
    '''public void addLockDurationIcon(final UIOptions opts, final boolean create)
    '''
def addFixUI():
    '''public void addFixUI(final UIOptions opts)
    '''
def setupBean():
    '''public void setupBean(final WebClientSession wcs)
    '''
def initializeProjectData():
    '''public void initializeProjectData()
    '''
def getUIOptions():
    '''public UIOptions getUIOptions()
    '''
def setSerializationHelper():
    '''public void setSerializationHelper(final MXSerializationHelper mxSerializationHelper)
    '''
def canNotAssignTo():
    '''public boolean canNotAssignTo(final String assignaction, final MXActivity act, final String[] selectedactivitys, final MXGanttModel model)
    '''
def clearSavedState():
    '''public void clearSavedState()
    '''
def getCalculatedProjectMinMax():
    '''public Range<Date> getCalculatedProjectMinMax()
    '''
def getActualStartEnd():
    '''public Range<Date> getActualStartEnd()
    '''
