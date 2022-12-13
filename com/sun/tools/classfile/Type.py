def isObject():
    '''    public boolean isObject()
    public boolean isObject()
    '''
def SimpleType():
    '''    public SimpleType(final String name)
    '''
def accept():
    '''    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    '''
def isPrimitiveType():
    '''    public boolean isPrimitiveType()
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    '''
def ArrayType():
    '''    public ArrayType(final Type elemType)
    '''
def MethodType():
    '''    public MethodType(final List<? extends Type> list, final Type type)
    public MethodType(final List<? extends TypeParamType> typeParamTypes, final List<? extends Type> paramTypes, final Type returnType, final List<? extends Type> throwsTypes)
    '''
def ClassSigType():
    '''    public ClassSigType(final List<TypeParamType> typeParamTypes, final Type superclassType, final List<Type> superinterfaceTypes)
    '''
def ClassType():
    '''    public ClassType(final ClassType outerType, final String name, final List<Type> typeArgs)
    '''
def getBinaryName():
    '''    public String getBinaryName()
    '''
def TypeParamType():
    '''    public TypeParamType(final String name, final Type classBound, final List<Type> interfaceBounds)
    '''
def WildcardType():
    '''    public WildcardType()
    public WildcardType(final Kind kind, final Type boundType)
    '''
