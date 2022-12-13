def InstructionFactory():
'''public InstructionFactory(final ClassGen cg, final ConstantPoolGen cp)
public InstructionFactory(final ClassGen cg)
public InstructionFactory(final ConstantPoolGen cp)
'''
pass
def createInvoke():
'''public InvokeInstruction createInvoke(final String class_name, final String name, final Type ret_type, final Type[] arg_types, final short kind)
'''
pass
def createPrintln():
'''public InstructionList createPrintln(final String s)
'''
pass
def createConstant():
'''public Instruction createConstant(final Object value)
'''
pass
def createAppend():
'''public Instruction createAppend(final Type type)
'''
pass
def createFieldAccess():
'''public FieldInstruction createFieldAccess(final String class_name, final String name, final Type type, final short kind)
'''
pass
def createThis():
'''public static Instruction createThis()
'''
pass
def createReturn():
'''public static ReturnInstruction createReturn(final Type type)
'''
pass
def createBinaryOperation():
'''public static ArithmeticInstruction createBinaryOperation(final String op, final Type type)
'''
pass
def createPop():
'''public static StackInstruction createPop(final int size)
'''
pass
def createDup():
'''public static StackInstruction createDup(final int size)
'''
pass
def createDup_2():
'''public static StackInstruction createDup_2(final int size)
'''
pass
def createDup_1():
'''public static StackInstruction createDup_1(final int size)
'''
pass
def createStore():
'''public static LocalVariableInstruction createStore(final Type type, final int index)
'''
pass
def createLoad():
'''public static LocalVariableInstruction createLoad(final Type type, final int index)
'''
pass
def createArrayLoad():
'''public static ArrayInstruction createArrayLoad(final Type type)
'''
pass
def createArrayStore():
'''public static ArrayInstruction createArrayStore(final Type type)
'''
pass
def createCast():
'''public Instruction createCast(final Type src_type, final Type dest_type)
'''
pass
def createGetField():
'''public GETFIELD createGetField(final String class_name, final String name, final Type t)
'''
pass
def createGetStatic():
'''public GETSTATIC createGetStatic(final String class_name, final String name, final Type t)
'''
pass
def createPutField():
'''public PUTFIELD createPutField(final String class_name, final String name, final Type t)
'''
pass
def createPutStatic():
'''public PUTSTATIC createPutStatic(final String class_name, final String name, final Type t)
'''
pass
def createCheckCast():
'''public CHECKCAST createCheckCast(final ReferenceType t)
'''
pass
def createInstanceOf():
'''public INSTANCEOF createInstanceOf(final ReferenceType t)
'''
pass
def createNew():
'''public NEW createNew(final ObjectType t)
public NEW createNew(final String s)
'''
pass
def createNewArray():
'''public Instruction createNewArray(final Type t, final short dim)
'''
pass
def createNull():
'''public static Instruction createNull(final Type type)
'''
pass
def createBranchInstruction():
'''public static BranchInstruction createBranchInstruction(final short opcode, final InstructionHandle target)
'''
pass
def setClassGen():
'''public void setClassGen(final ClassGen c)
'''
pass
def getClassGen():
'''public ClassGen getClassGen()
'''
pass
def setConstantPool():
'''public void setConstantPool(final ConstantPoolGen c)
'''
pass
def getConstantPool():
'''public ConstantPoolGen getConstantPool()
'''
pass
