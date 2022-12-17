MSG_METHOD_BODYARRAY = "int  1"
MSG_METHOD_SOAPENVELOPE = "int  2"
MSG_METHOD_ELEMENTARRAY = "int  3"
MSG_METHOD_DOCUMENT = "int  4"
MSG_METHOD_NONCONFORMING = "int  -4"
def ():
    '''returns OperationDesc\n\n
    ()\n
    (final String name, final ParameterDesc[] parameters, final QName returnQName)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getDocumentation():
    '''returns String\n\n
    getDocumentation()\n
    '''
def setDocumentation():
    '''returns None\n\n
    setDocumentation(final String documentation)\n
    '''
def getReturnQName():
    '''returns QName\n\n
    getReturnQName()\n
    '''
def setReturnQName():
    '''returns None\n\n
    setReturnQName(final QName returnQName)\n
    '''
def getReturnType():
    '''returns QName\n\n
    getReturnType()\n
    '''
def setReturnType():
    '''returns None\n\n
    setReturnType(final QName returnType)\n
    '''
def getReturnClass():
    '''returns Class\n\n
    getReturnClass()\n
    '''
def setReturnClass():
    '''returns None\n\n
    setReturnClass(final Class returnClass)\n
    '''
def getElementQName():
    '''returns QName\n\n
    getElementQName()\n
    '''
def setElementQName():
    '''returns None\n\n
    setElementQName(final QName elementQName)\n
    '''
def getParent():
    '''returns ServiceDesc\n\n
    getParent()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final ServiceDesc parent)\n
    '''
def getSoapAction():
    '''returns String\n\n
    getSoapAction()\n
    '''
def setSoapAction():
    '''returns None\n\n
    setSoapAction(final String soapAction)\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final Style style)\n
    '''
def getStyle():
    '''returns Style\n\n
    getStyle()\n
    '''
def setUse():
    '''returns None\n\n
    setUse(final Use use)\n
    '''
def getUse():
    '''returns Use\n\n
    getUse()\n
    '''
def addParameter():
    '''returns None\n\n
    addParameter(final ParameterDesc param)\n
    addParameter(final QName paramName, final QName xmlType, final Class javaType, final byte parameterMode, final boolean inHeader, final boolean outHeader)\n
    '''
def getParameter():
    '''returns ParameterDesc\n\n
    getParameter(final int i)\n
    '''
def getParameters():
    '''returns ArrayList\n\n
    getParameters()\n
    '''
def setParameters():
    '''returns None\n\n
    setParameters(final ArrayList newParameters)\n
    '''
def getNumInParams():
    '''returns int\n\n
    getNumInParams()\n
    '''
def getNumOutParams():
    '''returns int\n\n
    getNumOutParams()\n
    '''
def getNumParams():
    '''returns int\n\n
    getNumParams()\n
    '''
def getMethod():
    '''returns Method\n\n
    getMethod()\n
    '''
def setMethod():
    '''returns None\n\n
    setMethod(final Method method)\n
    '''
def isReturnHeader():
    '''returns boolean\n\n
    isReturnHeader()\n
    '''
def setReturnHeader():
    '''returns None\n\n
    setReturnHeader(final boolean value)\n
    '''
def getParamByQName():
    '''returns ParameterDesc\n\n
    getParamByQName(final QName qname)\n
    '''
def getInputParamByQName():
    '''returns ParameterDesc\n\n
    getInputParamByQName(final QName qname)\n
    '''
def getOutputParamByQName():
    '''returns ParameterDesc\n\n
    getOutputParamByQName(final QName qname)\n
    '''
def getAllInParams():
    '''returns ArrayList\n\n
    getAllInParams()\n
    '''
def getAllOutParams():
    '''returns ArrayList\n\n
    getAllOutParams()\n
    '''
def getOutParams():
    '''returns ArrayList\n\n
    getOutParams()\n
    '''
def addFault():
    '''returns None\n\n
    addFault(final FaultDesc fault)\n
    '''
def getFaults():
    '''returns ArrayList\n\n
    getFaults()\n
    '''
def getFaultByClass():
    '''returns FaultDesc\n\n
    getFaultByClass(Class cls)\n
    getFaultByClass(final Class cls, final boolean checkParents)\n
    '''
def getFaultByQName():
    '''returns FaultDesc\n\n
    getFaultByQName(final QName qname)\n
    '''
def getFaultByXmlType():
    '''returns FaultDesc\n\n
    getFaultByXmlType(final QName xmlType)\n
    '''
def getReturnParamDesc():
    '''returns ParameterDesc\n\n
    getReturnParamDesc()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final String indent)\n
    '''
def getMessageOperationStyle():
    '''returns int\n\n
    getMessageOperationStyle()\n
    '''
def setMessageOperationStyle():
    '''returns None\n\n
    setMessageOperationStyle(final int messageOperationStyle)\n
    '''
def getMep():
    '''returns OperationType\n\n
    getMep()\n
    '''
def setMep():
    '''returns None\n\n
    setMep(final OperationType mep)\n
    setMep(final String mepString)\n
    '''
