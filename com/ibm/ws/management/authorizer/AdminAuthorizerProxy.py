def isFineGrainedAdminSecurity():
    '''returns boolean\n\n
    isFineGrainedAdminSecurity()\n
    '''
def checkAccess():
    '''returns boolean\n\n
    checkAccess(final String resourceName, final String role)\n
    checkAccess(final ObjectName name, final String[] resourceNames, final String[] resourceTypes, final String methodName)\n
    checkAccess(final String moduleName, final String resourceName, final String methodName)\n
    '''
def isCallerInRole():
    '''returns boolean\n\n
    isCallerInRole(final String groupName, final String role)\n
    isCallerInRole(final String roleName)\n
    '''
def runningAsSystem():
    '''returns boolean\n\n
    runningAsSystem()\n
    '''
def getAllParentRoles():
    '''returns List\n\n
    getAllParentRoles(final String roleName)\n
    '''
def getParentRoles():
    '''returns List\n\n
    getParentRoles(final String roleName)\n
    '''
def isGrantedMinimumRolesForMBean():
    '''returns boolean\n\n
    isGrantedMinimumRolesForMBean(final String moduleName, final String resourceName, final String methodName)\n
    '''
def isGrantedRole():
    '''returns boolean\n\n
    isGrantedRole(final String[] requiredRoles, final Subject subject)\n
    '''
def isGrantedRoleInAnyGroup():
    '''returns boolean\n\n
    isGrantedRoleInAnyGroup(final String role)\n
    '''
