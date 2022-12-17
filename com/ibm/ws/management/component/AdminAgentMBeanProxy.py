def ():
    '''returns AdminAgentMBeanProxy\n\n
    ()\n
    '''
def getAdminStack():
    '''returns Map\n\n
    getAdminStack()\n
    '''
def addService():
    '''returns Object\n\n
    addService(final String serviceName, final Object serviceImpl)\n
    '''
def getService():
    '''returns Object\n\n
    getService(final String serviceName)\n
    '''
def removeService():
    '''returns Object\n\n
    removeService(final String serviceName)\n
    '''
def handleServantNotification():
    '''returns None\n\n
    handleServantNotification(final Notification notification)\n
    '''
def initializeAdminSubsystem():
    '''returns None\n\n
    initializeAdminSubsystem(final String uuid)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def destroyAdminSubsystem():
    '''returns None\n\n
    destroyAdminSubsystem(final String uuid)\n
    '''
def listManagedNodesUUIDs():
    '''returns String[]\n\n
    listManagedNodesUUIDs()\n
    '''
def getManagedNodeInfo():
    '''returns Map\n\n
    getManagedNodeInfo(final String profileKey)\n
    '''
def isAdminSubsystemStarted():
    '''returns boolean\n\n
    isAdminSubsystemStarted(final String uuid)\n
    '''
def addProfileDownstreamProcess():
    '''returns None\n\n
    addProfileDownstreamProcess(final String remoteProfileKey)\n
    '''
def createControlAdminService():
    '''returns None\n\n
    createControlAdminService()\n
    '''
def startAdminSubsystem():
    '''returns None\n\n
    startAdminSubsystem(final String uuid)\n
    '''
def stopAdminSubsystem():
    '''returns None\n\n
    stopAdminSubsystem(final String uuid)\n
    '''
def setAndThrowAdminException():
    '''returns None\n\n
    setAndThrowAdminException(final String key, final String defaultMsg, final Object[] args)\n
    '''
def removeProfileDownstreamProcess():
    '''returns None\n\n
    removeProfileDownstreamProcess(final String remoteProfileKey)\n
    '''
