XMSGS_OPTION = "String  \"-Xmsgs\""
XMSGS_CUSTOM_PREFIX = "String  \"-Xmsgs:\""
XIMPLICIT_HEADERS = "String  \"-XimplicitHeaders:\""
XCUSTOM_TAGS_PREFIX = "String  \"-XcustomTags:\""
TAGS_SEPARATOR = "String  \",\""
def ():
    '''returns DocLint\n\n
    ()\n
    '''
def run():
    '''returns None\n\n
    run(final String... array)\n
    run(final PrintWriter printWriter, final String... array)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def init():
    '''returns None\n\n
    init(final JavacTask javacTask, final String... array)\n
    init(final JavacTask javacTask, final String[] array, final boolean b)\n
    '''
def started():
    '''returns None\n\n
    started(final TaskEvent taskEvent)\n
    '''
def finished():
    '''returns None\n\n
    finished(final TaskEvent taskEvent)\n
    '''
def scan():
    '''returns None\n\n
    scan(final TreePath treePath)\n
    '''
def reportStats():
    '''returns None\n\n
    reportStats(final PrintWriter printWriter)\n
    '''
def visitCompilationUnit():
    '''returns Void\n\n
    visitCompilationUnit(final CompilationUnitTree compilationUnitTree, final Void void1)\n
    '''
def visitClass():
    '''returns Void\n\n
    visitClass(final ClassTree classTree, final Void void1)\n
    '''
def visitMethod():
    '''returns Void\n\n
    visitMethod(final MethodTree methodTree, final Void void1)\n
    '''
def visitVariable():
    '''returns Void\n\n
    visitVariable(final VariableTree variableTree, final Void void1)\n
    '''
