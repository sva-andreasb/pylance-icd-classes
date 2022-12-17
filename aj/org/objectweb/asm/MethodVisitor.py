def ():
    '''returns MethodVisitor\n\n
    (final int n)\n
    (final int api, final MethodVisitor mv)\n
    '''
def visitAnnotationDefault():
    '''returns AnnotationVisitor\n\n
    visitAnnotationDefault()\n
    '''
def visitAnnotation():
    '''returns AnnotationVisitor\n\n
    visitAnnotation(final String s, final boolean b)\n
    '''
def visitParameterAnnotation():
    '''returns AnnotationVisitor\n\n
    visitParameterAnnotation(final int n, final String s, final boolean b)\n
    '''
def visitAttribute():
    '''returns None\n\n
    visitAttribute(final Attribute attribute)\n
    '''
def visitCode():
    '''returns None\n\n
    visitCode()\n
    '''
def visitFrame():
    '''returns None\n\n
    visitFrame(final int n, final int n2, final Object[] array, final int n3, final Object[] array2)\n
    '''
def visitInsn():
    '''returns None\n\n
    visitInsn(final int n)\n
    '''
def visitIntInsn():
    '''returns None\n\n
    visitIntInsn(final int n, final int n2)\n
    '''
def visitVarInsn():
    '''returns None\n\n
    visitVarInsn(final int n, final int n2)\n
    '''
def visitTypeInsn():
    '''returns None\n\n
    visitTypeInsn(final int n, final String s)\n
    '''
def visitFieldInsn():
    '''returns None\n\n
    visitFieldInsn(final int n, final String s, final String s2, final String s3)\n
    '''
def visitMethodInsn():
    '''returns None\n\n
    visitMethodInsn(final int n, final String s, final String s2, final String s3)\n
    '''
def visitInvokeDynamicInsn():
    '''returns None\n\n
    visitInvokeDynamicInsn(final String s, final String s2, final Handle handle, final Object... array)\n
    '''
def visitJumpInsn():
    '''returns None\n\n
    visitJumpInsn(final int n, final Label label)\n
    '''
def visitLabel():
    '''returns None\n\n
    visitLabel(final Label label)\n
    '''
def visitLdcInsn():
    '''returns None\n\n
    visitLdcInsn(final Object o)\n
    '''
def visitIincInsn():
    '''returns None\n\n
    visitIincInsn(final int n, final int n2)\n
    '''
def visitTableSwitchInsn():
    '''returns None\n\n
    visitTableSwitchInsn(final int n, final int n2, final Label label, final Label... array)\n
    '''
def visitLookupSwitchInsn():
    '''returns None\n\n
    visitLookupSwitchInsn(final Label label, final int[] array, final Label[] array2)\n
    '''
def visitMultiANewArrayInsn():
    '''returns None\n\n
    visitMultiANewArrayInsn(final String s, final int n)\n
    '''
def visitTryCatchBlock():
    '''returns None\n\n
    visitTryCatchBlock(final Label label, final Label label2, final Label label3, final String s)\n
    '''
def visitLocalVariable():
    '''returns None\n\n
    visitLocalVariable(final String s, final String s2, final String s3, final Label label, final Label label2, final int n)\n
    '''
def visitLineNumber():
    '''returns None\n\n
    visitLineNumber(final int n, final Label label)\n
    '''
def visitMaxs():
    '''returns None\n\n
    visitMaxs(final int n, final int n2)\n
    '''
def visitEnd():
    '''returns None\n\n
    visitEnd()\n
    '''
