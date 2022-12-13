ATTR_NOTYPE = "byte  0"
ATTR_STRING = "byte  1"
ATTR_BOOL = "byte  2"
ATTR_INTEGER = "byte  3"
ATTR_BINARY = "byte  4"
SEL_DISABLE = "byte  0"
SEL_OVERRIDE = "byte  1"
SEL_INHERIT = "byte  2"
def PolicyValue():
    '''public PolicyValue(final String attrID, final byte attrType, final String value)
    public PolicyValue(final NdrInputStream ndrInputStream)
    public PolicyValue(final String s, final byte b, final String s2, final String attrName)
    public PolicyValue(final String s, final byte b, final String s2, final String attrName, final byte selector)
    '''
def getAttrID():
    '''public String getAttrID()
    '''
def setAttrID():
    '''public void setAttrID(final String attrID)
    '''
def getAttrType():
    '''public byte getAttrType()
    '''
def setAttrType():
    '''public void setAttrType(final byte attrType)
    '''
def getAttrValue():
    '''public String getAttrValue()
    '''
def setAttrValue():
    '''public void setAttrValue(final String value)
    '''
def getAttrName():
    '''public String getAttrName()
    '''
def setAttrName():
    '''public void setAttrName(final String attrName)
    '''
def getSelector():
    '''public byte getSelector()
    '''
def setSelector():
    '''public void setSelector(final byte selector)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def dump():
    '''public void dump(final NdrOutputStream ndrOutputStream)
    '''
def load():
    '''public void load(final NdrInputStream ndrInputStream)
    '''
def toString():
    '''public String toString()
    '''
