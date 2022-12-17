def ():
    '''returns Factory\n\n
    (final String filename, final Class lexicalClass)\n
    '''
def makeMethodSig():
    '''returns MethodSignature\n\n
    makeMethodSig(final String stringRep)\n
    makeMethodSig(final String modifiers, final String methodName, final String declaringType, final String paramTypes, final String paramNames, final String exceptionTypes, final String returnType)\n
    makeMethodSig(final int modifiers, final String name, final Class declaringType, final Class[] parameterTypes, final String[] parameterNames, final Class[] exceptionTypes, final Class returnType)\n
    '''
def makeConstructorSig():
    '''returns ConstructorSignature\n\n
    makeConstructorSig(final String stringRep)\n
    makeConstructorSig(final String modifiers, final String declaringType, final String paramTypes, final String paramNames, final String exceptionTypes)\n
    makeConstructorSig(final int modifiers, final Class declaringType, final Class[] parameterTypes, final String[] parameterNames, final Class[] exceptionTypes)\n
    '''
def makeFieldSig():
    '''returns FieldSignature\n\n
    makeFieldSig(final String stringRep)\n
    makeFieldSig(final String modifiers, final String name, final String declaringType, final String fieldType)\n
    makeFieldSig(final int modifiers, final String name, final Class declaringType, final Class fieldType)\n
    '''
def makeAdviceSig():
    '''returns AdviceSignature\n\n
    makeAdviceSig(final String stringRep)\n
    makeAdviceSig(final String modifiers, final String name, final String declaringType, final String paramTypes, final String paramNames, final String exceptionTypes, final String returnType)\n
    makeAdviceSig(final int modifiers, final String name, final Class declaringType, final Class[] parameterTypes, final String[] parameterNames, final Class[] exceptionTypes, final Class returnType)\n
    '''
def makeInitializerSig():
    '''returns InitializerSignature\n\n
    makeInitializerSig(final String stringRep)\n
    makeInitializerSig(final String modifiers, final String declaringType)\n
    makeInitializerSig(final int modifiers, final Class declaringType)\n
    '''
def makeCatchClauseSig():
    '''returns CatchClauseSignature\n\n
    makeCatchClauseSig(final String stringRep)\n
    makeCatchClauseSig(final String declaringType, final String parameterType, final String parameterName)\n
    makeCatchClauseSig(final Class declaringType, final Class parameterType, final String parameterName)\n
    '''
def makeLockSig():
    '''returns LockSignature\n\n
    makeLockSig(final String stringRep)\n
    makeLockSig()\n
    makeLockSig(final Class declaringType)\n
    '''
def makeUnlockSig():
    '''returns UnlockSignature\n\n
    makeUnlockSig(final String stringRep)\n
    makeUnlockSig()\n
    makeUnlockSig(final Class declaringType)\n
    '''
def makeSourceLoc():
    '''returns SourceLocation\n\n
    makeSourceLoc(final int line, final int col)\n
    '''
