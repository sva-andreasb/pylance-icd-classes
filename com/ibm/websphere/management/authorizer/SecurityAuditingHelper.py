SA_ACTION_EXECUTE_COMMAND = "String  \"execute command\""
SA_ACTION_CREATE_SESSION = "String  \"create session\""
SA_ACTION_SAVE_SESSION = "String  \"save session\""
SA_ACTION_DISCARD_SESSION = "String  \"discard session\""
SA_ACTION_PROCESS_PARAM = "String  \"process task parameters\""
SA_ACTION_PREINVOKE_MBEAN = "String  \"preinvoke MBean\""
SA_ACTION_RESOURCE_ADDED = "String  \"add resource\""
SA_ACTION_RESOURCE_MODIFIED = "String  \"modify resource\""
SA_ACTION_RESOURCE_DELETED = "String  \"delete resource\""
SA_ACTION_RESOURCE_ACCESS = "String  \"access resource\""
SA_ACTION_APPLICATION_INSTALL = "String  \"install application\""
SA_ACTION_APPLICATION_EDIT = "String  \"edit application\""
SA_ACTION_APPLICATION_UPDATE = "String  \"update application\""
def logSecurityAuditForCommand():
    '''returns None\n\n
    logSecurityAuditForCommand(final boolean success, final String className, final String cmdName, final String sessionId, final String action, final List requiredRoles)\n
    '''
def logSecurityAuditForMBean():
    '''returns None\n\n
    logSecurityAuditForMBean(final boolean success, final ObjectName mBeanObjName, final String methodName, final String sessionId, final String action)\n
    logSecurityAuditForMBean(final boolean success, final ObjectName mBeanObjName, final String methodName, String sessionId, String action, final String[] resNames, final String[] resTypes)\n
    '''
def logSecurityAuditForRepository():
    '''returns None\n\n
    logSecurityAuditForRepository(final boolean success, final String className, final String action, final String userID, final String url)\n
    '''
def logSecurityAuditForSession():
    '''returns None\n\n
    logSecurityAuditForSession(final boolean success, final String className, final String sessionId, String action, final String userId)\n
    '''
def logSecurityAuditForDeployment():
    '''returns None\n\n
    logSecurityAuditForDeployment(final DeploymentAction action, String sessionId, final String appName, final String taskName, final String module, final String uri, String ejb, String name, final String column, final String oldValue, final String newValue)\n
    '''
