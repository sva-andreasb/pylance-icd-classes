def ():
    '''returns SkinnyMethodAdapter\n\n
    (final ClassVisitor cv, final int flags, final String name, final String signature, final String something, final String[] exceptions)\n
    '''
def getMethodVisitor():
    '''returns MethodVisitor\n\n
    getMethodVisitor()\n
    '''
def setMethodVisitor():
    '''returns None\n\n
    setMethodVisitor(final MethodVisitor mv)\n
    '''
def aload():
    '''returns None\n\n
    aload(final int arg0)\n
    aload(final LocalVariable arg0)\n
    aload(final int... args)\n
    aload(final LocalVariable... args)\n
    '''
def iload():
    '''returns None\n\n
    iload(final int arg0)\n
    iload(final LocalVariable arg0)\n
    iload(final int... args)\n
    iload(final LocalVariable... args)\n
    '''
def lload():
    '''returns None\n\n
    lload(final int arg0)\n
    lload(final int... args)\n
    lload(final LocalVariable... args)\n
    '''
def fload():
    '''returns None\n\n
    fload(final int arg0)\n
    fload(final LocalVariable arg0)\n
    fload(final int... args)\n
    '''
def dload():
    '''returns None\n\n
    dload(final LocalVariable arg0)\n
    dload(final int arg0)\n
    dload(final int... args)\n
    '''
def astore():
    '''returns None\n\n
    astore(final int arg0)\n
    astore(final LocalVariable arg0)\n
    '''
def istore():
    '''returns None\n\n
    istore(final int arg0)\n
    istore(final LocalVariable arg0)\n
    '''
def lstore():
    '''returns None\n\n
    lstore(final int arg0)\n
    lstore(final LocalVariable arg0)\n
    '''
def fstore():
    '''returns None\n\n
    fstore(final int arg0)\n
    fstore(final LocalVariable arg0)\n
    '''
def dstore():
    '''returns None\n\n
    dstore(final int arg0)\n
    dstore(final LocalVariable arg0)\n
    '''
def ldc():
    '''returns None\n\n
    ldc(final Object arg0)\n
    '''
def bipush():
    '''returns None\n\n
    bipush(final int arg)\n
    '''
def sipush():
    '''returns None\n\n
    sipush(final int arg)\n
    '''
def pushInt():
    '''returns None\n\n
    pushInt(final int value)\n
    '''
def pushBoolean():
    '''returns None\n\n
    pushBoolean(final boolean bool)\n
    '''
def invokestatic():
    '''returns None\n\n
    invokestatic(final String arg1, final String arg2, final String arg3)\n
    invokestatic(final Class recv, final String methodName, final Class returnType, final Class... parameterTypes)\n
    '''
def invokespecial():
    '''returns None\n\n
    invokespecial(final String arg1, final String arg2, final String arg3)\n
    invokespecial(final Class recv, final String methodName, final Class returnType, final Class... parameterTypes)\n
    '''
def invokevirtual():
    '''returns None\n\n
    invokevirtual(final String arg1, final String arg2, final String arg3)\n
    invokevirtual(final Class recv, final String methodName, final Class returnType, final Class... parameterTypes)\n
    '''
def invokeinterface():
    '''returns None\n\n
    invokeinterface(final String arg1, final String arg2, final String arg3)\n
    invokeinterface(final Class recv, final String methodName, final Class returnType, final Class... parameterTypes)\n
    '''
def invokedynamic():
    '''returns None\n\n
    invokedynamic(final String arg1, final String arg2, final String arg3)\n
    '''
def aprintln():
    '''returns None\n\n
    aprintln()\n
    '''
def areturn():
    '''returns None\n\n
    areturn()\n
    '''
def ireturn():
    '''returns None\n\n
    ireturn()\n
    '''
def freturn():
    '''returns None\n\n
    freturn()\n
    '''
def lreturn():
    '''returns None\n\n
    lreturn()\n
    '''
def dreturn():
    '''returns None\n\n
    dreturn()\n
    '''
def newobj():
    '''returns None\n\n
    newobj(final String arg0)\n
    '''
def dup():
    '''returns None\n\n
    dup()\n
    '''
def swap():
    '''returns None\n\n
    swap()\n
    '''
def swap2():
    '''returns None\n\n
    swap2()\n
    '''
def getstatic():
    '''returns None\n\n
    getstatic(final String arg1, final String arg2, final String arg3)\n
    '''
def putstatic():
    '''returns None\n\n
    putstatic(final String arg1, final String arg2, final String arg3)\n
    '''
def getfield():
    '''returns None\n\n
    getfield(final String arg1, final String arg2, final String arg3)\n
    '''
def putfield():
    '''returns None\n\n
    putfield(final String arg1, final String arg2, final String arg3)\n
    '''
def voidreturn():
    '''returns None\n\n
    voidreturn()\n
    '''
