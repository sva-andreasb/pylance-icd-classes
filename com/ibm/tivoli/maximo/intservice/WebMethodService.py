def action():
    '''    public byte[] action(final byte[] actionData, final String maxServiceName)
    '''
def wsAction():
    '''    public byte[] wsAction(final byte[] actionData, final String wsName)
    '''
def maxSecureAction():
    '''    public byte[] maxSecureAction(final String loginid, final String password, final byte[] actionData, final String maxServiceName)
    '''
def maxAPIKeySecureAction():
    '''    public byte[] maxAPIKeySecureAction(final String apikey, final byte[] actionData, final String maxServiceName)
    '''
def wsMaxAPIKeySecureAction():
    '''    public byte[] wsMaxAPIKeySecureAction(final String apikey, final byte[] actionData, final String wsName)
    '''
def wsMaxSecureAction():
    '''    public byte[] wsMaxSecureAction(final String loginid, final String password, final byte[] actionData, final String wsName)
    '''
def secureAction():
    '''    public byte[] secureAction(final byte[] actionData, final String maxServiceName, final Principal principal)
    '''
def wsSecureAction():
    '''    public byte[] wsSecureAction(final byte[] actionData, final String wsName, final Principal principal)
    '''
def getDBConnection():
    '''    public Connection getDBConnection(final ConnectionKey conKey)
    '''
def freeDBConnection():
    '''    public void freeDBConnection(final ConnectionKey conKey)
    '''
