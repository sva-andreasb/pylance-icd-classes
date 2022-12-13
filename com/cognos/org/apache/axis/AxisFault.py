def makeFault():
    '''    public static AxisFault makeFault(Exception e)
    '''
def AxisFault():
    '''    public AxisFault(final String code, final String faultString, final String actor, final Element[] details)
    public AxisFault(final QName code, final String faultString, final String actor, final Element[] details)
    public AxisFault(final QName code, final QName[] subcodes, final String faultString, final String actor, final String node, final Element[] details)
    public AxisFault(final String message)
    public AxisFault()
    public AxisFault(final String message, final Throwable t)
    '''
def clearFaultDetails():
    '''    public void clearFaultDetails()
    '''
def dump():
    '''    public void dump()
    '''
def dumpToString():
    '''    public String dumpToString()
    '''
def setFaultCode():
    '''    public void setFaultCode(final QName code)
    public void setFaultCode(final String code)
    '''
def setFaultCodeAsString():
    '''    public void setFaultCodeAsString(final String code)
    '''
def getFaultCode():
    '''    public QName getFaultCode()
    '''
def addFaultSubCodeAsString():
    '''    public void addFaultSubCodeAsString(final String code)
    '''
def addFaultSubCode():
    '''    public void addFaultSubCode(final QName code)
    '''
def clearFaultSubCodes():
    '''    public void clearFaultSubCodes()
    '''
def getFaultSubCodes():
    '''    public QName[] getFaultSubCodes()
    '''
def setFaultString():
    '''    public void setFaultString(final String str)
    '''
def getFaultString():
    '''    public String getFaultString()
    '''
def setFaultReason():
    '''    public void setFaultReason(final String str)
    '''
def getFaultReason():
    '''    public String getFaultReason()
    '''
def setFaultActor():
    '''    public void setFaultActor(final String actor)
    '''
def getFaultActor():
    '''    public String getFaultActor()
    '''
def getFaultRole():
    '''    public String getFaultRole()
    '''
def setFaultRole():
    '''    public void setFaultRole(final String role)
    '''
def getFaultNode():
    '''    public String getFaultNode()
    '''
def setFaultNode():
    '''    public void setFaultNode(final String node)
    '''
def setFaultDetail():
    '''    public void setFaultDetail(final Element[] details)
    '''
def setFaultDetailString():
    '''    public void setFaultDetailString(final String details)
    '''
def addFaultDetailString():
    '''    public void addFaultDetailString(final String detail)
    '''
def addFaultDetail():
    '''    public void addFaultDetail(final Element detail)
    public void addFaultDetail(final QName qname, final String body)
    '''
def getFaultDetails():
    '''    public Element[] getFaultDetails()
    '''
def lookupFaultDetail():
    '''    public Element lookupFaultDetail(final QName qname)
    '''
def removeFaultDetail():
    '''    public boolean removeFaultDetail(final QName qname)
    '''
def output():
    '''    public void output(final SerializationContext context)
    '''
def toString():
    '''    public String toString()
    '''
def printStackTrace():
    '''    public void printStackTrace(final PrintStream ps)
    public void printStackTrace(final PrintWriter pw)
    '''
def addHeader():
    '''    public void addHeader(final SOAPHeaderElement header)
    '''
def getHeaders():
    '''    public ArrayList getHeaders()
    '''
def clearHeaders():
    '''    public void clearHeaders()
    '''
def writeDetails():
    '''    public void writeDetails(final QName qname, final SerializationContext context)
    '''
def addHostnameIfNeeded():
    '''    public void addHostnameIfNeeded()
    '''
def addHostname():
    '''    public void addHostname(final String hostname)
    '''
def removeHostname():
    '''    public void removeHostname()
    '''
