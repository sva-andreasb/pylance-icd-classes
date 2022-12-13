def KeyStoreConfiguration():
'''public KeyStoreConfiguration(final String location, final PasswordProvider passwordProvider, final String keyStoreType, final String keyManagerFactoryAlgorithm)
public KeyStoreConfiguration(final String location, final char[] password, final String keyStoreType, final String keyManagerFactoryAlgorithm)
public KeyStoreConfiguration(final String location, final String password, final String keyStoreType, final String keyManagerFactoryAlgorithm)
'''
pass
def createKeyStoreConfiguration():
'''public static KeyStoreConfiguration createKeyStoreConfiguration(@PluginAttribute("location") final String location, @PluginAttribute(value = "password", sensitive = true) final char[] password, @PluginAttribute("passwordEnvironmentVariable") final String passwordEnvironmentVariable, @PluginAttribute("passwordFile") final String passwordFile, @PluginAttribute("type") final String keyStoreType, @PluginAttribute("keyManagerFactoryAlgorithm") final String keyManagerFactoryAlgorithm)
public static KeyStoreConfiguration createKeyStoreConfiguration(final String location, final char[] password, final String keyStoreType, final String keyManagerFactoryAlgorithm)
public static KeyStoreConfiguration createKeyStoreConfiguration(final String location, final String password, final String keyStoreType, final String keyManagerFactoryAlgorithm)
'''
pass
def initKeyManagerFactory():
'''public KeyManagerFactory initKeyManagerFactory()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def getKeyManagerFactoryAlgorithm():
'''public String getKeyManagerFactoryAlgorithm()
'''
pass
