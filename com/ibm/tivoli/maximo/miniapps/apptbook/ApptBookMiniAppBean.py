APPTBOOK_MSG_GROUP = "String  \"apptbook\""
SCHEDULER_MSG_GROUP = "String  \"scheduler\""
APPTBKMGRWINDOWSIZE = "String  \"apptBookMgrWindowSize\""
def ():
    '''returns ApptBookMiniAppBean\n\n
    ()\n
    '''
def loadLocalizedData():
    '''returns JSONObject\n\n
    loadLocalizedData()\n
    '''
def gotoDate():
    '''returns JSONObject\n\n
    gotoDate(@MXEventParam("date") final long date, @MXEventParam("tzOffset") final long tzOffset, @MXEventParam("fmtDate") final String fmtDate)\n
    '''
def gotoDateOffset():
    '''returns JSONObject\n\n
    gotoDateOffset(@MXEventParam("dateOffset") final int offset)\n
    '''
def getDefaultUIJason():
    '''returns JSONObject\n\n
    getDefaultUIJason()\n
    '''
def createUI():
    '''returns JSONObject\n\n
    createUI(@MXEventParam("startDate") final long startDate)\n
    '''
def visitString():
    '''returns None\n\n
    visitString(final Object parent, final Object key, final String val)\n
    '''
def getResolver():
    '''returns FunctionMapResolver\n\n
    getResolver()\n
    '''
def getResolverWithCellText():
    '''returns FunctionMapResolver\n\n
    getResolverWithCellText()\n
    '''
def getRootData():
    '''returns JSONObject\n\n
    getRootData()\n
    '''
def getApptBook():
    '''returns MboRemote\n\n
    getApptBook()\n
    '''
def getModelLoader():
    '''returns ModelLoader\n\n
    getModelLoader()\n
    '''
def loadAppointments():
    '''returns None\n\n
    loadAppointments(final ApptBook apptBook, final Date start, final Date end)\n
    '''
def getModel():
    '''returns ApptBook\n\n
    getModel()\n
    '''
def loadResource():
    '''returns String\n\n
    loadResource(final String path)\n
    '''
def getBaseImageUrl():
    '''returns String\n\n
    getBaseImageUrl()\n
    '''
def filterCss():
    '''returns String\n\n
    filterCss(final String css, final MiniAppControl control)\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String selectedId, @MXEventParam("selection") final JSONObject selection, @MXEventParam("col") final String column, @MXEventParam("value") String value)\n
    '''
def label():
    '''returns String\n\n
    label(final String key, final String groupName)\n
    label(final String key)\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def addActionMenuItems():
    '''returns None\n\n
    addActionMenuItems(final TMenu popupmenu, final String[] selectedBuckets, final String projectId, final String propName, final String propValue, final HashMap<String, ApptActionInfo> apptactions)\n
    '''
def getAppName():
    '''returns String\n\n
    getAppName()\n
    '''
