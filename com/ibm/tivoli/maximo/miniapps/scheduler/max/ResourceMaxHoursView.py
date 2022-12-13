def ResourceMaxHoursView():
    '''public ResourceMaxHoursView()
    '''
def getLayoutUI():
    '''public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
    '''
def getProjectData():
    '''public JSONObject getProjectData(@MXEventParam("start") final long start, @MXEventParam("end") final long end)
    '''
def changeResourceDisplayMode():
    '''public JSONObject changeResourceDisplayMode(final WebClientSession sess, @MXEventParam("display") final String display)
    '''
def getProjectDataForDates():
    '''public JSONObject getProjectDataForDates(final Date start, final Date end)
    '''
def getTooltipForDate():
    '''public DynamicTooltip getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)
    '''
def async_get_table_context_menu():
    '''public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value, @MXEventParam("selection") final JSONObject selection)
    '''
