DEFAULT_MODE = "int  0"
UNIQUE_NAMES_MODE = "int  1"
JNDIPREFIX_ACTSPEC = "String  \"eis/\""
JNDIPREFIX_ADMINOBJECT = "String  \"eis/\""
def ():
    '''returns DefaultStrategy\n\n
    ()\n
    (final Preferences preferences)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getEJBBinding():
    '''returns String\n\n
    getEJBBinding(final EjbId ejbInfo, final String defaultName, final WarningCollaborator warningCollaborator)\n
    '''
def getEJBDatasourceBinding():
    '''returns DataSourceBinding\n\n
    getEJBDatasourceBinding(final EjbId ejbInfo, final DataSourceBinding defaults, final WarningCollaborator warningCollaborator)\n
    '''
def getEJBRefBinding():
    '''returns String\n\n
    getEJBRefBinding(final EjbId ejbInfo, final String defaultBinding, final WarningCollaborator warningCollaborator)\n
    '''
def getResourceRefBinding():
    '''returns ResourceRefMapElement\n\n
    getResourceRefBinding(final String resourceRefName, final String resourceType, final String moduleName, final String componentName, final String defaultBinding, final WarningCollaborator warningCollaborator)\n
    '''
def getVirtualHost():
    '''returns String\n\n
    getVirtualHost(final String defaultBinding, final String moduleName, final WarningCollaborator warningCollaborator)\n
    '''
def getDefaultDatasourceBindings():
    '''returns DataSourceBinding\n\n
    getDefaultDatasourceBindings(final String ejbJarName, final DataSourceBinding defaults, final WarningCollaborator warningCollaborator)\n
    '''
def getResourceEnvRefBinding():
    '''returns String\n\n
    getResourceEnvRefBinding(final String resourceEnvRefName, final String resourceType, final String moduleName, final String componentName, final String defaultBinding, final WarningCollaborator warningCollaborator)\n
    '''
def getMessageDestinationRefBinding():
    '''returns String\n\n
    getMessageDestinationRefBinding(final String mdRefName, final String linkName, final String moduleName, final String componentName, final String preExistingBinding, final WarningCollaborator warningCollaborator)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final int mode)\n
    '''
def setPreferences():
    '''returns None\n\n
    setPreferences(final Preferences prefs)\n
    '''
def getDefaultConnectionFactoryBindings():
    '''returns ConnectionFactoryBinding\n\n
    getDefaultConnectionFactoryBindings(final String ejbJarName, final ConnectionFactoryBinding defaults, final WarningCollaborator warningCollaborator)\n
    '''
def getEJBConnectionFactoryBinding():
    '''returns ConnectionFactoryBinding\n\n
    getEJBConnectionFactoryBinding(final EjbId ejbInfo, final ConnectionFactoryBinding defaults, final WarningCollaborator warningCollaborator)\n
    '''
def getMDBListenerPort():
    '''returns String\n\n
    getMDBListenerPort(final String mdbName, final String defaultListener, final WarningCollaborator warningCollaborator)\n
    '''
def getMDBActivationSpec():
    '''returns String\n\n
    getMDBActivationSpec(final String mdbName, final String defaultJNDI, final boolean bCreate, final WarningCollaborator warningCollaborator)\n
    '''
