def ():
    '''returns InstructionLV\n\n
    (final short opcode, final int lvar)\n
    (final short opcode)\n
    '''
def dump():
    '''returns None\n\n
    dump(final DataOutputStream out)\n
    '''
def toString():
    '''returns String\n\n
    toString(final boolean verbose)\n
    '''
def isALOAD():
    '''returns boolean\n\n
    isALOAD()\n
    '''
def isASTORE():
    '''returns boolean\n\n
    isASTORE()\n
    '''
def getBaseOpcode():
    '''returns int\n\n
    getBaseOpcode()\n
    '''
def setIndex():
    '''returns None\n\n
    setIndex(final int i)\n
    '''
def canSetIndex():
    '''returns boolean\n\n
    canSetIndex()\n
    '''
def setIndexAndCopyIfNecessary():
    '''returns InstructionLV\n\n
    setIndexAndCopyIfNecessary(final int newIndex)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
