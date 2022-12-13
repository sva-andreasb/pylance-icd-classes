MAX_STATUS_ENTRIES = "String  \"log4j2.status.entries\""
DEFAULT_STATUS_LISTENER_LEVEL = "String  \"log4j2.StatusLogger.level\""
STATUS_DATE_FORMAT = "String  \"log4j2.StatusLogger.DateFormat\""
def getLogger():
    '''    public static StatusLogger getLogger()
    '''
def setLevel():
    '''    public void setLevel(final Level level)
    '''
def registerListener():
    '''    public void registerListener(final StatusListener listener)
    '''
def removeListener():
    '''    public void removeListener(final StatusListener listener)
    '''
def updateListenerLevel():
    '''    public void updateListenerLevel(final Level status)
    '''
def getListeners():
    '''    public Iterable<StatusListener> getListeners()
    '''
def reset():
    '''    public void reset()
    '''
def getStatusData():
    '''    public List<StatusData> getStatusData()
    '''
def clear():
    '''    public void clear()
    '''
def getLevel():
    '''    public Level getLevel()
    '''
def logMessage():
    '''    public void logMessage(final String fqcn, final Level level, final Marker marker, final Message msg, final Throwable t)
    '''
def isEnabled():
    '''    public boolean isEnabled(final Level level, final Marker marker, final String message, final Throwable t)
    public boolean isEnabled(final Level level, final Marker marker, final String message)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object... params)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
    public boolean isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
    public boolean isEnabled(final Level level, final Marker marker, final CharSequence message, final Throwable t)
    public boolean isEnabled(final Level level, final Marker marker, final Object message, final Throwable t)
    public boolean isEnabled(final Level level, final Marker marker, final Message message, final Throwable t)
    public boolean isEnabled(final Level level, final Marker marker)
    '''
def add():
    '''    public boolean add(final E object)
    '''
