def ():
    '''returns JAXRClient\n\n
    (final String queryUrl, final String lifeCycleUrl, final String userid, final String password)\n
    '''
def releaseResources():
    '''returns None\n\n
    releaseResources()\n
    '''
def createBusinessEntity():
    '''returns String\n\n
    createBusinessEntity(final String businessName, final String description)\n
    '''
def isBusinessDefined():
    '''returns boolean\n\n
    isBusinessDefined(final String businessName)\n
    '''
def getBusinessEntity():
    '''returns Organization\n\n
    getBusinessEntity(final String businessName)\n
    '''
def deleteBusinessEntity():
    '''returns None\n\n
    deleteBusinessEntity(final String businessName)\n
    '''
def createService():
    '''returns String\n\n
    createService(final String businessName, final String serviceName, final String serviceDesc, final String accessUrl)\n
    createService(final Organization org, final String serviceName, final String serviceDesc, final String accessUrl)\n
    '''
def getService():
    '''returns Service\n\n
    getService(final String businessName, final String serviceName)\n
    '''
def getEndpointURL():
    '''returns String\n\n
    getEndpointURL(final String businessName, final String serviceName)\n
    '''
def deleteService():
    '''returns None\n\n
    deleteService(final String businessName, final String serviceName)\n
    '''
def createTModel():
    '''returns String\n\n
    createTModel(final String tomodelName, final String tmodelDesc, final String specUrl, final String specDesc)\n
    '''
def attachTModelToServiceBinding():
    '''returns None\n\n
    attachTModelToServiceBinding(final String serviceKeyId, final String conceptKeyId)\n
    attachTModelToServiceBinding(final ServiceBinding binding, final String conceptKeyId)\n
    '''
def getTModel():
    '''returns Concept\n\n
    getTModel(final String tmodelName)\n
    '''
def deleteTModel():
    '''returns None\n\n
    deleteTModel(final String tmodelName)\n
    '''
def getSpecURL():
    '''returns String\n\n
    getSpecURL(final String tmodelName)\n
    '''
def getServiceBinding():
    '''returns ServiceBinding\n\n
    getServiceBinding(final String serviceKeyId)\n
    '''
def registerService():
    '''returns None\n\n
    registerService(final String businessName, final String businessDesc, final String serviceName, final String serviceDesc, final String epUrl, final String tmodelName, final String tmodelDesc, final String specUrl, final String specDesc)\n
    '''
