def action():
    '''returns byte[]\n\n
    action(final byte[] actionData, final String maxServiceName)\n
    '''
def wsAction():
    '''returns byte[]\n\n
    wsAction(final byte[] actionData, final String wsName)\n
    '''
def maxSecureAction():
    '''returns byte[]\n\n
    maxSecureAction(final String loginid, final String password, final byte[] actionData, final String maxServiceName)\n
    '''
def maxAPIKeySecureAction():
    '''returns byte[]\n\n
    maxAPIKeySecureAction(final String apikey, final byte[] actionData, final String maxServiceName)\n
    '''
def wsMaxAPIKeySecureAction():
    '''returns byte[]\n\n
    wsMaxAPIKeySecureAction(final String apikey, final byte[] actionData, final String wsName)\n
    '''
def wsMaxSecureAction():
    '''returns byte[]\n\n
    wsMaxSecureAction(final String loginid, final String password, final byte[] actionData, final String wsName)\n
    '''
def secureAction():
    '''returns byte[]\n\n
    secureAction(final byte[] actionData, final String maxServiceName, final Principal principal)\n
    '''
def wsSecureAction():
    '''returns byte[]\n\n
    wsSecureAction(final byte[] actionData, final String wsName, final Principal principal)\n
    '''
def getDBConnection():
    '''returns Connection\n\n
    getDBConnection(final ConnectionKey conKey)\n
    '''
def freeDBConnection():
    '''returns None\n\n
    freeDBConnection(final ConnectionKey conKey)\n
    '''
