def sensitiveOperationOverInsecureConnection():
    '''returns None\n\n
    sensitiveOperationOverInsecureConnection(final boolean allow)\n
    '''
def supportsAccountCreation():
    '''returns boolean\n\n
    supportsAccountCreation()\n
    '''
def getAccountAttributes():
    '''returns Set<String>\n\n
    getAccountAttributes()\n
    '''
def getAccountAttribute():
    '''returns String\n\n
    getAccountAttribute(final String name)\n
    '''
def getAccountInstructions():
    '''returns String\n\n
    getAccountInstructions()\n
    '''
def createAccount():
    '''returns None\n\n
    createAccount(final Localpart username, final String password)\n
    createAccount(final Localpart username, final String password, final Map<String, String> attributes)\n
    '''
def changePassword():
    '''returns None\n\n
    changePassword(final String newPassword)\n
    '''
def deleteAccount():
    '''returns None\n\n
    deleteAccount()\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported()\n
    '''
