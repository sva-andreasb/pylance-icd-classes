def ():
    '''returns WSModelsLoader\n\n
    ()\n
    '''
def preInvoke():
    '''returns None\n\n
    preInvoke(final ConfigObject c)\n
    '''
def postInvoke():
    '''returns None\n\n
    postInvoke(final ConfigObject c)\n
    '''
def getWSBinding():
    '''returns WSBinding\n\n
    getWSBinding(final LoadStrategy loadStrategy, final String xmiFileName)\n
    '''
def getWSClientBinding():
    '''returns ClientBinding\n\n
    getWSClientBinding(final LoadStrategy loadStrategy, final String xmiFileName)\n
    '''
def getWSExtension():
    '''returns WsExtension\n\n
    getWSExtension(final LoadStrategy loadStrategy, final String xmiFileName)\n
    '''
def getWSClientExtension():
    '''returns WsClientExtension\n\n
    getWSClientExtension(final LoadStrategy loadStrategy, final String xmiFileName)\n
    '''
def getWebServices():
    '''returns WebServices\n\n
    getWebServices(final LoadStrategy loadStrategy, final String xmlFileName)\n
    '''
def getWebServicesClient():
    '''returns WebServicesClient\n\n
    getWebServicesClient(final LoadStrategy loadStrategy, final String xmlFileName)\n
    '''
def getJavaWSDLMapping():
    '''returns IMappingMetaData\n\n
    getJavaWSDLMapping(final LoadStrategy loadStrategy, final String xmlFileName)\n
    '''
def getWSBindingFromResourceSet():
    '''returns WSBinding\n\n
    getWSBindingFromResourceSet(final ResourceSet rs, final String xmiFileName)\n
    '''
def getWSClientBindingFromResourceSet():
    '''returns ClientBinding\n\n
    getWSClientBindingFromResourceSet(final ResourceSet rs, final String xmiFileName)\n
    '''
def getWSClientFromResourceSet():
    '''returns WebServicesClient\n\n
    getWSClientFromResourceSet(final ResourceSet rs, final String xmlFileName)\n
    '''
def getEJBJarFromResourceSet():
    '''returns EJBJar\n\n
    getEJBJarFromResourceSet(final ResourceSet rs, final String xmlFileName)\n
    '''
def getWebAppFromResourceSet():
    '''returns WebApp\n\n
    getWebAppFromResourceSet(final ResourceSet rs, final String xmlFileName)\n
    '''
def loadFromFile():
    '''returns IMappingMetaData\n\n
    loadFromFile(final String file, final LoadStrategy loadStrategy)\n
    '''
def loadFromRes():
    '''returns IMappingMetaData\n\n
    loadFromRes(final String file, final JaxrpcmapResource res)\n
    '''
def getJavaWSDLInputStream():
    '''returns InputStream\n\n
    getJavaWSDLInputStream(final String wsdlFileName, final LoadStrategy loadStrategy)\n
    '''
def buildWSDLPath():
    '''returns String\n\n
    buildWSDLPath(final String modulePath, final String wsdlFileName)\n
    '''
def getWSDLReader():
    '''returns WSDLReader\n\n
    getWSDLReader()\n
    '''
