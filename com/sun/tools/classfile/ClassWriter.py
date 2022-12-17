def ():
    '''returns ClassOutputStream\n\n
    ()\n
    ()\n
    '''
def write():
    '''returns None\n\n
    write(final ClassFile classFile, final File file)\n
    write(final ClassFile classFile, final OutputStream out)\n
    write(final Attributes attributes, final ClassOutputStream classOutputStream)\n
    write(final Attribute attribute, final ClassOutputStream classOutputStream)\n
    write(final StackMapTable_attribute.stack_map_frame stack_map_frame, final ClassOutputStream classOutputStream)\n
    write(final Annotation[] array, final ClassOutputStream classOutputStream)\n
    write(final TypeAnnotation[] array, final ClassOutputStream classOutputStream)\n
    write(final Annotation annotation, final ClassOutputStream classOutputStream)\n
    write(final TypeAnnotation typeAnnotation, final ClassOutputStream classOutputStream)\n
    write(final Annotation.element_value_pair element_value_pair, final ClassOutputStream classOutputStream)\n
    write(final Annotation.element_value element_value, final ClassOutputStream classOutputStream)\n
    '''
def writeByte():
    '''returns None\n\n
    writeByte(final int v)\n
    '''
def writeShort():
    '''returns None\n\n
    writeShort(final int v)\n
    '''
def writeInt():
    '''returns None\n\n
    writeInt(final int v)\n
    '''
def writeLong():
    '''returns None\n\n
    writeLong(final long v)\n
    '''
def writeFloat():
    '''returns None\n\n
    writeFloat(final float v)\n
    '''
def writeDouble():
    '''returns None\n\n
    writeDouble(final double v)\n
    '''
def writeUTF():
    '''returns None\n\n
    writeUTF(final String str)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final ClassOutputStream out)\n
    '''
def visitClass():
    '''returns Void\n\n
    visitClass(final ConstantPool.CONSTANT_Class_info constant_Class_info, final ClassOutputStream classOutputStream)\n
    visitClass(final Annotation.Class_element_value class_element_value, final ClassOutputStream classOutputStream)\n
    '''
def visitDouble():
    '''returns Integer\n\n
    visitDouble(final ConstantPool.CONSTANT_Double_info constant_Double_info, final ClassOutputStream classOutputStream)\n
    '''
def visitFieldref():
    '''returns Integer\n\n
    visitFieldref(final ConstantPool.CONSTANT_Fieldref_info constant_Fieldref_info, final ClassOutputStream classOutputStream)\n
    '''
def visitFloat():
    '''returns Integer\n\n
    visitFloat(final ConstantPool.CONSTANT_Float_info constant_Float_info, final ClassOutputStream classOutputStream)\n
    '''
def visitInteger():
    '''returns Integer\n\n
    visitInteger(final ConstantPool.CONSTANT_Integer_info constant_Integer_info, final ClassOutputStream classOutputStream)\n
    '''
def visitInterfaceMethodref():
    '''returns Integer\n\n
    visitInterfaceMethodref(final ConstantPool.CONSTANT_InterfaceMethodref_info constant_InterfaceMethodref_info, final ClassOutputStream classOutputStream)\n
    '''
def visitInvokeDynamic():
    '''returns Integer\n\n
    visitInvokeDynamic(final ConstantPool.CONSTANT_InvokeDynamic_info constant_InvokeDynamic_info, final ClassOutputStream classOutputStream)\n
    '''
def visitLong():
    '''returns Integer\n\n
    visitLong(final ConstantPool.CONSTANT_Long_info constant_Long_info, final ClassOutputStream classOutputStream)\n
    '''
def visitNameAndType():
    '''returns Integer\n\n
    visitNameAndType(final ConstantPool.CONSTANT_NameAndType_info constant_NameAndType_info, final ClassOutputStream classOutputStream)\n
    '''
def visitMethodHandle():
    '''returns Integer\n\n
    visitMethodHandle(final ConstantPool.CONSTANT_MethodHandle_info constant_MethodHandle_info, final ClassOutputStream classOutputStream)\n
    '''
def visitMethodType():
    '''returns Integer\n\n
    visitMethodType(final ConstantPool.CONSTANT_MethodType_info constant_MethodType_info, final ClassOutputStream classOutputStream)\n
    '''
def visitMethodref():
    '''returns Integer\n\n
    visitMethodref(final ConstantPool.CONSTANT_Methodref_info constant_Methodref_info, final ClassOutputStream classOutputStream)\n
    '''
def visitString():
    '''returns Integer\n\n
    visitString(final ConstantPool.CONSTANT_String_info constant_String_info, final ClassOutputStream classOutputStream)\n
    '''
def visitUtf8():
    '''returns Integer\n\n
    visitUtf8(final ConstantPool.CONSTANT_Utf8_info constant_Utf8_info, final ClassOutputStream classOutputStream)\n
    '''
def visitDefault():
    '''returns Void\n\n
    visitDefault(final DefaultAttribute defaultAttribute, final ClassOutputStream classOutputStream)\n
    '''
