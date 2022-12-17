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
def ():
    '''returns Paging\n\n
    (final Properties skdProps)\n
    ()\n
    (final String action2, final String label)\n
    (final int childPartLength, final int childPartMin, final int ganttPaging, final boolean progressiveRendering)\n
    '''
def canEdit():
    '''returns boolean\n\n
    canEdit(final String field)\n
    '''
def setCanEdit():
    '''returns None\n\n
    setCanEdit(final String field)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String prop)\n
    getProperty(final String prop, final String def)\n
    '''
def getIntProperty():
    '''returns int\n\n
    getIntProperty(final String prop, final int defValue)\n
    '''
def getBooleanProperty():
    '''returns boolean\n\n
    getBooleanProperty(final String prop, final boolean defValue)\n
    '''
def addColumn():
    '''returns None\n\n
    addColumn(final TreeGridColumn col)\n
    '''
def addItem():
    '''returns ToolBarItem\n\n
    addItem(final String action, final String label)\n
    addItem(final String action)\n
    '''
def getItem():
    '''returns ToolBarItem\n\n
    getItem(final String item)\n
    '''
def hasItem():
    '''returns boolean\n\n
    hasItem(final String item)\n
    '''
def addPrintHeader():
    '''returns None\n\n
    addPrintHeader(final String printHeader)\n
    '''
