EXCEPTION_ALIEN_SECURITY_MANAGER = "String  \"ApplicationSecurityEnforcer.message.security.exception.alien.security.manager\""
EXCEPTION_NO_POLICY_FILE = "String  \"ApplicationSecurityEnforcer.message.null.pointer.exception.no.policy.file\""
PROPERTY_JAVA_SECURITY_POLICY = "String  \"java.security.policy\""
JAR_PROTOCOL = "String  \"jar:\""
JAR_URL_FILE_SEPARATOR = "String  \"!/\""
PROPERTY_APP_DEV_BASE = "String  \"app.dev.base\""
PROPERTY_APP_JAR_BASE = "String  \"app.jar.base\""
APP_MAIN_CLASS_DIR = "String  \"classes/\""
def ApplicationSecurityEnforcer():
    '''    public ApplicationSecurityEnforcer(final Class appMainClass, final String securityPolicy, final String appJarFile)
    public ApplicationSecurityEnforcer(final Class appMainClass, final String securityPolicy)
    '''
def enforceSecurity():
    '''    public void enforceSecurity(final boolean enforce)
    '''
def getPolicyURL():
    '''    public URL getPolicyURL()
    '''
def installSecurityManager():
    '''    public void installSecurityManager()
    '''
