def ClassWriter():
    '''public ClassWriter()
    '''
def write():
    '''public void write(final ClassFile classFile, final File file)
    public void write(final ClassFile classFile, final OutputStream out)
    public void write(final Attributes attributes, final ClassOutputStream classOutputStream)
    public void write(final Attribute attribute, final ClassOutputStream classOutputStream)
    public void write(final StackMapTable_attribute.stack_map_frame stack_map_frame, final ClassOutputStream classOutputStream)
    public void write(final Annotation[] array, final ClassOutputStream classOutputStream)
    public void write(final TypeAnnotation[] array, final ClassOutputStream classOutputStream)
    public void write(final Annotation annotation, final ClassOutputStream classOutputStream)
    public void write(final TypeAnnotation typeAnnotation, final ClassOutputStream classOutputStream)
    public void write(final Annotation.element_value_pair element_value_pair, final ClassOutputStream classOutputStream)
    public void write(final Annotation.element_value element_value, final ClassOutputStream classOutputStream)
    '''
def ClassOutputStream():
    '''public ClassOutputStream()
    '''
def writeByte():
    '''public void writeByte(final int v)
    '''
def writeShort():
    '''public void writeShort(final int v)
    '''
def writeInt():
    '''public void writeInt(final int v)
    '''
def writeLong():
    '''public void writeLong(final long v)
    '''
def writeFloat():
    '''public void writeFloat(final float v)
    '''
def writeDouble():
    '''public void writeDouble(final double v)
    '''
def writeUTF():
    '''public void writeUTF(final String str)
    '''
def writeTo():
    '''public void writeTo(final ClassOutputStream out)
    '''
def visitClass():
    '''public Integer visitClass(final ConstantPool.CONSTANT_Class_info constant_Class_info, final ClassOutputStream classOutputStream)
    public Void visitClass(final Annotation.Class_element_value class_element_value, final ClassOutputStream classOutputStream)
    '''
def visitDouble():
    '''public Integer visitDouble(final ConstantPool.CONSTANT_Double_info constant_Double_info, final ClassOutputStream classOutputStream)
    '''
def visitFieldref():
    '''public Integer visitFieldref(final ConstantPool.CONSTANT_Fieldref_info constant_Fieldref_info, final ClassOutputStream classOutputStream)
    '''
def visitFloat():
    '''public Integer visitFloat(final ConstantPool.CONSTANT_Float_info constant_Float_info, final ClassOutputStream classOutputStream)
    '''
def visitInteger():
    '''public Integer visitInteger(final ConstantPool.CONSTANT_Integer_info constant_Integer_info, final ClassOutputStream classOutputStream)
    '''
def visitInterfaceMethodref():
    '''public Integer visitInterfaceMethodref(final ConstantPool.CONSTANT_InterfaceMethodref_info constant_InterfaceMethodref_info, final ClassOutputStream classOutputStream)
    '''
def visitInvokeDynamic():
    '''public Integer visitInvokeDynamic(final ConstantPool.CONSTANT_InvokeDynamic_info constant_InvokeDynamic_info, final ClassOutputStream classOutputStream)
    '''
def visitLong():
    '''public Integer visitLong(final ConstantPool.CONSTANT_Long_info constant_Long_info, final ClassOutputStream classOutputStream)
    '''
def visitNameAndType():
    '''public Integer visitNameAndType(final ConstantPool.CONSTANT_NameAndType_info constant_NameAndType_info, final ClassOutputStream classOutputStream)
    '''
def visitMethodHandle():
    '''public Integer visitMethodHandle(final ConstantPool.CONSTANT_MethodHandle_info constant_MethodHandle_info, final ClassOutputStream classOutputStream)
    '''
def visitMethodType():
    '''public Integer visitMethodType(final ConstantPool.CONSTANT_MethodType_info constant_MethodType_info, final ClassOutputStream classOutputStream)
    '''
def visitMethodref():
    '''public Integer visitMethodref(final ConstantPool.CONSTANT_Methodref_info constant_Methodref_info, final ClassOutputStream classOutputStream)
    '''