def anewarray():
    '''returns None\n\n
    anewarray(final String arg0)\n
    '''
def multianewarray():
    '''returns None\n\n
    multianewarray(final String arg0, final int dims)\n
    '''
def newarray():
    '''returns None\n\n
    newarray(final int arg0)\n
    '''
def iconst_m1():
    '''returns None\n\n
    iconst_m1()\n
    '''
def iconst_0():
    '''returns None\n\n
    iconst_0()\n
    '''
def iconst_1():
    '''returns None\n\n
    iconst_1()\n
    '''
def iconst_2():
    '''returns None\n\n
    iconst_2()\n
    '''
def iconst_3():
    '''returns None\n\n
    iconst_3()\n
    '''
def iconst_4():
    '''returns None\n\n
    iconst_4()\n
    '''
def iconst_5():
    '''returns None\n\n
    iconst_5()\n
    '''
def lconst_0():
    '''returns None\n\n
    lconst_0()\n
    '''
def aconst_null():
    '''returns None\n\n
    aconst_null()\n
    '''
def label():
    '''returns None\n\n
    label(final Label label)\n
    '''
def nop():
    '''returns None\n\n
    nop()\n
    '''
def pop():
    '''returns None\n\n
    pop()\n
    '''
def pop2():
    '''returns None\n\n
    pop2()\n
    '''
def arrayload():
    '''returns None\n\n
    arrayload()\n
    '''
def arraystore():
    '''returns None\n\n
    arraystore()\n
    '''
def iarrayload():
    '''returns None\n\n
    iarrayload()\n
    '''
def barrayload():
    '''returns None\n\n
    barrayload()\n
    '''
def barraystore():
    '''returns None\n\n
    barraystore()\n
    '''
def aaload():
    '''returns None\n\n
    aaload()\n
    '''
def aastore():
    '''returns None\n\n
    aastore()\n
    '''
def iaload():
    '''returns None\n\n
    iaload()\n
    '''
def iastore():
    '''returns None\n\n
    iastore()\n
    '''
def laload():
    '''returns None\n\n
    laload()\n
    '''
def lastore():
    '''returns None\n\n
    lastore()\n
    '''
def baload():
    '''returns None\n\n
    baload()\n
    '''
def bastore():
    '''returns None\n\n
    bastore()\n
    '''
def saload():
    '''returns None\n\n
    saload()\n
    '''
def sastore():
    '''returns None\n\n
    sastore()\n
    '''
def caload():
    '''returns None\n\n
    caload()\n
    '''
def castore():
    '''returns None\n\n
    castore()\n
    '''
def faload():
    '''returns None\n\n
    faload()\n
    '''
def fastore():
    '''returns None\n\n
    fastore()\n
    '''
def daload():
    '''returns None\n\n
    daload()\n
    '''
def dastore():
    '''returns None\n\n
    dastore()\n
    '''
def fcmpl():
    '''returns None\n\n
    fcmpl()\n
    '''
def fcmpg():
    '''returns None\n\n
    fcmpg()\n
    '''
def dcmpl():
    '''returns None\n\n
    dcmpl()\n
    '''
def dcmpg():
    '''returns None\n\n
    dcmpg()\n
    '''
def dup_x2():
    '''returns None\n\n
    dup_x2()\n
    '''
def dup_x1():
    '''returns None\n\n
    dup_x1()\n
    '''
def dup2_x2():
    '''returns None\n\n
    dup2_x2()\n
    '''
def dup2_x1():
    '''returns None\n\n
    dup2_x1()\n
    '''
def dup2():
    '''returns None\n\n
    dup2()\n
    '''
def trycatch():
    '''returns None\n\n
    trycatch(final Label arg0, final Label arg1, final Label arg2, final String arg3)\n
    trycatch(final String type, final Runnable body, final Runnable catchBody)\n
    '''
def go_to():
    '''returns None\n\n
    go_to(final Label arg0)\n
    '''
def lookupswitch():
    '''returns None\n\n
    lookupswitch(final Label arg0, final int[] arg1, final Label[] arg2)\n
    '''
def athrow():
    '''returns None\n\n
    athrow()\n
    '''
def instance_of():
    '''returns None\n\n
    instance_of(final String arg0)\n
    '''
def ifeq():
    '''returns None\n\n
    ifeq(final Label arg0)\n
    '''
def iffalse():
    '''returns None\n\n
    iffalse(final Label arg0)\n
    '''
def ifne():
    '''returns None\n\n
    ifne(final Label arg0)\n
    '''
def iftrue():
    '''returns None\n\n
    iftrue(final Label arg0)\n
    '''
def if_acmpne():
    '''returns None\n\n
    if_acmpne(final Label arg0)\n
    '''
def if_acmpeq():
    '''returns None\n\n
    if_acmpeq(final Label arg0)\n
    '''
