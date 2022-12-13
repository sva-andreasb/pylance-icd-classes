NAMESPACE = "String  urn:xmpp:jingle:1""
ACTION_ATTRIBUTE_NAME = "String  action""
INITIATOR_ATTRIBUTE_NAME = "String  initiator""
RESPONDER_ATTRIBUTE_NAME = "String  responder""
SESSION_ID_ATTRIBUTE_NAME = "String  sid""
ELEMENT = "String  jingle""
def getInitiator():
'''public FullJid getInitiator()
'''
pass
def getResponder():
'''public FullJid getResponder()
'''
pass
def getSid():
'''public String getSid()
'''
pass
def getAction():
'''public JingleAction getAction()
'''
pass
def getReason():
'''public JingleReason getReason()
'''
pass
def getContents():
'''public List<JingleContent> getContents()
'''
pass
def getSoleContentOrThrow():
'''public JingleContent getSoleContentOrThrow()
'''
pass
def getBuilder():
'''public static Builder getBuilder()
'''
pass
def setSessionId():
'''public Builder setSessionId(final String sessionId)
'''
pass
def setAction():
'''public Builder setAction(final JingleAction action)
'''
pass
def setInitiator():
'''public Builder setInitiator(final FullJid initator)
'''
pass
def setResponder():
'''public Builder setResponder(final FullJid responder)
'''
pass
def addJingleContent():
'''public Builder addJingleContent(final JingleContent content)
'''
pass
def setReason():
'''public Builder setReason(final JingleReason.Reason reason)
public Builder setReason(final JingleReason reason)
'''
pass
def build():
'''public Jingle build()
'''
pass
