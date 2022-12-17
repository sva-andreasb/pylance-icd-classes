def ():
    '''returns Instruction\n\n
    (final short opcode)\n
    '''
def dump():
    '''returns None\n\n
    dump(final DataOutputStream out)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def consumeStack():
    '''returns int\n\n
    consumeStack(final ConstantPool cpg)\n
    '''
def produceStack():
    '''returns int\n\n
    produceStack(final ConstantPool cpg)\n
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
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    getType(final ConstantPool cp)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    getValue(final ConstantPool cpg)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def setIndex():
    '''returns None\n\n
    setIndex(final int i)\n
    '''
def isLoadInstruction():
    '''returns boolean\n\n
    isLoadInstruction()\n
    '''
def isASTORE():
    '''returns boolean\n\n
    isASTORE()\n
    '''
def isALOAD():
    '''returns boolean\n\n
    isALOAD()\n
    '''
def isStoreInstruction():
    '''returns boolean\n\n
    isStoreInstruction()\n
    '''
def isJsrInstruction():
    '''returns boolean\n\n
    isJsrInstruction()\n
    '''
def isConstantInstruction():
    '''returns boolean\n\n
    isConstantInstruction()\n
    '''
def isConstantPoolInstruction():
    '''returns boolean\n\n
    isConstantPoolInstruction()\n
    '''
def isStackProducer():
    '''returns boolean\n\n
    isStackProducer()\n
    '''
def isStackConsumer():
    '''returns boolean\n\n
    isStackConsumer()\n
    '''
def isIndexedInstruction():
    '''returns boolean\n\n
    isIndexedInstruction()\n
    '''
def isArrayCreationInstruction():
    '''returns boolean\n\n
    isArrayCreationInstruction()\n
    '''
def getLoadClassType():
    '''returns ObjectType\n\n
    getLoadClassType(final ConstantPool cpg)\n
    '''
def isReturnInstruction():
    '''returns boolean\n\n
    isReturnInstruction()\n
    '''
def isLocalVariableInstruction():
    '''returns boolean\n\n
    isLocalVariableInstruction()\n
    '''
def toString():
    '''returns String\n\n
    toString(final boolean verbose)\n
    toString()\n
    '''
