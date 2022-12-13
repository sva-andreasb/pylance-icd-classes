def addFilter():
'''public CompositeFilter addFilter(final Filter filter)
'''
pass
def removeFilter():
'''public CompositeFilter removeFilter(final Filter filter)
'''
pass
def iterator():
'''public Iterator<Filter> iterator()
'''
pass
def getFilters():
'''public List<Filter> getFilters()
'''
pass
def getFiltersArray():
'''public Filter[] getFiltersArray()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def size():
'''public int size()
'''
pass
def start():
'''public void start()
'''
pass
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def getOnMismatch():
'''public Result getOnMismatch()
'''
pass
def getOnMatch():
'''public Result getOnMatch()
'''
pass
def filter():
'''public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object... params)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2, final Object p3)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public Result filter(final Logger logger, final Level level, final Marker marker, final Object msg, final Throwable t)
public Result filter(final Logger logger, final Level level, final Marker marker, final Message msg, final Throwable t)
public Result filter(final LogEvent event)
'''
pass
def toString():
'''public String toString()
'''
pass
def createFilters():
'''public static CompositeFilter createFilters(@PluginElement("Filters") final Filter[] filters)
'''
pass
