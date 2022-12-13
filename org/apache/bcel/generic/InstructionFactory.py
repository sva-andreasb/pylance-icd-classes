def InstructionFactory():
    '''    public InstructionFactory(final ClassGen cg, final ConstantPoolGen cp)
    public InstructionFactory(final ClassGen cg)
    public InstructionFactory(final ConstantPoolGen cp)
    '''
def createInvoke():
    '''    public InvokeInstruction createInvoke(final String class_name, final String name, final Type ret_type, final Type[] arg_types, final short kind)
    '''
def createPrintln():
    '''    public InstructionList createPrintln(final String s)
    '''
def createConstant():
    '''    public Instruction createConstant(final Object value)
    '''
def createAppend():
    '''    public Instruction createAppend(final Type type)
    '''
def createFieldAccess():
    '''    public FieldInstruction createFieldAccess(final String class_name, final String name, final Type type, final short kind)
    '''
def createThis():
    '''    public static Instruction createThis()
    '''
def createReturn():
    '''    public static ReturnInstruction createReturn(final Type type)
    '''
def createBinaryOperation():
    '''    public static ArithmeticInstruction createBinaryOperation(final String op, final Type type)
    '''
def createPop():
    '''    public static StackInstruction createPop(final int size)
    '''
def createDup():
    '''    public static StackInstruction createDup(final int size)
    '''
def createDup_2():
    '''    public static StackInstruction createDup_2(final int size)
    '''
def createDup_1():
    '''    public static StackInstruction createDup_1(final int size)
    '''
def createStore():
    '''    public static LocalVariableInstruction createStore(final Type type, final int index)
    '''
def createLoad():
    '''    public static LocalVariableInstruction createLoad(final Type type, final int index)
    '''
def createArrayLoad():
    '''    public static ArrayInstruction createArrayLoad(final Type type)
    '''
def createArrayStore():
    '''    public static ArrayInstruction createArrayStore(final Type type)
    '''
def createCast():
    '''    public Instruction createCast(final Type src_type, final Type dest_type)
    '''
def createGetField():
    '''    public GETFIELD createGetField(final String class_name, final String name, final Type t)
    '''
def createGetStatic():
    '''    public GETSTATIC createGetStatic(final String class_name, final String name, final Type t)
    '''
def createPutField():
    '''    public PUTFIELD createPutField(final String class_name, final String name, final Type t)
    '''
def createPutStatic():
    '''    public PUTSTATIC createPutStatic(final String class_name, final String name, final Type t)
    '''
def createCheckCast():
    '''    public CHECKCAST createCheckCast(final ReferenceType t)
    '''
def createInstanceOf():
    '''    public INSTANCEOF createInstanceOf(final ReferenceType t)
    '''
def createNew():
    '''    public NEW createNew(final ObjectType t)
    public NEW createNew(final String s)
    '''
def createNewArray():
    '''    public Instruction createNewArray(final Type t, final short dim)
    '''
def createNull():
    '''    public static Instruction createNull(final Type type)
    '''
def createBranchInstruction():
    '''    public static BranchInstruction createBranchInstruction(final short opcode, final InstructionHandle target)
    '''
def setClassGen():
    '''    public void setClassGen(final ClassGen c)
    '''
def getClassGen():
    '''    public ClassGen getClassGen()
    '''
def setConstantPool():
    '''    public void setConstantPool(final ConstantPoolGen c)
    '''
def getConstantPool():
    '''    public ConstantPoolGen getConstantPool()
    '''
