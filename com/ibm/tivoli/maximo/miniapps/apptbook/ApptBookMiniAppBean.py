APPTBOOK_MSG_GROUP = "String  \"apptbook\""
SCHEDULER_MSG_GROUP = "String  \"scheduler\""
APPTBKMGRWINDOWSIZE = "String  \"apptBookMgrWindowSize\""
def ApptBookMiniAppBean():
    '''    public ApptBookMiniAppBean()
    '''
def loadLocalizedData():
    '''    public JSONObject loadLocalizedData()
    '''
def gotoDate():
    '''    public JSONObject gotoDate(@MXEventParam("date") final long date, @MXEventParam("tzOffset") final long tzOffset, @MXEventParam("fmtDate") final String fmtDate)
    '''
def gotoDateOffset():
    '''    public JSONObject gotoDateOffset(@MXEventParam("dateOffset") final int offset)
    '''
def getDefaultUIJason():
    '''    public JSONObject getDefaultUIJason()
    '''
def createUI():
    '''    public JSONObject createUI(@MXEventParam("startDate") final long startDate)
    '''
def visitString():
    '''    public void visitString(final Object parent, final Object key, final String val)
    '''
def getResolver():
    '''    public FunctionMapResolver getResolver()
    '''
def getResolverWithCellText():
    '''    public FunctionMapResolver getResolverWithCellText()
    '''
def getRootData():
    '''    public JSONObject getRootData()
    '''
def getApptBook():
    '''    public MboRemote getApptBook()
    '''
def getModelLoader():
    '''    public ModelLoader getModelLoader()
    '''
def loadAppointments():
    '''    public void loadAppointments(final ApptBook apptBook, final Date start, final Date end)
    '''
def getModel():
    '''    public ApptBook getModel()
    '''
def loadResource():
    '''    public String loadResource(final String path)
    '''
def getBaseImageUrl():
    '''    public String getBaseImageUrl()
    '''
def filterCss():
    '''    public String filterCss(final String css, final MiniAppControl control)
    '''
def async_get_table_context_menu():
    '''    public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String selectedId, @MXEventParam("selection") final JSONObject selection, @MXEventParam("col") final String column, @MXEventParam("value") String value)
    '''
def label():
    '''    public String label(final String key, final String groupName)
    public String label(final String key)
    '''
def getUserInfo():
    '''    public UserInfo getUserInfo()
    '''
def getApptActions():
    '''    public HashMap<String, ApptActionInfo> getApptActions()
    '''
def addActionMenuItems():
    '''    public void addActionMenuItems(final TMenu popupmenu, final String[] selectedBuckets, final String projectId, final String propName, final String propValue, final HashMap<String, ApptActionInfo> apptactions)
    '''
def getAppName():
    '''    public String getAppName()
    '''