def if_icmple():
    '''returns None\n\n
    if_icmple(final Label arg0)\n
    '''
def if_icmpgt():
    '''returns None\n\n
    if_icmpgt(final Label arg0)\n
    '''
def if_icmpge():
    '''returns None\n\n
    if_icmpge(final Label arg0)\n
    '''
def if_icmplt():
    '''returns None\n\n
    if_icmplt(final Label arg0)\n
    '''
def if_icmpne():
    '''returns None\n\n
    if_icmpne(final Label arg0)\n
    '''
def if_icmpeq():
    '''returns None\n\n
    if_icmpeq(final Label arg0)\n
    '''
def checkcast():
    '''returns None\n\n
    checkcast(final String arg0)\n
    checkcast(final Class clazz)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def line():
    '''returns None\n\n
    line(final int line)\n
    line(final int line, final Label label)\n
    '''
def ifnonnull():
    '''returns None\n\n
    ifnonnull(final Label arg0)\n
    '''
def ifnull():
    '''returns None\n\n
    ifnull(final Label arg0)\n
    '''
def iflt():
    '''returns None\n\n
    iflt(final Label arg0)\n
    '''
def ifle():
    '''returns None\n\n
    ifle(final Label arg0)\n
    '''
def ifgt():
    '''returns None\n\n
    ifgt(final Label arg0)\n
    '''
def ifge():
    '''returns None\n\n
    ifge(final Label arg0)\n
    '''
def arraylength():
    '''returns None\n\n
    arraylength()\n
    '''
def ishr():
    '''returns None\n\n
    ishr()\n
    '''
def ishl():
    '''returns None\n\n
    ishl()\n
    '''
def iushr():
    '''returns None\n\n
    iushr()\n
    '''
def lshr():
    '''returns None\n\n
    lshr()\n
    '''
def lshl():
    '''returns None\n\n
    lshl()\n
    '''
def lushr():
    '''returns None\n\n
    lushr()\n
    '''
def lcmp():
    '''returns None\n\n
    lcmp()\n
    '''
def iand():
    '''returns None\n\n
    iand()\n
    '''
def ior():
    '''returns None\n\n
    ior()\n
    '''
def ixor():
    '''returns None\n\n
    ixor()\n
    '''
def land():
    '''returns None\n\n
    land()\n
    '''
def lor():
    '''returns None\n\n
    lor()\n
    '''
def lxor():
    '''returns None\n\n
    lxor()\n
    '''
def iadd():
    '''returns None\n\n
    iadd()\n
    '''
def ladd():
    '''returns None\n\n
    ladd()\n
    '''
def fadd():
    '''returns None\n\n
    fadd()\n
    '''
def dadd():
    '''returns None\n\n
    dadd()\n
    '''
def isub():
    '''returns None\n\n
    isub()\n
    '''
def lsub():
    '''returns None\n\n
    lsub()\n
    '''
def fsub():
    '''returns None\n\n
    fsub()\n
    '''
def dsub():
    '''returns None\n\n
    dsub()\n
    '''
def idiv():
    '''returns None\n\n
    idiv()\n
    '''
def irem():
    '''returns None\n\n
    irem()\n
    '''
def ineg():
    '''returns None\n\n
    ineg()\n
    '''
def i2d():
    '''returns None\n\n
    i2d()\n
    '''
def i2l():
    '''returns None\n\n
    i2l()\n
    '''
def i2f():
    '''returns None\n\n
    i2f()\n
    '''
def i2s():
    '''returns None\n\n
    i2s()\n
    '''
def i2c():
    '''returns None\n\n
    i2c()\n
    '''
def i2b():
    '''returns None\n\n
    i2b()\n
    '''
def ldiv():
    '''returns None\n\n
    ldiv()\n
    '''
def lrem():
    '''returns None\n\n
    lrem()\n
    '''
def lneg():
    '''returns None\n\n
    lneg()\n
    '''
def l2d():
    '''returns None\n\n
    l2d()\n
    '''
def l2i():
    '''returns None\n\n
    l2i()\n
    '''
def l2f():
    '''returns None\n\n
    l2f()\n
    '''
def fdiv():
    '''returns None\n\n
    fdiv()\n
    '''
def frem():
    '''returns None\n\n
    frem()\n
    '''
def fneg():
    '''returns None\n\n
    fneg()\n
    '''
def f2d():
    '''returns None\n\n
    f2d()\n
    '''
def f2i():
    '''returns None\n\n
    f2i()\n
    '''
def f2l():
    '''returns None\n\n
    f2l()\n
    '''
def ddiv():
    '''returns None\n\n
    ddiv()\n
    '''
def drem():
    '''returns None\n\n
    drem()\n
    '''
def dneg():
    '''returns None\n\n
    dneg()\n
    '''
def d2f():
    '''returns None\n\n
    d2f()\n
    '''
def d2i():
    '''returns None\n\n
    d2i()\n
    '''
def d2l():
    '''returns None\n\n
    d2l()\n
    '''
def imul():
    '''returns None\n\n
    imul()\n
    '''
def lmul():
    '''returns None\n\n
    lmul()\n
    '''
def fmul():
    '''returns None\n\n
    fmul()\n
    '''
def dmul():
    '''returns None\n\n
    dmul()\n
    '''
def iinc():
    '''returns None\n\n
    iinc(final int arg0, final int arg1)\n
    iinc(final LocalVariable arg0, final int arg1)\n
    '''
def monitorenter():
    '''returns None\n\n
    monitorenter()\n
    '''
def monitorexit():
    '''returns None\n\n
    monitorexit()\n
    '''
def jsr():
    '''returns None\n\n
    jsr(final Label branch)\n
    '''
def ret():
    '''returns None\n\n
    ret(final int arg0)\n
    '''
def visitAnnotationDefault():
    '''returns AnnotationVisitor\n\n
    visitAnnotationDefault()\n
    '''
def visitAnnotation():
    '''returns AnnotationVisitor\n\n
    visitAnnotation(final String arg0, final boolean arg1)\n
    '''
def visitParameterAnnotation():
    '''returns AnnotationVisitor\n\n
    visitParameterAnnotation(final int arg0, final String arg1, final boolean arg2)\n
    '''
def visitAnnotationWithFields():
    '''returns None\n\n
    visitAnnotationWithFields(final String name, final boolean visible, final Map<String, Object> fields)\n
    '''
def visitParameterAnnotationWithFields():
    '''returns None\n\n
    visitParameterAnnotationWithFields(final int param, final String name, final boolean visible, final Map<String, Object> fields)\n
    '''
def visitAttribute():
    '''returns None\n\n
    visitAttribute(final Attribute arg0)\n
    '''
def visitCode():
    '''returns None\n\n
    visitCode()\n
    '''
def visitInsn():
    '''returns None\n\n
    visitInsn(final int arg0)\n
    '''
def visitIntInsn():
    '''returns None\n\n
    visitIntInsn(final int arg0, final int arg1)\n
    '''
def visitVarInsn():
    '''returns None\n\n
    visitVarInsn(final int arg0, final int arg1)\n
    '''
def visitTypeInsn():
    '''returns None\n\n
    visitTypeInsn(final int arg0, final String arg1)\n
    '''
def visitFieldInsn():
    '''returns None\n\n
    visitFieldInsn(final int arg0, final String arg1, final String arg2, final String arg3)\n
    '''
def visitMethodInsn():
    '''returns None\n\n
    visitMethodInsn(final int arg0, final String arg1, final String arg2, final String arg3)\n
    '''
def visitJumpInsn():
    '''returns None\n\n
    visitJumpInsn(final int arg0, final Label arg1)\n
    '''
def visitLabel():
    '''returns None\n\n
    visitLabel(final Label arg0)\n
    '''
def visitLdcInsn():
    '''returns None\n\n
    visitLdcInsn(final Object arg0)\n
    '''
def visitIincInsn():
    '''returns None\n\n
    visitIincInsn(final int arg0, final int arg1)\n
    '''
def visitTableSwitchInsn():
    '''returns None\n\n
    visitTableSwitchInsn(final int arg0, final int arg1, final Label arg2, final Label[] arg3)\n
    '''
def visitLookupSwitchInsn():
    '''returns None\n\n
    visitLookupSwitchInsn(final Label arg0, final int[] arg1, final Label[] arg2)\n
    '''
def visitMultiANewArrayInsn():
    '''returns None\n\n
    visitMultiANewArrayInsn(final String arg0, final int arg1)\n
    '''
def visitTryCatchBlock():
    '''returns None\n\n
    visitTryCatchBlock(final Label arg0, final Label arg1, final Label arg2, final String arg3)\n
    '''
def visitLocalVariable():
    '''returns None\n\n
    visitLocalVariable(final String arg0, final String arg1, final String arg2, final Label arg3, final Label arg4, final int arg5)\n
    '''
def visitLineNumber():
    '''returns None\n\n
    visitLineNumber(final int arg0, final Label arg1)\n
    '''
def visitMaxs():
    '''returns None\n\n
    visitMaxs(final int arg0, final int arg1)\n
    '''
def visitEnd():
    '''returns None\n\n
    visitEnd()\n
    '''
def tableswitch():
    '''returns None\n\n
    tableswitch(final int min, final int max, final Label defaultLabel, final Label[] cases)\n
    '''
def visitFrame():
    '''returns None\n\n
    visitFrame(final int arg0, final int arg1, final Object[] arg2, final int arg3, final Object[] arg4)\n
    '''
