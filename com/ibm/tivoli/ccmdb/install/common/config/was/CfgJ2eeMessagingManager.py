def ():
    '''returns CfgJ2eeMessagingManager\n\n
    (final String wasUser, final String wasPassword, final String wasHostName, final String wasPort)\n
    '''
def getQueueDefinitions():
    '''returns List<JMSQueueDefinition>\n\n
    getQueueDefinitions()\n
    '''
def createServiceIntegrationBus():
    '''returns TaskResult\n\n
    createServiceIntegrationBus(final String siBusName, final String wasAppServerName, final String sibDatasourceName, final String sibDatasourceSchemaName, final boolean persistJmsMessages)\n
    '''
def deleteServiceIntegrationBus():
    '''returns TaskResult\n\n
    deleteServiceIntegrationBus(final String siBusName, final String wasAppServerName)\n
    '''
def validateServiceIntegrationBusExists():
    '''returns boolean\n\n
    validateServiceIntegrationBusExists(final String siBusName)\n
    '''
def validateServiceIntegrationBusConfigured():
    '''returns boolean\n\n
    validateServiceIntegrationBusConfigured(final String siBusName)\n
    '''
def jmsQueuesExist():
    '''returns TaskResult\n\n
    jmsQueuesExist(final String scope, final boolean continuousQueuesRequired)\n
    '''
def jmsActivationSpecExists():
    '''returns TaskResult\n\n
    jmsActivationSpecExists(final String scope)\n
    '''
def jmsErrorActivationSpecExists():
    '''returns TaskResult\n\n
    jmsErrorActivationSpecExists(final String scope)\n
    '''
def deleteJmsResources():
    '''returns TaskResult\n\n
    deleteJmsResources(final String serverName, final String siBusName)\n
    '''
def createJmsResources():
    '''returns TaskResult\n\n
    createJmsResources(final String siBusName, final String serverName)\n
    '''
def loadDBTenantList():
    '''returns Set<String>\n\n
    loadDBTenantList(final ReadConfiguration configProperties)\n
    '''
