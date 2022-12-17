def ():
    '''returns AuthorizationManagerApiImpl\n\n
    (final ApiSession sess)\n
    '''
def getSession():
    '''returns ApiSession\n\n
    getSession()\n
    '''
def addAccess():
    '''returns None\n\n
    addAccess(final Principal user, final Resource resource, final String role, final String[] permissions)\n
    addAccess(final Principal user, final AccessDefinition[] accessDefinition)\n
    '''
def deleteAccess():
    '''returns None\n\n
    deleteAccess(final Principal user, final Resource resource, final String role, final String[] permissions)\n
    '''
def getEntitlements():
    '''returns Resource[]\n\n
    getEntitlements(final Principal user, final String[] permissions)\n
    '''
def getEntitlementsForRole():
    '''returns Resource[]\n\n
    getEntitlementsForRole(final Principal user, final String role)\n
    '''
def getAccessDecisions():
    '''returns AccessDecision[]\n\n
    getAccessDecisions(final Principal user, final Resource[] resources, final String[] permissions)\n
    '''
def getDataPermissions():
    '''returns String[]\n\n
    getDataPermissions(final Principal user, final Resource[] resources)\n
    '''
def addRuntimeAccess():
    '''returns None\n\n
    addRuntimeAccess(final Principal user, final String role, final String[] permissions)\n
    '''
def deleteRuntimeAccess():
    '''returns None\n\n
    deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)\n
    '''
def getRuntimeAccess():
    '''returns String[]\n\n
    getRuntimeAccess(final Principal user)\n
    '''
def getRuntimeAccessDecisions():
    '''returns RuntimeAccessDecision[]\n\n
    getRuntimeAccessDecisions(final Principal user, final String[] permissions)\n
    '''
def getRoles():
    '''returns String[]\n\n
    getRoles(final Principal user)\n
    '''
def assignPersonInRoleToAccessCollection():
    '''returns None\n\n
    assignPersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)\n
    '''
def removePersonInRoleToAccessCollection():
    '''returns None\n\n
    removePersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)\n
    '''
def deleteRole():
    '''returns None\n\n
    deleteRole(final String role)\n
    '''
def deletePermission():
    '''returns None\n\n
    deletePermission(final String permission)\n
    '''
def deletePermissionFromRole():
    '''returns None\n\n
    deletePermissionFromRole(final String role, final String permission)\n
    '''
def addDataPermissionToRole():
    '''returns None\n\n
    addDataPermissionToRole(final String role, final String permission)\n
    '''
def addRuntimePermissionToRole():
    '''returns None\n\n
    addRuntimePermissionToRole(final String role, final String permission)\n
    '''
