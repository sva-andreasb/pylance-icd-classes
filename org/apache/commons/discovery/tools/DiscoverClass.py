def DiscoverClass():
    '''    public DiscoverClass()
    public DiscoverClass(final ClassLoaders classLoaders)
    '''
def getClassLoaders():
    '''    public ClassLoaders getClassLoaders(final Class spiClass)
    '''
def find():
    '''    public Class find(final Class spiClass)
    public Class find(final Class spiClass, final Properties properties)
    public Class find(final Class spiClass, final String defaultImpl)
    public Class find(final Class spiClass, final Properties properties, final String defaultImpl)
    public Class find(final Class spiClass, final String propertiesFileName, final String defaultImpl)
    public static Class find(ClassLoaders loaders, final SPInterface spi, final PropertiesHolder properties, final DefaultClassHolder defaultImpl)
    '''
def newInstance():
    '''    public Object newInstance(final Class spiClass)
    public Object newInstance(final Class spiClass, final Properties properties)
    public Object newInstance(final Class spiClass, final String defaultImpl)
    public Object newInstance(final Class spiClass, final Properties properties, final String defaultImpl)
    public Object newInstance(final Class spiClass, final String propertiesFileName, final String defaultImpl)
    public static Object newInstance(final ClassLoaders loaders, final SPInterface spi, final PropertiesHolder properties, final DefaultClassHolder defaultImpl)
    '''
def discoverClassNames():
    '''    public static String[] discoverClassNames(final SPInterface spi, final Properties properties)
    '''
def getManagedProperty():
    '''    public static String getManagedProperty(final String propertyName)
    '''
