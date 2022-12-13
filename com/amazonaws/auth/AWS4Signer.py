def AWS4Signer():
    '''public AWS4Signer()
    public AWS4Signer(final boolean doubleUrlEncoding)
    '''
def setServiceName():
    '''public void setServiceName(final String serviceName)
    '''
def setRegionName():
    '''public void setRegionName(final String regionName)
    '''
def getRegionName():
    '''public String getRegionName()
    '''
def getServiceName():
    '''public String getServiceName()
    '''
def getOverriddenDate():
    '''public Date getOverriddenDate()
    '''
def sign():
    '''public void sign(final SignableRequest<?> request, final AWSCredentials credentials)
    '''
def presignRequest():
    '''public void presignRequest(final SignableRequest<?> request, final AWSCredentials credentials, final Date userSpecifiedExpirationDate)
    '''
