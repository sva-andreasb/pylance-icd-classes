def ():
    '''returns InstructionBranch\n\n
    (final short opcode, final InstructionHandle target)\n
    (final short opcode, final int index)\n
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
def getTarget():
    '''returns InstructionHandle\n\n
    getTarget()\n
    '''
def setTarget():
    '''returns None\n\n
    setTarget(final InstructionHandle target)\n
    '''
def updateTarget():
    '''returns None\n\n
    updateTarget(final InstructionHandle oldHandle, final InstructionHandle newHandle)\n
    '''
def containsTarget():
    '''returns boolean\n\n
    containsTarget(final InstructionHandle ih)\n
    '''
def getType():
    '''returns Type\n\n
    getType(final ConstantPool cp)\n
    '''
def physicalSuccessor():
    '''returns InstructionHandle\n\n
    physicalSuccessor()\n
    '''
def isIfInstruction():
    '''returns boolean\n\n
    isIfInstruction()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
