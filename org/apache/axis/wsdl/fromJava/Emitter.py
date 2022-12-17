MODE_ALL = "int  0"
MODE_INTERFACE = "int  1"
MODE_IMPLEMENTATION = "int  2"
MODE_RPC = "int  0"
MODE_DOCUMENT = "int  1"
MODE_DOC_WRAPPED = "int  2"
def ():
    '''returns Emitter\n\n
    ()\n
    '''
def emit():
    '''returns None\n\n
    emit(String filename1, String filename2)\n
    emit(final String filename)\n
    emit(final int mode)\n
    emit(String filename, final int mode)\n
    '''
def emitToString():
    '''returns String\n\n
    emitToString(final int mode)\n
    '''
def getWSDL():
    '''returns Definition\n\n
    getWSDL()\n
    '''
def getIntfWSDL():
    '''returns Definition\n\n
    getIntfWSDL()\n
    '''
def getImplWSDL():
    '''returns Definition\n\n
    getImplWSDL()\n
    '''
def writeWrapperPart():
    '''returns String\n\n
    writeWrapperPart(final Definition def, final Message msg, final OperationDesc oper, final boolean request)\n
    '''
def writePartToMessage():
    '''returns String\n\n
    writePartToMessage(final Definition def, final Message msg, final boolean request, final ParameterDesc param)\n
    '''
def getCls():
    '''returns Class\n\n
    getCls()\n
    '''
def setCls():
    '''returns None\n\n
    setCls(final Class cls)\n
    setCls(final String className)\n
    '''
def setClsSmart():
    '''returns None\n\n
    setClsSmart(final Class cls, String location)\n
    '''
def getImplCls():
    '''returns Class\n\n
    getImplCls()\n
    '''
def setImplCls():
    '''returns None\n\n
    setImplCls(final Class implCls)\n
    setImplCls(final String className)\n
    '''
def getIntfNamespace():
    '''returns String\n\n
    getIntfNamespace()\n
    '''
def setIntfNamespace():
    '''returns None\n\n
    setIntfNamespace(final String ns)\n
    '''
def getImplNamespace():
    '''returns String\n\n
    getImplNamespace()\n
    '''
def setImplNamespace():
    '''returns None\n\n
    setImplNamespace(final String ns)\n
    '''
def getAllowedMethods():
    '''returns Vector\n\n
    getAllowedMethods()\n
    '''
def setAllowedMethods():
    '''returns None\n\n
    setAllowedMethods(final String text)\n
    setAllowedMethods(final Vector allowedMethods)\n
    '''
def getUseInheritedMethods():
    '''returns boolean\n\n
    getUseInheritedMethods()\n
    '''
def setUseInheritedMethods():
    '''returns None\n\n
    setUseInheritedMethods(final boolean useInheritedMethods)\n
    '''
def setDisallowedMethods():
    '''returns None\n\n
    setDisallowedMethods(final Vector disallowedMethods)\n
    setDisallowedMethods(final String text)\n
    '''
def getDisallowedMethods():
    '''returns Vector\n\n
    getDisallowedMethods()\n
    '''
def setStopClasses():
    '''returns None\n\n
    setStopClasses(final ArrayList stopClasses)\n
    setStopClasses(final String text)\n
    '''
def getStopClasses():
    '''returns ArrayList\n\n
    getStopClasses()\n
    '''
def getNamespaceMap():
    '''returns Map\n\n
    getNamespaceMap()\n
    '''
def setNamespaceMap():
    '''returns None\n\n
    setNamespaceMap(final Map map)\n
    '''
def getInputWSDL():
    '''returns String\n\n
    getInputWSDL()\n
    '''
def setInputWSDL():
    '''returns None\n\n
    setInputWSDL(final String inputWSDL)\n
    '''
def getInputSchema():
    '''returns String\n\n
    getInputSchema()\n
    '''
def setInputSchema():
    '''returns None\n\n
    setInputSchema(final String inputSchema)\n
    '''
def getLocationUrl():
    '''returns String\n\n
    getLocationUrl()\n
    '''
def setLocationUrl():
    '''returns None\n\n
    setLocationUrl(final String locationUrl)\n
    '''
def getImportUrl():
    '''returns String\n\n
    getImportUrl()\n
    '''
def setImportUrl():
    '''returns None\n\n
    setImportUrl(final String importUrl)\n
    '''
def getServicePortName():
    '''returns String\n\n
    getServicePortName()\n
    '''
def setServicePortName():
    '''returns None\n\n
    setServicePortName(final String servicePortName)\n
    '''
def getServiceElementName():
    '''returns String\n\n
    getServiceElementName()\n
    '''
def setServiceElementName():
    '''returns None\n\n
    setServiceElementName(final String serviceElementName)\n
    '''
def getPortTypeName():
    '''returns String\n\n
    getPortTypeName()\n
    '''
def setPortTypeName():
    '''returns None\n\n
    setPortTypeName(final String portTypeName)\n
    '''
def getBindingName():
    '''returns String\n\n
    getBindingName()\n
    '''
def setBindingName():
    '''returns None\n\n
    setBindingName(final String bindingName)\n
    '''
def getTargetService():
    '''returns String\n\n
    getTargetService()\n
    '''
def setTargetService():
    '''returns None\n\n
    setTargetService(final String targetService)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final String description)\n
    '''
def getSoapAction():
    '''returns String\n\n
    getSoapAction()\n
    '''
def setSoapAction():
    '''returns None\n\n
    setSoapAction(final String value)\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping()\n
    '''
def setTypeMapping():
    '''returns None\n\n
    setTypeMapping(final TypeMapping tm)\n
    '''
def getDefaultTypeMapping():
    '''returns TypeMapping\n\n
    getDefaultTypeMapping()\n
    '''
def setDefaultTypeMapping():
    '''returns None\n\n
    setDefaultTypeMapping(final TypeMapping tm)\n
    '''
def setTypeMappingRegistry():
    '''returns None\n\n
    setTypeMappingRegistry(final TypeMappingRegistry tmr)\n
    '''
def getStyle():
    '''returns Style\n\n
    getStyle()\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final String value)\n
    setStyle(final Style value)\n
    '''
def getUse():
    '''returns Use\n\n
    getUse()\n
    '''
def setUse():
    '''returns None\n\n
    setUse(final String value)\n
    setUse(final Use value)\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final int mode)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def getServiceDesc():
    '''returns ServiceDesc\n\n
    getServiceDesc()\n
    '''
def setServiceDesc():
    '''returns None\n\n
    setServiceDesc(final ServiceDesc serviceDesc)\n
    '''
def getExtraClasses():
    '''returns Class[]\n\n
    getExtraClasses()\n
    '''
def setExtraClasses():
    '''returns None\n\n
    setExtraClasses(final Class[] extraClasses)\n
    setExtraClasses(final String text)\n
    '''
def setEmitAllTypes():
    '''returns None\n\n
    setEmitAllTypes(final boolean emitAllTypes)\n
    '''
def getVersionMessage():
    '''returns String\n\n
    getVersionMessage()\n
    '''
def setVersionMessage():
    '''returns None\n\n
    setVersionMessage(final String versionMessage)\n
    '''
def getQName2ClassMap():
    '''returns HashMap\n\n
    getQName2ClassMap()\n
    '''
