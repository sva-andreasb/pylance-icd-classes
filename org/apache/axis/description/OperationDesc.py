MSG_METHOD_BODYARRAY = "int  1"
MSG_METHOD_SOAPENVELOPE = "int  2"
MSG_METHOD_ELEMENTARRAY = "int  3"
MSG_METHOD_DOCUMENT = "int  4"
MSG_METHOD_NONCONFORMING = "int  -4"
def OperationDesc():
'''public OperationDesc()
public OperationDesc(final String name, final ParameterDesc[] parameters, final QName returnQName)
'''
pass
def getName():
'''public String getName()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getDocumentation():
'''public String getDocumentation()
'''
pass
def setDocumentation():
'''public void setDocumentation(final String documentation)
'''
pass
def getReturnQName():
'''public QName getReturnQName()
'''
pass
def setReturnQName():
'''public void setReturnQName(final QName returnQName)
'''
pass
def getReturnType():
'''public QName getReturnType()
'''
pass
def setReturnType():
'''public void setReturnType(final QName returnType)
'''
pass
def getReturnClass():
'''public Class getReturnClass()
'''
pass
def setReturnClass():
'''public void setReturnClass(final Class returnClass)
'''
pass
def getElementQName():
'''public QName getElementQName()
'''
pass
def setElementQName():
'''public void setElementQName(final QName elementQName)
'''
pass
def getParent():
'''public ServiceDesc getParent()
'''
pass
def setParent():
'''public void setParent(final ServiceDesc parent)
'''
pass
def getSoapAction():
'''public String getSoapAction()
'''
pass
def setSoapAction():
'''public void setSoapAction(final String soapAction)
'''
pass
def setStyle():
'''public void setStyle(final Style style)
'''
pass
def getStyle():
'''public Style getStyle()
'''
pass
def setUse():
'''public void setUse(final Use use)
'''
pass
def getUse():
'''public Use getUse()
'''
pass
def addParameter():
'''public void addParameter(final ParameterDesc param)
public void addParameter(final QName paramName, final QName xmlType, final Class javaType, final byte parameterMode, final boolean inHeader, final boolean outHeader)
'''
pass
def getParameter():
'''public ParameterDesc getParameter(final int i)
'''
pass
def getParameters():
'''public ArrayList getParameters()
'''
pass
def setParameters():
'''public void setParameters(final ArrayList newParameters)
'''
pass
def getNumInParams():
'''public int getNumInParams()
'''
pass
def getNumOutParams():
'''public int getNumOutParams()
'''
pass
def getNumParams():
'''public int getNumParams()
'''
pass
def getMethod():
'''public Method getMethod()
'''
pass
def setMethod():
'''public void setMethod(final Method method)
'''
pass
def isReturnHeader():
'''public boolean isReturnHeader()
'''
pass
def setReturnHeader():
'''public void setReturnHeader(final boolean value)
'''
pass
def getParamByQName():
'''public ParameterDesc getParamByQName(final QName qname)
'''
pass
def getInputParamByQName():
'''public ParameterDesc getInputParamByQName(final QName qname)
'''
pass
def getOutputParamByQName():
'''public ParameterDesc getOutputParamByQName(final QName qname)
'''
pass
def getAllInParams():
'''public ArrayList getAllInParams()
'''
pass
def getAllOutParams():
'''public ArrayList getAllOutParams()
'''
pass
def getOutParams():
'''public ArrayList getOutParams()
'''
pass
def addFault():
'''public void addFault(final FaultDesc fault)
'''
pass
def getFaults():
'''public ArrayList getFaults()
'''
pass
def getFaultByClass():
'''public FaultDesc getFaultByClass(Class cls)
public FaultDesc getFaultByClass(final Class cls, final boolean checkParents)
'''
pass
def getFaultByQName():
'''public FaultDesc getFaultByQName(final QName qname)
'''
pass
def getFaultByXmlType():
'''public FaultDesc getFaultByXmlType(final QName xmlType)
'''
pass
def getReturnParamDesc():
'''public ParameterDesc getReturnParamDesc()
'''
pass
def toString():
'''public String toString()
public String toString(final String indent)
'''
pass
def getMessageOperationStyle():
'''public int getMessageOperationStyle()
'''
pass
def setMessageOperationStyle():
'''public void setMessageOperationStyle(final int messageOperationStyle)
'''
pass
def getMep():
'''public OperationType getMep()
'''
pass
def setMep():
'''public void setMep(final OperationType mep)
public void setMep(final String mepString)
'''
pass
