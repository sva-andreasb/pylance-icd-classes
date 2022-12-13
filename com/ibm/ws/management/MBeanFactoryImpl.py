def MBeanFactoryImpl():
    '''    public MBeanFactoryImpl(final String serverName)
    public MBeanFactoryImpl(final String serverName, final MBeanServer mbeanServer)
    '''
def getMBeanServer():
    '''    public MBeanServer getMBeanServer()
    '''
def setCellName():
    '''    public void setCellName(final String name)
    '''
def setNodeName():
    '''    public void setNodeName(final String name)
    '''
def setProcessName():
    '''    public void setProcessName(final String name)
    '''
def setRepositoryDir():
    '''    public void setRepositoryDir(final String dir)
    '''
def getMBeanTypes():
    '''    public List getMBeanTypes()
    '''
def getConfigId():
    '''    public String getConfigId(final Object target)
    '''
def activateMBean():
    '''    public ObjectName activateMBean(final String type, final RuntimeCollaborator collaborator, final String configId, final String descriptor)
    public ObjectName activateMBean(final String type, final RuntimeCollaborator collaborator, final String configId)
    public ObjectName activateMBean(final String type, final RuntimeCollaborator collaborator, String configId, final String descriptor, final Properties props)
    public ObjectName activateMBean(final String type, final Proxy proxy, final String configId, final String descriptor, final ModelMBeanInfo info)
    public ObjectName activateMBean(final Proxy proxy, final ModelMBeanInfo info)
    '''
def completeActivateMBeans():
    '''    public void completeActivateMBeans()
    '''
def createObjectName():
    '''    public ObjectName createObjectName(final String type, String configId, final String descriptor, final Properties props)
    '''
def deactivateMBean():
    '''    public void deactivateMBean(final String configId)
    public void deactivateMBean(final ObjectName mbean)
    '''
def findMBean():
    '''    public ObjectName findMBean(String configId)
    '''
def getDescriptorManager():
    '''    public MBeanDescriptorManager getDescriptorManager()
    '''
def completeApplySecurityPolicy():
    '''    public void completeApplySecurityPolicy()
    '''
def printModelMBeanInfo():
    '''    public static String printModelMBeanInfo(final ModelMBeanInfo info)
    '''
def setAdminAgentDeactivatedMBeanTypes():
    '''    public void setAdminAgentDeactivatedMBeanTypes(final ArrayList<ObjectName> adminAgentActivatedMBeans)
    '''
def add():
    '''    public boolean add(final Object o)
    '''
def remove():
    '''    public boolean remove(final Object o)
    '''
def MBeanSecurityPolicyInfo():
    '''    public MBeanSecurityPolicyInfo(final ModelMBeanInfo i, final String s)
    '''
def getDescriptor():
    '''    public String getDescriptor()
    '''
def setDescriptor():
    '''    public void setDescriptor(final String descriptor)
    '''
def getInfo():
    '''    public ModelMBeanInfo getInfo()
    '''
def setInfo():
    '''    public void setInfo(final ModelMBeanInfo info)
    '''
