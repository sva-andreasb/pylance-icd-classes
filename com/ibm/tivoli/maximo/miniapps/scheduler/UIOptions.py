RESIZE_NONE = "int  0"
RESIZE_VERTICAL = "int  1"
RESIZE_HORIZONTAL = "int  2"
RESIZE_BOTH = "int  3"
RESIZE_SHOW_GRID_WHEN_RESIZING = "int  4"
NO_SELECT_DELETED_ROWS = "int  1"
NO_SELECT_FILTERED_ROWS = "int  2"
NO_SELECT_MANUALLY_HIDDEN_ROWS = "int  4"
NO_SELECT_COLLAPSED_ROWS = "int  8"
FILTER_HIDE_ALL_NOT_FOUND = "int  0"
FILTER_HIDE_ALL_NOT_FOUND_ITERATE_ALL = "int  1"
FILTER_SHOW_ALL_FOUND = "int  2"
FILTER_SHOW_ALL_FOUND_WITH_CHILDREN = "int  3"
def UIOptions():
'''public UIOptions(final Properties skdProps)
'''
pass
def canEdit():
'''public boolean canEdit(final String field)
'''
pass
def setCanEdit():
'''public void setCanEdit(final String field)
'''
pass
def getProperty():
'''public Object getProperty(final String prop)
public String getProperty(final String prop, final String def)
'''
pass
def getIntProperty():
'''public int getIntProperty(final String prop, final int defValue)
'''
pass
def getBooleanProperty():
'''public boolean getBooleanProperty(final String prop, final boolean defValue)
'''
pass
def addColumn():
'''public void addColumn(final TreeGridColumn col)
'''
pass
def ToolbarOptions():
'''public ToolbarOptions()
'''
pass
def addItem():
'''public ToolBarItem addItem(final String action, final String label)
public ToolBarItem addItem(final String action)
'''
pass
def getItem():
'''public ToolBarItem getItem(final String item)
'''
pass
def hasItem():
'''public boolean hasItem(final String item)
'''
pass
def ToolBarItem():
'''public ToolBarItem(final String action2, final String label)
'''
pass
def addPrintHeader():
'''public void addPrintHeader(final String printHeader)
'''
pass
def Paging():
'''public Paging(final int childPartLength, final int childPartMin, final int ganttPaging, final boolean progressiveRendering)
'''
pass
