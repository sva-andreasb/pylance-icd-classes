NAME = "String  \"IFACEPROC\""
def RulesCacheImpl():
    '''public RulesCacheImpl()
    '''
def init():
    '''public void init()
    '''
def reload():
    '''public void reload()
    public void reload(final String key)
    '''
def getName():
    '''public String getName()
    '''
def hasOutboundRules():
    '''public boolean hasOutboundRules(final String ifacename)
    public boolean hasOutboundRules(final String ifacename, final String mosname)
    '''
def hasInboundMboRules():
    '''public boolean hasInboundMboRules(final String ifacename)
    public boolean hasInboundMboRules(final String ifacename, final String mosname)
    '''
def hasInboundObjectRules():
    '''public boolean hasInboundObjectRules(final String ifacename)
    public boolean hasInboundObjectRules(final String ifacename, final String mosname)
    '''
def hasMigrationObjectRules():
    '''public boolean hasMigrationObjectRules(final String mosname)
    '''
def hasMigrationPackageRules():
    '''public boolean hasMigrationPackageRules(final String packageName)
    '''
def hasMigrationPackageRulesForObject():
    '''public boolean hasMigrationPackageRulesForObject(final String packageName, final String mosname)
    '''
def getTableProcsObjIn():
    '''public List getTableProcsObjIn(final String ifacename, final String mosname, final String hpath)
    '''
def getTableProcsMboIn():
    '''public List getTableProcsMboIn(final String ifacename, final String mosname, final String hpath)
    '''
def getTableProcsOut():
    '''public List getTableProcsOut(final String ifacename, final String mosname, final String hpath)
    '''
def getProcessingRules():
    '''public List getProcessingRules(final String useWith, final String entityName, final String objStructName, final String hpath)
    '''
def isAnyOutBoundRulesEnabled():
    '''public boolean isAnyOutBoundRulesEnabled(final String ifacename)
    '''
def isAnyInBoundMBORulesEnabled():
    '''public boolean isAnyInBoundMBORulesEnabled(final String ifacename)
    '''
def isAnyInBoundObjectRulesEnabled():
    '''public boolean isAnyInBoundObjectRulesEnabled(final String ifacename)
    '''
def refresh():
    '''public synchronized void refresh()
    '''
