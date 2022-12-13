COL_ID = "String  \"id\""
COL_RESOURCE = "String  \"CRAFT\""
COL_DESCRIPTION = "String  \"name\""
COL_LOAD = "String  \"load\""
COL_OVERLOAD = "String  \"overload\""
COL_AVAIL = "String  \"avail\""
COL_COMMON = "String  \"common\""
def useOverlappingAvails():
    '''public static boolean useOverlappingAvails()
    '''
def availGroupName():
    '''public static String availGroupName(final String shift)
    '''
def loadGroupName():
    '''public static String loadGroupName(final String shift)
    '''
def overloadGroupName():
    '''public static String overloadGroupName(final String shift)
    '''
def getLayoutUI():
    '''public static JSONObject getLayoutUI(final WebClientSession sess, final BaseTreeGridMiniAppBean bean, final UIOptions uiOptions, final SKDUIInfo skdUIInfo, final Future modelFuture)
    public static JSONObject getLayoutUI(final WebClientSession sess, final BaseTreeGridMiniAppBean bean, final UIOptions uiOptions, final SKDUIInfo skdUIInfo, final IMXGanttModel model)
    public static JSONObject getLayoutUI(final WebClientSession sess, final AbstractTreeGridMiniAppBean bean, final UIOptions uiOptions, final SKDUIInfo skdUIInfo, final IMXGanttModel model, final Range<Date> projectDates)
    '''
def hide():
    '''public static JSONObject hide(final JSONObject col)
    '''
def configureGantt():
    '''public static void configureGantt(final BaseTreeGridMiniAppBean bean, final IMXGanttModel model, final JSONObject Gantt, final UIBuilder builder, final UIOptions options, final ISKDUIInfo uiInfo)
    public static void configureGantt(final AbstractTreeGridMiniAppBean bean, final IMXGanttModel model, final Range<Date> projectDates, final JSONObject Gantt, final UIBuilder builder, final UIOptions options, final ISKDUIInfo uiInfo)
    '''
def getTooltipForDate():
    '''public static DynamicTooltip getTooltipForDate(final AbstractTreeGridMiniAppBean bean, final IMXGanttModel model, final String id, final Date d)
    '''
