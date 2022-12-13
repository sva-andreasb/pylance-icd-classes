def MXParser():
    '''public MXParser()
    '''
def setFeature():
    '''public void setFeature(final String name, final boolean state)
    '''
def getFeature():
    '''public boolean getFeature(final String name)
    '''
def setProperty():
    '''public void setProperty(final String name, final Object value)
    '''
def getProperty():
    '''public Object getProperty(final String name)
    '''
def setInput():
    '''public void setInput(final Reader in)
    public void setInput(final InputStream inputStream, final String inputEncoding)
    '''
def getInputEncoding():
    '''public String getInputEncoding()
    '''
def defineEntityReplacementText():
    '''public void defineEntityReplacementText(final String entityName, final String replacementText)
    '''
def getNamespaceCount():
    '''public int getNamespaceCount(final int depth)
    '''
def getNamespacePrefix():
    '''public String getNamespacePrefix(final int pos)
    '''
def getNamespaceUri():
    '''public String getNamespaceUri(final int pos)
    '''
def getNamespace():
    '''public String getNamespace(final String prefix)
    public String getNamespace()
    '''
def getDepth():
    '''public int getDepth()
    '''
def getPositionDescription():
    '''public String getPositionDescription()
    '''
def getLineNumber():
    '''public int getLineNumber()
    '''
def getColumnNumber():
    '''public int getColumnNumber()
    '''
def isWhitespace():
    '''public boolean isWhitespace()
    '''
def getText():
    '''public String getText()
    '''
def getTextCharacters():
    '''public char[] getTextCharacters(final int[] holderForStartAndLength)
    '''
def getName():
    '''public String getName()
    '''
def getPrefix():
    '''public String getPrefix()
    '''
def isEmptyElementTag():
    '''public boolean isEmptyElementTag()
    '''
def getAttributeCount():
    '''public int getAttributeCount()
    '''
def getAttributeNamespace():
    '''public String getAttributeNamespace(final int index)
    '''
def getAttributeName():
    '''public String getAttributeName(final int index)
    '''
def getAttributePrefix():
    '''public String getAttributePrefix(final int index)
    '''
def getAttributeType():
    '''public String getAttributeType(final int index)
    '''
def isAttributeDefault():
    '''public boolean isAttributeDefault(final int index)
    '''
def getAttributeValue():
    '''public String getAttributeValue(final int index)
    public String getAttributeValue(String namespace, final String name)
    '''
def getEventType():
    '''public int getEventType()
    '''
def require():
    '''public void require(final int type, final String namespace, final String name)
    '''
def skipSubTree():
    '''public void skipSubTree()
    '''
def nextText():
    '''public String nextText()
    '''
def nextTag():
    '''public int nextTag()
    '''
def next():
    '''public int next()
    '''
def nextToken():
    '''public int nextToken()
    '''
def parseEndTag():
    '''public int parseEndTag()
    '''
def parseStartTag():
    '''public int parseStartTag()
    '''
