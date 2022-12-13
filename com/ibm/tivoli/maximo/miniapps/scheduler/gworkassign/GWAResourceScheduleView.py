def GWAResourceScheduleView():
    '''    public GWAResourceScheduleView()
    '''
def getLayoutUI():
    '''    public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
    '''
def createUIOptions():
    '''    public UIOptions createUIOptions(final String projectId)
    '''
def addLockDurationIcon():
    '''    public void addLockDurationIcon(final UIOptions opts, final boolean create)
    '''
def addGotoToolbarOptions():
    '''    public void addGotoToolbarOptions(final UIOptions opts)
    '''
def addViewNavToolbarOptions():
    '''    public void addViewNavToolbarOptions(final UIOptions opts)
    '''
def async_load_gantt_data():
    '''    public synchronized JSONObject async_load_gantt_data(final WebClientSession sess)
    '''
def async_upload_changes():
    '''    public ReplyBuilder async_upload_changes(final WebClientSession sess)
    '''
def processMove():
    '''    public void processMove(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)
    '''
def processChange():
    '''    public void processChange(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)
    '''
def updateStartEndTimes():
    '''    public int updateStartEndTimes(final GWASchedule schedule, final JSONObject change, final WebClientSession sess, final Activity activity)
    '''
def on_handle_applink_menu_item():
    '''    public Object on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values, @MXEventParam("selection") final JSONObject selection)
    '''
def getActualStartEnd():
    '''    public Range<Date> getActualStartEnd()
    '''
def getCalculatedProjectMinMax():
    '''    public Range<Date> getCalculatedProjectMinMax()
    '''
def getTooltip():
    '''    public DynamicTooltip getTooltip(final WebClientSession sess, final String projectid, final String col, final String id)
    '''
def getTooltipForCPM():
    '''    public DynamicTooltip getTooltipForCPM(final WebClientSession sess, final String projectid, final String fromId, final String toId)
    '''
def getTooltipForDate():
    '''    public DynamicTooltip getTooltipForDate(final WebClientSession sess, final String projectid, final String col, final String id, final long date)
    '''
def addActionMenuItems():
    '''    public void addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final GWASchedule schedule, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)
    '''
def getRelatedAssignments():
    '''    public ReplyBuilder getRelatedAssignments(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
    '''
def gotoWeek():
    '''    public JSONObject gotoWeek(final WebClientSession sess, @MXEventParam("direction") final int direction)
    '''
def gotoWeekDate():
    '''    public JSONObject gotoWeekDate(final WebClientSession sess, @MXEventParam("selectedDate") final long selectedDate)
    '''
def setWeekDate():
    '''    public JSONObject setWeekDate(final WebClientSession sess, @MXEventParam("currentDate") final long currentDate)
    '''
def _refreshSelected():
    '''    public JSONObject _refreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)
    '''
def newWorkAction():
    '''    public JSONObject newWorkAction(final WebClientSession sess, final String actionid, final String params)
    '''
def createNewAssignment():
    '''    public Activity createNewAssignment(final GWASchedule model, final WebClientSession session, final Activity act, final Resource res, final long assignmentId, final MboRemote wo)
    '''
def deleteWorkAction():
    '''    public JSONObject deleteWorkAction(final WebClientSession sess, final String actionid, final String params)
    '''
def unassign():
    '''    public JSONObject unassign(final WebClientSession sess, final String actionid, final String params)
    '''
def mergeWorkAction():
    '''    public JSONObject mergeWorkAction(final WebClientSession sess, final String actionid, final String params)
    '''
def updateDuration():
    '''    public void updateDuration(final GWASchedule schedule, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final Activity activity)
    '''
