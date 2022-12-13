def AliasedX509KeyManager():
    '''    public AliasedX509KeyManager(final String keyAlias, final X509KeyManager keyManager)
    '''
def chooseClientAlias():
    '''    public String chooseClientAlias(final String[] keyType, final Principal[] issuers, final Socket socket)
    '''
def chooseServerAlias():
    '''    public String chooseServerAlias(final String keyType, final Principal[] issuers, final Socket socket)
    '''
def getClientAliases():
    '''    public String[] getClientAliases(final String keyType, final Principal[] issuers)
    '''
def getServerAliases():
    '''    public String[] getServerAliases(final String keyType, final Principal[] issuers)
    '''
def getCertificateChain():
    '''    public X509Certificate[] getCertificateChain(final String alias)
    '''
def getPrivateKey():
    '''    public PrivateKey getPrivateKey(final String alias)
    '''
