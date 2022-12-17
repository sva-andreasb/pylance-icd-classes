CLIENT_USER = "int  0"
CLIENT_WORKSTATION = "int  1"
CLIENT_APPLICATION = "int  2"
CLIENT_ACCOUNTING = "int  3"
def ():
    '''returns DataBeanTransactionExecution\n\n
    ()\n
    '''
def addStatementExecution():
    '''returns None\n\n
    addStatementExecution(final DataBeanStatementExecution dataBeanStatementExecution)\n
    '''
def transactionStarted():
    '''returns boolean\n\n
    transactionStarted()\n
    '''
def beginTransaction():
    '''returns None\n\n
    beginTransaction()\n
    '''
def completeTransaction():
    '''returns None\n\n
    completeTransaction(final boolean isCompleted_)\n
    '''
def cloneForInflight():
    '''returns DataBeanTransactionExecution\n\n
    cloneForInflight()\n
    '''
def prepareForAggregation():
    '''returns None\n\n
    prepareForAggregation()\n
    '''
def aggregateInflight():
    '''returns None\n\n
    aggregateInflight(final DataBeanTransactionExecution dataBeanTransactionExecution)\n
    '''
def aggregate():
    '''returns None\n\n
    aggregate(final DataBeanTransactionExecution dataBeanTransactionExecution)\n
    '''
def toJSON_DSM():
    '''returns JSONArray\n\n
    toJSON_DSM()\n
    '''
def toJSONv1():
    '''returns JSONArray\n\n
    toJSONv1()\n
    '''
def toJSONv2():
    '''returns JSONArray\n\n
    toJSONv2()\n
    '''
def toJSONv3():
    '''returns JSONArray\n\n
    toJSONv3()\n
    '''
def toJSONv4():
    '''returns JSONArray\n\n
    toJSONv4()\n
    '''
def toJSONv5():
    '''returns JSONArray\n\n
    toJSONv5()\n
    '''
def toJSON():
    '''returns JSONArray\n\n
    toJSON(final int n)\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    '''
def getClientInfoString():
    '''returns String\n\n
    getClientInfoString()\n
    '''
def getEUOWClientInfoString():
    '''returns String\n\n
    getEUOWClientInfoString()\n
    '''
def getEUOWSettingsString():
    '''returns String\n\n
    getEUOWSettingsString()\n
    '''
def setDb2PackagePath():
    '''returns None\n\n
    setDb2PackagePath(final String db2PackagePath_)\n
    '''
