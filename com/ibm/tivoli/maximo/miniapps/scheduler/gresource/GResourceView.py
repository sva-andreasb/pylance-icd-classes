def GResourceView():
    '''public GResourceView()
    '''
def getLayoutUI():
    '''public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
    '''
def getProjectData():
    '''public JSONObject getProjectData(final WebClientSession sess, @MXEventParam("ganttStart") final long ganttStart)
    '''
def async_get_table_context_menu():
    '''public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value, @MXEventParam("selection") final JSONObject selection, @MXEventParam("selecteddate") final long selecteddate)
    '''
def getTooltip():
    '''public DynamicTooltip getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)
    '''
def saveModAvailReasonCode():
    '''public JSONObject saveModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("reasonCode") final String reasonCode, @MXEventParam("durationType") final String durationType)
    '''
def deleteModAvailReasonCode():
    '''public JSONObject deleteModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("durationType") final String durationType)
    '''
def addGotoToolbarOptions():
    '''public void addGotoToolbarOptions(final UIOptions opts)
    '''
def gotoPeriod():
    '''public JSONObject gotoPeriod(final WebClientSession sess, @MXEventParam("direction") final int direction, @MXEventParam("zoomLevel") final int zoomLevel, @MXEventParam("weekStart") final long weekStart)
    '''
def setStartDate():
    '''public JSONObject setStartDate(final WebClientSession sess, @MXEventParam("currentDate") final long currentDate)
    '''
