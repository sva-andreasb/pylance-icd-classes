def MBeanFactoryImpl():
'''public MBeanFactoryImpl(final String serverName)
public MBeanFactoryImpl(final String serverName, final MBeanServer mbeanServer)
'''
pass
def getMBeanServer():
'''public MBeanServer getMBeanServer()
'''
pass
def setCellName():
'''public void setCellName(final String name)
'''
pass
def setNodeName():
'''public void setNodeName(final String name)
'''
pass
def setProcessName():
'''public void setProcessName(final String name)
'''
pass
def setRepositoryDir():
'''public void setRepositoryDir(final String dir)
'''
pass
def getMBeanTypes():
'''public List getMBeanTypes()
'''
pass
def getConfigId():
'''public String getConfigId(final Object target)
'''
pass
def activateMBean():
'''public ObjectName activateMBean(final String type, final RuntimeCollaborator collaborator, final String configId, final String descriptor)
public ObjectName activateMBean(final String type, final RuntimeCollaborator collaborator, final String configId)
public ObjectName activateMBean(final String type, final RuntimeCollaborator collaborator, String configId, final String descriptor, final Properties props)
public ObjectName activateMBean(final String type, final Proxy proxy, final String configId, final String descriptor, final ModelMBeanInfo info)
public ObjectName activateMBean(final Proxy proxy, final ModelMBeanInfo info)
'''
pass
def completeActivateMBeans():
'''public void completeActivateMBeans()
'''
pass
def createObjectName():
'''public ObjectName createObjectName(final String type, String configId, final String descriptor, final Properties props)
'''
pass
def deactivateMBean():
'''public void deactivateMBean(final String configId)
public void deactivateMBean(final ObjectName mbean)
'''
pass
def findMBean():
'''public ObjectName findMBean(String configId)
'''
pass
def getDescriptorManager():
'''public MBeanDescriptorManager getDescriptorManager()
'''
pass
def completeApplySecurityPolicy():
'''public void completeApplySecurityPolicy()
'''
pass
def printModelMBeanInfo():
'''public static String printModelMBeanInfo(final ModelMBeanInfo info)
'''
pass
def setAdminAgentDeactivatedMBeanTypes():
'''public void setAdminAgentDeactivatedMBeanTypes(final ArrayList<ObjectName> adminAgentActivatedMBeans)
'''
pass
def add():
'''public boolean add(final Object o)
'''
pass
def remove():
'''public boolean remove(final Object o)
'''
pass
def MBeanSecurityPolicyInfo():
'''public MBeanSecurityPolicyInfo(final ModelMBeanInfo i, final String s)
'''
pass
def getDescriptor():
'''public String getDescriptor()
'''
pass
def setDescriptor():
'''public void setDescriptor(final String descriptor)
'''
pass
def getInfo():
'''public ModelMBeanInfo getInfo()
'''
pass
def setInfo():
'''public void setInfo(final ModelMBeanInfo info)
'''
pass
