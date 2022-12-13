def MXParser():
'''public MXParser()
'''
pass
def setFeature():
'''public void setFeature(final String name, final boolean state)
'''
pass
def getFeature():
'''public boolean getFeature(final String name)
'''
pass
def setProperty():
'''public void setProperty(final String name, final Object value)
'''
pass
def getProperty():
'''public Object getProperty(final String name)
'''
pass
def setInput():
'''public void setInput(final Reader in)
public void setInput(final InputStream inputStream, final String inputEncoding)
'''
pass
def getInputEncoding():
'''public String getInputEncoding()
'''
pass
def defineEntityReplacementText():
'''public void defineEntityReplacementText(final String entityName, final String replacementText)
'''
pass
def getNamespaceCount():
'''public int getNamespaceCount(final int depth)
'''
pass
def getNamespacePrefix():
'''public String getNamespacePrefix(final int pos)
'''
pass
def getNamespaceUri():
'''public String getNamespaceUri(final int pos)
'''
pass
def getNamespace():
'''public String getNamespace(final String prefix)
public String getNamespace()
'''
pass
def getDepth():
'''public int getDepth()
'''
pass
def getPositionDescription():
'''public String getPositionDescription()
'''
pass
def getLineNumber():
'''public int getLineNumber()
'''
pass
def getColumnNumber():
'''public int getColumnNumber()
'''
pass
def isWhitespace():
'''public boolean isWhitespace()
'''
pass
def getText():
'''public String getText()
'''
pass
def getTextCharacters():
'''public char[] getTextCharacters(final int[] holderForStartAndLength)
'''
pass
def getName():
'''public String getName()
'''
pass
def getPrefix():
'''public String getPrefix()
'''
pass
def isEmptyElementTag():
'''public boolean isEmptyElementTag()
'''
pass
def getAttributeCount():
'''public int getAttributeCount()
'''
pass
def getAttributeNamespace():
'''public String getAttributeNamespace(final int index)
'''
pass
def getAttributeName():
'''public String getAttributeName(final int index)
'''
pass
def getAttributePrefix():
'''public String getAttributePrefix(final int index)
'''
pass
def getAttributeType():
'''public String getAttributeType(final int index)
'''
pass
def isAttributeDefault():
'''public boolean isAttributeDefault(final int index)
'''
pass
def getAttributeValue():
'''public String getAttributeValue(final int index)
public String getAttributeValue(String namespace, final String name)
'''
pass
def getEventType():
'''public int getEventType()
'''
pass
def require():
'''public void require(final int type, final String namespace, final String name)
'''
pass
def skipSubTree():
'''public void skipSubTree()
'''
pass
def nextText():
'''public String nextText()
'''
pass
def nextTag():
'''public int nextTag()
'''
pass
def next():
'''public int next()
'''
pass
def nextToken():
'''public int nextToken()
'''
pass
def parseEndTag():
'''public int parseEndTag()
'''
pass
def parseStartTag():
'''public int parseStartTag()
'''
pass
