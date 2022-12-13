def Principal():
    '''    public Principal(final Services service)
    public Principal(final String accountId)
    public Principal(final String provider, final String id)
    public Principal(final String provider, final String id, final boolean stripHyphen)
    public Principal(final WebIdentityProviders webIdentityProvider)
    '''
def getProvider():
    '''    public String getProvider()
    '''
def getId():
    '''    public String getId()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object principal)
    '''
def getServiceId():
    '''    public String getServiceId()
    '''
def fromString():
    '''    public static Services fromString(final String serviceId)
    public static WebIdentityProviders fromString(final String webIdentityProvider)
    '''
def getWebIdentityProvider():
    '''    public String getWebIdentityProvider()
    '''
