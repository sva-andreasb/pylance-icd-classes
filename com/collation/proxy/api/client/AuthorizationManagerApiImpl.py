def AuthorizationManagerApiImpl():
    '''    public AuthorizationManagerApiImpl(final ApiSession sess)
    '''
def getSession():
    '''    public ApiSession getSession()
    '''
def addAccess():
    '''    public void addAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
    public void addAccess(final Principal user, final AccessDefinition[] accessDefinition)
    '''
def deleteAccess():
    '''    public void deleteAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
    '''
def getEntitlements():
    '''    public Resource[] getEntitlements(final Principal user, final String[] permissions)
    '''
def getEntitlementsForRole():
    '''    public Resource[] getEntitlementsForRole(final Principal user, final String role)
    '''
def getAccessDecisions():
    '''    public AccessDecision[] getAccessDecisions(final Principal user, final Resource[] resources, final String[] permissions)
    '''
def getDataPermissions():
    '''    public String[] getDataPermissions(final Principal user, final Resource[] resources)
    '''
def addRuntimeAccess():
    '''    public void addRuntimeAccess(final Principal user, final String role, final String[] permissions)
    '''
def deleteRuntimeAccess():
    '''    public void deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)
    '''
def getRuntimeAccess():
    '''    public String[] getRuntimeAccess(final Principal user)
    '''
def getRuntimeAccessDecisions():
    '''    public RuntimeAccessDecision[] getRuntimeAccessDecisions(final Principal user, final String[] permissions)
    '''
def getRoles():
    '''    public String[] getRoles(final Principal user)
    '''
def assignPersonInRoleToAccessCollection():
    '''    public void assignPersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
    '''
def removePersonInRoleToAccessCollection():
    '''    public void removePersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
    '''
def deleteRole():
    '''    public void deleteRole(final String role)
    '''
def deletePermission():
    '''    public void deletePermission(final String permission)
    '''
def deletePermissionFromRole():
    '''    public void deletePermissionFromRole(final String role, final String permission)
    '''
def addDataPermissionToRole():
    '''    public void addDataPermissionToRole(final String role, final String permission)
    '''
def addRuntimePermissionToRole():
    '''    public void addRuntimePermissionToRole(final String role, final String permission)
    '''
