STATUS_OK = "int  0"
STATUS_WARNING = "int  1"
STATUS_REQUIRED = "int  2"
STATUS_ERROR = "int  3"
TYPE_UNKNOWN = "int  0"
TYPE_DATABASE = "int  1"
TYPE_APP_SERVER = "int  2"
TYPE_DIRECTORY_SERVER = "int  3"
TYPE_SECURITY = "int  4"
TYPE_DEPLOYMENT = "int  5"
TYPE_GENERAL = "int  6"
def ():
    '''returns ANavTreeNode\n\n
    (final String name, final String ID, final int type)\n
    '''
def remove():
    '''returns None\n\n
    remove(final ANavTreeNode node)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def add():
    '''returns None\n\n
    add(final ANavTreeNode node)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final NavTreeEventListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final NavTreeEventListener listener)\n
    '''
def getChildren():
    '''returns Object[]\n\n
    getChildren()\n
    '''
def hasChildren():
    '''returns boolean\n\n
    hasChildren()\n
    '''
def getParent():
    '''returns ANavTreeNode\n\n
    getParent()\n
    '''
def getStatus():
    '''returns int\n\n
    getStatus()\n
    '''
def getDisplayStatus():
    '''returns int\n\n
    getDisplayStatus()\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final int status)\n
    '''
def getPageID():
    '''returns String\n\n
    getPageID()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
