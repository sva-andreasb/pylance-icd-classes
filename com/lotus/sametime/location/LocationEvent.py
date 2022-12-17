SET_MY_LOCATION_FAILED = "int  220"
SET_MY_LOCATION_SUCCESSFUL = "int  221"
REMOVE_MY_LOCATION = "int  250"
REMOVE_MY_LOCATION_SUCCESSFUL = "int  251"
REMOVE_MY_LOCATION_FAILED = "int  252"
LOCATION_SERVICE_UNAVAILABLE = "int  101"
LOCATION_SERVICE_AVAILABLE = "int  102"
LOCATION_CHANGED = "int  300"
LOCATION_REMOVED = "int  301"
def ():
    '''returns LocationEvent\n\n
    (final Object o, final int n)\n
    (final Object o, final int n, final Location location)\n
    (final Object o, final int n, final Location location, final STUser stUser)\n
    (final Object o, final int n, final STUser stUser)\n
    (final Object o, final int n, final int reason)\n
    '''
def getLocation():
    '''returns Location\n\n
    getLocation()\n
    '''
def getReason():
    '''returns int\n\n
    getReason()\n
    '''
def getSTUser():
    '''returns STUser\n\n
    getSTUser()\n
    '''