def visitAnnotationDefault():
    '''returns Void\n\n
    visitAnnotationDefault(final AnnotationDefault_attribute annotationDefault_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitBootstrapMethods():
    '''returns Void\n\n
    visitBootstrapMethods(final BootstrapMethods_attribute bootstrapMethods_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitCharacterRangeTable():
    '''returns Void\n\n
    visitCharacterRangeTable(final CharacterRangeTable_attribute characterRangeTable_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitCode():
    '''returns Void\n\n
    visitCode(final Code_attribute code_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitCompilationID():
    '''returns Void\n\n
    visitCompilationID(final CompilationID_attribute compilationID_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitConstantValue():
    '''returns Void\n\n
    visitConstantValue(final ConstantValue_attribute constantValue_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitDeprecated():
    '''returns Void\n\n
    visitDeprecated(final Deprecated_attribute deprecated_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitEnclosingMethod():
    '''returns Void\n\n
    visitEnclosingMethod(final EnclosingMethod_attribute enclosingMethod_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitExceptions():
    '''returns Void\n\n
    visitExceptions(final Exceptions_attribute exceptions_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitInnerClasses():
    '''returns Void\n\n
    visitInnerClasses(final InnerClasses_attribute innerClasses_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitLineNumberTable():
    '''returns Void\n\n
    visitLineNumberTable(final LineNumberTable_attribute lineNumberTable_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitLocalVariableTable():
    '''returns Void\n\n
    visitLocalVariableTable(final LocalVariableTable_attribute localVariableTable_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitLocalVariableTypeTable():
    '''returns Void\n\n
    visitLocalVariableTypeTable(final LocalVariableTypeTable_attribute localVariableTypeTable_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitMethodParameters():
    '''returns Void\n\n
    visitMethodParameters(final MethodParameters_attribute methodParameters_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitRuntimeVisibleAnnotations():
    '''returns Void\n\n
    visitRuntimeVisibleAnnotations(final RuntimeVisibleAnnotations_attribute runtimeVisibleAnnotations_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitRuntimeInvisibleAnnotations():
    '''returns Void\n\n
    visitRuntimeInvisibleAnnotations(final RuntimeInvisibleAnnotations_attribute runtimeInvisibleAnnotations_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitRuntimeVisibleTypeAnnotations():
    '''returns Void\n\n
    visitRuntimeVisibleTypeAnnotations(final RuntimeVisibleTypeAnnotations_attribute runtimeVisibleTypeAnnotations_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitRuntimeInvisibleTypeAnnotations():
    '''returns Void\n\n
    visitRuntimeInvisibleTypeAnnotations(final RuntimeInvisibleTypeAnnotations_attribute runtimeInvisibleTypeAnnotations_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitRuntimeVisibleParameterAnnotations():
    '''returns Void\n\n
    visitRuntimeVisibleParameterAnnotations(final RuntimeVisibleParameterAnnotations_attribute runtimeVisibleParameterAnnotations_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitRuntimeInvisibleParameterAnnotations():
    '''returns Void\n\n
    visitRuntimeInvisibleParameterAnnotations(final RuntimeInvisibleParameterAnnotations_attribute runtimeInvisibleParameterAnnotations_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitSignature():
    '''returns Void\n\n
    visitSignature(final Signature_attribute signature_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitSourceDebugExtension():
    '''returns Void\n\n
    visitSourceDebugExtension(final SourceDebugExtension_attribute sourceDebugExtension_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitSourceFile():
    '''returns Void\n\n
    visitSourceFile(final SourceFile_attribute sourceFile_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitSourceID():
    '''returns Void\n\n
    visitSourceID(final SourceID_attribute sourceID_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitStackMap():
    '''returns Void\n\n
    visitStackMap(final StackMap_attribute stackMap_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitStackMapTable():
    '''returns Void\n\n
    visitStackMapTable(final StackMapTable_attribute stackMapTable_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visitSynthetic():
    '''returns Void\n\n
    visitSynthetic(final Synthetic_attribute synthetic_attribute, final ClassOutputStream classOutputStream)\n
    '''
def visit_same_frame():
    '''returns Void\n\n
    visit_same_frame(final StackMapTable_attribute.same_frame same_frame, final ClassOutputStream classOutputStream)\n
    '''
def visit_same_locals_1_stack_item_frame():
    '''returns Void\n\n
    visit_same_locals_1_stack_item_frame(final StackMapTable_attribute.same_locals_1_stack_item_frame same_locals_1_stack_item_frame, final ClassOutputStream classOutputStream)\n
    '''
def visit_same_locals_1_stack_item_frame_extended():
    '''returns Void\n\n
    visit_same_locals_1_stack_item_frame_extended(final StackMapTable_attribute.same_locals_1_stack_item_frame_extended same_locals_1_stack_item_frame_extended, final ClassOutputStream classOutputStream)\n
    '''
def visit_chop_frame():
    '''returns Void\n\n
    visit_chop_frame(final StackMapTable_attribute.chop_frame chop_frame, final ClassOutputStream classOutputStream)\n
    '''
def visit_same_frame_extended():
    '''returns Void\n\n
    visit_same_frame_extended(final StackMapTable_attribute.same_frame_extended same_frame_extended, final ClassOutputStream classOutputStream)\n
    '''
def visit_append_frame():
    '''returns Void\n\n
    visit_append_frame(final StackMapTable_attribute.append_frame append_frame, final ClassOutputStream classOutputStream)\n
    '''
def visit_full_frame():
    '''returns Void\n\n
    visit_full_frame(final StackMapTable_attribute.full_frame full_frame, final ClassOutputStream classOutputStream)\n
    '''
def visitPrimitive():
    '''returns Void\n\n
    visitPrimitive(final Annotation.Primitive_element_value primitive_element_value, final ClassOutputStream classOutputStream)\n
    '''
def visitEnum():
    '''returns Void\n\n
    visitEnum(final Annotation.Enum_element_value enum_element_value, final ClassOutputStream classOutputStream)\n
    '''
def visitAnnotation():
    '''returns Void\n\n
    visitAnnotation(final Annotation.Annotation_element_value annotation_element_value, final ClassOutputStream classOutputStream)\n
    '''
def visitArray():
    '''returns Void\n\n
    visitArray(final Annotation.Array_element_value array_element_value, final ClassOutputStream classOutputStream)\n
    '''
