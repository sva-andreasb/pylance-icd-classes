def nopInstance():
    '''    public static AnnotationIntrospector nopInstance()
    '''
def pair():
    '''    public static AnnotationIntrospector pair(final AnnotationIntrospector a1, final AnnotationIntrospector a2)
    '''
def allIntrospectors():
    '''    public Collection<AnnotationIntrospector> allIntrospectors()
    public Collection<AnnotationIntrospector> allIntrospectors(final Collection<AnnotationIntrospector> result)
    '''
def isAnnotationBundle():
    '''    public boolean isAnnotationBundle(final Annotation ann)
    '''
def findObjectIdInfo():
    '''    public ObjectIdInfo findObjectIdInfo(final Annotated ann)
    '''
def findObjectReferenceInfo():
    '''    public ObjectIdInfo findObjectReferenceInfo(final Annotated ann, final ObjectIdInfo objectIdInfo)
    '''
def findRootName():
    '''    public PropertyName findRootName(final AnnotatedClass ac)
    '''
def isIgnorableType():
    '''    public Boolean isIgnorableType(final AnnotatedClass ac)
    '''
def findFilterId():
    '''    public Object findFilterId(final Annotated ann)
    '''
def findNamingStrategy():
    '''    public Object findNamingStrategy(final AnnotatedClass ac)
    '''
def findClassDescription():
    '''    public String findClassDescription(final AnnotatedClass ac)
    '''
def findPropertiesToIgnore():
    '''    public String[] findPropertiesToIgnore(final Annotated ac, final boolean forSerialization)
    public String[] findPropertiesToIgnore(final Annotated ac)
    '''
def findIgnoreUnknownProperties():
    '''    public Boolean findIgnoreUnknownProperties(final AnnotatedClass ac)
    '''
def findSubtypes():
    '''    public List<NamedType> findSubtypes(final Annotated a)
    '''
def findTypeName():
    '''    public String findTypeName(final AnnotatedClass ac)
    '''
def isTypeId():
    '''    public Boolean isTypeId(final AnnotatedMember member)
    '''
def findReferenceType():
    '''    public ReferenceProperty findReferenceType(final AnnotatedMember member)
    '''
def findUnwrappingNameTransformer():
    '''    public NameTransformer findUnwrappingNameTransformer(final AnnotatedMember member)
    '''
def hasIgnoreMarker():
    '''    public boolean hasIgnoreMarker(final AnnotatedMember m)
    '''
def hasRequiredMarker():
    '''    public Boolean hasRequiredMarker(final AnnotatedMember m)
    '''
def findWrapperName():
    '''    public PropertyName findWrapperName(final Annotated ann)
    '''
def findPropertyDefaultValue():
    '''    public String findPropertyDefaultValue(final Annotated ann)
    '''
def findPropertyDescription():
    '''    public String findPropertyDescription(final Annotated ann)
    '''
def findPropertyIndex():
    '''    public Integer findPropertyIndex(final Annotated ann)
    '''
def findImplicitPropertyName():
    '''    public String findImplicitPropertyName(final AnnotatedMember member)
    '''
def findPropertyAliases():
    '''    public List<PropertyName> findPropertyAliases(final Annotated ann)
    '''
def resolveSetterConflict():
    '''    public AnnotatedMethod resolveSetterConflict(final MapperConfig<?> config, final AnnotatedMethod setter1, final AnnotatedMethod setter2)
    '''
def findInjectableValueId():
    '''    public Object findInjectableValueId(final AnnotatedMember m)
    '''
def findSerializer():
    '''    public Object findSerializer(final Annotated am)
    '''
def findKeySerializer():
    '''    public Object findKeySerializer(final Annotated am)
    '''
def findContentSerializer():
    '''    public Object findContentSerializer(final Annotated am)
    '''
def findNullSerializer():
    '''    public Object findNullSerializer(final Annotated am)
    '''
def findSerializationConverter():
    '''    public Object findSerializationConverter(final Annotated a)
    '''
def findSerializationContentConverter():
    '''    public Object findSerializationContentConverter(final AnnotatedMember a)
    '''
def refineSerializationType():
    '''    public JavaType refineSerializationType(final MapperConfig<?> config, final Annotated a, final JavaType baseType)
    '''
def findSerializationPropertyOrder():
    '''    public String[] findSerializationPropertyOrder(final AnnotatedClass ac)
    '''
def findSerializationSortAlphabetically():
    '''    public Boolean findSerializationSortAlphabetically(final Annotated ann)
    '''
def findAndAddVirtualProperties():
    '''    public void findAndAddVirtualProperties(final MapperConfig<?> config, final AnnotatedClass ac, final List<BeanPropertyWriter> properties)
    '''
def findNameForSerialization():
    '''    public PropertyName findNameForSerialization(final Annotated a)
    '''
def hasAsValue():
    '''    public Boolean hasAsValue(final Annotated a)
    '''
def hasAnyGetter():
    '''    public Boolean hasAnyGetter(final Annotated a)
    '''
def findEnumValues():
    '''    public String[] findEnumValues(final Class<?> enumType, final Enum<?>[] enumValues, final String[] names)
    '''
def findEnumValue():
    '''    public String findEnumValue(final Enum<?> value)
    '''
def hasAsValueAnnotation():
    '''    public boolean hasAsValueAnnotation(final AnnotatedMethod am)
    '''
def hasAnyGetterAnnotation():
    '''    public boolean hasAnyGetterAnnotation(final AnnotatedMethod am)
    '''
def findDeserializer():
    '''    public Object findDeserializer(final Annotated am)
    '''
def findKeyDeserializer():
    '''    public Object findKeyDeserializer(final Annotated am)
    '''
def findContentDeserializer():
    '''    public Object findContentDeserializer(final Annotated am)
    '''
def findDeserializationConverter():
    '''    public Object findDeserializationConverter(final Annotated a)
    '''
def findDeserializationContentConverter():
    '''    public Object findDeserializationContentConverter(final AnnotatedMember a)
    '''
def refineDeserializationType():
    '''    public JavaType refineDeserializationType(final MapperConfig<?> config, final Annotated a, final JavaType baseType)
    '''
def findValueInstantiator():
    '''    public Object findValueInstantiator(final AnnotatedClass ac)
    '''
def findNameForDeserialization():
    '''    public PropertyName findNameForDeserialization(final Annotated a)
    '''
def hasAnySetter():
    '''    public Boolean hasAnySetter(final Annotated a)
    '''
def findMergeInfo():
    '''    public Boolean findMergeInfo(final Annotated a)
    '''
def hasCreatorAnnotation():
    '''    public boolean hasCreatorAnnotation(final Annotated a)
    '''
def hasAnySetterAnnotation():
    '''    public boolean hasAnySetterAnnotation(final AnnotatedMethod am)
    '''
def ReferenceProperty():
    '''    public ReferenceProperty(final Type t, final String n)
    '''
def managed():
    '''    public static ReferenceProperty managed(final String name)
    '''
def back():
    '''    public static ReferenceProperty back(final String name)
    '''
def getType():
    '''    public Type getType()
    '''
def getName():
    '''    public String getName()
    '''
def isManagedReference():
    '''    public boolean isManagedReference()
    '''
def isBackReference():
    '''    public boolean isBackReference()
    '''
