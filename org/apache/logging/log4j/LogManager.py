FACTORY_PROPERTY_NAME = "String  log4j2.loggerContextFactory""
ROOT_LOGGER_NAME = "String  "
def exists():
'''public static boolean exists(final String name)
'''
pass
def getContext():
'''public static LoggerContext getContext()
public static LoggerContext getContext(final boolean currentContext)
public static LoggerContext getContext(final ClassLoader loader, final boolean currentContext)
public static LoggerContext getContext(final ClassLoader loader, final boolean currentContext, final Object externalContext)
public static LoggerContext getContext(final ClassLoader loader, final boolean currentContext, final URI configLocation)
public static LoggerContext getContext(final ClassLoader loader, final boolean currentContext, final Object externalContext, final URI configLocation)
public static LoggerContext getContext(final ClassLoader loader, final boolean currentContext, final Object externalContext, final URI configLocation, final String name)
'''
pass
def shutdown():
'''public static void shutdown()
public static void shutdown(final boolean currentContext)
public static void shutdown(final boolean currentContext, final boolean allContexts)
public static void shutdown(final LoggerContext context)
'''
pass
def getFactory():
'''public static LoggerContextFactory getFactory()
'''
pass
def setFactory():
'''public static void setFactory(final LoggerContextFactory factory)
'''
pass
def getFormatterLogger():
'''public static Logger getFormatterLogger()
public static Logger getFormatterLogger(final Class<?> clazz)
public static Logger getFormatterLogger(final Object value)
public static Logger getFormatterLogger(final String name)
'''
pass
def getLogger():
'''public static Logger getLogger()
public static Logger getLogger(final Class<?> clazz)
public static Logger getLogger(final Class<?> clazz, final MessageFactory messageFactory)
public static Logger getLogger(final MessageFactory messageFactory)
public static Logger getLogger(final Object value)
public static Logger getLogger(final Object value, final MessageFactory messageFactory)
public static Logger getLogger(final String name)
public static Logger getLogger(final String name, final MessageFactory messageFactory)
'''
pass
def getRootLogger():
'''public static Logger getRootLogger()
'''
pass
