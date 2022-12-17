BATCH_BUILD = "int  0"
INCREMENTAL_BUILD = "int  1"
PROCESSING_COMPILATION_UNIT = "int  2"
RESOLVING_COMPILATION_UNIT = "int  3"
ANALYSING_COMPILATION_UNIT = "int  4"
GENERATING_UNWOVEN_CODE_FOR_COMPILATION_UNIT = "int  5"
COMPLETING_TYPE_BINDINGS = "int  6"
PROCESSING_DECLARE_PARENTS = "int  7"
CHECK_AND_SET_IMPORTS = "int  8"
CONNECTING_TYPE_HIERARCHY = "int  9"
BUILDING_FIELDS_AND_METHODS = "int  10"
COLLECTING_ITDS_AND_DECLARES = "int  11"
PROCESSING_DECLARE_ANNOTATIONS = "int  12"
WEAVING_INTERTYPE_DECLARATIONS = "int  13"
RESOLVING_POINTCUT_DECLARATIONS = "int  14"
ADDING_DECLARE_WARNINGS_AND_ERRORS = "int  15"
VALIDATING_AT_ASPECTJ_ANNOTATIONS = "int  16"
ACCESS_FOR_INLINE = "int  17"
ADDING_AT_ASPECTJ_ANNOTATIONS = "int  18"
FIXING_SUPER_CALLS_IN_ITDS = "int  19"
FIXING_SUPER_CALLS = "int  20"
OPTIMIZING_THIS_JOIN_POINT_CALLS = "int  21"
WEAVING = "int  22"
PROCESSING_REWEAVABLE_STATE = "int  23"
PROCESSING_TYPE_MUNGERS = "int  24"
WEAVING_ASPECTS = "int  25"
WEAVING_CLASSES = "int  26"
WEAVING_TYPE = "int  27"
MATCHING_SHADOW = "int  28"
IMPLEMENTING_ON_SHADOW = "int  29"
MATCHING_POINTCUT = "int  30"
MUNGING_WITH = "int  31"
PROCESSING_ATASPECTJTYPE_MUNGERS_ONLY = "int  32"
def ():
    '''returns ContextStackEntry\n\n
    (final int id)\n
    (final ContextTokenImpl ct, final int phase, final WeakReference<Object> data)\n
    '''
def getData():
    '''returns Object\n\n
    getData()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def formatEntry():
    '''returns String\n\n
    formatEntry(final int phaseId, final Object data)\n
    '''
