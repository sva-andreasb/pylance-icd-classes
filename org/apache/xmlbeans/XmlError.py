SEVERITY_ERROR = "int  0"
SEVERITY_WARNING = "int  1"
SEVERITY_INFO = "int  2"
def XmlError():
    '''public XmlError(final XmlError src)
    '''
def forMessage():
    '''public static XmlError forMessage(final String message)
    public static XmlError forMessage(final String message, final int severity)
    public static XmlError forMessage(final String code, final Object[] args)
    public static XmlError forMessage(final String code, final Object[] args, final int severity)
    '''
def forSource():
    '''public static XmlError forSource(final String message, final String sourceName)
    public static XmlError forSource(final String message, final int severity, final String sourceName)
    public static XmlError forSource(final String code, final Object[] args, final int severity, final String sourceName)
    '''
def forLocation():
    '''public static XmlError forLocation(final String message, final String sourceName, final Location location)
    public static XmlError forLocation(final String message, final String sourceName, final int line, final int column, final int offset)
    public static XmlError forLocation(final String code, final Object[] args, final int severity, final String sourceName, final int line, final int column, final int offset)
    public static XmlError forLocation(final String message, final int severity, final String sourceName, final int line, final int column, final int offset)
    '''
def forLocationAndCursor():
    '''public static XmlError forLocationAndCursor(final String message, final int severity, final String sourceName, final int line, final int column, final int offset, final XmlCursor cursor)
    '''
def forObject():
    '''public static XmlError forObject(final String message, final XmlObject xobj)
    public static XmlError forObject(final String code, final Object[] args, final XmlObject xobj)
    public static XmlError forObject(final String message, final int severity, final XmlObject xobj)
    public static XmlError forObject(final String code, final Object[] args, final int severity, final XmlObject xobj)
    '''
def forCursor():
    '''public static XmlError forCursor(final String message, final XmlCursor cursor)
    public static XmlError forCursor(final String code, final Object[] args, final XmlCursor cursor)
    public static XmlError forCursor(final String message, final int severity, final XmlCursor cursor)
    public static XmlError forCursor(final String code, final Object[] args, final int severity, final XmlCursor cursor)
    '''
def formattedMessage():
    '''public static String formattedMessage(final String code, final Object[] args)
    '''
def getSeverity():
    '''public int getSeverity()
    '''
def getMessage():
    '''public String getMessage()
    '''
def getErrorCode():
    '''public String getErrorCode()
    '''
def getSourceName():
    '''public String getSourceName()
    '''
def getLine():
    '''public int getLine()
    '''
def getColumn():
    '''public int getColumn()
    '''
def getOffset():
    '''public int getOffset()
    '''
def getLocation():
    '''public Object getLocation(final Object type)
    '''
def getCursorLocation():
    '''public XmlCursor getCursorLocation()
    '''
def getObjectLocation():
    '''public XmlObject getObjectLocation()
    '''
def toString():
    '''public String toString()
    public String toString(final URI base)
    '''
def severityAsString():
    '''public static String severityAsString(final int severity)
    '''
