def DefaultLogBuilder():
    '''    public DefaultLogBuilder(final Logger logger, final Level level)
    public DefaultLogBuilder(final Logger logger)
    '''
def reset():
    '''    public LogBuilder reset(final Level level)
    '''
def withMarker():
    '''    public LogBuilder withMarker(final Marker marker)
    '''
def withThrowable():
    '''    public LogBuilder withThrowable(final Throwable throwable)
    '''
def withLocation():
    '''    public LogBuilder withLocation()
    public LogBuilder withLocation(final StackTraceElement location)
    '''
def isInUse():
    '''    public boolean isInUse()
    '''
def log():
    '''    public void log(final Message message)
    public void log(final CharSequence message)
    public void log(final String message)
    public void log(final String message, final Object... params)
    public void log(final String message, final Supplier<?>... params)
    public void log(final Supplier<Message> messageSupplier)
    public void log(final Object message)
    public void log(final String message, final Object p0)
    public void log(final String message, final Object p0, final Object p1)
    public void log(final String message, final Object p0, final Object p1, final Object p2)
    public void log(final String message, final Object p0, final Object p1, final Object p2, final Object p3)
    public void log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
    public void log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
    public void log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
    public void log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
    public void log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
    public void log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
    public void log()
    '''
