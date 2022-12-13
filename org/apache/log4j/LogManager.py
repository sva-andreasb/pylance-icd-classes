DEFAULT_CONFIGURATION_FILE = "String  \"log4j.properties\""
DEFAULT_CONFIGURATION_KEY = "String  \"log4j.configuration\""
CONFIGURATOR_CLASS_KEY = "String  \"log4j.configuratorClass\""
DEFAULT_INIT_OVERRIDE_KEY = "String  \"log4j.defaultInitOverride\""
def getRootLogger():
    '''public static Logger getRootLogger()
    public Logger getRootLogger()
    '''
def getLogger():
    '''public static Logger getLogger(final String name)
    public static Logger getLogger(final Class<?> clazz)
    public static Logger getLogger(final String name, final LoggerFactory factory)
    public Logger getLogger(final String name)
    public Logger getLogger(final String name, final LoggerFactory factory)
    '''
def exists():
    '''public static Logger exists(final String name)
    public Logger exists(final String name)
    '''
def getCurrentLoggers():
    '''public static Enumeration getCurrentLoggers()
    public Enumeration getCurrentLoggers()
    '''
def shutdown():
    '''public static void shutdown()
    public void shutdown()
    '''
def resetConfiguration():
    '''public static void resetConfiguration()
    public void resetConfiguration()
    '''
def setRepositorySelector():
    '''public static void setRepositorySelector(final RepositorySelector selector, final Object guard)
    '''
def getLoggerRepository():
    '''public static LoggerRepository getLoggerRepository()
    '''
def addHierarchyEventListener():
    '''public void addHierarchyEventListener(final HierarchyEventListener listener)
    '''
def isDisabled():
    '''public boolean isDisabled(final int level)
    '''
def setThreshold():
    '''public void setThreshold(final Level level)
    public void setThreshold(final String val)
    '''
def emitNoAppenderWarning():
    '''public void emitNoAppenderWarning(final Category cat)
    '''
def getThreshold():
    '''public Level getThreshold()
    '''
def getCurrentCategories():
    '''public Enumeration getCurrentCategories()
    '''
def fireAddAppenderEvent():
    '''public void fireAddAppenderEvent(final Category logger, final Appender appender)
    '''
def getContext():
    '''public static LoggerContext getContext()
    '''
