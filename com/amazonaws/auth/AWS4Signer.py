def ():
    '''returns AWS4Signer\n\n
    ()\n
    (final boolean doubleUrlEncoding)\n
    '''
def setServiceName():
    '''returns None\n\n
    setServiceName(final String serviceName)\n
    '''
def setRegionName():
    '''returns None\n\n
    setRegionName(final String regionName)\n
    '''
def getRegionName():
    '''returns String\n\n
    getRegionName()\n
    '''
def getServiceName():
    '''returns String\n\n
    getServiceName()\n
    '''
def getOverriddenDate():
    '''returns Date\n\n
    getOverriddenDate()\n
    '''
def sign():
    '''returns None\n\n
    sign(final SignableRequest<?> request, final AWSCredentials credentials)\n
    '''
def presignRequest():
    '''returns None\n\n
    presignRequest(final SignableRequest<?> request, final AWSCredentials credentials, final Date userSpecifiedExpirationDate)\n
    '''
