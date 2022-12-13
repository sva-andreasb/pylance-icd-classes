SCHEDMAX_SYNC_ID = "String  \"schedmax_sync\""
SESSION_VALUES_REF = "String  \"session_values_ref\""
def SchedulerMaxWorkView():
    '''    public SchedulerMaxWorkView()
    '''
def async_set_compliance():
    '''    public boolean async_set_compliance(@MXEventParam("projectid") final String id, @MXEventParam("state") final boolean state)
    '''
def getLayoutUI():
    '''    public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
    '''
def createUIOptions():
    '''    public UIOptions createUIOptions(final String projectId)
    '''
def async_export_xls():
    '''    public void async_export_xls(final WebClientSession sess)
    '''
def async_load_gantt_pages():
    '''    public synchronized JSONObject async_load_gantt_pages(final WebClientSession sess)
    '''
def async_load_gantt_page():
    '''    public synchronized JSONObject async_load_gantt_page(final WebClientSession sess)
    '''
def async_load_gantt_data():
    '''    public synchronized JSONObject async_load_gantt_data(final WebClientSession sess)
    '''
def getTooltipForDate():
    '''    public DynamicTooltip getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)
    '''
def async_upload_changes():
    '''    public ReplyBuilder async_upload_changes(final WebClientSession sess)
    '''
def run():
    '''    public void run()
    '''
def _cpmall():
    '''    public JSONObject _cpmall(final WebClientSession sess, final String ids, final String values)
    '''
def _cpmselected():
    '''    public JSONObject _cpmselected(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)
    '''
def _cpmcreatelinks():
    '''    public JSONObject _cpmcreatelinks(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)
    '''
def _cpmfilter():
    '''    public JSONObject _cpmfilter(final WebClientSession sess, @MXEventParam("filteredByCriticalPath") final boolean filteredByCriticalPath)
    '''
def _discardRefreshSelected():
    '''    public JSONObject _discardRefreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)
    '''
def _refreshSelected():
    '''    public JSONObject _refreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)
    '''
def _expandToLevel():
    '''    public JSONObject _expandToLevel(final WebClientSession sess, @MXEventParam("level") final Integer level)
    '''
def _updateSummary():
    '''    public JSONObject _updateSummary(final WebClientSession sess, final String ids, final String values)
    '''
def _getSelectedTab():
    '''    public JSONObject _getSelectedTab(final WebClientSession sess)
    '''
def processChange():
    '''    public void processChange(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)
    '''
def updateStartEndTimes():
    '''    public int updateStartEndTimes(final Schedule schedule, final JSONObject change, final WebClientSession sess, final Activity activity)
    '''
def updateDuration():
    '''    public void updateDuration(final Schedule schedule, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final Activity activity)
    '''
def _DELETECONSTRAINTS():
    '''    public ReplyBuilder _DELETECONSTRAINTS(final WebClientSession session, final String value, final String valueList, final JSONObject selection)
    '''
def on_handle_applink_menu_item():
    '''    public Object on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values, @MXEventParam("selection") final JSONObject selection)
    '''
def addActionMenuItems():
    '''    public void addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final Schedule schedule, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)
    '''
def updateDateTimeProperty():
    '''    public void updateDateTimeProperty(final String prop, final JSONObject obj, final IMXActivity act)
    '''
