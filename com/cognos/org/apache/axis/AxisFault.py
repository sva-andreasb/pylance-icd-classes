def ():
    '''returns AxisFault\n\n
    (final String code, final String faultString, final String actor, final Element[] details)\n
    (final QName code, final String faultString, final String actor, final Element[] details)\n
    (final QName code, final QName[] subcodes, final String faultString, final String actor, final String node, final Element[] details)\n
    (final String message)\n
    ()\n
    (final String message, final Throwable t)\n
    '''
def clearFaultDetails():
    '''returns None\n\n
    clearFaultDetails()\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    '''
def dumpToString():
    '''returns String\n\n
    dumpToString()\n
    '''
def setFaultCode():
    '''returns None\n\n
    setFaultCode(final QName code)\n
    setFaultCode(final String code)\n
    '''
def setFaultCodeAsString():
    '''returns None\n\n
    setFaultCodeAsString(final String code)\n
    '''
def getFaultCode():
    '''returns QName\n\n
    getFaultCode()\n
    '''
def addFaultSubCodeAsString():
    '''returns None\n\n
    addFaultSubCodeAsString(final String code)\n
    '''
def addFaultSubCode():
    '''returns None\n\n
    addFaultSubCode(final QName code)\n
    '''
def clearFaultSubCodes():
    '''returns None\n\n
    clearFaultSubCodes()\n
    '''
def getFaultSubCodes():
    '''returns QName[]\n\n
    getFaultSubCodes()\n
    '''
def setFaultString():
    '''returns None\n\n
    setFaultString(final String str)\n
    '''
def getFaultString():
    '''returns String\n\n
    getFaultString()\n
    '''
def setFaultReason():
    '''returns None\n\n
    setFaultReason(final String str)\n
    '''
def getFaultReason():
    '''returns String\n\n
    getFaultReason()\n
    '''
def setFaultActor():
    '''returns None\n\n
    setFaultActor(final String actor)\n
    '''
def getFaultActor():
    '''returns String\n\n
    getFaultActor()\n
    '''
def getFaultRole():
    '''returns String\n\n
    getFaultRole()\n
    '''
def setFaultRole():
    '''returns None\n\n
    setFaultRole(final String role)\n
    '''
def getFaultNode():
    '''returns String\n\n
    getFaultNode()\n
    '''
def setFaultNode():
    '''returns None\n\n
    setFaultNode(final String node)\n
    '''
def setFaultDetail():
    '''returns None\n\n
    setFaultDetail(final Element[] details)\n
    '''
def setFaultDetailString():
    '''returns None\n\n
    setFaultDetailString(final String details)\n
    '''
def addFaultDetailString():
    '''returns None\n\n
    addFaultDetailString(final String detail)\n
    '''
def addFaultDetail():
    '''returns None\n\n
    addFaultDetail(final Element detail)\n
    addFaultDetail(final QName qname, final String body)\n
    '''
def getFaultDetails():
    '''returns Element[]\n\n
    getFaultDetails()\n
    '''
def lookupFaultDetail():
    '''returns Element\n\n
    lookupFaultDetail(final QName qname)\n
    '''
def removeFaultDetail():
    '''returns boolean\n\n
    removeFaultDetail(final QName qname)\n
    '''
def output():
    '''returns None\n\n
    output(final SerializationContext context)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def printStackTrace():
    '''returns None\n\n
    printStackTrace(final PrintStream ps)\n
    printStackTrace(final PrintWriter pw)\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final SOAPHeaderElement header)\n
    '''
def getHeaders():
    '''returns ArrayList\n\n
    getHeaders()\n
    '''
def clearHeaders():
    '''returns None\n\n
    clearHeaders()\n
    '''
def writeDetails():
    '''returns None\n\n
    writeDetails(final QName qname, final SerializationContext context)\n
    '''
def addHostnameIfNeeded():
    '''returns None\n\n
    addHostnameIfNeeded()\n
    '''
def addHostname():
    '''returns None\n\n
    addHostname(final String hostname)\n
    '''
def removeHostname():
    '''returns None\n\n
    removeHostname()\n
    '''
