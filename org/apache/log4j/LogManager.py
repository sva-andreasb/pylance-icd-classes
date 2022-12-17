DEFAULT_CONFIGURATION_FILE = "String  \"log4j.properties\""
DEFAULT_CONFIGURATION_KEY = "String  \"log4j.configuration\""
CONFIGURATOR_CLASS_KEY = "String  \"log4j.configuratorClass\""
DEFAULT_INIT_OVERRIDE_KEY = "String  \"log4j.defaultInitOverride\""
def addHierarchyEventListener():
    '''returns None\n\n
    addHierarchyEventListener(final HierarchyEventListener listener)\n
    '''
def isDisabled():
    '''returns boolean\n\n
    isDisabled(final int level)\n
    '''
def setThreshold():
    '''returns None\n\n
    setThreshold(final Level level)\n
    setThreshold(final String val)\n
    '''
def emitNoAppenderWarning():
    '''returns None\n\n
    emitNoAppenderWarning(final Category cat)\n
    '''
def getThreshold():
    '''returns Level\n\n
    getThreshold()\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger(final String name)\n
    getLogger(final String name, final LoggerFactory factory)\n
    '''
def getRootLogger():
    '''returns Logger\n\n
    getRootLogger()\n
    '''
def exists():
    '''returns Logger\n\n
    exists(final String name)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getCurrentLoggers():
    '''returns Enumeration\n\n
    getCurrentLoggers()\n
    '''
def getCurrentCategories():
    '''returns Enumeration\n\n
    getCurrentCategories()\n
    '''
def fireAddAppenderEvent():
    '''returns None\n\n
    fireAddAppenderEvent(final Category logger, final Appender appender)\n
    '''
def resetConfiguration():
    '''returns None\n\n
    resetConfiguration()\n
    '''
