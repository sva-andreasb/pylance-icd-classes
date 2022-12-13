def GWAResourceHoursView():
    '''    public GWAResourceHoursView()
    '''
def getLayoutUI():
    '''    public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
    '''
def getProjectData():
    '''    public JSONObject getProjectData(final WebClientSession sess)
    '''
def async_get_table_context_menu():
    '''    public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value, @MXEventParam("selection") final JSONObject selection, @MXEventParam("selecteddate") final long selecteddate)
    '''
def getTooltip():
    '''    public DynamicTooltip getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)
    '''
def workviewSelected():
    '''    public JSONObject workviewSelected(final WebClientSession sess, @MXEventParam("selection") final String selection)
    '''
def saveModAvailReasonCode():
    '''    public JSONObject saveModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("reasonCode") final String reasonCode, @MXEventParam("durationType") final String durationType)
    '''
def deleteModAvailReasonCode():
    '''    public JSONObject deleteModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("durationType") final String durationType)
    '''
def unassignAll():
    '''    public JSONObject unassignAll(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("date") final long date)
    '''
def gotoWeek():
    '''    public JSONObject gotoWeek(final WebClientSession sess, @MXEventParam("startWeekDay") final long startWeekDay, @MXEventParam("resetWeek") final boolean resetWeek)
    '''
