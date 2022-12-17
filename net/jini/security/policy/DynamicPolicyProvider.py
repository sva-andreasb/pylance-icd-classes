def ():
    '''returns DynamicPolicyProvider\n\n
    ()\n
    (final Policy basePolicy)\n
    '''
def getPermissions():
    '''returns PermissionCollection\n\n
    getPermissions(final CodeSource codesource)\n
    getPermissions(final ProtectionDomain protectionDomain)\n
    '''
def implies():
    '''returns boolean\n\n
    implies(final ProtectionDomain protectionDomain, final Permission permission)\n
    '''
def refresh():
    '''returns None\n\n
    refresh()\n
    '''
def grantSupported():
    '''returns boolean\n\n
    grantSupported()\n
    '''
def grant():
    '''returns None\n\n
    grant(final Class clazz, Principal[] array, Permission[] array2)\n
    '''
def getGrants():
    '''returns Permission[]\n\n
    getGrants(final Class clazz, Principal[] array)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    run()\n
    run()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
