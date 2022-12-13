def action():
'''public byte[] action(final byte[] actionData, final String maxServiceName)
'''
pass
def wsAction():
'''public byte[] wsAction(final byte[] actionData, final String wsName)
'''
pass
def maxSecureAction():
'''public byte[] maxSecureAction(final String loginid, final String password, final byte[] actionData, final String maxServiceName)
'''
pass
def maxAPIKeySecureAction():
'''public byte[] maxAPIKeySecureAction(final String apikey, final byte[] actionData, final String maxServiceName)
'''
pass
def wsMaxAPIKeySecureAction():
'''public byte[] wsMaxAPIKeySecureAction(final String apikey, final byte[] actionData, final String wsName)
'''
pass
def wsMaxSecureAction():
'''public byte[] wsMaxSecureAction(final String loginid, final String password, final byte[] actionData, final String wsName)
'''
pass
def secureAction():
'''public byte[] secureAction(final byte[] actionData, final String maxServiceName, final Principal principal)
'''
pass
def wsSecureAction():
'''public byte[] wsSecureAction(final byte[] actionData, final String wsName, final Principal principal)
'''
pass
def getDBConnection():
'''public Connection getDBConnection(final ConnectionKey conKey)
'''
pass
def freeDBConnection():
'''public void freeDBConnection(final ConnectionKey conKey)
'''
pass
