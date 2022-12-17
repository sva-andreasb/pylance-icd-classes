def ():
    '''returns LocalVariableGen\n\n
    (final int index, final String name, final Type type, final InstructionHandle start, final InstructionHandle end)\n
    '''
def getLocalVariable():
    '''returns LocalVariable\n\n
    getLocalVariable(final ConstantPool cp)\n
    '''
def setIndex():
    '''returns None\n\n
    setIndex(final int index)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setType():
    '''returns None\n\n
    setType(final Type type)\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getStart():
    '''returns InstructionHandle\n\n
    getStart()\n
    '''
def getEnd():
    '''returns InstructionHandle\n\n
    getEnd()\n
    '''
def setStart():
    '''returns None\n\n
    setStart(final InstructionHandle start)\n
    '''
def setEnd():
    '''returns None\n\n
    setEnd(final InstructionHandle end)\n
    '''
def updateTarget():
    '''returns None\n\n
    updateTarget(final InstructionHandle old_ih, final InstructionHandle new_ih)\n
    '''
def containsTarget():
    '''returns boolean\n\n
    containsTarget(final InstructionHandle ih)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
