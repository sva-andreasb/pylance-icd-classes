def PropertiesUtil():
'''public PropertiesUtil(final Properties props)
public PropertiesUtil(final String propertiesFileName)
'''
pass
def getProperties():
'''public static PropertiesUtil getProperties()
'''
pass
def hasProperty():
'''public boolean hasProperty(final String name)
'''
pass
def getBooleanProperty():
'''public boolean getBooleanProperty(final String name)
public boolean getBooleanProperty(final String name, final boolean defaultValue)
public boolean getBooleanProperty(final String name, final boolean defaultValueIfAbsent, final boolean defaultValueIfPresent)
public Boolean getBooleanProperty(final String[] prefixes, final String key, final Supplier<Boolean> supplier)
'''
pass
def getCharsetProperty():
'''public Charset getCharsetProperty(final String name)
public Charset getCharsetProperty(final String name, final Charset defaultValue)
'''
pass
def getDoubleProperty():
'''public double getDoubleProperty(final String name, final double defaultValue)
'''
pass
def getIntegerProperty():
'''public int getIntegerProperty(final String name, final int defaultValue)
public Integer getIntegerProperty(final String[] prefixes, final String key, final Supplier<Integer> supplier)
'''
pass
def getLongProperty():
'''public long getLongProperty(final String name, final long defaultValue)
public Long getLongProperty(final String[] prefixes, final String key, final Supplier<Long> supplier)
'''
pass
def getDurationProperty():
'''public Duration getDurationProperty(final String name, final Duration defaultValue)
public Duration getDurationProperty(final String[] prefixes, final String key, final Supplier<Duration> supplier)
'''
pass
def getStringProperty():
'''public String getStringProperty(final String[] prefixes, final String key, final Supplier<String> supplier)
public String getStringProperty(final String name)
public String getStringProperty(final String name, final String defaultValue)
'''
pass
def getSystemProperties():
'''public static Properties getSystemProperties()
'''
pass
def reload():
'''public void reload()
'''
pass
def extractSubset():
'''public static Properties extractSubset(final Properties properties, final String prefix)
'''
pass
def partitionOnCommonPrefixes():
'''public static Map<String, Properties> partitionOnCommonPrefixes(final Properties properties)
'''
pass
def isOsWindows():
'''public boolean isOsWindows()
'''
pass
