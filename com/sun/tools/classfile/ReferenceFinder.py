def ():
    '''returns ReferenceFinder\n\n
    (final Filter obj, final Visitor obj2)\n
    '''
def visitClass():
    '''returns Boolean\n\n
    visitClass(final ConstantPool.CONSTANT_Class_info constant_Class_info, final ConstantPool constantPool)\n
    '''
def visitInterfaceMethodref():
    '''returns Boolean\n\n
    visitInterfaceMethodref(final ConstantPool.CONSTANT_InterfaceMethodref_info constant_InterfaceMethodref_info, final ConstantPool constantPool)\n
    '''
def visitMethodref():
    '''returns Boolean\n\n
    visitMethodref(final ConstantPool.CONSTANT_Methodref_info constant_Methodref_info, final ConstantPool constantPool)\n
    '''
def visitFieldref():
    '''returns Boolean\n\n
    visitFieldref(final ConstantPool.CONSTANT_Fieldref_info constant_Fieldref_info, final ConstantPool constantPool)\n
    '''
def visitDouble():
    '''returns Boolean\n\n
    visitDouble(final ConstantPool.CONSTANT_Double_info constant_Double_info, final ConstantPool constantPool)\n
    '''
def visitFloat():
    '''returns Boolean\n\n
    visitFloat(final ConstantPool.CONSTANT_Float_info constant_Float_info, final ConstantPool constantPool)\n
    '''
def visitInteger():
    '''returns Boolean\n\n
    visitInteger(final ConstantPool.CONSTANT_Integer_info constant_Integer_info, final ConstantPool constantPool)\n
    '''
def visitInvokeDynamic():
    '''returns Boolean\n\n
    visitInvokeDynamic(final ConstantPool.CONSTANT_InvokeDynamic_info constant_InvokeDynamic_info, final ConstantPool constantPool)\n
    '''
def visitLong():
    '''returns Boolean\n\n
    visitLong(final ConstantPool.CONSTANT_Long_info constant_Long_info, final ConstantPool constantPool)\n
    '''
def visitNameAndType():
    '''returns Boolean\n\n
    visitNameAndType(final ConstantPool.CONSTANT_NameAndType_info constant_NameAndType_info, final ConstantPool constantPool)\n
    '''
def visitMethodHandle():
    '''returns Boolean\n\n
    visitMethodHandle(final ConstantPool.CONSTANT_MethodHandle_info constant_MethodHandle_info, final ConstantPool constantPool)\n
    '''
def visitMethodType():
    '''returns Boolean\n\n
    visitMethodType(final ConstantPool.CONSTANT_MethodType_info constant_MethodType_info, final ConstantPool constantPool)\n
    '''
def visitString():
    '''returns Boolean\n\n
    visitString(final ConstantPool.CONSTANT_String_info constant_String_info, final ConstantPool constantPool)\n
    '''
def visitUtf8():
    '''returns Boolean\n\n
    visitUtf8(final ConstantPool.CONSTANT_Utf8_info constant_Utf8_info, final ConstantPool constantPool)\n
    '''
def visitNoOperands():
    '''returns Integer\n\n
    visitNoOperands(final Instruction instruction, final List<Integer> list)\n
    '''
def visitArrayType():
    '''returns Integer\n\n
    visitArrayType(final Instruction instruction, final Instruction.TypeKind typeKind, final List<Integer> list)\n
    '''
def visitBranch():
    '''returns Integer\n\n
    visitBranch(final Instruction instruction, final int n, final List<Integer> list)\n
    '''
def visitConstantPoolRef():
    '''returns Integer\n\n
    visitConstantPoolRef(final Instruction instruction, final int i, final List<Integer> list)\n
    '''
def visitConstantPoolRefAndValue():
    '''returns Integer\n\n
    visitConstantPoolRefAndValue(final Instruction instruction, final int i, final int n, final List<Integer> list)\n
    '''
def visitLocal():
    '''returns Integer\n\n
    visitLocal(final Instruction instruction, final int n, final List<Integer> list)\n
    '''
def visitLocalAndValue():
    '''returns Integer\n\n
    visitLocalAndValue(final Instruction instruction, final int n, final int n2, final List<Integer> list)\n
    '''
def visitLookupSwitch():
    '''returns Integer\n\n
    visitLookupSwitch(final Instruction instruction, final int n, final int n2, final int[] array, final int[] array2, final List<Integer> list)\n
    '''
def visitTableSwitch():
    '''returns Integer\n\n
    visitTableSwitch(final Instruction instruction, final int n, final int n2, final int n3, final int[] array, final List<Integer> list)\n
    '''
def visitValue():
    '''returns Integer\n\n
    visitValue(final Instruction instruction, final int n, final List<Integer> list)\n
    '''
def visitUnknown():
    '''returns Integer\n\n
    visitUnknown(final Instruction instruction, final List<Integer> list)\n
    '''
def parse():
    '''returns boolean\n\n
    parse(final ClassFile classFile)\n
    '''
