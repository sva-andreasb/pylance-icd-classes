def isAssignable():
    '''    public static boolean isAssignable(final Type type, final Type toType)
    '''
def isInstance():
    '''    public static boolean isInstance(final Object value, final Type type)
    '''
def normalizeUpperBounds():
    '''    public static Type[] normalizeUpperBounds(final Type[] bounds)
    '''
def getImplicitBounds():
    '''    public static Type[] getImplicitBounds(final TypeVariable<?> typeVariable)
    '''
def getImplicitUpperBounds():
    '''    public static Type[] getImplicitUpperBounds(final WildcardType wildcardType)
    '''
def getImplicitLowerBounds():
    '''    public static Type[] getImplicitLowerBounds(final WildcardType wildcardType)
    '''
def typesSatisfyVariables():
    '''    public static boolean typesSatisfyVariables(final Map<TypeVariable<?>, Type> typeVarAssigns)
    '''
def isArrayType():
    '''    public static boolean isArrayType(final Type type)
    '''
def getArrayComponentType():
    '''    public static Type getArrayComponentType(final Type type)
    '''
def unrollVariables():
    '''    public static Type unrollVariables(Map<TypeVariable<?>, Type> typeArguments, final Type type)
    '''
def containsTypeVariables():
    '''    public static boolean containsTypeVariables(final Type type)
    '''
def parameterize():
    '''    public static final ParameterizedType parameterize(final Class<?> raw, final Type... typeArguments)
    public static final ParameterizedType parameterize(final Class<?> raw, final Map<TypeVariable<?>, Type> typeArgMappings)
    '''
def parameterizeWithOwner():
    '''    public static final ParameterizedType parameterizeWithOwner(final Type owner, final Class<?> raw, final Type... typeArguments)
    public static final ParameterizedType parameterizeWithOwner(final Type owner, final Class<?> raw, final Map<TypeVariable<?>, Type> typeArgMappings)
    '''
def wildcardType():
    '''    public static WildcardTypeBuilder wildcardType()
    '''
def genericArrayType():
    '''    public static GenericArrayType genericArrayType(final Type componentType)
    '''
def equals():
    '''    public static boolean equals(final Type t1, final Type t2)
    public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    '''
def toString():
    '''    public static String toString(final Type type)
    public String toString()
    public String toString()
    public String toString()
    '''
def toLongString():
    '''    public static String toLongString(final TypeVariable<?> var)
    '''
def wrap():
    '''    public static <T> Typed<T> wrap(final Type type)
    public static <T> Typed<T> wrap(final Class<T> type)
    '''
def getType():
    '''    public Type getType()
    '''
def withUpperBounds():
    '''    public WildcardTypeBuilder withUpperBounds(final Type... bounds)
    '''
def withLowerBounds():
    '''    public WildcardTypeBuilder withLowerBounds(final Type... bounds)
    '''
def build():
    '''    public WildcardType build()
    '''
def getGenericComponentType():
    '''    public Type getGenericComponentType()
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    public int hashCode()
    '''
def getRawType():
    '''    public Type getRawType()
    '''
def getOwnerType():
    '''    public Type getOwnerType()
    '''
def getActualTypeArguments():
    '''    public Type[] getActualTypeArguments()
    '''
def getUpperBounds():
    '''    public Type[] getUpperBounds()
    '''
def getLowerBounds():
    '''    public Type[] getLowerBounds()
    '''
