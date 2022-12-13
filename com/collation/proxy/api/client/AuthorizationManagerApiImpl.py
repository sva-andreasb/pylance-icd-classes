def AuthorizationManagerApiImpl():
'''public AuthorizationManagerApiImpl(final ApiSession sess)
'''
pass
def getSession():
'''public ApiSession getSession()
'''
pass
def addAccess():
'''public void addAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
public void addAccess(final Principal user, final AccessDefinition[] accessDefinition)
'''
pass
def deleteAccess():
'''public void deleteAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
'''
pass
def getEntitlements():
'''public Resource[] getEntitlements(final Principal user, final String[] permissions)
'''
pass
def getEntitlementsForRole():
'''public Resource[] getEntitlementsForRole(final Principal user, final String role)
'''
pass
def getAccessDecisions():
'''public AccessDecision[] getAccessDecisions(final Principal user, final Resource[] resources, final String[] permissions)
'''
pass
def getDataPermissions():
'''public String[] getDataPermissions(final Principal user, final Resource[] resources)
'''
pass
def addRuntimeAccess():
'''public void addRuntimeAccess(final Principal user, final String role, final String[] permissions)
'''
pass
def deleteRuntimeAccess():
'''public void deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)
'''
pass
def getRuntimeAccess():
'''public String[] getRuntimeAccess(final Principal user)
'''
pass
def getRuntimeAccessDecisions():
'''public RuntimeAccessDecision[] getRuntimeAccessDecisions(final Principal user, final String[] permissions)
'''
pass
def getRoles():
'''public String[] getRoles(final Principal user)
'''
pass
def assignPersonInRoleToAccessCollection():
'''public void assignPersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
'''
pass
def removePersonInRoleToAccessCollection():
'''public void removePersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
'''
pass
def deleteRole():
'''public void deleteRole(final String role)
'''
pass
def deletePermission():
'''public void deletePermission(final String permission)
'''
pass
def deletePermissionFromRole():
'''public void deletePermissionFromRole(final String role, final String permission)
'''
pass
def addDataPermissionToRole():
'''public void addDataPermissionToRole(final String role, final String permission)
'''
pass
def addRuntimePermissionToRole():
'''public void addRuntimePermissionToRole(final String role, final String permission)
'''
pass
