def ():
    '''returns ClassVisitor\n\n
    (final int n)\n
    (final int api, final ClassVisitor cv)\n
    '''
def visit():
    '''returns None\n\n
    visit(final int n, final int n2, final String s, final String s2, final String s3, final String[] array)\n
    '''
def visitSource():
    '''returns None\n\n
    visitSource(final String s, final String s2)\n
    '''
def visitOuterClass():
    '''returns None\n\n
    visitOuterClass(final String s, final String s2, final String s3)\n
    '''
def visitAnnotation():
    '''returns AnnotationVisitor\n\n
    visitAnnotation(final String s, final boolean b)\n
    '''
def visitAttribute():
    '''returns None\n\n
    visitAttribute(final Attribute attribute)\n
    '''
def visitInnerClass():
    '''returns None\n\n
    visitInnerClass(final String s, final String s2, final String s3, final int n)\n
    '''
def visitField():
    '''returns FieldVisitor\n\n
    visitField(final int n, final String s, final String s2, final String s3, final Object o)\n
    '''
def visitMethod():
    '''returns MethodVisitor\n\n
    visitMethod(final int n, final String s, final String s2, final String s3, final String[] array)\n
    '''
def visitEnd():
    '''returns None\n\n
    visitEnd()\n
    '''
