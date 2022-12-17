def ():
    '''returns MBeanSecurityPolicyInfo\n\n
    (final String serverName)\n
    (final String serverName, final MBeanServer mbeanServer)\n
    (final ModelMBeanInfo i, final String s)\n
    '''
def getMBeanServer():
    '''returns MBeanServer\n\n
    getMBeanServer()\n
    '''
def setCellName():
    '''returns None\n\n
    setCellName(final String name)\n
    '''
def setNodeName():
    '''returns None\n\n
    setNodeName(final String name)\n
    '''
def setProcessName():
    '''returns None\n\n
    setProcessName(final String name)\n
    '''
def setRepositoryDir():
    '''returns None\n\n
    setRepositoryDir(final String dir)\n
    '''
def getMBeanTypes():
    '''returns List\n\n
    getMBeanTypes()\n
    '''
def getConfigId():
    '''returns String\n\n
    getConfigId(final Object target)\n
    '''
def activateMBean():
    '''returns ObjectName\n\n
    activateMBean(final String type, final RuntimeCollaborator collaborator, final String configId, final String descriptor)\n
    activateMBean(final String type, final RuntimeCollaborator collaborator, final String configId)\n
    activateMBean(final String type, final RuntimeCollaborator collaborator, String configId, final String descriptor, final Properties props)\n
    activateMBean(final String type, final Proxy proxy, final String configId, final String descriptor, final ModelMBeanInfo info)\n
    activateMBean(final Proxy proxy, final ModelMBeanInfo info)\n
    '''
def completeActivateMBeans():
    '''returns None\n\n
    completeActivateMBeans()\n
    '''
def createObjectName():
    '''returns ObjectName\n\n
    createObjectName(final String type, String configId, final String descriptor, final Properties props)\n
    '''
def deactivateMBean():
    '''returns None\n\n
    deactivateMBean(final String configId)\n
    deactivateMBean(final ObjectName mbean)\n
    '''
def findMBean():
    '''returns ObjectName\n\n
    findMBean(String configId)\n
    '''
def getDescriptorManager():
    '''returns MBeanDescriptorManager\n\n
    getDescriptorManager()\n
    '''
def completeApplySecurityPolicy():
    '''returns None\n\n
    completeApplySecurityPolicy()\n
    '''
def setAdminAgentDeactivatedMBeanTypes():
    '''returns None\n\n
    setAdminAgentDeactivatedMBeanTypes(final ArrayList<ObjectName> adminAgentActivatedMBeans)\n
    '''
def add():
    '''returns boolean\n\n
    add(final Object o)\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final Object o)\n
    '''
def getDescriptor():
    '''returns String\n\n
    getDescriptor()\n
    '''
def setDescriptor():
    '''returns None\n\n
    setDescriptor(final String descriptor)\n
    '''
def getInfo():
    '''returns ModelMBeanInfo\n\n
    getInfo()\n
    '''
def setInfo():
    '''returns None\n\n
    setInfo(final ModelMBeanInfo info)\n
    '''
