def ():
    '''returns StackMapEntry\n\n
    (final int byte_code_offset, final int number_of_locals, final StackMapType[] types_of_locals, final int number_of_stack_items, final StackMapType[] types_of_stack_items, final ConstantPool constant_pool)\n
    '''
def setByteCodeOffset():
    '''returns None\n\n
    setByteCodeOffset(final int b)\n
    '''
def getByteCodeOffset():
    '''returns int\n\n
    getByteCodeOffset()\n
    '''
def setNumberOfLocals():
    '''returns None\n\n
    setNumberOfLocals(final int n)\n
    '''
def getNumberOfLocals():
    '''returns int\n\n
    getNumberOfLocals()\n
    '''
def setTypesOfLocals():
    '''returns None\n\n
    setTypesOfLocals(final StackMapType[] t)\n
    '''
def getTypesOfLocals():
    '''returns StackMapType[]\n\n
    getTypesOfLocals()\n
    '''
def setNumberOfStackItems():
    '''returns None\n\n
    setNumberOfStackItems(final int n)\n
    '''
def getNumberOfStackItems():
    '''returns int\n\n
    getNumberOfStackItems()\n
    '''
def setTypesOfStackItems():
    '''returns None\n\n
    setTypesOfStackItems(final StackMapType[] t)\n
    '''
def getTypesOfStackItems():
    '''returns StackMapType[]\n\n
    getTypesOfStackItems()\n
    '''
def copy():
    '''returns StackMapEntry\n\n
    copy()\n
    '''
def accept():
    '''returns None\n\n
    accept(final ClassVisitor v)\n
    '''
