def ():
    '''returns TextSerializationContext\n\n
    (final Writer writer)\n
    (final Writer writer, final MessageContext msgContext)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Boolean sendNull, final Boolean sendType)\n
    '''
def writeDOMElement():
    '''returns None\n\n
    writeDOMElement(final Element el)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement()\n
    '''
def writeChars():
    '''returns None\n\n
    writeChars(final char[] p1, final int p2, final int p3)\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final String string)\n
    '''
