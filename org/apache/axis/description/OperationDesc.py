MSG_METHOD_BODYARRAY = "int  1"
MSG_METHOD_SOAPENVELOPE = "int  2"
MSG_METHOD_ELEMENTARRAY = "int  3"
MSG_METHOD_DOCUMENT = "int  4"
MSG_METHOD_NONCONFORMING = "int  -4"
def OperationDesc():
    '''    public OperationDesc()
    public OperationDesc(final String name, final ParameterDesc[] parameters, final QName returnQName)
    '''
def getName():
    '''    public String getName()
    '''
def setName():
    '''    public void setName(final String name)
    '''
def getDocumentation():
    '''    public String getDocumentation()
    '''
def setDocumentation():
    '''    public void setDocumentation(final String documentation)
    '''
def getReturnQName():
    '''    public QName getReturnQName()
    '''
def setReturnQName():
    '''    public void setReturnQName(final QName returnQName)
    '''
def getReturnType():
    '''    public QName getReturnType()
    '''
def setReturnType():
    '''    public void setReturnType(final QName returnType)
    '''
def getReturnClass():
    '''    public Class getReturnClass()
    '''
def setReturnClass():
    '''    public void setReturnClass(final Class returnClass)
    '''
def getElementQName():
    '''    public QName getElementQName()
    '''
def setElementQName():
    '''    public void setElementQName(final QName elementQName)
    '''
def getParent():
    '''    public ServiceDesc getParent()
    '''
def setParent():
    '''    public void setParent(final ServiceDesc parent)
    '''
def getSoapAction():
    '''    public String getSoapAction()
    '''
def setSoapAction():
    '''    public void setSoapAction(final String soapAction)
    '''
def setStyle():
    '''    public void setStyle(final Style style)
    '''
def getStyle():
    '''    public Style getStyle()
    '''
def setUse():
    '''    public void setUse(final Use use)
    '''
def getUse():
    '''    public Use getUse()
    '''
def addParameter():
    '''    public void addParameter(final ParameterDesc param)
    public void addParameter(final QName paramName, final QName xmlType, final Class javaType, final byte parameterMode, final boolean inHeader, final boolean outHeader)
    '''
def getParameter():
    '''    public ParameterDesc getParameter(final int i)
    '''
def getParameters():
    '''    public ArrayList getParameters()
    '''
def setParameters():
    '''    public void setParameters(final ArrayList newParameters)
    '''
def getNumInParams():
    '''    public int getNumInParams()
    '''
def getNumOutParams():
    '''    public int getNumOutParams()
    '''
def getNumParams():
    '''    public int getNumParams()
    '''
def getMethod():
    '''    public Method getMethod()
    '''
def setMethod():
    '''    public void setMethod(final Method method)
    '''
def isReturnHeader():
    '''    public boolean isReturnHeader()
    '''
def setReturnHeader():
    '''    public void setReturnHeader(final boolean value)
    '''
def getParamByQName():
    '''    public ParameterDesc getParamByQName(final QName qname)
    '''
def getInputParamByQName():
    '''    public ParameterDesc getInputParamByQName(final QName qname)
    '''
def getOutputParamByQName():
    '''    public ParameterDesc getOutputParamByQName(final QName qname)
    '''
def getAllInParams():
    '''    public ArrayList getAllInParams()
    '''
def getAllOutParams():
    '''    public ArrayList getAllOutParams()
    '''
def getOutParams():
    '''    public ArrayList getOutParams()
    '''
def addFault():
    '''    public void addFault(final FaultDesc fault)
    '''
def getFaults():
    '''    public ArrayList getFaults()
    '''
def getFaultByClass():
    '''    public FaultDesc getFaultByClass(Class cls)
    public FaultDesc getFaultByClass(final Class cls, final boolean checkParents)
    '''
def getFaultByQName():
    '''    public FaultDesc getFaultByQName(final QName qname)
    '''
def getFaultByXmlType():
    '''    public FaultDesc getFaultByXmlType(final QName xmlType)
    '''
def getReturnParamDesc():
    '''    public ParameterDesc getReturnParamDesc()
    '''
def toString():
    '''    public String toString()
    public String toString(final String indent)
    '''
def getMessageOperationStyle():
    '''    public int getMessageOperationStyle()
    '''
def setMessageOperationStyle():
    '''    public void setMessageOperationStyle(final int messageOperationStyle)
    '''
def getMep():
    '''    public OperationType getMep()
    '''
def setMep():
    '''    public void setMep(final OperationType mep)
    public void setMep(final String mepString)
    '''
