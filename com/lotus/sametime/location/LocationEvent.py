SET_MY_LOCATION_FAILED = "int  220"
SET_MY_LOCATION_SUCCESSFUL = "int  221"
REMOVE_MY_LOCATION = "int  250"
REMOVE_MY_LOCATION_SUCCESSFUL = "int  251"
REMOVE_MY_LOCATION_FAILED = "int  252"
LOCATION_SERVICE_UNAVAILABLE = "int  101"
LOCATION_SERVICE_AVAILABLE = "int  102"
LOCATION_CHANGED = "int  300"
LOCATION_REMOVED = "int  301"
def LocationEvent():
    '''    public LocationEvent(final Object o, final int n)
    public LocationEvent(final Object o, final int n, final Location location)
    public LocationEvent(final Object o, final int n, final Location location, final STUser stUser)
    public LocationEvent(final Object o, final int n, final STUser stUser)
    public LocationEvent(final Object o, final int n, final int reason)
    '''
def getLocation():
    '''    public Location getLocation()
    '''
def getReason():
    '''    public int getReason()
    '''
def getSTUser():
    '''    public STUser getSTUser()
    '''
