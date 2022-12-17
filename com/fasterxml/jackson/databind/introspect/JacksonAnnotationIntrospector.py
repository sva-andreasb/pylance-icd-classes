def ():
    '''returns JacksonAnnotationIntrospector\n\n
    ()\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def setConstructorPropertiesImpliesCreator():
    '''returns JacksonAnnotationIntrospector\n\n
    setConstructorPropertiesImpliesCreator(final boolean b)\n
    '''
def isAnnotationBundle():
    '''returns boolean\n\n
    isAnnotationBundle(final Annotation ann)\n
    '''
def findEnumValue():
    '''returns String\n\n
    findEnumValue(final Enum<?> value)\n
    '''
def findEnumValues():
    '''returns String[]\n\n
    findEnumValues(final Class<?> enumType, final Enum<?>[] enumValues, final String[] names)\n
    '''
def findRootName():
    '''returns PropertyName\n\n
    findRootName(final AnnotatedClass ac)\n
    '''
def isIgnorableType():
    '''returns Boolean\n\n
    isIgnorableType(final AnnotatedClass ac)\n
    '''
def findFilterId():
    '''returns Object\n\n
    findFilterId(final Annotated a)\n
    '''
def findNamingStrategy():
    '''returns Object\n\n
    findNamingStrategy(final AnnotatedClass ac)\n
    '''
def findClassDescription():
    '''returns String\n\n
    findClassDescription(final AnnotatedClass ac)\n
    '''
def findImplicitPropertyName():
    '''returns String\n\n
    findImplicitPropertyName(final AnnotatedMember m)\n
    '''
def findPropertyAliases():
    '''returns List<PropertyName>\n\n
    findPropertyAliases(final Annotated m)\n
    '''
def hasIgnoreMarker():
    '''returns boolean\n\n
    hasIgnoreMarker(final AnnotatedMember m)\n
    '''
def hasRequiredMarker():
    '''returns Boolean\n\n
    hasRequiredMarker(final AnnotatedMember m)\n
    '''
def findPropertyDescription():
    '''returns String\n\n
    findPropertyDescription(final Annotated ann)\n
    '''
def findPropertyIndex():
    '''returns Integer\n\n
    findPropertyIndex(final Annotated ann)\n
    '''
def findPropertyDefaultValue():
    '''returns String\n\n
    findPropertyDefaultValue(final Annotated ann)\n
    '''
def findReferenceType():
    '''returns ReferenceProperty\n\n
    findReferenceType(final AnnotatedMember member)\n
    '''
def findUnwrappingNameTransformer():
    '''returns NameTransformer\n\n
    findUnwrappingNameTransformer(final AnnotatedMember member)\n
    '''
def findInjectableValueId():
    '''returns Object\n\n
    findInjectableValueId(final AnnotatedMember m)\n
    '''
def resolveSetterConflict():
    '''returns AnnotatedMethod\n\n
    resolveSetterConflict(final MapperConfig<?> config, final AnnotatedMethod setter1, final AnnotatedMethod setter2)\n
    '''
def findSubtypes():
    '''returns List<NamedType>\n\n
    findSubtypes(final Annotated a)\n
    '''
def findTypeName():
    '''returns String\n\n
    findTypeName(final AnnotatedClass ac)\n
    '''
def isTypeId():
    '''returns Boolean\n\n
    isTypeId(final AnnotatedMember member)\n
    '''
def findObjectIdInfo():
    '''returns ObjectIdInfo\n\n
    findObjectIdInfo(final Annotated ann)\n
    '''
def findObjectReferenceInfo():
    '''returns ObjectIdInfo\n\n
    findObjectReferenceInfo(final Annotated ann, ObjectIdInfo objectIdInfo)\n
    '''
def findSerializer():
    '''returns Object\n\n
    findSerializer(final Annotated a)\n
    '''
def findKeySerializer():
    '''returns Object\n\n
    findKeySerializer(final Annotated a)\n
    '''
def findContentSerializer():
    '''returns Object\n\n
    findContentSerializer(final Annotated a)\n
    '''
def findNullSerializer():
    '''returns Object\n\n
    findNullSerializer(final Annotated a)\n
    '''
def findSerializationConverter():
    '''returns Object\n\n
    findSerializationConverter(final Annotated a)\n
    '''
def findSerializationContentConverter():
    '''returns Object\n\n
    findSerializationContentConverter(final AnnotatedMember a)\n
    '''
def refineSerializationType():
    '''returns JavaType\n\n
    refineSerializationType(final MapperConfig<?> config, final Annotated a, final JavaType baseType)\n
    '''
def findSerializationPropertyOrder():
    '''returns String[]\n\n
    findSerializationPropertyOrder(final AnnotatedClass ac)\n
    '''
def findSerializationSortAlphabetically():
    '''returns Boolean\n\n
    findSerializationSortAlphabetically(final Annotated ann)\n
    '''
def findAndAddVirtualProperties():
    '''returns None\n\n
    findAndAddVirtualProperties(final MapperConfig<?> config, final AnnotatedClass ac, final List<BeanPropertyWriter> properties)\n
    '''
def findNameForSerialization():
    '''returns PropertyName\n\n
    findNameForSerialization(final Annotated a)\n
    '''
def hasAsValue():
    '''returns Boolean\n\n
    hasAsValue(final Annotated a)\n
    '''
def hasAnyGetter():
    '''returns Boolean\n\n
    hasAnyGetter(final Annotated a)\n
    '''
def hasAnyGetterAnnotation():
    '''returns boolean\n\n
    hasAnyGetterAnnotation(final AnnotatedMethod am)\n
    '''
def hasAsValueAnnotation():
    '''returns boolean\n\n
    hasAsValueAnnotation(final AnnotatedMethod am)\n
    '''
def findDeserializer():
    '''returns Object\n\n
    findDeserializer(final Annotated a)\n
    '''
def findKeyDeserializer():
    '''returns Object\n\n
    findKeyDeserializer(final Annotated a)\n
    '''
def findContentDeserializer():
    '''returns Object\n\n
    findContentDeserializer(final Annotated a)\n
    '''
def findDeserializationConverter():
    '''returns Object\n\n
    findDeserializationConverter(final Annotated a)\n
    '''
def findDeserializationContentConverter():
    '''returns Object\n\n
    findDeserializationContentConverter(final AnnotatedMember a)\n
    '''
def refineDeserializationType():
    '''returns JavaType\n\n
    refineDeserializationType(final MapperConfig<?> config, final Annotated a, final JavaType baseType)\n
    '''
def findValueInstantiator():
    '''returns Object\n\n
    findValueInstantiator(final AnnotatedClass ac)\n
    '''
def findNameForDeserialization():
    '''returns PropertyName\n\n
    findNameForDeserialization(final Annotated a)\n
    '''
def hasAnySetter():
    '''returns Boolean\n\n
    hasAnySetter(final Annotated a)\n
    '''
def findMergeInfo():
    '''returns Boolean\n\n
    findMergeInfo(final Annotated a)\n
    '''
def hasAnySetterAnnotation():
    '''returns boolean\n\n
    hasAnySetterAnnotation(final AnnotatedMethod am)\n
    '''
def hasCreatorAnnotation():
    '''returns boolean\n\n
    hasCreatorAnnotation(final Annotated a)\n
    '''
