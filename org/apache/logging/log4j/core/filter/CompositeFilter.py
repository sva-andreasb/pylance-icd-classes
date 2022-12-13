def addFilter():
    '''    public CompositeFilter addFilter(final Filter filter)
    '''
def removeFilter():
    '''    public CompositeFilter removeFilter(final Filter filter)
    '''
def iterator():
    '''    public Iterator<Filter> iterator()
    '''
def getFilters():
    '''    public List<Filter> getFilters()
    '''
def getFiltersArray():
    '''    public Filter[] getFiltersArray()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def size():
    '''    public int size()
    '''
def start():
    '''    public void start()
    '''
def stop():
    '''    public boolean stop(final long timeout, final TimeUnit timeUnit)
    '''
def getOnMismatch():
    '''    public Result getOnMismatch()
    '''
def getOnMatch():
    '''    public Result getOnMatch()
    '''
def filter():
    '''    public Result filter(final Logger logger, final Level level, final Marker marker, final String msg, final Object... params)
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
def toString():
    '''    public String toString()
    '''
def createFilters():
    '''    public static CompositeFilter createFilters(@PluginElement("Filters") final Filter[] filters)
    '''
