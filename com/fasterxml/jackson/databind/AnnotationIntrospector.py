def nopInstance():
'''public static AnnotationIntrospector nopInstance()
'''
pass
def pair():
'''public static AnnotationIntrospector pair(final AnnotationIntrospector a1, final AnnotationIntrospector a2)
'''
pass
def allIntrospectors():
'''public Collection<AnnotationIntrospector> allIntrospectors()
public Collection<AnnotationIntrospector> allIntrospectors(final Collection<AnnotationIntrospector> result)
'''
pass
def isAnnotationBundle():
'''public boolean isAnnotationBundle(final Annotation ann)
'''
pass
def findObjectIdInfo():
'''public ObjectIdInfo findObjectIdInfo(final Annotated ann)
'''
pass
def findObjectReferenceInfo():
'''public ObjectIdInfo findObjectReferenceInfo(final Annotated ann, final ObjectIdInfo objectIdInfo)
'''
pass
def findRootName():
'''public PropertyName findRootName(final AnnotatedClass ac)
'''
pass
def isIgnorableType():
'''public Boolean isIgnorableType(final AnnotatedClass ac)
'''
pass
def findFilterId():
'''public Object findFilterId(final Annotated ann)
'''
pass
def findNamingStrategy():
'''public Object findNamingStrategy(final AnnotatedClass ac)
'''
pass
def findClassDescription():
'''public String findClassDescription(final AnnotatedClass ac)
'''
pass
def findPropertiesToIgnore():
'''public String[] findPropertiesToIgnore(final Annotated ac, final boolean forSerialization)
public String[] findPropertiesToIgnore(final Annotated ac)
'''
pass
def findIgnoreUnknownProperties():
'''public Boolean findIgnoreUnknownProperties(final AnnotatedClass ac)
'''
pass
def findSubtypes():
'''public List<NamedType> findSubtypes(final Annotated a)
'''
pass
def findTypeName():
'''public String findTypeName(final AnnotatedClass ac)
'''
pass
def isTypeId():
'''public Boolean isTypeId(final AnnotatedMember member)
'''
pass
def findReferenceType():
'''public ReferenceProperty findReferenceType(final AnnotatedMember member)
'''
pass
def findUnwrappingNameTransformer():
'''public NameTransformer findUnwrappingNameTransformer(final AnnotatedMember member)
'''
pass
def hasIgnoreMarker():
'''public boolean hasIgnoreMarker(final AnnotatedMember m)
'''
pass
def hasRequiredMarker():
'''public Boolean hasRequiredMarker(final AnnotatedMember m)
'''
pass
def findWrapperName():
'''public PropertyName findWrapperName(final Annotated ann)
'''
pass
def findPropertyDefaultValue():
'''public String findPropertyDefaultValue(final Annotated ann)
'''
pass
def findPropertyDescription():
'''public String findPropertyDescription(final Annotated ann)
'''
pass
def findPropertyIndex():
'''public Integer findPropertyIndex(final Annotated ann)
'''
pass
def findImplicitPropertyName():
'''public String findImplicitPropertyName(final AnnotatedMember member)
'''
pass
def findPropertyAliases():
'''public List<PropertyName> findPropertyAliases(final Annotated ann)
'''
pass
def resolveSetterConflict():
'''public AnnotatedMethod resolveSetterConflict(final MapperConfig<?> config, final AnnotatedMethod setter1, final AnnotatedMethod setter2)
'''
pass
def findInjectableValueId():
'''public Object findInjectableValueId(final AnnotatedMember m)
'''
pass
def findSerializer():
'''public Object findSerializer(final Annotated am)
'''
pass
def findKeySerializer():
'''public Object findKeySerializer(final Annotated am)
'''
pass
def findContentSerializer():
'''public Object findContentSerializer(final Annotated am)
'''
pass
def findNullSerializer():
'''public Object findNullSerializer(final Annotated am)
'''
pass
def findSerializationConverter():
'''public Object findSerializationConverter(final Annotated a)
'''
pass
def findSerializationContentConverter():
'''public Object findSerializationContentConverter(final AnnotatedMember a)
'''
pass
def refineSerializationType():
'''public JavaType refineSerializationType(final MapperConfig<?> config, final Annotated a, final JavaType baseType)
'''
pass
def findSerializationPropertyOrder():
'''public String[] findSerializationPropertyOrder(final AnnotatedClass ac)
'''
pass
def findSerializationSortAlphabetically():
'''public Boolean findSerializationSortAlphabetically(final Annotated ann)
'''
pass
def findAndAddVirtualProperties():
'''public void findAndAddVirtualProperties(final MapperConfig<?> config, final AnnotatedClass ac, final List<BeanPropertyWriter> properties)
'''
pass
def findNameForSerialization():
'''public PropertyName findNameForSerialization(final Annotated a)
'''
pass
def hasAsValue():
'''public Boolean hasAsValue(final Annotated a)
'''
pass
def hasAnyGetter():
'''public Boolean hasAnyGetter(final Annotated a)
'''
pass
def findEnumValues():
'''public String[] findEnumValues(final Class<?> enumType, final Enum<?>[] enumValues, final String[] names)
'''
pass
def findEnumValue():
'''public String findEnumValue(final Enum<?> value)
'''
pass
def hasAsValueAnnotation():
'''public boolean hasAsValueAnnotation(final AnnotatedMethod am)
'''
pass
def hasAnyGetterAnnotation():
'''public boolean hasAnyGetterAnnotation(final AnnotatedMethod am)
'''
pass
def findDeserializer():
'''public Object findDeserializer(final Annotated am)
'''
pass
def findKeyDeserializer():
'''public Object findKeyDeserializer(final Annotated am)
'''
pass
def findContentDeserializer():
'''public Object findContentDeserializer(final Annotated am)
'''
pass
def findDeserializationConverter():
'''public Object findDeserializationConverter(final Annotated a)
'''
pass
def findDeserializationContentConverter():
'''public Object findDeserializationContentConverter(final AnnotatedMember a)
'''
pass
def refineDeserializationType():
'''public JavaType refineDeserializationType(final MapperConfig<?> config, final Annotated a, final JavaType baseType)
'''
pass
def findValueInstantiator():
'''public Object findValueInstantiator(final AnnotatedClass ac)
'''
pass
def findNameForDeserialization():
'''public PropertyName findNameForDeserialization(final Annotated a)
'''
pass
def hasAnySetter():
'''public Boolean hasAnySetter(final Annotated a)
'''
pass
def findMergeInfo():
'''public Boolean findMergeInfo(final Annotated a)
'''
pass
def hasCreatorAnnotation():
'''public boolean hasCreatorAnnotation(final Annotated a)
'''
pass
def hasAnySetterAnnotation():
'''public boolean hasAnySetterAnnotation(final AnnotatedMethod am)
'''
pass
def ReferenceProperty():
'''public ReferenceProperty(final Type t, final String n)
'''
pass
def managed():
'''public static ReferenceProperty managed(final String name)
'''
pass
def back():
'''public static ReferenceProperty back(final String name)
'''
pass
def getType():
'''public Type getType()
'''
pass
def getName():
'''public String getName()
'''
pass
def isManagedReference():
'''public boolean isManagedReference()
'''
pass
def isBackReference():
'''public boolean isBackReference()
'''
pass
