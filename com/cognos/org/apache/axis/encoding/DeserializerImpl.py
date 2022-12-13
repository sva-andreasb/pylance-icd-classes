def DeserializerImpl():
    '''    public DeserializerImpl()
    '''
def getMechanismType():
    '''    public String getMechanismType()
    '''
def getValue():
    '''    public Object getValue()
    public Object getValue(final Object hint)
    '''
def setValue():
    '''    public void setValue(final Object value)
    public void setValue(final Object value, final Object hint)
    '''
def setChildValue():
    '''    public void setChildValue(final Object value, final Object hint)
    '''
def setDefaultType():
    '''    public void setDefaultType(final QName qName)
    '''
def getDefaultType():
    '''    public QName getDefaultType()
    '''
def registerValueTarget():
    '''    public void registerValueTarget(final Target target)
    '''
def getValueTargets():
    '''    public Vector getValueTargets()
    '''
def removeValueTargets():
    '''    public void removeValueTargets()
    '''
def moveValueTargets():
    '''    public void moveValueTargets(final Deserializer other)
    '''
def componentsReady():
    '''    public boolean componentsReady()
    '''
def valueComplete():
    '''    public void valueComplete()
    '''
def addChildDeserializer():
    '''    public void addChildDeserializer(final Deserializer dSer)
    '''
def startElement():
    '''    public void startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)
    '''
def onStartElement():
    '''    public void onStartElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)
    '''
def onStartChild():
    '''    public SOAPHandler onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)
    '''
def endElement():
    '''    public final void endElement(final String namespace, final String localName, final DeserializationContext context)
    '''
def onEndElement():
    '''    public void onEndElement(final String namespace, final String localName, final DeserializationContext context)
    '''
