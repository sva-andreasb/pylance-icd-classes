def JAXRClient():
    '''    public JAXRClient(final String queryUrl, final String lifeCycleUrl, final String userid, final String password)
    '''
def releaseResources():
    '''    public void releaseResources()
    '''
def createBusinessEntity():
    '''    public String createBusinessEntity(final String businessName, final String description)
    '''
def isBusinessDefined():
    '''    public boolean isBusinessDefined(final String businessName)
    '''
def getBusinessEntity():
    '''    public Organization getBusinessEntity(final String businessName)
    '''
def deleteBusinessEntity():
    '''    public void deleteBusinessEntity(final String businessName)
    '''
def createService():
    '''    public String createService(final String businessName, final String serviceName, final String serviceDesc, final String accessUrl)
    public String createService(final Organization org, final String serviceName, final String serviceDesc, final String accessUrl)
    '''
def getService():
    '''    public Service getService(final String businessName, final String serviceName)
    '''
def getEndpointURL():
    '''    public String getEndpointURL(final String businessName, final String serviceName)
    '''
def deleteService():
    '''    public void deleteService(final String businessName, final String serviceName)
    '''
def createTModel():
    '''    public String createTModel(final String tomodelName, final String tmodelDesc, final String specUrl, final String specDesc)
    '''
def attachTModelToServiceBinding():
    '''    public void attachTModelToServiceBinding(final String serviceKeyId, final String conceptKeyId)
    public void attachTModelToServiceBinding(final ServiceBinding binding, final String conceptKeyId)
    '''
def getTModel():
    '''    public Concept getTModel(final String tmodelName)
    '''
def deleteTModel():
    '''    public void deleteTModel(final String tmodelName)
    '''
def getSpecURL():
    '''    public String getSpecURL(final String tmodelName)
    '''
def getServiceBinding():
    '''    public ServiceBinding getServiceBinding(final String serviceKeyId)
    '''
def registerService():
    '''    public void registerService(final String businessName, final String businessDesc, final String serviceName, final String serviceDesc, final String epUrl, final String tmodelName, final String tmodelDesc, final String specUrl, final String specDesc)
    '''
def main():
    '''    public static void main(final String[] args)
    '''
