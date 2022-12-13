APPTBOOK_MSG_GROUP = "String  apptbook""
SCHEDULER_MSG_GROUP = "String  scheduler""
APPTBKMGRWINDOWSIZE = "String  apptBookMgrWindowSize""
def ApptBookMiniAppBean():
'''public ApptBookMiniAppBean()
'''
pass
def loadLocalizedData():
'''public JSONObject loadLocalizedData()
'''
pass
def gotoDate():
'''public JSONObject gotoDate(@MXEventParam("date") final long date, @MXEventParam("tzOffset") final long tzOffset, @MXEventParam("fmtDate") final String fmtDate)
'''
pass
def gotoDateOffset():
'''public JSONObject gotoDateOffset(@MXEventParam("dateOffset") final int offset)
'''
pass
def getDefaultUIJason():
'''public JSONObject getDefaultUIJason()
'''
pass
def createUI():
'''public JSONObject createUI(@MXEventParam("startDate") final long startDate)
'''
pass
def visitString():
'''public void visitString(final Object parent, final Object key, final String val)
'''
pass
def getResolver():
'''public FunctionMapResolver getResolver()
'''
pass
def getResolverWithCellText():
'''public FunctionMapResolver getResolverWithCellText()
'''
pass
def getRootData():
'''public JSONObject getRootData()
'''
pass
def getApptBook():
'''public MboRemote getApptBook()
'''
pass
def getModelLoader():
'''public ModelLoader getModelLoader()
'''
pass
def loadAppointments():
'''public void loadAppointments(final ApptBook apptBook, final Date start, final Date end)
'''
pass
def getModel():
'''public ApptBook getModel()
'''
pass
def loadResource():
'''public String loadResource(final String path)
'''
pass
def getBaseImageUrl():
'''public String getBaseImageUrl()
'''
pass
def filterCss():
'''public String filterCss(final String css, final MiniAppControl control)
'''
pass
def async_get_table_context_menu():
'''public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String selectedId, @MXEventParam("selection") final JSONObject selection, @MXEventParam("col") final String column, @MXEventParam("value") String value)
'''
pass
def label():
'''public String label(final String key, final String groupName)
public String label(final String key)
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def getApptActions():
'''public HashMap<String, ApptActionInfo> getApptActions()
'''
pass
def addActionMenuItems():
'''public void addActionMenuItems(final TMenu popupmenu, final String[] selectedBuckets, final String projectId, final String propName, final String propValue, final HashMap<String, ApptActionInfo> apptactions)
'''
pass
def getAppName():
'''public String getAppName()
'''
pass