def visitString():
    '''public Integer visitString(final ConstantPool.CONSTANT_String_info constant_String_info, final ClassOutputStream classOutputStream)
    '''
def visitUtf8():
    '''public Integer visitUtf8(final ConstantPool.CONSTANT_Utf8_info constant_Utf8_info, final ClassOutputStream classOutputStream)
    '''
def visitDefault():
    '''public Void visitDefault(final DefaultAttribute defaultAttribute, final ClassOutputStream classOutputStream)
    '''
def visitAnnotationDefault():
    '''public Void visitAnnotationDefault(final AnnotationDefault_attribute annotationDefault_attribute, final ClassOutputStream classOutputStream)
    '''
def visitBootstrapMethods():
    '''public Void visitBootstrapMethods(final BootstrapMethods_attribute bootstrapMethods_attribute, final ClassOutputStream classOutputStream)
    '''
def visitCharacterRangeTable():
    '''public Void visitCharacterRangeTable(final CharacterRangeTable_attribute characterRangeTable_attribute, final ClassOutputStream classOutputStream)
    '''
def visitCode():
    '''public Void visitCode(final Code_attribute code_attribute, final ClassOutputStream classOutputStream)
    '''
def visitCompilationID():
    '''public Void visitCompilationID(final CompilationID_attribute compilationID_attribute, final ClassOutputStream classOutputStream)
    '''
def visitConstantValue():
    '''public Void visitConstantValue(final ConstantValue_attribute constantValue_attribute, final ClassOutputStream classOutputStream)
    '''
def visitDeprecated():
    '''public Void visitDeprecated(final Deprecated_attribute deprecated_attribute, final ClassOutputStream classOutputStream)
    '''
def visitEnclosingMethod():
    '''public Void visitEnclosingMethod(final EnclosingMethod_attribute enclosingMethod_attribute, final ClassOutputStream classOutputStream)
    '''
def visitExceptions():
    '''public Void visitExceptions(final Exceptions_attribute exceptions_attribute, final ClassOutputStream classOutputStream)
    '''
def visitInnerClasses():
    '''public Void visitInnerClasses(final InnerClasses_attribute innerClasses_attribute, final ClassOutputStream classOutputStream)
    '''
def visitLineNumberTable():
    '''public Void visitLineNumberTable(final LineNumberTable_attribute lineNumberTable_attribute, final ClassOutputStream classOutputStream)
    '''
def visitLocalVariableTable():
    '''public Void visitLocalVariableTable(final LocalVariableTable_attribute localVariableTable_attribute, final ClassOutputStream classOutputStream)
    '''
def visitLocalVariableTypeTable():
    '''public Void visitLocalVariableTypeTable(final LocalVariableTypeTable_attribute localVariableTypeTable_attribute, final ClassOutputStream classOutputStream)
    '''
def visitMethodParameters():
    '''public Void visitMethodParameters(final MethodParameters_attribute methodParameters_attribute, final ClassOutputStream classOutputStream)
    '''
def visitRuntimeVisibleAnnotations():
    '''public Void visitRuntimeVisibleAnnotations(final RuntimeVisibleAnnotations_attribute runtimeVisibleAnnotations_attribute, final ClassOutputStream classOutputStream)
    '''
def visitRuntimeInvisibleAnnotations():
    '''public Void visitRuntimeInvisibleAnnotations(final RuntimeInvisibleAnnotations_attribute runtimeInvisibleAnnotations_attribute, final ClassOutputStream classOutputStream)
    '''
def visitRuntimeVisibleTypeAnnotations():
    '''public Void visitRuntimeVisibleTypeAnnotations(final RuntimeVisibleTypeAnnotations_attribute runtimeVisibleTypeAnnotations_attribute, final ClassOutputStream classOutputStream)
    '''
