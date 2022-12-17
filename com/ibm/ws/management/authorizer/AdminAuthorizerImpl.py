def isFineGrainedAdminSecurity():
    '''returns boolean\n\n
    isFineGrainedAdminSecurity()\n
    '''
def checkAccess():
    '''returns boolean\n\n
    checkAccess(final String resNameIn, final String role)\n
    checkAccess(final String moduleName, final String resourceName, final String methodName)\n
    checkAccess(final ObjectName name, final String[] resourceNames, final String[] resourceTypes, final String methodName)\n
    checkAccess(final String modName, final ObjectName name, final String[] resourceNames, final String[] resourceTypes, final String methodName)\n
    '''
def isCallerInRole():
    '''returns boolean\n\n
    isCallerInRole(final String groupName, final String role)\n
    isCallerInRole(final String roleName)\n
    '''
def getAllParentRoles():
    '''returns List\n\n
    getAllParentRoles(final String roleName)\n
    '''
def getParentRoles():
    '''returns List\n\n
    getParentRoles(final String roleName)\n
    '''
def setRoleBasedConfigurator():
    '''returns None\n\n
    setRoleBasedConfigurator(final RoleBasedConfigurator roleBasedConfigurator)\n
    '''
def getRoleBasedConfigurator():
    '''returns RoleBasedConfigurator\n\n
    getRoleBasedConfigurator()\n
    '''
def setCellName():
    '''returns None\n\n
    setCellName(final String cellName)\n
    '''
def setNodeName():
    '''returns None\n\n
    setNodeName(final String nodeName)\n
    '''
def setServerName():
    '''returns None\n\n
    setServerName(final String serverName)\n
    '''
def setCacheEnabled():
    '''returns None\n\n
    setCacheEnabled()\n
    '''
def setCacheDisabled():
    '''returns None\n\n
    setCacheDisabled()\n
    '''
def runningAsSystem():
    '''returns boolean\n\n
    runningAsSystem()\n
    '''
def isGrantedRoleInAnyGroup():
    '''returns boolean\n\n
    isGrantedRoleInAnyGroup(final String role)\n
    '''
def setAuthzCache():
    '''returns None\n\n
    setAuthzCache(final AuthzCache aCache)\n
    '''
def isGrantedMinimumRolesForMBean():
    '''returns boolean\n\n
    isGrantedMinimumRolesForMBean(final String moduleName, final String resourceName, final String methodName)\n
    '''
def isGrantedRole():
    '''returns boolean\n\n
    isGrantedRole(final String[] roleNames, final Subject subject)\n
    '''
