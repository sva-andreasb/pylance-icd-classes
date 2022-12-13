def JAXRClient():
'''public JAXRClient(final String queryUrl, final String lifeCycleUrl, final String userid, final String password)
'''
pass
def releaseResources():
'''public void releaseResources()
'''
pass
def createBusinessEntity():
'''public String createBusinessEntity(final String businessName, final String description)
'''
pass
def isBusinessDefined():
'''public boolean isBusinessDefined(final String businessName)
'''
pass
def getBusinessEntity():
'''public Organization getBusinessEntity(final String businessName)
'''
pass
def deleteBusinessEntity():
'''public void deleteBusinessEntity(final String businessName)
'''
pass
def createService():
'''public String createService(final String businessName, final String serviceName, final String serviceDesc, final String accessUrl)
public String createService(final Organization org, final String serviceName, final String serviceDesc, final String accessUrl)
'''
pass
def getService():
'''public Service getService(final String businessName, final String serviceName)
'''
pass
def getEndpointURL():
'''public String getEndpointURL(final String businessName, final String serviceName)
'''
pass
def deleteService():
'''public void deleteService(final String businessName, final String serviceName)
'''
pass
def createTModel():
'''public String createTModel(final String tomodelName, final String tmodelDesc, final String specUrl, final String specDesc)
'''
pass
def attachTModelToServiceBinding():
'''public void attachTModelToServiceBinding(final String serviceKeyId, final String conceptKeyId)
public void attachTModelToServiceBinding(final ServiceBinding binding, final String conceptKeyId)
'''
pass
def getTModel():
'''public Concept getTModel(final String tmodelName)
'''
pass
def deleteTModel():
'''public void deleteTModel(final String tmodelName)
'''
pass
def getSpecURL():
'''public String getSpecURL(final String tmodelName)
'''
pass
def getServiceBinding():
'''public ServiceBinding getServiceBinding(final String serviceKeyId)
'''
pass
def registerService():
'''public void registerService(final String businessName, final String businessDesc, final String serviceName, final String serviceDesc, final String epUrl, final String tmodelName, final String tmodelDesc, final String specUrl, final String specDesc)
'''
pass
def main():
'''public static void main(final String[] args)
'''
pass
