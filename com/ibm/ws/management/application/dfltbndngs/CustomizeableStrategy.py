CONNFACT = "String  \"connection-factory\""
DATASOURCE = "String  \"data-source\""
EJB_BINDING = "String  \"ejb-binding\""
EJB_BINDINGS = "String  \"ejb-bindings\""
EJB_JAR_BINDING = "String  \"ejb-jar-binding\""
JAR_NAME = "String  \"jar-name\""
EJB_NAME = "String  \"ejb-name\""
GLOBAL_BINDINGS = "String  \"global-bindings\""
JAVA_BINDING = "String  \"java-binding\""
JNDI_NAME = "String  \"jndi-name\""
LISTERNER_PORT = "String  \"listener-port\""
ACTIVATIONSPEC_JNDI_NAME = "String  \"activationspec-jndi-name\""
MODULE_BINDINGS = "String  \"module-bindings\""
PASSWORD = "String  \"password\""
RESAUTH = "String  \"res-auth\""
EJB_REF = "String  \"ejb-ref-binding\""
EJB_REFS = "String  \"ejb-ref-bindings\""
EJB_REF_NAME = "String  \"ejb-ref-name\""
RESOURCE_ENV_REF = "String  \"resource-env-ref-binding\""
RESOURCE_ENV_REFS = "String  \"resource-env-ref-bindings\""
RESOURCE_ENV_REF_NAME = "String  \"resource-env-ref-name\""
RESOURCE_REF = "String  \"resource-ref-binding\""
RESOURCE_REFS = "String  \"resource-ref-bindings\""
RESOURCE_REF_NAME = "String  \"resource-ref-name\""
USER = "String  \"user\""
VIRTUAL_HOST = "String  \"virtual-host\""
WAR_BINDING = "String  \"war-binding\""
MSGDEST_REF = "String  \"message-destination-ref-binding\""
MSGDEST_REFS = "String  \"message-destination-ref-bindings\""
MSGDEST_REF_NAME = "String  \"message-destination-ref-name\""
LOGIN_CFG = "String  \"login-cfg\""
AUTH_PROPS = "String  \"auth-props\""
def ():
    '''returns EjbBindingMapElement\n\n
    ()\n
    (final Preferences prefs)\n
    (final String j, final String u, final String p, final String lc, final String ap)\n
    (final String j)\n
    (final String jndi, final DataSourceMapElement dsi, final ConnectionFactoryBinding cfb, final String listenerPort, final String actSpec)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
def parse():
    '''returns None\n\n
    parse(final String docuri)\n
    '''
def getDefaultDatasourceBindings():
    '''returns DataSourceBinding\n\n
    getDefaultDatasourceBindings(final String ejbJarName, final DataSourceBinding defaults, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getDefaultConnectionFactoryBindings():
    '''returns ConnectionFactoryBinding\n\n
    getDefaultConnectionFactoryBindings(final String ejbJarName, final ConnectionFactoryBinding defaults, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getEJBBinding():
    '''returns String\n\n
    getEJBBinding(final EjbId ejbInfo, final String defaultName, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getEJBConnectionFactoryBinding():
    '''returns ConnectionFactoryBinding\n\n
    getEJBConnectionFactoryBinding(final EjbId ejbInfo, final ConnectionFactoryBinding defaults, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getEJBDatasourceBinding():
    '''returns DataSourceBinding\n\n
    getEJBDatasourceBinding(final EjbId ejbInfo, final DataSourceBinding defaults, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getMDBListenerPort():
    '''returns String\n\n
    getMDBListenerPort(final String mdbName, final String defaults, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def hasMDBListenerPortCustom():
    '''returns boolean\n\n
    hasMDBListenerPortCustom(final String mdbName)\n
    '''
def getMDBActivationSpec():
    '''returns String\n\n
    getMDBActivationSpec(final String mdbName, final String defaults, final boolean bCreate, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getVirtualHost():
    '''returns String\n\n
    getVirtualHost(final String defaultBinding, final String moduleName, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getEJBRefBinding():
    '''returns String\n\n
    getEJBRefBinding(final EjbId ejbInfo, final String preExistingBinding, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getResourceRefBinding():
    '''returns ResourceRefMapElement\n\n
    getResourceRefBinding(final String resourceRefName, final String resourceType, final String moduleName, final String componentName, final String preExistingBinding, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getResourceEnvRefBinding():
    '''returns String\n\n
    getResourceEnvRefBinding(final String resourceEnvRefName, final String resourceType, final String moduleName, final String componentName, final String preExistingBinding, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def getMessageDestinationRefBinding():
    '''returns String\n\n
    getMessageDestinationRefBinding(final String messageDestinationRefName, final String linkName, final String moduleName, final String componentName, final String preExistingBinding, final BindingStrategy.WarningCollaborator warningCollaborator)\n
    '''
def setDataSourceBinding():
    '''returns None\n\n
    setDataSourceBinding(final String moduleName, final String ejbName, final String jndiName, final String user, final String password, final String loginCfg, final String authProps)\n
    '''
def setConnectionFactoryBinding():
    '''returns None\n\n
    setConnectionFactoryBinding(final String moduleName, final String ejbName, final String jndiName, final String resauth, final String loginCfg, final String authProps)\n
    '''
def setVirtualHost():
    '''returns None\n\n
    setVirtualHost(final String moduleName, final String virtualHost)\n
    '''
def setListenerPort():
    '''returns None\n\n
    setListenerPort(final String moduleName, final String ejbName, final String listenerPortName)\n
    '''
def setActivationSpecJNDIName():
    '''returns None\n\n
    setActivationSpecJNDIName(final String moduleName, final String ejbName, final String actSpec)\n
    '''
def setEjbJndiName():
    '''returns None\n\n
    setEjbJndiName(final String moduleName, final String ejbName, final String jndiName)\n
    '''
def setEjbDatasource():
    '''returns None\n\n
    setEjbDatasource(final String moduleName, final String ejbName, final String jndiName, final String user, final String password, final String loginCfg, final String authProps)\n
    '''
def setEjbConnectionFactory():
    '''returns None\n\n
    setEjbConnectionFactory(final String moduleName, final String ejbName, final String jndiName, final String resAuth, final String loginCfg, final String authProps)\n
    '''
def setEjbRefBinding():
    '''returns None\n\n
    setEjbRefBinding(final String moduleName, final String ejbRefName, final String jndiName)\n
    '''
def setResourceRefBinding():
    '''returns None\n\n
    setResourceRefBinding(final String moduleName, final String componentName, final String refName, final String jndiName, final String loginCfg, final String authProps)\n
    '''
def setResourceEnvRefBinding():
    '''returns None\n\n
    setResourceEnvRefBinding(final String moduleName, final String componentName, final String refName, final String jndiName)\n
    '''
def setMessageDestinationRefBinding():
    '''returns None\n\n
    setMessageDestinationRefBinding(final String moduleName, final String componentName, final String refName, final String jndiName)\n
    '''
