def ():
    '''returns AliasedX509KeyManager\n\n
    (final String keyAlias, final X509KeyManager keyManager)\n
    '''
def chooseClientAlias():
    '''returns String\n\n
    chooseClientAlias(final String[] keyType, final Principal[] issuers, final Socket socket)\n
    '''
def chooseServerAlias():
    '''returns String\n\n
    chooseServerAlias(final String keyType, final Principal[] issuers, final Socket socket)\n
    '''
def getClientAliases():
    '''returns String[]\n\n
    getClientAliases(final String keyType, final Principal[] issuers)\n
    '''
def getServerAliases():
    '''returns String[]\n\n
    getServerAliases(final String keyType, final Principal[] issuers)\n
    '''
def getCertificateChain():
    '''returns X509Certificate[]\n\n
    getCertificateChain(final String alias)\n
    '''
def getPrivateKey():
    '''returns PrivateKey\n\n
    getPrivateKey(final String alias)\n
    '''
