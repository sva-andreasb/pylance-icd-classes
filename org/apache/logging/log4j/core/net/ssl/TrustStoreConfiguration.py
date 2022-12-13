def TrustStoreConfiguration():
'''public TrustStoreConfiguration(final String location, final PasswordProvider passwordProvider, final String keyStoreType, final String trustManagerFactoryAlgorithm)
public TrustStoreConfiguration(final String location, final char[] password, final String keyStoreType, final String trustManagerFactoryAlgorithm)
public TrustStoreConfiguration(final String location, final String password, final String keyStoreType, final String trustManagerFactoryAlgorithm)
'''
pass
def createKeyStoreConfiguration():
'''public static TrustStoreConfiguration createKeyStoreConfiguration(@PluginAttribute("location") final String location, @PluginAttribute(value = "password", sensitive = true) final char[] password, @PluginAttribute("passwordEnvironmentVariable") final String passwordEnvironmentVariable, @PluginAttribute("passwordFile") final String passwordFile, @PluginAttribute("type") final String keyStoreType, @PluginAttribute("trustManagerFactoryAlgorithm") final String trustManagerFactoryAlgorithm)
public static TrustStoreConfiguration createKeyStoreConfiguration(final String location, final char[] password, final String keyStoreType, final String trustManagerFactoryAlgorithm)
public static TrustStoreConfiguration createKeyStoreConfiguration(final String location, final String password, final String keyStoreType, final String trustManagerFactoryAlgorithm)
'''
pass
def initTrustManagerFactory():
'''public TrustManagerFactory initTrustManagerFactory()
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
def getTrustManagerFactoryAlgorithm():
'''public String getTrustManagerFactoryAlgorithm()
'''
pass
