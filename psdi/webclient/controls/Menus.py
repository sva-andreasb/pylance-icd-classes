PROPERTY_MODULE = "String  \"module\""
PROPERTY_APP = "String  \"app\""
PROPERTY_QUERY = "String  \"query\""
PROPERTY_HEADER = "String  \"header\""
PROPERTY_OPENAT = "String  \"openat\""
LIBRARY_MENUS = "String  \"menus\""
ID_MENUITEM = "String  \"menuitem_\""
PROPERTY_MENUTYPE = "String  \"menutype\""
PROPERTY_APPTYPE = "String  \"apptype\""
PROPERTY_CUSTAPPTYPE = "String  \"custapptype\""
PROPERTY_TARGET = "String  \"target\""
PROPERTY_ID = "String  \"id\""
PROPERTY_ACCESSKEY = "String  \"accesskey\""
PROPERTY_CLAUSENAME = "String  \"clausename\""
PROPERTY_COMPONENT = "String  \"component\""
PROPERTY_CONTROL = "String  \"control\""
PROPERTY_CSSCLASS = "String  \"cssclass\""
PROPERTY_DISABLED = "String  \"disabled\""
PROPERTY_DISABLE_NULL = "String  \"disablenull\""
PROPERTY_DISABLE_READONLY = "String  \"disablereadonly\""
PROPERTY_DISABLE_QUERY = "String  \"disablequery\""
PROPERTY_READONLY = "String  \"readonly\""
PROPERTY_KEY = "String  \"key\""
PROPERTY_EVENTVALUE = "String  \"eventvalue\""
PROPERTY_IMAGE = "String  \"image\""
PROPERTY_ELEMENTTYPE = "String  \"elementtype\""
PROPERTY_TEXT = "String  \"text\""
PROPERTY_MAINMENU = "String  \"mainmenu\""
PROPERTY_SUBMENU = "String  \"submenu\""
PROPERTY_TAG = "String  \"tag\""
PROPERTY_MENUPARENT = "String  \"menuparent\""
PROPERTY_MXEVENT = "String  \"mxevent\""
PROPERTY_MXEVENT_CHG = "String  \"mxeventchg\""
PROPERTY_TABDISPLAY = "String  \"tabdisplay\""
COMPONENT_TYPE_MENU = "String  \"menu\""
COMPONENT_TYPE_MENUITEM = "String  \"menuitem\""
PROPERTY_APPLINK = "String  \"applink\""
PROPERTY_LOOKUP = "String  \"lookup\""
PROPERTY_LOADLINK = "String  \"loadlink\""
PROPERTY_SELECTVALUE = "String  \"selectvalue\""
PROPERTY_LINK = "String  \"link\""
PROPERTY_LABEL = "String  \"label\""
PROPERTY_EVENT = "String  \"event\""
PROPERTY_BORDER = "String  \"border\""
PROPERTY_LICENSEKEY = "String  \"licensekey\""
PROPERTY_APPNAME = "String  \"appname\""
PROPERTY_APPUID = "String  \"appuid\""
PROPERTY_CONTROLVALUE = "String  \"controlvalue\""
PROPERTY_INPUTMODE = "String  \"inputmode\""
COMMON_MENU_LIBRARY_ID = "String  \"NORMAL\""
COMMON_APPLINK_MENUITEM_LIBRARY_ID = "String  \"normal1\""
PROPERTY_CMSITEM = "String  \"cmsitem\""
PROPERTY_CMSEVENT = "String  \"CMS_EVENT\""
PROPERTY_CMSENTRYID = "String  \"cmsentryid\""
MENUTYPE_UNKNOWN = "int  -1"
MENUTYPE_COMBOBOX = "int  0"
MENUTYPE_GOTO = "int  1"
MENUTYPE_QUERY = "int  2"
MENUTYPE_ACTIONS = "int  3"
MENUTYPE_MENUBAR = "int  4"
MENUTYPE_REPORTS = "int  5"
MENUTYPE_PROFILE = "int  6"
MENUTYPE_DYNAMIC = "int  6"
MENUTYPE_TOOLBAR = "int  7"
def Menus():
    '''    public Menus()
    '''
def render():
    '''    public int render()
    '''
def clearMenuData():
    '''    public void clearMenuData()
    '''
def setIsGotoMenu():
    '''    public void setIsGotoMenu(final boolean showGoto)
    '''
def getParentComponent():
    '''    public ComponentInstance getParentComponent()
    '''
def getTriggerItemId():
    '''    public String getTriggerItemId()
    '''
def setRendered():
    '''    public void setRendered()
    '''
def getMenuType():
    '''    public int getMenuType()
    '''
def getFirstMenuId():
    '''    public String getFirstMenuId()
    '''
def getFirstMenuItemId():
    '''    public String getFirstMenuItemId()
    '''
def isGotoMenu():
    '''    public boolean isGotoMenu()
    '''
def getOriginalEvent():
    '''    public WebClientEvent getOriginalEvent()
    '''
def showmenu():
    '''    public int showmenu()
    '''
def getMenus():
    '''    public ArrayList<MenuInstance> getMenus()
    '''
def buildMenuCache():
    '''    public JSONObject buildMenuCache(final String componentId)
    '''
def fetchMenuDef():
    '''    public JSONObject fetchMenuDef(final int type, final String compId, final String menuId)
    public JSONObject fetchMenuDef(final int type, final String compId, final String menuId, final boolean inLeftNav)
    '''
def fetchmenucache():
    '''    public int fetchmenucache()
    '''
def getMenusAsJson():
    '''    public JSONObject getMenusAsJson()
    '''
def getMenubarOptions():
    '''    public Map<String, Map<String, String>> getMenubarOptions()
    '''
def getQueryOptions():
    '''    public Map<String, Map<String, String>> getQueryOptions()
    '''
def buildMenu():
    '''    public String buildMenu(final Element libraryMenu, final boolean isSub, final String parentId)
    public void buildMenu(final Map<?, Map<String, String>> options)
    public void buildMenu(final Map<?, Map<String, String>> options, final int limit)
    public void buildMenu(final Map<?, Map<String, String>> options, final int limit, final WebClientEvent overflowEvent)
    '''
def buildDummyMenu():
    '''    public String buildDummyMenu(final Element libraryMenu, final boolean isSub, final String parentId)
    '''
def createMenuItemProperties():
    '''    public Map<String, String> createMenuItemProperties(final Map<String, String> oldMap)
    '''
def changePropertyName():
    '''    public Map<String, String> changePropertyName(final Map<String, String> props, final String oldName, final String newName)
    '''
def getMenuItem():
    '''    public Map<String, String> getMenuItem(final String id)
    '''
def click():
    '''    public int click()
    '''
def getShowSingle():
    '''    public boolean getShowSingle()
    '''
def setNeedsRender():
    '''    public void setNeedsRender(final boolean needsRender)
    '''
def hiddenByProperty():
    '''    public boolean hiddenByProperty(String hideWhen)
    '''
def getId():
    '''    public String getId()
    '''
