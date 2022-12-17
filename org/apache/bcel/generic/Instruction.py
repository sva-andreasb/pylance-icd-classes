def ():
    '''returns Instruction\n\n
    (final short opcode, final short length)\n
    '''
def dump():
    '''returns None\n\n
    dump(final DataOutputStream out)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def toString():
    '''returns String\n\n
    toString(final boolean verbose)\n
    toString()\n
    toString(final ConstantPool cp)\n
    '''
def copy():
    '''returns Instruction\n\n
    copy()\n
    '''
def consumeStack():
    '''returns int\n\n
    consumeStack(final ConstantPoolGen cpg)\n
    '''
def produceStack():
    '''returns int\n\n
    produceStack(final ConstantPoolGen cpg)\n
    '''
def getOpcode():
    '''returns short\n\n
    getOpcode()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object that)\n
    '''
