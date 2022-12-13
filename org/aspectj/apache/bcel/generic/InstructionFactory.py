def InstructionFactory():
'''public InstructionFactory(final ClassGen cg, final ConstantPool cp)
public InstructionFactory(final ClassGen cg)
public InstructionFactory(final ConstantPool cp)
'''
pass
def createInvoke():
'''public InvokeInstruction createInvoke(final String class_name, final String name, final Type ret_type, final Type[] arg_types, final short kind)
public InvokeInstruction createInvoke(final String class_name, final String name, final String signature, final short kind)
'''
pass
def createALOAD():
'''public static Instruction createALOAD(final int n)
'''
pass
def createASTORE():
'''public static Instruction createASTORE(final int n)
'''
pass
def createConstant():
'''public Instruction createConstant(final Object value)
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
'''public static Instruction createReturn(final Type type)
'''
pass
def createPop():
'''public static Instruction createPop(final int size)
'''
pass
def createDup():
'''public static Instruction createDup(final int size)
'''
pass
def createDup_2():
'''public static Instruction createDup_2(final int size)
'''
pass
def createDup_1():
'''public static Instruction createDup_1(final int size)
'''
pass
def createStore():
'''public static InstructionLV createStore(final Type type, final int index)
'''
pass
def createLoad():
'''public static InstructionLV createLoad(final Type type, final int index)
'''
pass
def createArrayLoad():
'''public static Instruction createArrayLoad(final Type type)
'''
pass
def createArrayStore():
'''public static Instruction createArrayStore(final Type type)
'''
pass
def createCast():
'''public Instruction createCast(final Type src_type, final Type dest_type)
'''
pass
def createGetField():
'''public FieldInstruction createGetField(final String class_name, final String name, final Type t)
'''
pass
def createGetStatic():
'''public FieldInstruction createGetStatic(final String class_name, final String name, final Type t)
'''
pass
def createPutField():
'''public FieldInstruction createPutField(final String class_name, final String name, final Type t)
'''
pass
def createPutStatic():
'''public FieldInstruction createPutStatic(final String class_name, final String name, final Type t)
'''
pass
def createCheckCast():
'''public Instruction createCheckCast(final ReferenceType t)
'''
pass
def createInstanceOf():
'''public Instruction createInstanceOf(final ReferenceType t)
'''
pass
def createNew():
'''public Instruction createNew(final ObjectType t)
public Instruction createNew(final String s)
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
'''public static InstructionBranch createBranchInstruction(final short opcode, final InstructionHandle target)
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
'''public void setConstantPool(final ConstantPool c)
'''
pass
def getConstantPool():
'''public ConstantPool getConstantPool()
'''
pass
def PUSH():
'''public static Instruction PUSH(final ConstantPool cp, final int value)
public static Instruction PUSH(final ConstantPool cp, final ObjectType t)
public static Instruction PUSH(final ConstantPool cp, final boolean value)
public static Instruction PUSH(final ConstantPool cp, final float value)
public static Instruction PUSH(final ConstantPool cp, final long value)
public static Instruction PUSH(final ConstantPool cp, final double value)
public static Instruction PUSH(final ConstantPool cp, final String value)
public static Instruction PUSH(final ConstantPool cp, final Number value)
public static Instruction PUSH(final ConstantPool cp, final Character value)
public static Instruction PUSH(final ConstantPool cp, final Boolean value)
'''
pass
def PUSHCLASS():
'''public InstructionList PUSHCLASS(final ConstantPool cp, final String className)
'''
pass