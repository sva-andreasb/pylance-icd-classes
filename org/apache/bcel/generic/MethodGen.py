def MethodGen():
'''public MethodGen(final int access_flags, final Type return_type, final Type[] arg_types, String[] arg_names, final String method_name, final String class_name, final InstructionList il, final ConstantPoolGen cp)
public MethodGen(final Method m, final String class_name, final ConstantPoolGen cp)
'''
pass
def addLocalVariable():
'''public LocalVariableGen addLocalVariable(final String name, final Type type, final int slot, final InstructionHandle start, final InstructionHandle end)
public LocalVariableGen addLocalVariable(final String name, final Type type, final InstructionHandle start, final InstructionHandle end)
'''
pass
def removeLocalVariable():
'''public void removeLocalVariable(final LocalVariableGen l)
'''
pass
def removeLocalVariables():
'''public void removeLocalVariables()
'''
pass
def getLocalVariables():
'''public LocalVariableGen[] getLocalVariables()
'''
pass
def getLocalVariableTable():
'''public LocalVariableTable getLocalVariableTable(final ConstantPoolGen cp)
'''
pass
def addLineNumber():
'''public LineNumberGen addLineNumber(final InstructionHandle ih, final int src_line)
'''
pass
def removeLineNumber():
'''public void removeLineNumber(final LineNumberGen l)
'''
pass
def removeLineNumbers():
'''public void removeLineNumbers()
'''
pass
def getLineNumbers():
'''public LineNumberGen[] getLineNumbers()
'''
pass
def getLineNumberTable():
'''public LineNumberTable getLineNumberTable(final ConstantPoolGen cp)
'''
pass
def addExceptionHandler():
'''public CodeExceptionGen addExceptionHandler(final InstructionHandle start_pc, final InstructionHandle end_pc, final InstructionHandle handler_pc, final ObjectType catch_type)
'''
pass
def removeExceptionHandler():
'''public void removeExceptionHandler(final CodeExceptionGen c)
'''
pass
def removeExceptionHandlers():
'''public void removeExceptionHandlers()
'''
pass
def getExceptionHandlers():
'''public CodeExceptionGen[] getExceptionHandlers()
'''
pass
def addException():
'''public void addException(final String class_name)
'''
pass
def removeException():
'''public void removeException(final String c)
'''
pass
def removeExceptions():
'''public void removeExceptions()
'''
pass
def getExceptions():
'''public String[] getExceptions()
'''
pass
def addCodeAttribute():
'''public void addCodeAttribute(final Attribute a)
'''
pass
def removeCodeAttribute():
'''public void removeCodeAttribute(final Attribute a)
'''
pass
def removeCodeAttributes():
'''public void removeCodeAttributes()
'''
pass
def getCodeAttributes():
'''public Attribute[] getCodeAttributes()
'''
pass
def getMethod():
'''public Method getMethod()
'''
pass
def removeNOPs():
'''public void removeNOPs()
'''
pass
def setMaxLocals():
'''public void setMaxLocals(final int m)
public void setMaxLocals()
'''
pass
def getMaxLocals():
'''public int getMaxLocals()
'''
pass
def setMaxStack():
'''public void setMaxStack(final int m)
public void setMaxStack()
'''
pass
def getMaxStack():
'''public int getMaxStack()
public static int getMaxStack(final ConstantPoolGen cp, final InstructionList il, final CodeExceptionGen[] et)
'''
pass
def getClassName():
'''public String getClassName()
'''
pass
def setClassName():
'''public void setClassName(final String class_name)
'''
pass
def setReturnType():
'''public void setReturnType(final Type return_type)
'''
pass
def getReturnType():
'''public Type getReturnType()
'''
pass
def setArgumentTypes():
'''public void setArgumentTypes(final Type[] arg_types)
'''
pass
def getArgumentTypes():
'''public Type[] getArgumentTypes()
'''
pass
def setArgumentType():
'''public void setArgumentType(final int i, final Type type)
'''
pass
def getArgumentType():
'''public Type getArgumentType(final int i)
'''
pass
def setArgumentNames():
'''public void setArgumentNames(final String[] arg_names)
'''
pass
def getArgumentNames():
'''public String[] getArgumentNames()
'''
pass
def setArgumentName():
'''public void setArgumentName(final int i, final String name)
'''
pass
def getArgumentName():
'''public String getArgumentName(final int i)
'''
pass
def getInstructionList():
'''public InstructionList getInstructionList()
'''
pass
def setInstructionList():
'''public void setInstructionList(final InstructionList il)
'''
pass
def getSignature():
'''public String getSignature()
'''
pass
def stripAttributes():
'''public void stripAttributes(final boolean flag)
'''
pass
def addObserver():
'''public void addObserver(final MethodObserver o)
'''
pass
def removeObserver():
'''public void removeObserver(final MethodObserver o)
'''
pass
def update():
'''public void update()
'''
pass
def toString():
'''public final String toString()
'''
pass
def copy():
'''public MethodGen copy(final String class_name, final ConstantPoolGen cp)
'''
pass
def getComparator():
'''public static BCELComparator getComparator()
'''
pass
def setComparator():
'''public static void setComparator(final BCELComparator comparator)
'''
pass
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final Object o1, final Object o2)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode(final Object o)
'''
pass
def push():
'''public void push(final InstructionHandle target, final int stackDepth)
'''
pass
def pop():
'''public BranchTarget pop()
'''
pass
