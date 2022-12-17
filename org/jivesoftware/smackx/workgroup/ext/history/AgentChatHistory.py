ELEMENT_NAME = "String  \"chat-sessions\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def ():
    '''returns AgentChatHistory\n\n
    (final EntityBareJid agentJID, final int maxSessions, final Date startDate)\n
    (final EntityBareJid agentJID, final int maxSessions)\n
    ()\n
    '''
def addChatSession():
    '''returns None\n\n
    addChatSession(final AgentChatSession chatSession)\n
    '''
def getAgentChatSessions():
    '''returns Collection<AgentChatSession>\n\n
    getAgentChatSessions()\n
    '''
def parse():
    '''returns AgentChatHistory\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
