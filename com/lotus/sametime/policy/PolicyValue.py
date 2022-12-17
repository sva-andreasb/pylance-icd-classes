ATTR_NOTYPE = "byte  0"
ATTR_STRING = "byte  1"
ATTR_BOOL = "byte  2"
ATTR_INTEGER = "byte  3"
ATTR_BINARY = "byte  4"
SEL_DISABLE = "byte  0"
SEL_OVERRIDE = "byte  1"
SEL_INHERIT = "byte  2"
def ():
    '''returns PolicyValue\n\n
    (final String attrID, final byte attrType, final String value)\n
    (final NdrInputStream ndrInputStream)\n
    (final String s, final byte b, final String s2, final String attrName)\n
    (final String s, final byte b, final String s2, final String attrName, final byte selector)\n
    '''
def getAttrID():
    '''returns String\n\n
    getAttrID()\n
    '''
def setAttrID():
    '''returns None\n\n
    setAttrID(final String attrID)\n
    '''
def getAttrType():
    '''returns byte\n\n
    getAttrType()\n
    '''
def setAttrType():
    '''returns None\n\n
    setAttrType(final byte attrType)\n
    '''
def getAttrValue():
    '''returns String\n\n
    getAttrValue()\n
    '''
def setAttrValue():
    '''returns None\n\n
    setAttrValue(final String value)\n
    '''
def getAttrName():
    '''returns String\n\n
    getAttrName()\n
    '''
def setAttrName():
    '''returns None\n\n
    setAttrName(final String attrName)\n
    '''
def getSelector():
    '''returns byte\n\n
    getSelector()\n
    '''
def setSelector():
    '''returns None\n\n
    setSelector(final byte selector)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def dump():
    '''returns None\n\n
    dump(final NdrOutputStream ndrOutputStream)\n
    '''
def load():
    '''returns None\n\n
    load(final NdrInputStream ndrInputStream)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
