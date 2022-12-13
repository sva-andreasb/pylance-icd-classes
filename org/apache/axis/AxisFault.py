def makeFault():
'''public static AxisFault makeFault(Exception e)
'''
pass
def AxisFault():
'''public AxisFault(final String code, final String faultString, final String actor, final Element[] details)
public AxisFault(final QName code, final String faultString, final String actor, final Element[] details)
public AxisFault(final QName code, final QName[] subcodes, final String faultString, final String actor, final String node, final Element[] details)
public AxisFault(final String message)
public AxisFault()
public AxisFault(final String message, final Throwable t)
'''
pass
def clearFaultDetails():
'''public void clearFaultDetails()
'''
pass
def dump():
'''public void dump()
'''
pass
def dumpToString():
'''public String dumpToString()
'''
pass
def setFaultCode():
'''public void setFaultCode(final QName code)
public void setFaultCode(final String code)
'''
pass
def setFaultCodeAsString():
'''public void setFaultCodeAsString(final String code)
'''
pass
def getFaultCode():
'''public QName getFaultCode()
'''
pass
def addFaultSubCodeAsString():
'''public void addFaultSubCodeAsString(final String code)
'''
pass
def addFaultSubCode():
'''public void addFaultSubCode(final QName code)
'''
pass
def clearFaultSubCodes():
'''public void clearFaultSubCodes()
'''
pass
def getFaultSubCodes():
'''public QName[] getFaultSubCodes()
'''
pass
def setFaultString():
'''public void setFaultString(final String str)
'''
pass
def getFaultString():
'''public String getFaultString()
'''
pass
def setFaultReason():
'''public void setFaultReason(final String str)
'''
pass
def getFaultReason():
'''public String getFaultReason()
'''
pass
def setFaultActor():
'''public void setFaultActor(final String actor)
'''
pass
def getFaultActor():
'''public String getFaultActor()
'''
pass
def getFaultRole():
'''public String getFaultRole()
'''
pass
def setFaultRole():
'''public void setFaultRole(final String role)
'''
pass
def getFaultNode():
'''public String getFaultNode()
'''
pass
def setFaultNode():
'''public void setFaultNode(final String node)
'''
pass
def setFaultDetail():
'''public void setFaultDetail(final Element[] details)
'''
pass
def setFaultDetailString():
'''public void setFaultDetailString(final String details)
'''
pass
def addFaultDetailString():
'''public void addFaultDetailString(final String detail)
'''
pass
def addFaultDetail():
'''public void addFaultDetail(final Element detail)
public void addFaultDetail(final QName qname, final String body)
'''
pass
def getFaultDetails():
'''public Element[] getFaultDetails()
'''
pass
def lookupFaultDetail():
'''public Element lookupFaultDetail(final QName qname)
'''
pass
def removeFaultDetail():
'''public boolean removeFaultDetail(final QName qname)
'''
pass
def output():
'''public void output(final SerializationContext context)
'''
pass
def toString():
'''public String toString()
'''
pass
def printStackTrace():
'''public void printStackTrace(final PrintStream ps)
public void printStackTrace(final PrintWriter pw)
'''
pass
def addHeader():
'''public void addHeader(final SOAPHeaderElement header)
'''
pass
def getHeaders():
'''public ArrayList getHeaders()
'''
pass
def clearHeaders():
'''public void clearHeaders()
'''
pass
def writeDetails():
'''public void writeDetails(final QName qname, final SerializationContext context)
'''
pass
def addHostnameIfNeeded():
'''public void addHostnameIfNeeded()
'''
pass
def addHostname():
'''public void addHostname(final String hostname)
'''
pass
def removeHostname():
'''public void removeHostname()
'''
pass
