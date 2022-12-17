def ():
    '''returns JavaGeneratorFactory\n\n
    ()\n
    (final Emitter emitter)\n
    '''
def setEmitter():
    '''returns None\n\n
    setEmitter(final Emitter emitter)\n
    '''
def generatorPass():
    '''returns None\n\n
    generatorPass(final Definition def, final SymbolTable symbolTable)\n
    '''
def getGenerator():
    '''returns Generator\n\n
    getGenerator(final Message message, final SymbolTable symbolTable)\n
    getGenerator(final PortType portType, final SymbolTable symbolTable)\n
    getGenerator(final Binding binding, final SymbolTable symbolTable)\n
    getGenerator(final Service service, final SymbolTable symbolTable)\n
    getGenerator(final TypeEntry type, final SymbolTable symbolTable)\n
    getGenerator(final Definition definition, final SymbolTable symbolTable)\n
    '''
def addGenerator():
    '''returns None\n\n
    addGenerator(final Class wsdlClass, final Class generator)\n
    addGenerator(final Class writer)\n
    '''
def setBaseTypeMapping():
    '''returns None\n\n
    setBaseTypeMapping(final BaseTypeMapping btm)\n
    '''
def getBaseTypeMapping():
    '''returns BaseTypeMapping\n\n
    getBaseTypeMapping()\n
    '''
def getBaseName():
    '''returns String\n\n
    getBaseName(final QName qNameIn)\n
    '''
def addStuff():
    '''returns None\n\n
    addStuff(final Generator baseWriter, final SymTabEntry entry, final SymbolTable symbolTable)\n
    addStuff(final Generator baseWriter, final Definition def, final SymbolTable symbolTable)\n
    '''
def generate():
    '''returns None\n\n
    generate()\n
    '''
