INNERCLASSES = "int  0"
ENUM_CONSTANTS = "int  1"
FIELDS = "int  2"
CONSTRUCTORS = "int  3"
METHODS = "int  4"
ANNOTATION_TYPE_FIELDS = "int  5"
ANNOTATION_TYPE_MEMBER_OPTIONAL = "int  6"
ANNOTATION_TYPE_MEMBER_REQUIRED = "int  7"
PROPERTIES = "int  8"
NUM_MEMBER_TYPES = "int  9"
STARTLEVEL = "String  \"start\""
def ():
    '''returns GetterSetter\n\n
    (final ClassDoc classdoc, final int kind, final Configuration configuration)\n
    (final ProgramElementDoc programElementDoc)\n
    (final ProgramElementDoc getter, final ProgramElementDoc setter)\n
    '''
def getVisibleClassesList():
    '''returns List<ClassDoc>\n\n
    getVisibleClassesList()\n
    '''
def getPropertyMemberDoc():
    '''returns ProgramElementDoc\n\n
    getPropertyMemberDoc(final ProgramElementDoc programElementDoc)\n
    '''
def getGetterForProperty():
    '''returns ProgramElementDoc\n\n
    getGetterForProperty(final ProgramElementDoc programElementDoc)\n
    '''
def getSetterForProperty():
    '''returns ProgramElementDoc\n\n
    getSetterForProperty(final ProgramElementDoc programElementDoc)\n
    '''
def getLeafClassMembers():
    '''returns List<ProgramElementDoc>\n\n
    getLeafClassMembers(final Configuration configuration)\n
    '''
def getMembersFor():
    '''returns List<ProgramElementDoc>\n\n
    getMembersFor(final ClassDoc classDoc)\n
    '''
def noVisibleMembers():
    '''returns boolean\n\n
    noVisibleMembers()\n
    '''
def addMember():
    '''returns None\n\n
    addMember(final ProgramElementDoc programElementDoc)\n
    '''
def isEqual():
    '''returns boolean\n\n
    isEqual(final MethodDoc methodDoc)\n
    '''
def getMembers():
    '''returns List<ProgramElementDoc>\n\n
    getMembers()\n
    '''
def getGetter():
    '''returns ProgramElementDoc\n\n
    getGetter()\n
    '''
def getSetter():
    '''returns ProgramElementDoc\n\n
    getSetter()\n
    '''
