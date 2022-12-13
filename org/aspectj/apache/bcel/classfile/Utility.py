def accessToString():
    '''    public static final String accessToString(final int access_flags)
    public static final String accessToString(final int access_flags, final boolean for_class)
    '''
def classOrInterface():
    '''    public static final String classOrInterface(final int access_flags)
    '''
def codeToString():
    '''    public static final String codeToString(final byte[] code, final ConstantPool constant_pool, final int index, final int length, final boolean verbose)
    public static final String codeToString(final byte[] code, final ConstantPool constant_pool, final int index, final int length)
    public static final String codeToString(final ByteSequence bytes, final ConstantPool constant_pool)
    public static final String codeToString(final ByteSequence bytes, final ConstantPool constant_pool, final boolean verbose)
    '''
def compactClassName():
    '''    public static final String compactClassName(final String str)
    public static final String compactClassName(String str, final String prefix, final boolean chopit)
    public static final String compactClassName(final String str, final boolean chopit)
    '''
def methodSignatureToString():
    '''    public static final String methodSignatureToString(final String signature, final String name, final String access)
    public static final String methodSignatureToString(final String signature, final String name, final String access, final boolean chopit)
    public static final String methodSignatureToString(final String signature, final String name, final String access, final boolean chopit, final LocalVariableTable vars)
    '''
def replace():
    '''    public static final String replace(String str, final String old, final String new_)
    '''
def signatureToString():
    '''    public static final String signatureToString(final String signature)
    public static final String signatureToString(final String signature, final boolean chopit)
    '''
def signatureToStringInternal():
    '''    public static final ResultHolder signatureToStringInternal(final String signature, final boolean chopit)
    '''
def typeOfMethodSignature():
    '''    public static final byte typeOfMethodSignature(final String signature)
    '''
def toHexString():
    '''    public static final String toHexString(final byte[] bytes)
    '''
def format():
    '''    public static final String format(final int i, final int length, final boolean left_justify, final char fill)
    '''
def fillup():
    '''    public static final String fillup(final String str, final int length, final boolean left_justify, final char fill)
    '''
def convertString():
    '''    public static final String convertString(final String label)
    '''
def getAnnotationAttributes():
    '''    public static Collection<RuntimeAnnos> getAnnotationAttributes(final ConstantPool cp, final List<AnnotationGen> annotations)
    '''
def getParameterAnnotationAttributes():
    '''    public static Attribute[] getParameterAnnotationAttributes(final ConstantPool cp, final List<AnnotationGen>[] vec)
    '''
def typeOfSignature():
    '''    public static final byte typeOfSignature(final String signature)
    public static final byte typeOfSignature(final char c)
    '''
def toMethodSignature():
    '''    public static String toMethodSignature(final Type returnType, final Type[] argTypes)
    '''
def ResultHolder():
    '''    public ResultHolder(final String s, final int c)
    '''
def getResult():
    '''    public String getResult()
    '''
def getConsumedChars():
    '''    public int getConsumedChars()
    '''
