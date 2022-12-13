def RuntimeConfigurable():
    '''public RuntimeConfigurable(final Object proxy, final String elementTag)
    '''
def setProxy():
    '''public synchronized void setProxy(final Object proxy)
    '''
def getProxy():
    '''public synchronized Object getProxy()
    '''
def getId():
    '''public synchronized String getId()
    '''
def getPolyType():
    '''public synchronized String getPolyType()
    '''
def setPolyType():
    '''public synchronized void setPolyType(final String polyType)
    '''
def setAttributes():
    '''public synchronized void setAttributes(final AttributeList attributes)
    '''
def setAttribute():
    '''public synchronized void setAttribute(final String name, final String value)
    '''
def removeAttribute():
    '''public synchronized void removeAttribute(final String name)
    '''
def getAttributeMap():
    '''public synchronized Hashtable getAttributeMap()
    '''
def getAttributes():
    '''public synchronized AttributeList getAttributes()
    '''
def addChild():
    '''public synchronized void addChild(final RuntimeConfigurable child)
    '''
def getChildren():
    '''public synchronized Enumeration getChildren()
    '''
def addText():
    '''public synchronized void addText(final String data)
    public synchronized void addText(final char[] buf, final int start, final int count)
    '''
def getText():
    '''public synchronized StringBuffer getText()
    '''
def setElementTag():
    '''public synchronized void setElementTag(final String elementTag)
    '''
def getElementTag():
    '''public synchronized String getElementTag()
    '''
def maybeConfigure():
    '''public void maybeConfigure(final Project p)
    public synchronized void maybeConfigure(final Project p, final boolean configureChildren)
    '''
def reconfigure():
    '''public void reconfigure(final Project p)
    '''
def applyPreSet():
    '''public void applyPreSet(final RuntimeConfigurable r)
    '''
