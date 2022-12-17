COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomServiceImpl\n\n
    (final IloApplicationContext applicationContext)\n
    '''
def registerModelInitializer():
    '''returns None\n\n
    registerModelInitializer(final String scope, final IloDomServiceModelInitializer initializer)\n
    '''
def unregisterModelInitializer():
    '''returns None\n\n
    unregisterModelInitializer(final String scope, final IloDomServiceModelInitializer initializer)\n
    '''
def getModelInitializers():
    '''returns List<IloDomServiceModelInitializer>\n\n
    getModelInitializers(final String scope)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final String scope, final IloDomModelManager<?> modelManager)\n
    '''
