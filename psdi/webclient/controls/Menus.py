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
def ():
    '''returns Menus\n\n
    ()\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def clearMenuData():
    '''returns None\n\n
    clearMenuData()\n
    '''
def setIsGotoMenu():
    '''returns None\n\n
    setIsGotoMenu(final boolean showGoto)\n
    '''
def getParentComponent():
    '''returns ComponentInstance\n\n
    getParentComponent()\n
    '''
def getTriggerItemId():
    '''returns String\n\n
    getTriggerItemId()\n
    '''
def setRendered():
    '''returns None\n\n
    setRendered()\n
    '''
def getMenuType():
    '''returns int\n\n
    getMenuType()\n
    '''
def getFirstMenuId():
    '''returns String\n\n
    getFirstMenuId()\n
    '''
def getFirstMenuItemId():
    '''returns String\n\n
    getFirstMenuItemId()\n
    '''
def isGotoMenu():
    '''returns boolean\n\n
    isGotoMenu()\n
    '''
def getOriginalEvent():
    '''returns WebClientEvent\n\n
    getOriginalEvent()\n
    '''
def showmenu():
    '''returns int\n\n
    showmenu()\n
    '''
def getMenus():
    '''returns ArrayList<MenuInstance>\n\n
    getMenus()\n
    '''
def buildMenuCache():
    '''returns JSONObject\n\n
    buildMenuCache(final String componentId)\n
    '''
def fetchMenuDef():
    '''returns JSONObject\n\n
    fetchMenuDef(final int type, final String compId, final String menuId)\n
    fetchMenuDef(final int type, final String compId, final String menuId, final boolean inLeftNav)\n
    '''
def fetchmenucache():
    '''returns int\n\n
    fetchmenucache()\n
    '''
def getMenusAsJson():
    '''returns JSONObject\n\n
    getMenusAsJson()\n
    '''
def buildMenu():
    '''returns None\n\n
    buildMenu(final Element libraryMenu, final boolean isSub, final String parentId)\n
    buildMenu(final Map<?, Map<String, String>> options)\n
    buildMenu(final Map<?, Map<String, String>> options, final int limit)\n
    buildMenu(final Map<?, Map<String, String>> options, final int limit, final WebClientEvent overflowEvent)\n
    '''
def buildDummyMenu():
    '''returns String\n\n
    buildDummyMenu(final Element libraryMenu, final boolean isSub, final String parentId)\n
    '''
def click():
    '''returns int\n\n
    click()\n
    '''
def getShowSingle():
    '''returns boolean\n\n
    getShowSingle()\n
    '''
def setNeedsRender():
    '''returns None\n\n
    setNeedsRender(final boolean needsRender)\n
    '''
def hiddenByProperty():
    '''returns boolean\n\n
    hiddenByProperty(String hideWhen)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
