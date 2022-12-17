def ():
    '''returns CodeExceptionGen\n\n
    (final InstructionHandle start_pc, final InstructionHandle end_pc, final InstructionHandle handler_pc, final ObjectType catch_type)\n
    '''
def getCodeException():
    '''returns CodeException\n\n
    getCodeException(final ConstantPool cp)\n
    '''
def setStartPC():
    '''returns None\n\n
    setStartPC(final InstructionHandle start_pc)\n
    '''
def setEndPC():
    '''returns None\n\n
    setEndPC(final InstructionHandle end_pc)\n
    '''
def setHandlerPC():
    '''returns None\n\n
    setHandlerPC(final InstructionHandle handler_pc)\n
    '''
def updateTarget():
    '''returns None\n\n
    updateTarget(final InstructionHandle old_ih, final InstructionHandle new_ih)\n
    '''
def containsTarget():
    '''returns boolean\n\n
    containsTarget(final InstructionHandle ih)\n
    '''
def setCatchType():
    '''returns None\n\n
    setCatchType(final ObjectType catch_type)\n
    '''
def getCatchType():
    '''returns ObjectType\n\n
    getCatchType()\n
    '''
def getStartPC():
    '''returns InstructionHandle\n\n
    getStartPC()\n
    '''
def getEndPC():
    '''returns InstructionHandle\n\n
    getEndPC()\n
    '''
def getHandlerPC():
    '''returns InstructionHandle\n\n
    getHandlerPC()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
