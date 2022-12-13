MAX_STATUS_ENTRIES = "String  log4j2.status.entries""
DEFAULT_STATUS_LISTENER_LEVEL = "String  log4j2.StatusLogger.level""
STATUS_DATE_FORMAT = "String  log4j2.StatusLogger.DateFormat""
def getLogger():
'''public static StatusLogger getLogger()
'''
pass
def setLevel():
'''public void setLevel(final Level level)
'''
pass
def registerListener():
'''public void registerListener(final StatusListener listener)
'''
pass
def removeListener():
'''public void removeListener(final StatusListener listener)
'''
pass
def updateListenerLevel():
'''public void updateListenerLevel(final Level status)
'''
pass
def getListeners():
'''public Iterable<StatusListener> getListeners()
'''
pass
def reset():
'''public void reset()
'''
pass
def getStatusData():
'''public List<StatusData> getStatusData()
'''
pass
def clear():
'''public void clear()
'''
pass
def getLevel():
'''public Level getLevel()
'''
pass
def logMessage():
'''public void logMessage(final String fqcn, final Level level, final Marker marker, final Message msg, final Throwable t)
'''
pass
def isEnabled():
'''public boolean isEnabled(final Level level, final Marker marker, final String message, final Throwable t)
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
pass
def add():
'''public boolean add(final E object)
'''
pass
