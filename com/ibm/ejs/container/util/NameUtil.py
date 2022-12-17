homeRemotePrefix = "String  \"EJSRemote\""
homeBeanPrefix = "String  \"EJS\""
remotePrefix = "String  \"EJSRemote\""
concreteBeanPrefix = "String  \"Concrete\""
persisterPrefix = "String  \"EJSJDBCPersister\""
endpointPrefix = "String  \"WSEJBProxy\""
homeLocalPrefix = "String  \"EJSLocal\""
localPrefix = "String  \"EJSLocal\""
Max_Gen_File_Size = "int  100"
Max_EjbName_Size = "int  32"
UNKNOWN = "String  \"UNKNOWN\""
STATELESS = "String  \"SL\""
STATEFUL = "String  \"SF\""
BEAN_MANAGED = "String  \"BMP\""
CONTAINER_MANAGED = "String  \"CMP\""
MESSAGE_DRIVEN = "String  \"MDB\""
EJB_1X = "int  1"
EJB_2X = "int  2"
EJB_3X = "int  3"
def ():
    '''returns NameUtil\n\n
    (final String beanName, final String remoteHomeInterface, final String remoteInterface, final String localHomeInterface, final String localInterface, final String[] remoteBusinessInterfaces, final String[] localBusinessInterfaces, final String beanClass, final String primaryKey, final String beanType, final int version)\n
    '''
def getBusinessRemoteImplClassName():
    '''returns String\n\n
    getBusinessRemoteImplClassName(final int index)\n
    '''
def getBusinessLocalImplClassName():
    '''returns String\n\n
    getBusinessLocalImplClassName(final int index)\n
    '''
def getRemoteImplClassName():
    '''returns String\n\n
    getRemoteImplClassName()\n
    '''
def getLocalImplClassName():
    '''returns String\n\n
    getLocalImplClassName()\n
    '''
def getHomeRemoteImplClassName():
    '''returns String\n\n
    getHomeRemoteImplClassName()\n
    '''
def getHomeLocalImplClassName():
    '''returns String\n\n
    getHomeLocalImplClassName()\n
    '''
def getHomeBeanClassName():
    '''returns String\n\n
    getHomeBeanClassName()\n
    '''
def getConcreteBeanClassName():
    '''returns String\n\n
    getConcreteBeanClassName()\n
    '''
def getDeployedPersisterClassName():
    '''returns String\n\n
    getDeployedPersisterClassName()\n
    '''
def getWebServiceEndpointProxyClassName():
    '''returns String\n\n
    getWebServiceEndpointProxyClassName()\n
    '''
