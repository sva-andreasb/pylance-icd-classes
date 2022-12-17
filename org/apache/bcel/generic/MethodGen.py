def ():
    '''returns MethodGen\n\n
    (final int access_flags, final Type return_type, final Type[] arg_types, String[] arg_names, final String method_name, final String class_name, final InstructionList il, final ConstantPoolGen cp)\n
    (final Method m, final String class_name, final ConstantPoolGen cp)\n
    '''
def addLocalVariable():
    '''returns LocalVariableGen\n\n
    addLocalVariable(final String name, final Type type, final int slot, final InstructionHandle start, final InstructionHandle end)\n
    addLocalVariable(final String name, final Type type, final InstructionHandle start, final InstructionHandle end)\n
    '''
def removeLocalVariable():
    '''returns None\n\n
    removeLocalVariable(final LocalVariableGen l)\n
    '''
def removeLocalVariables():
    '''returns None\n\n
    removeLocalVariables()\n
    '''
def getLocalVariables():
    '''returns LocalVariableGen[]\n\n
    getLocalVariables()\n
    '''
def getLocalVariableTable():
    '''returns LocalVariableTable\n\n
    getLocalVariableTable(final ConstantPoolGen cp)\n
    '''
def addLineNumber():
    '''returns LineNumberGen\n\n
    addLineNumber(final InstructionHandle ih, final int src_line)\n
    '''
def removeLineNumber():
    '''returns None\n\n
    removeLineNumber(final LineNumberGen l)\n
    '''
def removeLineNumbers():
    '''returns None\n\n
    removeLineNumbers()\n
    '''
def getLineNumbers():
    '''returns LineNumberGen[]\n\n
    getLineNumbers()\n
    '''
def getLineNumberTable():
    '''returns LineNumberTable\n\n
    getLineNumberTable(final ConstantPoolGen cp)\n
    '''
def addExceptionHandler():
    '''returns CodeExceptionGen\n\n
    addExceptionHandler(final InstructionHandle start_pc, final InstructionHandle end_pc, final InstructionHandle handler_pc, final ObjectType catch_type)\n
    '''
def removeExceptionHandler():
    '''returns None\n\n
    removeExceptionHandler(final CodeExceptionGen c)\n
    '''
def removeExceptionHandlers():
    '''returns None\n\n
    removeExceptionHandlers()\n
    '''
def getExceptionHandlers():
    '''returns CodeExceptionGen[]\n\n
    getExceptionHandlers()\n
    '''
def addException():
    '''returns None\n\n
    addException(final String class_name)\n
    '''
def removeException():
    '''returns None\n\n
    removeException(final String c)\n
    '''
def removeExceptions():
    '''returns None\n\n
    removeExceptions()\n
    '''
def getExceptions():
    '''returns String[]\n\n
    getExceptions()\n
    '''
def addCodeAttribute():
    '''returns None\n\n
    addCodeAttribute(final Attribute a)\n
    '''
def removeCodeAttribute():
    '''returns None\n\n
    removeCodeAttribute(final Attribute a)\n
    '''
def removeCodeAttributes():
    '''returns None\n\n
    removeCodeAttributes()\n
    '''
def getCodeAttributes():
    '''returns Attribute[]\n\n
    getCodeAttributes()\n
    '''
def getMethod():
    '''returns Method\n\n
    getMethod()\n
    '''
def removeNOPs():
    '''returns None\n\n
    removeNOPs()\n
    '''
def setMaxLocals():
    '''returns None\n\n
    setMaxLocals(final int m)\n
    setMaxLocals()\n
    '''
def getMaxLocals():
    '''returns int\n\n
    getMaxLocals()\n
    '''
def setMaxStack():
    '''returns None\n\n
    setMaxStack(final int m)\n
    setMaxStack()\n
    '''
def getMaxStack():
    '''returns int\n\n
    getMaxStack()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def setClassName():
    '''returns None\n\n
    setClassName(final String class_name)\n
    '''
def setReturnType():
    '''returns None\n\n
    setReturnType(final Type return_type)\n
    '''
def getReturnType():
    '''returns Type\n\n
    getReturnType()\n
    '''
def setArgumentTypes():
    '''returns None\n\n
    setArgumentTypes(final Type[] arg_types)\n
    '''
def getArgumentTypes():
    '''returns Type[]\n\n
    getArgumentTypes()\n
    '''
def setArgumentType():
    '''returns None\n\n
    setArgumentType(final int i, final Type type)\n
    '''
def getArgumentType():
    '''returns Type\n\n
    getArgumentType(final int i)\n
    '''
def setArgumentNames():
    '''returns None\n\n
    setArgumentNames(final String[] arg_names)\n
    '''
def getArgumentNames():
    '''returns String[]\n\n
    getArgumentNames()\n
    '''
def setArgumentName():
    '''returns None\n\n
    setArgumentName(final int i, final String name)\n
    '''
def getArgumentName():
    '''returns String\n\n
    getArgumentName(final int i)\n
    '''
def getInstructionList():
    '''returns InstructionList\n\n
    getInstructionList()\n
    '''
def setInstructionList():
    '''returns None\n\n
    setInstructionList(final InstructionList il)\n
    '''
def getSignature():
    '''returns String\n\n
    getSignature()\n
    '''
def stripAttributes():
    '''returns None\n\n
    stripAttributes(final boolean flag)\n
    '''
def addObserver():
    '''returns None\n\n
    addObserver(final MethodObserver o)\n
    '''
def removeObserver():
    '''returns None\n\n
    removeObserver(final MethodObserver o)\n
    '''
def update():
    '''returns None\n\n
    update()\n
    '''
def copy():
    '''returns MethodGen\n\n
    copy(final String class_name, final ConstantPoolGen cp)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object o1, final Object o2)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode(final Object o)\n
    '''
def push():
    '''returns None\n\n
    push(final InstructionHandle target, final int stackDepth)\n
    '''
def pop():
    '''returns BranchTarget\n\n
    pop()\n
    '''
