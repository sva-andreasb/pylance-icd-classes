def ReferenceFinder():
    '''public ReferenceFinder(final Filter obj, final Visitor obj2)
    '''
def visitClass():
    '''public Boolean visitClass(final ConstantPool.CONSTANT_Class_info constant_Class_info, final ConstantPool constantPool)
    '''
def visitInterfaceMethodref():
    '''public Boolean visitInterfaceMethodref(final ConstantPool.CONSTANT_InterfaceMethodref_info constant_InterfaceMethodref_info, final ConstantPool constantPool)
    '''
def visitMethodref():
    '''public Boolean visitMethodref(final ConstantPool.CONSTANT_Methodref_info constant_Methodref_info, final ConstantPool constantPool)
    '''
def visitFieldref():
    '''public Boolean visitFieldref(final ConstantPool.CONSTANT_Fieldref_info constant_Fieldref_info, final ConstantPool constantPool)
    '''
def visitDouble():
    '''public Boolean visitDouble(final ConstantPool.CONSTANT_Double_info constant_Double_info, final ConstantPool constantPool)
    '''
def visitFloat():
    '''public Boolean visitFloat(final ConstantPool.CONSTANT_Float_info constant_Float_info, final ConstantPool constantPool)
    '''
def visitInteger():
    '''public Boolean visitInteger(final ConstantPool.CONSTANT_Integer_info constant_Integer_info, final ConstantPool constantPool)
    '''
def visitInvokeDynamic():
    '''public Boolean visitInvokeDynamic(final ConstantPool.CONSTANT_InvokeDynamic_info constant_InvokeDynamic_info, final ConstantPool constantPool)
    '''
def visitLong():
    '''public Boolean visitLong(final ConstantPool.CONSTANT_Long_info constant_Long_info, final ConstantPool constantPool)
    '''
def visitNameAndType():
    '''public Boolean visitNameAndType(final ConstantPool.CONSTANT_NameAndType_info constant_NameAndType_info, final ConstantPool constantPool)
    '''
def visitMethodHandle():
    '''public Boolean visitMethodHandle(final ConstantPool.CONSTANT_MethodHandle_info constant_MethodHandle_info, final ConstantPool constantPool)
    '''
def visitMethodType():
    '''public Boolean visitMethodType(final ConstantPool.CONSTANT_MethodType_info constant_MethodType_info, final ConstantPool constantPool)
    '''
def visitString():
    '''public Boolean visitString(final ConstantPool.CONSTANT_String_info constant_String_info, final ConstantPool constantPool)
    '''
def visitUtf8():
    '''public Boolean visitUtf8(final ConstantPool.CONSTANT_Utf8_info constant_Utf8_info, final ConstantPool constantPool)
    '''
def visitNoOperands():
    '''public Integer visitNoOperands(final Instruction instruction, final List<Integer> list)
    '''
def visitArrayType():
    '''public Integer visitArrayType(final Instruction instruction, final Instruction.TypeKind typeKind, final List<Integer> list)
    '''
def visitBranch():
    '''public Integer visitBranch(final Instruction instruction, final int n, final List<Integer> list)
    '''
def visitConstantPoolRef():
    '''public Integer visitConstantPoolRef(final Instruction instruction, final int i, final List<Integer> list)
    '''
def visitConstantPoolRefAndValue():
    '''public Integer visitConstantPoolRefAndValue(final Instruction instruction, final int i, final int n, final List<Integer> list)
    '''
def visitLocal():
    '''public Integer visitLocal(final Instruction instruction, final int n, final List<Integer> list)
    '''
def visitLocalAndValue():
    '''public Integer visitLocalAndValue(final Instruction instruction, final int n, final int n2, final List<Integer> list)
    '''
def visitLookupSwitch():
    '''public Integer visitLookupSwitch(final Instruction instruction, final int n, final int n2, final int[] array, final int[] array2, final List<Integer> list)
    '''
def visitTableSwitch():
    '''public Integer visitTableSwitch(final Instruction instruction, final int n, final int n2, final int n3, final int[] array, final List<Integer> list)
    '''
def visitValue():
    '''public Integer visitValue(final Instruction instruction, final int n, final List<Integer> list)
    '''
def visitUnknown():
    '''public Integer visitUnknown(final Instruction instruction, final List<Integer> list)
    '''
def parse():
    '''public boolean parse(final ClassFile classFile)
    '''
