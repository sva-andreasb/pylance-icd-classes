def DeserializerImpl():
'''public DeserializerImpl()
'''
pass
def getMechanismType():
'''public String getMechanismType()
'''
pass
def getValue():
'''public Object getValue()
public Object getValue(final Object hint)
'''
pass
def setValue():
'''public void setValue(final Object value)
public void setValue(final Object value, final Object hint)
'''
pass
def setChildValue():
'''public void setChildValue(final Object value, final Object hint)
'''
pass
def setDefaultType():
'''public void setDefaultType(final QName qName)
'''
pass
def getDefaultType():
'''public QName getDefaultType()
'''
pass
def registerValueTarget():
'''public void registerValueTarget(final Target target)
'''
pass
def getValueTargets():
'''public Vector getValueTargets()
'''
pass
def removeValueTargets():
'''public void removeValueTargets()
'''
pass
def moveValueTargets():
'''public void moveValueTargets(final Deserializer other)
'''
pass
def componentsReady():
'''public boolean componentsReady()
'''
pass
def valueComplete():
'''public void valueComplete()
'''
pass
def addChildDeserializer():
'''public void addChildDeserializer(final Deserializer dSer)
'''
pass
def startElement():
'''public void startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)
'''
pass
def onStartElement():
'''public void onStartElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)
'''
pass
def onStartChild():
'''public SOAPHandler onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)
'''
pass
def endElement():
'''public final void endElement(final String namespace, final String localName, final DeserializationContext context)
'''
pass
def onEndElement():
'''public void onEndElement(final String namespace, final String localName, final DeserializationContext context)
'''
pass
