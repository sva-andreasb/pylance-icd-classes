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
pass
def getUserID():
'''public STId getUserID()
'''
pass
def hasUserID():
'''public boolean hasUserID()
'''
pass
def getMsgType():
'''public short getMsgType()
'''
pass
def getRequestID():
'''public Integer getRequestID()
'''
pass
def getReqAttributes():
'''public ArrayList getReqAttributes()
'''
pass
def getRequestedAttribute():
'''public String getRequestedAttribute(final int index)
'''
pass
def getEffectivePolicies():
'''public ArrayList getEffectivePolicies()
'''
pass
def getEffectivePoliciesStringArray():
'''public PolicyValue[] getEffectivePoliciesStringArray()
'''
pass
def getStatus():
'''public int getStatus()
'''
pass
def setStatus():
'''public void setStatus(final int status)
'''
pass
def isAllAttributeRequest():
'''public boolean isAllAttributeRequest()
'''
pass
def isDataLoaded():
'''public boolean isDataLoaded()
'''
pass
def addAttributeListForRequest():
'''public void addAttributeListForRequest(final ArrayList c)
'''
pass
def addAttributeForRequest():
'''public void addAttributeForRequest(final String e)
'''
pass
def addPolicyValueListForResponse():
'''public void addPolicyValueListForResponse(final ArrayList c)
'''
pass
def addAttributeForResponse():
'''public void addAttributeForResponse(final PolicyValue e)
'''
pass
def dumpRequestInfo():
'''public void dumpRequestInfo(final NdrOutputStream ndrOutputStream)
'''
pass
def dumpResponseInfo():
'''public void dumpResponseInfo(final NdrOutputStream ndrOutputStream)
'''
pass
def isIncorrectClientRequest():
'''public boolean isIncorrectClientRequest(final ChannelEvent channelEvent)
'''
pass
