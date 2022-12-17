def ():
    '''returns PatternParser\n\n
    (final ITokenSource tokenSource)\n
    (final String data)\n
    (final String data, final ISourceContext context)\n
    '''
def setPointcutDesignatorHandlers():
    '''returns None\n\n
    setPointcutDesignatorHandlers(final Set<PointcutDesignatorHandler> handlers, final World world)\n
    '''
def maybeParsePerClause():
    '''returns PerClause\n\n
    maybeParsePerClause()\n
    '''
def parseDeclare():
    '''returns Declare\n\n
    parseDeclare()\n
    '''
def parseDeclareAnnotation():
    '''returns Declare\n\n
    parseDeclareAnnotation()\n
    '''
def parseDeclareAtType():
    '''returns DeclareAnnotation\n\n
    parseDeclareAtType()\n
    '''
def parseDeclareAtMethod():
    '''returns DeclareAnnotation\n\n
    parseDeclareAtMethod(final boolean isMethod)\n
    '''
def parseDeclareAtField():
    '''returns DeclareAnnotation\n\n
    parseDeclareAtField()\n
    '''
def parseCompoundFieldSignaturePattern():
    '''returns ISignaturePattern\n\n
    parseCompoundFieldSignaturePattern()\n
    '''
def parseCompoundMethodOrConstructorSignaturePattern():
    '''returns ISignaturePattern\n\n
    parseCompoundMethodOrConstructorSignaturePattern(final boolean isMethod)\n
    '''
def parseDominates():
    '''returns DeclarePrecedence\n\n
    parseDominates()\n
    '''
def parsePointcut():
    '''returns Pointcut\n\n
    parsePointcut()\n
    '''
def parseSinglePointcut():
    '''returns Pointcut\n\n
    parseSinglePointcut()\n
    '''
def parseAnnotationPointcut():
    '''returns Pointcut\n\n
    parseAnnotationPointcut()\n
    '''
def parseDottedIdentifier():
    '''returns List<String>\n\n
    parseDottedIdentifier()\n
    '''
def parseTypePattern():
    '''returns TypePattern\n\n
    parseTypePattern()\n
    parseTypePattern(final boolean insideTypeParameters, final boolean parameterAnnotationsPossible)\n
    '''
def maybeParseAnnotationPattern():
    '''returns AnnotationTypePattern\n\n
    maybeParseAnnotationPattern()\n
    '''
def maybeParseSingleAnnotationPattern():
    '''returns AnnotationTypePattern\n\n
    maybeParseSingleAnnotationPattern()\n
    '''
def parseSingleTypePattern():
    '''returns TypePattern\n\n
    parseSingleTypePattern()\n
    parseSingleTypePattern(final boolean insideTypeParameters)\n
    '''
def parseHasMethodTypePattern():
    '''returns TypePattern\n\n
    parseHasMethodTypePattern()\n
    '''
def parseIsTypePattern():
    '''returns TypePattern\n\n
    parseIsTypePattern()\n
    '''
def parseHasFieldTypePattern():
    '''returns TypePattern\n\n
    parseHasFieldTypePattern()\n
    '''
def parseGenericsWildcardTypePattern():
    '''returns TypePattern\n\n
    parseGenericsWildcardTypePattern()\n
    '''
def parseDottedNamePattern():
    '''returns List<NamePattern>\n\n
    parseDottedNamePattern()\n
    '''
def parseAnnotationNameValuePattern():
    '''returns String\n\n
    parseAnnotationNameValuePattern()\n
    '''
def parseNamePattern():
    '''returns NamePattern\n\n
    parseNamePattern()\n
    '''
def parseModifiersPattern():
    '''returns ModifiersPattern\n\n
    parseModifiersPattern()\n
    '''
def parseArgumentsPattern():
    '''returns TypePatternList\n\n
    parseArgumentsPattern(final boolean parameterAnnotationsPossible)\n
    '''
def parseArgumentsAnnotationPattern():
    '''returns AnnotationPatternList\n\n
    parseArgumentsAnnotationPattern()\n
    '''
def parseOptionalThrowsPattern():
    '''returns ThrowsPattern\n\n
    parseOptionalThrowsPattern()\n
    '''
def parseMethodOrConstructorSignaturePattern():
    '''returns SignaturePattern\n\n
    parseMethodOrConstructorSignaturePattern()\n
    '''
def parseMaybeParenthesizedFieldSignaturePattern():
    '''returns ISignaturePattern\n\n
    parseMaybeParenthesizedFieldSignaturePattern()\n
    '''
def parseMaybeParenthesizedMethodOrConstructorSignaturePattern():
    '''returns ISignaturePattern\n\n
    parseMaybeParenthesizedMethodOrConstructorSignaturePattern(final boolean isMethod)\n
    '''
def parseFieldSignaturePattern():
    '''returns SignaturePattern\n\n
    parseFieldSignaturePattern()\n
    '''
def maybeParseTypeVariableList():
    '''returns TypeVariablePatternList\n\n
    maybeParseTypeVariableList()\n
    '''
def maybeParseSimpleTypeVariableList():
    '''returns String[]\n\n
    maybeParseSimpleTypeVariableList()\n
    '''
def maybeParseTypeParameterList():
    '''returns TypePatternList\n\n
    maybeParseTypeParameterList()\n
    '''
def parseTypeVariable():
    '''returns TypeVariablePattern\n\n
    parseTypeVariable()\n
    '''
def parsePossibleStringSequence():
    '''returns String\n\n
    parsePossibleStringSequence(final boolean shouldEnd)\n
    '''
def parseStringLiteral():
    '''returns String\n\n
    parseStringLiteral()\n
    '''
def parseIdentifier():
    '''returns String\n\n
    parseIdentifier()\n
    '''
def eatIdentifier():
    '''returns None\n\n
    eatIdentifier(final String expectedValue)\n
    '''
def maybeEatIdentifier():
    '''returns String\n\n
    maybeEatIdentifier(final String expectedValue)\n
    maybeEatIdentifier()\n
    '''
def eat():
    '''returns None\n\n
    eat(final String expectedValue)\n
    '''
def maybeEatAdjacent():
    '''returns boolean\n\n
    maybeEatAdjacent(final String token)\n
    '''
def maybeEat():
    '''returns boolean\n\n
    maybeEat(final String token)\n
    '''
def peek():
    '''returns boolean\n\n
    peek(final String token)\n
    '''
def checkEof():
    '''returns None\n\n
    checkEof()\n
    '''
