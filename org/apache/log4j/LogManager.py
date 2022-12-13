DEFAULT_CONFIGURATION_FILE = "String  log4j.properties""
DEFAULT_CONFIGURATION_KEY = "String  log4j.configuration""
CONFIGURATOR_CLASS_KEY = "String  log4j.configuratorClass""
DEFAULT_INIT_OVERRIDE_KEY = "String  log4j.defaultInitOverride""
def getRootLogger():
'''public static Logger getRootLogger()
public Logger getRootLogger()
'''
pass
def getLogger():
'''public static Logger getLogger(final String name)
public static Logger getLogger(final Class<?> clazz)
public static Logger getLogger(final String name, final LoggerFactory factory)
public Logger getLogger(final String name)
public Logger getLogger(final String name, final LoggerFactory factory)
'''
pass
def exists():
'''public static Logger exists(final String name)
public Logger exists(final String name)
'''
pass
def getCurrentLoggers():
'''public static Enumeration getCurrentLoggers()
public Enumeration getCurrentLoggers()
'''
pass
def shutdown():
'''public static void shutdown()
public void shutdown()
'''
pass
def resetConfiguration():
'''public static void resetConfiguration()
public void resetConfiguration()
'''
pass
def setRepositorySelector():
'''public static void setRepositorySelector(final RepositorySelector selector, final Object guard)
'''
pass
def getLoggerRepository():
'''public static LoggerRepository getLoggerRepository()
'''
pass
def addHierarchyEventListener():
'''public void addHierarchyEventListener(final HierarchyEventListener listener)
'''
pass
def isDisabled():
'''public boolean isDisabled(final int level)
'''
pass
def setThreshold():
'''public void setThreshold(final Level level)
public void setThreshold(final String val)
'''
pass
def emitNoAppenderWarning():
'''public void emitNoAppenderWarning(final Category cat)
'''
pass
def getThreshold():
'''public Level getThreshold()
'''
pass
def getCurrentCategories():
'''public Enumeration getCurrentCategories()
'''
pass
def fireAddAppenderEvent():
'''public void fireAddAppenderEvent(final Category logger, final Appender appender)
'''
pass
def getContext():
'''public static LoggerContext getContext()
'''
pass
