def endDocument():
'''public void endDocument()
'''
pass
def startElement():
'''public void startElement(final String namespaceURI, final String localName, final String name, final Attributes atts)
public void startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)
'''
pass
def endElement():
'''public void endElement(final String namespaceURI, final String localName, final String name)
public void endElement(final String elemName)
'''
pass
def characters():
'''public void characters(final char[] ch, final int start, final int length)
public void characters(final String characters)
'''
pass
def charactersRaw():
'''public void charactersRaw(final char[] ch, final int start, final int length)
'''
pass
def cdata():
'''public void cdata(final char[] ch, final int start, final int length)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] ch, final int start, final int length)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String target, final String data)
'''
pass
def comment():
'''public void comment(final String data)
public void comment(final char[] ch, final int start, final int length)
'''
pass
def entityReference():
'''public void entityReference(final String name)
'''
pass
def addAttribute():
'''public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)
public void addAttribute(final String name, final String value)
'''
pass
def endCDATA():
'''public void endCDATA()
'''
pass
def addUniqueAttribute():
'''public void addUniqueAttribute(final String qName, final String value, final int flags)
'''
pass
def startPrefixMapping():
'''public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
public void startPrefixMapping(final String prefix, final String uri)
'''
pass
def namespaceAfterStartElement():
'''public void namespaceAfterStartElement(final String prefix, final String uri)
'''
pass
def flushPending():
'''public void flushPending()
'''
pass
