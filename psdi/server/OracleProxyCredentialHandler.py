def ():
    '''returns OracleProxyCredentialHandler\n\n
    (final DBManager owner)\n
    (final DBManager owner, final int t)\n
    '''
def setServer():
    '''returns None\n\n
    setServer(final MXServerRemote server)\n
    '''
def handleInput():
    '''returns Object\n\n
    handleInput(final String loginID, final MaxUsrDBAuthInfoRemote authInfo)\n
    handleInput(final String loginID, final String password, Object credential)\n
    handleInput(final String loginID, final String stringCredential)\n
    '''
def handleOutput():
    '''returns Object[]\n\n
    handleOutput(final Object credential)\n
    '''
def getCertificateObject():
    '''returns X509Certificate\n\n
    getCertificateObject(final String encoded)\n
    '''
