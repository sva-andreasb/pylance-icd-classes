ST_USER_STATUS_OFFLINE = "short  0"
ST_USER_STATUS_ACTIVE = "short  32"
ST_USER_STATUS_NOT_USING = "short  64"
ST_USER_STATUS_AWAY = "short  96"
ST_USER_STATUS_DND = "short  128"
ST_USER_STATUS_MOBILE = "short  512"
ST_USER_STATUS_ACTIVE_MOBILE = "short  544"
ST_USER_STATUS_UNKNOWN = "short  Short.MIN_VALUE"
ST_USER_STATUS_DONTCARE = "short  16384"
ST_USER_STATUS_IN_MEETING = "short  8"
def STUserStatus():
    '''    public STUserStatus(final short type, final int time, final String description)
    public STUserStatus(final NdrInputStream ndrInputStream)
    '''
def clone():
    '''    public Object clone()
    '''
def dump():
    '''    public void dump(final NdrOutputStream ndrOutputStream)
    '''
def load():
    '''    public void load(final NdrInputStream ndrInputStream)
    '''
def getStatusType():
    '''    public synchronized short getStatusType()
    '''
def getTime():
    '''    public synchronized int getTime()
    '''
def getStatusDescription():
    '''    public synchronized String getStatusDescription()
    '''
def setStatusType():
    '''    public synchronized void setStatusType(final short type)
    '''
def isStatus():
    '''    public boolean isStatus(final short n)
    '''
