def getName():
    '''returns String\n\n
    getName()\n
    '''
def hasOutboundRules():
    '''returns boolean\n\n
    hasOutboundRules(final String ifacename)\n
    hasOutboundRules(final String ifacename, final String mosname)\n
    '''
def hasInboundMboRules():
    '''returns boolean\n\n
    hasInboundMboRules(final String ifacename)\n
    hasInboundMboRules(final String ifacename, final String mosname)\n
    '''
def hasInboundObjectRules():
    '''returns boolean\n\n
    hasInboundObjectRules(final String ifacename)\n
    hasInboundObjectRules(final String ifacename, final String mosname)\n
    '''
def hasMigrationObjectRules():
    '''returns boolean\n\n
    hasMigrationObjectRules(final String mosname)\n
    '''
def hasMigrationPackageRules():
    '''returns boolean\n\n
    hasMigrationPackageRules(final String packageName)\n
    '''
def hasMigrationPackageRulesForObject():
    '''returns boolean\n\n
    hasMigrationPackageRulesForObject(final String packageName, final String mosname)\n
    '''
def getTableProcsObjIn():
    '''returns List\n\n
    getTableProcsObjIn(final String ifacename, final String mosname, final String hpath)\n
    '''
def getTableProcsMboIn():
    '''returns List\n\n
    getTableProcsMboIn(final String ifacename, final String mosname, final String hpath)\n
    '''
def getTableProcsOut():
    '''returns List\n\n
    getTableProcsOut(final String ifacename, final String mosname, final String hpath)\n
    '''
def getProcessingRules():
    '''returns List\n\n
    getProcessingRules(final String useWith, final String entityName, final String objStructName, final String hpath)\n
    '''
def isAnyOutBoundRulesEnabled():
    '''returns boolean\n\n
    isAnyOutBoundRulesEnabled(final String ifacename)\n
    '''
def isAnyInBoundMBORulesEnabled():
    '''returns boolean\n\n
    isAnyInBoundMBORulesEnabled(final String ifacename)\n
    '''
def isAnyInBoundObjectRulesEnabled():
    '''returns boolean\n\n
    isAnyInBoundObjectRulesEnabled(final String ifacename)\n
    '''
