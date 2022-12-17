COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloCredentialManagerImpl\n\n
    ()\n
    '''
def setPrompter():
    '''returns None\n\n
    setPrompter(final IloCredentialPrompter prompter)\n
    '''
def getPrompter():
    '''returns IloCredentialPrompter\n\n
    getPrompter()\n
    '''
def getCredential():
    '''returns IloCredential\n\n
    getCredential(final String credentialId, final String message)\n
    '''
def validateCredential():
    '''returns None\n\n
    validateCredential(final String credentialId, IloCredential credential)\n
    '''
def revokeCredential():
    '''returns None\n\n
    revokeCredential(final String credentialId)\n
    '''