def visitRuntimeInvisibleTypeAnnotations():
    '''public Void visitRuntimeInvisibleTypeAnnotations(final RuntimeInvisibleTypeAnnotations_attribute runtimeInvisibleTypeAnnotations_attribute, final ClassOutputStream classOutputStream)
    '''
def visitRuntimeVisibleParameterAnnotations():
    '''public Void visitRuntimeVisibleParameterAnnotations(final RuntimeVisibleParameterAnnotations_attribute runtimeVisibleParameterAnnotations_attribute, final ClassOutputStream classOutputStream)
    '''
def visitRuntimeInvisibleParameterAnnotations():
    '''public Void visitRuntimeInvisibleParameterAnnotations(final RuntimeInvisibleParameterAnnotations_attribute runtimeInvisibleParameterAnnotations_attribute, final ClassOutputStream classOutputStream)
    '''
def visitSignature():
    '''public Void visitSignature(final Signature_attribute signature_attribute, final ClassOutputStream classOutputStream)
    '''
def visitSourceDebugExtension():
    '''public Void visitSourceDebugExtension(final SourceDebugExtension_attribute sourceDebugExtension_attribute, final ClassOutputStream classOutputStream)
    '''
def visitSourceFile():
    '''public Void visitSourceFile(final SourceFile_attribute sourceFile_attribute, final ClassOutputStream classOutputStream)
    '''
def visitSourceID():
    '''public Void visitSourceID(final SourceID_attribute sourceID_attribute, final ClassOutputStream classOutputStream)
    '''
def visitStackMap():
    '''public Void visitStackMap(final StackMap_attribute stackMap_attribute, final ClassOutputStream classOutputStream)
    '''
def visitStackMapTable():
    '''public Void visitStackMapTable(final StackMapTable_attribute stackMapTable_attribute, final ClassOutputStream classOutputStream)
    '''
def visitSynthetic():
    '''public Void visitSynthetic(final Synthetic_attribute synthetic_attribute, final ClassOutputStream classOutputStream)
    '''
def visit_same_frame():
    '''public Void visit_same_frame(final StackMapTable_attribute.same_frame same_frame, final ClassOutputStream classOutputStream)
    '''
def visit_same_locals_1_stack_item_frame():
    '''public Void visit_same_locals_1_stack_item_frame(final StackMapTable_attribute.same_locals_1_stack_item_frame same_locals_1_stack_item_frame, final ClassOutputStream classOutputStream)
    '''
def visit_same_locals_1_stack_item_frame_extended():
    '''public Void visit_same_locals_1_stack_item_frame_extended(final StackMapTable_attribute.same_locals_1_stack_item_frame_extended same_locals_1_stack_item_frame_extended, final ClassOutputStream classOutputStream)
    '''
def visit_chop_frame():
    '''public Void visit_chop_frame(final StackMapTable_attribute.chop_frame chop_frame, final ClassOutputStream classOutputStream)
    '''
def visit_same_frame_extended():
    '''public Void visit_same_frame_extended(final StackMapTable_attribute.same_frame_extended same_frame_extended, final ClassOutputStream classOutputStream)
    '''
def visit_append_frame():
    '''public Void visit_append_frame(final StackMapTable_attribute.append_frame append_frame, final ClassOutputStream classOutputStream)
    '''
def visit_full_frame():
    '''public Void visit_full_frame(final StackMapTable_attribute.full_frame full_frame, final ClassOutputStream classOutputStream)
    '''
def visitPrimitive():
    '''public Void visitPrimitive(final Annotation.Primitive_element_value primitive_element_value, final ClassOutputStream classOutputStream)
    '''
def visitEnum():
    '''public Void visitEnum(final Annotation.Enum_element_value enum_element_value, final ClassOutputStream classOutputStream)
    '''
def visitAnnotation():
    '''public Void visitAnnotation(final Annotation.Annotation_element_value annotation_element_value, final ClassOutputStream classOutputStream)
    '''
def visitArray():
    '''public Void visitArray(final Annotation.Array_element_value array_element_value, final ClassOutputStream classOutputStream)
    '''
