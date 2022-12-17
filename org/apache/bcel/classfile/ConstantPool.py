def ():
    '''returns ConstantPool\n\n
    (final Constant[] constant_pool)\n
    '''
def accept():
    '''returns None\n\n
    accept(final Visitor v)\n
    '''
def constantToString():
    '''returns String\n\n
    constantToString(Constant c)\n
    constantToString(final int index, final byte tag)\n
    '''
def dump():
    '''returns None\n\n
    dump(final DataOutputStream file)\n
    '''
def getConstant():
    '''returns Constant\n\n
    getConstant(final int index)\n
    getConstant(final int index, final byte tag)\n
    '''
def getConstantPool():
    '''returns Constant[]\n\n
    getConstantPool()\n
    '''
def getConstantString():
    '''returns String\n\n
    getConstantString(final int index, final byte tag)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def setConstant():
    '''returns None\n\n
    setConstant(final int index, final Constant constant)\n
    '''
def setConstantPool():
    '''returns None\n\n
    setConstantPool(final Constant[] constant_pool)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def copy():
    '''returns ConstantPool\n\n
    copy()\n
    '''
