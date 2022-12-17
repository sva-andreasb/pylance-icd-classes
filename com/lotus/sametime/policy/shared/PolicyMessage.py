POLICY_QUERY_ATTRIBUTE_CLIENT = "short  1"
POLICY_QUERY_ATTRIBUTE_SA = "short  2"
POLICY_QUERY_RESPONSE = "short  Short.MIN_VALUE"
def ():
    '''returns PolicyMessage\n\n
    (final short msgType, final Integer requestID, final STId userID)\n
    (final short n, final Integer n2, final STId stId, final ArrayList c)\n
    (final short msgType, final Integer requestID)\n
    (final short n, final Integer n2, final ArrayList c)\n
    (final short msgType, final NdrInputStream ndrInputStream)\n
    '''
def getUserID():
    '''returns STId\n\n
    getUserID()\n
    '''
def hasUserID():
    '''returns boolean\n\n
    hasUserID()\n
    '''
def getMsgType():
    '''returns short\n\n
    getMsgType()\n
    '''
def getRequestID():
    '''returns Integer\n\n
    getRequestID()\n
    '''
def getReqAttributes():
    '''returns ArrayList\n\n
    getReqAttributes()\n
    '''
def getRequestedAttribute():
    '''returns String\n\n
    getRequestedAttribute(final int index)\n
    '''
def getEffectivePolicies():
    '''returns ArrayList\n\n
    getEffectivePolicies()\n
    '''
def getEffectivePoliciesStringArray():
    '''returns PolicyValue[]\n\n
    getEffectivePoliciesStringArray()\n
    '''
def getStatus():
    '''returns int\n\n
    getStatus()\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final int status)\n
    '''
def isAllAttributeRequest():
    '''returns boolean\n\n
    isAllAttributeRequest()\n
    '''
def isDataLoaded():
    '''returns boolean\n\n
    isDataLoaded()\n
    '''
def addAttributeListForRequest():
    '''returns None\n\n
    addAttributeListForRequest(final ArrayList c)\n
    '''
def addAttributeForRequest():
    '''returns None\n\n
    addAttributeForRequest(final String e)\n
    '''
def addPolicyValueListForResponse():
    '''returns None\n\n
    addPolicyValueListForResponse(final ArrayList c)\n
    '''
def addAttributeForResponse():
    '''returns None\n\n
    addAttributeForResponse(final PolicyValue e)\n
    '''
def dumpRequestInfo():
    '''returns None\n\n
    dumpRequestInfo(final NdrOutputStream ndrOutputStream)\n
    '''
def dumpResponseInfo():
    '''returns None\n\n
    dumpResponseInfo(final NdrOutputStream ndrOutputStream)\n
    '''
def isIncorrectClientRequest():
    '''returns boolean\n\n
    isIncorrectClientRequest(final ChannelEvent channelEvent)\n
    '''
