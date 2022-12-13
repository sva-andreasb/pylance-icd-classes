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
pass
def getAttrID():
'''public String getAttrID()
'''
pass
def setAttrID():
'''public void setAttrID(final String attrID)
'''
pass
def getAttrType():
'''public byte getAttrType()
'''
pass
def setAttrType():
'''public void setAttrType(final byte attrType)
'''
pass
def getAttrValue():
'''public String getAttrValue()
'''
pass
def setAttrValue():
'''public void setAttrValue(final String value)
'''
pass
def getAttrName():
'''public String getAttrName()
'''
pass
def setAttrName():
'''public void setAttrName(final String attrName)
'''
pass
def getSelector():
'''public byte getSelector()
'''
pass
def setSelector():
'''public void setSelector(final byte selector)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def dump():
'''public void dump(final NdrOutputStream ndrOutputStream)
'''
pass
def load():
'''public void load(final NdrInputStream ndrInputStream)
'''
pass
def toString():
'''public String toString()
'''
pass
