def library():
    '''returns LibraryLoader<T>\n\n
    library(final String libraryName)\n
    '''
def search():
    '''returns LibraryLoader<T>\n\n
    search(final String path)\n
    '''
def option():
    '''returns LibraryLoader<T>\n\n
    option(final LibraryOption option, final Object value)\n
    '''
def mapper():
    '''returns LibraryLoader<T>\n\n
    mapper(final TypeMapper typeMapper)\n
    mapper(final SignatureTypeMapper typeMapper)\n
    mapper(final FunctionMapper functionMapper)\n
    '''
def map():
    '''returns LibraryLoader<T>\n\n
    map(final String javaName, final String nativeFunction)\n
    '''
def convention():
    '''returns LibraryLoader<T>\n\n
    convention(final CallingConvention convention)\n
    '''
def load():
    '''returns T\n\n
    load(final String libraryName)\n
    load()\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final Object proxy, final Method method, final Object[] args)\n
    '''
