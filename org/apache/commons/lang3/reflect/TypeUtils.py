def isAssignable():
'''public static boolean isAssignable(final Type type, final Type toType)
'''
pass
def isInstance():
'''public static boolean isInstance(final Object value, final Type type)
'''
pass
def normalizeUpperBounds():
'''public static Type[] normalizeUpperBounds(final Type[] bounds)
'''
pass
def getImplicitBounds():
'''public static Type[] getImplicitBounds(final TypeVariable<?> typeVariable)
'''
pass
def getImplicitUpperBounds():
'''public static Type[] getImplicitUpperBounds(final WildcardType wildcardType)
'''
pass
def getImplicitLowerBounds():
'''public static Type[] getImplicitLowerBounds(final WildcardType wildcardType)
'''
pass
def typesSatisfyVariables():
'''public static boolean typesSatisfyVariables(final Map<TypeVariable<?>, Type> typeVarAssigns)
'''
pass
def isArrayType():
'''public static boolean isArrayType(final Type type)
'''
pass
def getArrayComponentType():
'''public static Type getArrayComponentType(final Type type)
'''
pass
def unrollVariables():
'''public static Type unrollVariables(Map<TypeVariable<?>, Type> typeArguments, final Type type)
'''
pass
def containsTypeVariables():
'''public static boolean containsTypeVariables(final Type type)
'''
pass
def parameterize():
'''public static final ParameterizedType parameterize(final Class<?> raw, final Type... typeArguments)
public static final ParameterizedType parameterize(final Class<?> raw, final Map<TypeVariable<?>, Type> typeArgMappings)
'''
pass
def parameterizeWithOwner():
'''public static final ParameterizedType parameterizeWithOwner(final Type owner, final Class<?> raw, final Type... typeArguments)
public static final ParameterizedType parameterizeWithOwner(final Type owner, final Class<?> raw, final Map<TypeVariable<?>, Type> typeArgMappings)
'''
pass
def wildcardType():
'''public static WildcardTypeBuilder wildcardType()
'''
pass
def genericArrayType():
'''public static GenericArrayType genericArrayType(final Type componentType)
'''
pass
def equals():
'''public static boolean equals(final Type t1, final Type t2)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
'''
pass
def toString():
'''public static String toString(final Type type)
public String toString()
public String toString()
public String toString()
'''
pass
def toLongString():
'''public static String toLongString(final TypeVariable<?> var)
'''
pass
def wrap():
'''public static <T> Typed<T> wrap(final Type type)
public static <T> Typed<T> wrap(final Class<T> type)
'''
pass
def getType():
'''public Type getType()
'''
pass
def withUpperBounds():
'''public WildcardTypeBuilder withUpperBounds(final Type... bounds)
'''
pass
def withLowerBounds():
'''public WildcardTypeBuilder withLowerBounds(final Type... bounds)
'''
pass
def build():
'''public WildcardType build()
'''
pass
def getGenericComponentType():
'''public Type getGenericComponentType()
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
public int hashCode()
'''
pass
def getRawType():
'''public Type getRawType()
'''
pass
def getOwnerType():
'''public Type getOwnerType()
'''
pass
def getActualTypeArguments():
'''public Type[] getActualTypeArguments()
'''
pass
def getUpperBounds():
'''public Type[] getUpperBounds()
'''
pass
def getLowerBounds():
'''public Type[] getLowerBounds()
'''
pass
