ELEMENT = "String  fields""
NAMESPACE = "String  urn:xmpp:iot:sensordata""
def IoTFieldsExtension():
'''public IoTFieldsExtension(final int seqNr, final boolean done, final NodeElement node)
public IoTFieldsExtension(final int seqNr, final boolean done, final List<NodeElement> nodes)
'''
pass
def getSequenceNr():
'''public int getSequenceNr()
'''
pass
def isDone():
'''public boolean isDone()
'''
pass
def getNodes():
'''public List<NodeElement> getNodes()
'''
pass
def getElementName():
'''public String getElementName()
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def toXML():
'''public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
def buildFor():
'''public static IoTFieldsExtension buildFor(final int seqNr, final boolean done, final NodeInfo nodeInfo, final List<? extends IoTDataField> data)
'''
pass
def from():
'''public static IoTFieldsExtension from(final Message message)
'''
pass
