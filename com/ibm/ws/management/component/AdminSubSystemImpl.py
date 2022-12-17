def ():
    '''returns AdminSubSystemImpl\n\n
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
def initialize():
    '''returns None\n\n
    initialize(final Object config)\n
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
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def destroyAdminSubsystem():
    '''returns None\n\n
    destroyAdminSubsystem(final String uuid)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def startAdminSubsystem():
    '''returns None\n\n
    startAdminSubsystem(final String uuid)\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def stopAdminSubsystem():
    '''returns None\n\n
    stopAdminSubsystem(final String uuid)\n
    '''
def initializeConnectors():
    '''returns None\n\n
    initializeConnectors(final String remoteProfileKey)\n
    '''
def setAndThrowAdminException():
    '''returns None\n\n
    setAndThrowAdminException(final String key, final String defaultMsg, final Object[] args)\n
    '''
def listManagedNodesUUIDs():
    '''returns String[]\n\n
    listManagedNodesUUIDs()\n
    '''
def getManagedNodeInfo():
    '''returns Map\n\n
    getManagedNodeInfo(final String uuid)\n
    '''
def isAdminSubsystemStarted():
    '''returns boolean\n\n
    isAdminSubsystemStarted(final String uuid)\n
    '''
