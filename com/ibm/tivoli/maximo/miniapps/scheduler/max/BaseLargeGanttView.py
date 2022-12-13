def BaseLargeGanttView():
    '''public BaseLargeGanttView()
    '''
def loadSKDUIInfo():
    '''public SKDUIInfo loadSKDUIInfo()
    '''
def getTooltip():
    '''public DynamicTooltip getTooltip(final WebClientSession sess, final String projectid, final String col, final String id)
    '''
def getTooltipForUnloadedCPM():
    '''public DynamicTooltip getTooltipForUnloadedCPM(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityId, @MXEventParam("fromdependency") final boolean fromDependency)
    '''
def getTooltipForCPM():
    '''public DynamicTooltip getTooltipForCPM(final WebClientSession sess, final String projectid, final String fromId, final String toId)
    '''
def getTooltipForDate():
    '''public DynamicTooltip getTooltipForDate(final WebClientSession sess, final String projectid, final String col, final String id, final long date)
    '''
def async_upload_changes():
    '''public ReplyBuilder async_upload_changes(final WebClientSession sess)
    '''
def getActualStartEnd():
    '''public Range<Date> getActualStartEnd()
    '''
def getCalculatedProjectMinMax():
    '''public Range<Date> getCalculatedProjectMinMax()
    '''
def async_get_table_context_menu():
    '''public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value)
    '''
