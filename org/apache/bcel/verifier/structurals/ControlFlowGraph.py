def ():
    '''returns InstructionContextImpl\n\n
    (final MethodGen method_gen)\n
    (final InstructionHandle inst)\n
    '''
def contextOf():
    '''returns InstructionContext\n\n
    contextOf(final InstructionHandle inst)\n
    '''
def contextsOf():
    '''returns InstructionContext[]\n\n
    contextsOf(final InstructionHandle[] insts)\n
    '''
def getInstructionContexts():
    '''returns InstructionContext[]\n\n
    getInstructionContexts()\n
    '''
def isDead():
    '''returns boolean\n\n
    isDead(final InstructionHandle i)\n
    '''
def getTag():
    '''returns int\n\n
    getTag()\n
    '''
def setTag():
    '''returns None\n\n
    setTag(final int tag)\n
    '''
def getExceptionHandlers():
    '''returns ExceptionHandler[]\n\n
    getExceptionHandlers()\n
    '''
def getOutFrame():
    '''returns Frame\n\n
    getOutFrame(final ArrayList execChain)\n
    '''
def getInFrame():
    '''returns Frame\n\n
    getInFrame()\n
    '''
def execute():
    '''returns boolean\n\n
    execute(final Frame inFrame, final ArrayList execPreds, final InstConstraintVisitor icv, final ExecutionVisitor ev)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getInstruction():
    '''returns InstructionHandle\n\n
    getInstruction()\n
    '''
def getSuccessors():
    '''returns InstructionContext[]\n\n
    getSuccessors()\n
    '''
