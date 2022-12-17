CONFIGURATION_FACTORY_PROPERTY = "String  \"log4j.configurationFactory\""
CONFIGURATION_FILE_PROPERTY = "String  \"log4j.configurationFile\""
LOG4J1_CONFIGURATION_FILE_PROPERTY = "String  \"log4j.configuration\""
LOG4J1_EXPERIMENTAL = "String  \"log4j1.compatibility\""
AUTHORIZATION_PROVIDER = "String  \"log4j2.authorizationProvider\""
CATEGORY = "String  \"ConfigurationFactory\""
def ():
    '''returns ConfigurationFactory\n\n
    ()\n
    '''
def getConfiguration():
    '''returns Configuration\n\n
    getConfiguration(final LoggerContext loggerContext, final String name, final URI configLocation)\n
    getConfiguration(final LoggerContext loggerContext, final String name, final URI configLocation, final ClassLoader loader)\n
    getConfiguration(final LoggerContext loggerContext, final String name, final URI configLocation)\n
    getConfiguration(final LoggerContext loggerContext, final ConfigurationSource source)\n
    '''
def getSupportedTypes():
    '''returns String[]\n\n
    getSupportedTypes()\n
    '''
