def ():
    '''returns PropertiesUtil\n\n
    (final Properties props)\n
    (final String propertiesFileName)\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final String name)\n
    '''
def getBooleanProperty():
    '''returns Boolean\n\n
    getBooleanProperty(final String name)\n
    getBooleanProperty(final String name, final boolean defaultValue)\n
    getBooleanProperty(final String name, final boolean defaultValueIfAbsent, final boolean defaultValueIfPresent)\n
    getBooleanProperty(final String[] prefixes, final String key, final Supplier<Boolean> supplier)\n
    '''
def getCharsetProperty():
    '''returns Charset\n\n
    getCharsetProperty(final String name)\n
    getCharsetProperty(final String name, final Charset defaultValue)\n
    '''
def getDoubleProperty():
    '''returns double\n\n
    getDoubleProperty(final String name, final double defaultValue)\n
    '''
def getIntegerProperty():
    '''returns Integer\n\n
    getIntegerProperty(final String name, final int defaultValue)\n
    getIntegerProperty(final String[] prefixes, final String key, final Supplier<Integer> supplier)\n
    '''
def getLongProperty():
    '''returns Long\n\n
    getLongProperty(final String name, final long defaultValue)\n
    getLongProperty(final String[] prefixes, final String key, final Supplier<Long> supplier)\n
    '''
def getDurationProperty():
    '''returns Duration\n\n
    getDurationProperty(final String name, final Duration defaultValue)\n
    getDurationProperty(final String[] prefixes, final String key, final Supplier<Duration> supplier)\n
    '''
def getStringProperty():
    '''returns String\n\n
    getStringProperty(final String[] prefixes, final String key, final Supplier<String> supplier)\n
    getStringProperty(final String name)\n
    getStringProperty(final String name, final String defaultValue)\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    '''
def isOsWindows():
    '''returns boolean\n\n
    isOsWindows()\n
    '''
