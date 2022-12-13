def MethodGen():
    '''public MethodGen(final int access_flags, final Type return_type, final Type[] arg_types, final String[] arg_names, final String method_name, final String class_name, final InstructionList il, final ConstantPool cp)
    public MethodGen(final Method m, final String class_name, final ConstantPool cp)
    public MethodGen(final Method m, final String class_name, final ConstantPool cp, final boolean useTags)
    '''
def getHighestlinenumber():
    '''public int getHighestlinenumber()
    '''
def addLocalVariable():
    '''public LocalVariableGen addLocalVariable(final String name, final Type type, final int slot, final InstructionHandle start, final InstructionHandle end)
    public LocalVariableGen addLocalVariable(final String name, final Type type, final InstructionHandle start, final InstructionHandle end)
    '''
def removeLocalVariable():
    '''public void removeLocalVariable(final LocalVariableGen l)
    '''
def removeLocalVariables():
    '''public void removeLocalVariables()
    '''
def getLocalVariables():
    '''public LocalVariableGen[] getLocalVariables()
    '''
def getLocalVariableTable():
    '''public LocalVariableTable getLocalVariableTable(final ConstantPool cp)
    '''
def addLineNumber():
    '''public LineNumberGen addLineNumber(final InstructionHandle ih, final int src_line)
    '''
def removeLineNumber():
    '''public void removeLineNumber(final LineNumberGen l)
    '''
def removeLineNumbers():
    '''public void removeLineNumbers()
    '''
def getLineNumbers():
    '''public LineNumberGen[] getLineNumbers()
    '''
def getLineNumberTable():
    '''public LineNumberTable getLineNumberTable(final ConstantPool cp)
    '''
def addExceptionHandler():
    '''public CodeExceptionGen addExceptionHandler(final InstructionHandle start_pc, final InstructionHandle end_pc, final InstructionHandle handler_pc, final ObjectType catch_type)
    '''
def removeExceptionHandler():
    '''public void removeExceptionHandler(final CodeExceptionGen c)
    '''
def removeExceptionHandlers():
    '''public void removeExceptionHandlers()
    '''
def getExceptionHandlers():
    '''public CodeExceptionGen[] getExceptionHandlers()
    '''
def addException():
    '''public void addException(final String class_name)
    '''
def removeException():
    '''public void removeException(final String c)
    '''
def removeExceptions():
    '''public void removeExceptions()
    '''
def getExceptions():
    '''public String[] getExceptions()
    '''
def addCodeAttribute():
    '''public void addCodeAttribute(final Attribute a)
    '''
def addParameterAnnotationsAsAttribute():
    '''public void addParameterAnnotationsAsAttribute(final ConstantPool cp)
    '''
def removeCodeAttribute():
    '''public void removeCodeAttribute(final Attribute a)
    '''
def removeCodeAttributes():
    '''public void removeCodeAttributes()
    '''
def getCodeAttributes():
    '''public Attribute[] getCodeAttributes()
    '''
def getMethod():
    '''public Method getMethod()
    '''
def setMaxLocals():
    '''public void setMaxLocals(final int m)
    public void setMaxLocals()
    '''
def getMaxLocals():
    '''public int getMaxLocals()
    '''
def setMaxStack():
    '''public void setMaxStack(final int m)
    public void setMaxStack()
    '''
def getMaxStack():
    '''public int getMaxStack()
    public static int getMaxStack(final ConstantPool cp, final InstructionList il, final CodeExceptionGen[] et)
    '''
def getClassName():
    '''public String getClassName()
    '''
def setClassName():
    '''public void setClassName(final String class_name)
    '''
def setReturnType():
    '''public void setReturnType(final Type return_type)
    '''
def getReturnType():
    '''public Type getReturnType()
    '''
def setArgumentTypes():
    '''public void setArgumentTypes(final Type[] arg_types)
    '''
def getArgumentTypes():
    '''public Type[] getArgumentTypes()
    '''
def setArgumentType():
    '''public void setArgumentType(final int i, final Type type)
    '''
def getArgumentType():
    '''public Type getArgumentType(final int i)
    '''
def setArgumentNames():
    '''public void setArgumentNames(final String[] arg_names)
    '''
def getArgumentNames():
    '''public String[] getArgumentNames()
    '''
def setArgumentName():
    '''public void setArgumentName(final int i, final String name)
    '''
def getArgumentName():
    '''public String getArgumentName(final int i)
    '''
def getInstructionList():
    '''public InstructionList getInstructionList()
    '''
def setInstructionList():
    '''public void setInstructionList(final InstructionList il)
    '''
def getSignature():
    '''public String getSignature()
    '''
def stripAttributes():
    '''public void stripAttributes(final boolean flag)
    '''
def toString():
    '''public final String toString()
    '''
def getAnnotationsOnParameter():
    '''public List getAnnotationsOnParameter(final int i)
    '''
def addParameterAnnotation():
    '''public void addParameterAnnotation(final int parameterIndex, final AnnotationGen annotation)
    '''
def push():
    '''public void push(final InstructionHandle target, final int stackDepth)
    '''
def pop():
    '''public BranchTarget pop()
    '''
