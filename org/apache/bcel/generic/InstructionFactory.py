def ():
    '''returns InstructionFactory\n\n
    (final ClassGen cg, final ConstantPoolGen cp)\n
    (final ClassGen cg)\n
    (final ConstantPoolGen cp)\n
    '''
def createInvoke():
    '''returns InvokeInstruction\n\n
    createInvoke(final String class_name, final String name, final Type ret_type, final Type[] arg_types, final short kind)\n
    '''
def createPrintln():
    '''returns InstructionList\n\n
    createPrintln(final String s)\n
    '''
def createConstant():
    '''returns Instruction\n\n
    createConstant(final Object value)\n
    '''
def createAppend():
    '''returns Instruction\n\n
    createAppend(final Type type)\n
    '''
def createFieldAccess():
    '''returns FieldInstruction\n\n
    createFieldAccess(final String class_name, final String name, final Type type, final short kind)\n
    '''
def createCast():
    '''returns Instruction\n\n
    createCast(final Type src_type, final Type dest_type)\n
    '''
def createGetField():
    '''returns GETFIELD\n\n
    createGetField(final String class_name, final String name, final Type t)\n
    '''
def createGetStatic():
    '''returns GETSTATIC\n\n
    createGetStatic(final String class_name, final String name, final Type t)\n
    '''
def createPutField():
    '''returns PUTFIELD\n\n
    createPutField(final String class_name, final String name, final Type t)\n
    '''
def createPutStatic():
    '''returns PUTSTATIC\n\n
    createPutStatic(final String class_name, final String name, final Type t)\n
    '''
def createCheckCast():
    '''returns CHECKCAST\n\n
    createCheckCast(final ReferenceType t)\n
    '''
def createInstanceOf():
    '''returns INSTANCEOF\n\n
    createInstanceOf(final ReferenceType t)\n
    '''
def createNew():
    '''returns NEW\n\n
    createNew(final ObjectType t)\n
    createNew(final String s)\n
    '''
def createNewArray():
    '''returns Instruction\n\n
    createNewArray(final Type t, final short dim)\n
    '''
def setClassGen():
    '''returns None\n\n
    setClassGen(final ClassGen c)\n
    '''
def getClassGen():
    '''returns ClassGen\n\n
    getClassGen()\n
    '''
def setConstantPool():
    '''returns None\n\n
    setConstantPool(final ConstantPoolGen c)\n
    '''
def getConstantPool():
    '''returns ConstantPoolGen\n\n
    getConstantPool()\n
    '''
