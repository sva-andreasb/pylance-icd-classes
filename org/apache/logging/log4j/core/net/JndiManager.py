def isJndiEnabled():
    '''public static boolean isJndiEnabled()
    '''
def isJndiContextSelectorEnabled():
    '''public static boolean isJndiContextSelectorEnabled()
    '''
def isJndiJdbcEnabled():
    '''public static boolean isJndiJdbcEnabled()
    '''
def isJndiJmsEnabled():
    '''public static boolean isJndiJmsEnabled()
    '''
def isJndiLookupEnabled():
    '''public static boolean isJndiLookupEnabled()
    '''
def getDefaultManager():
    '''public static JndiManager getDefaultManager()
    public static JndiManager getDefaultManager(final String name)
    '''
def getJndiManager():
    '''public static JndiManager getJndiManager(final String initialContextFactoryName, final String providerURL, final String urlPkgPrefixes, final String securityPrincipal, final String securityCredentials, final Properties additionalProperties)
    public static JndiManager getJndiManager(final Properties properties)
    '''
def createProperties():
    '''public static Properties createProperties(final String initialContextFactoryName, final String providerURL, final String urlPkgPrefixes, final String securityPrincipal, final String securityCredentials, final Properties additionalProperties)
    '''
def lookup():
    '''public <T> T lookup(final String name)
    '''
def toString():
    '''public String toString()
    '''
def createManager():
    '''public JndiManager createManager(final String name, final Properties data)
    '''
