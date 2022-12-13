POLICY_QUERY_ATTRIBUTE_CLIENT = "short  1"
POLICY_QUERY_ATTRIBUTE_SA = "short  2"
POLICY_QUERY_RESPONSE = "short  Short.MIN_VALUE"
def PolicyMessage():
    '''public PolicyMessage(final short msgType, final Integer requestID, final STId userID)
    public PolicyMessage(final short n, final Integer n2, final STId stId, final ArrayList c)
    public PolicyMessage(final short msgType, final Integer requestID)
    public PolicyMessage(final short n, final Integer n2, final ArrayList c)
    public PolicyMessage(final short msgType, final NdrInputStream ndrInputStream)
    '''
def getUserID():
    '''public STId getUserID()
    '''
def hasUserID():
    '''public boolean hasUserID()
    '''
def getMsgType():
    '''public short getMsgType()
    '''
def getRequestID():
    '''public Integer getRequestID()
    '''
def getReqAttributes():
    '''public ArrayList getReqAttributes()
    '''
def getRequestedAttribute():
    '''public String getRequestedAttribute(final int index)
    '''
def getEffectivePolicies():
    '''public ArrayList getEffectivePolicies()
    '''
def getEffectivePoliciesStringArray():
    '''public PolicyValue[] getEffectivePoliciesStringArray()
    '''
def getStatus():
    '''public int getStatus()
    '''
def setStatus():
    '''public void setStatus(final int status)
    '''
def isAllAttributeRequest():
    '''public boolean isAllAttributeRequest()
    '''
def isDataLoaded():
    '''public boolean isDataLoaded()
    '''
def addAttributeListForRequest():
    '''public void addAttributeListForRequest(final ArrayList c)
    '''
def addAttributeForRequest():
    '''public void addAttributeForRequest(final String e)
    '''
def addPolicyValueListForResponse():
    '''public void addPolicyValueListForResponse(final ArrayList c)
    '''
def addAttributeForResponse():
    '''public void addAttributeForResponse(final PolicyValue e)
    '''
def dumpRequestInfo():
    '''public void dumpRequestInfo(final NdrOutputStream ndrOutputStream)
    '''
def dumpResponseInfo():
    '''public void dumpResponseInfo(final NdrOutputStream ndrOutputStream)
    '''
def isIncorrectClientRequest():
    '''public boolean isIncorrectClientRequest(final ChannelEvent channelEvent)
    '''
