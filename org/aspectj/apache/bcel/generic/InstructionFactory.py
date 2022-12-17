def ():
    '''returns InstructionFactory\n\n
    (final ClassGen cg, final ConstantPool cp)\n
    (final ClassGen cg)\n
    (final ConstantPool cp)\n
    '''
def createInvoke():
    '''returns InvokeInstruction\n\n
    createInvoke(final String class_name, final String name, final Type ret_type, final Type[] arg_types, final short kind)\n
    createInvoke(final String class_name, final String name, final String signature, final short kind)\n
    '''
def createConstant():
    '''returns Instruction\n\n
    createConstant(final Object value)\n
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
    '''returns FieldInstruction\n\n
    createGetField(final String class_name, final String name, final Type t)\n
    '''
def createGetStatic():
    '''returns FieldInstruction\n\n
    createGetStatic(final String class_name, final String name, final Type t)\n
    '''
def createPutField():
    '''returns FieldInstruction\n\n
    createPutField(final String class_name, final String name, final Type t)\n
    '''
def createPutStatic():
    '''returns FieldInstruction\n\n
    createPutStatic(final String class_name, final String name, final Type t)\n
    '''
def createCheckCast():
    '''returns Instruction\n\n
    createCheckCast(final ReferenceType t)\n
    '''
def createInstanceOf():
    '''returns Instruction\n\n
    createInstanceOf(final ReferenceType t)\n
    '''
def createNew():
    '''returns Instruction\n\n
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
    setConstantPool(final ConstantPool c)\n
    '''
def getConstantPool():
    '''returns ConstantPool\n\n
    getConstantPool()\n
    '''
def PUSHCLASS():
    '''returns InstructionList\n\n
    PUSHCLASS(final ConstantPool cp, final String className)\n
    '''
