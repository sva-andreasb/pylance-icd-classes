ADDITIONAL_PROCESSOR = "String  \"ADDITIONAL_PROCESSOR\""
APPLIANCE_INSTALL = "String  \"APPLIANCE_INSTALL\""
APPLICATION = "String  \"APPLICATION\""
APPLICATION_INSTANCE = "String  \"APPLICATION_INSTANCE\""
APPSERVER_CONNECTED = "String  \"APPSERVER_CONNECTED\""
ASSET = "String  \"ASSET\""
AUTHORIZED_USER = "String  \"AUTHORIZED_USER\""
AUTHORIZED_USER_SINGLE_INSTALL = "String  \"AUTHORIZED_USER_SINGLE_INSTALL\""
AUTHORIZED_USER_SINGLE_SESSION = "String  \"AUTHORIZED_USER_SINGLE_SESSION\""
BASE_PROCESSOR = "String  \"BASE_PROCESSOR\""
CLIENT = "String  \"CLIENT\""
CLIENT_DEVICE = "String  \"CLIENT_DEVICE\""
CLIENT_USER = "String  \"CLIENT_USER\""
CONCURRENT_SESSION = "String  \"CONCURRENT_SESSION\""
CONCURRENT_USER = "String  \"CONCURRENT_USER\""
CONNECTION = "String  \"CONNECTION\""
CONNECTOR = "String  \"CONNECTOR\""
CONNECTOR_FOR_DEMAND_SIDE = "String  \"CONNECTOR_FOR_DEMAND_SIDE\""
CONNECTOR_FOR_SUPPLY_SIDE = "String  \"CONNECTOR_FOR_SUPPLY_SIDE\""
CURRENCY_VALUE_UNIT = "String  \"CURRENCY_VALUE_UNIT\""
DECIMAL_TERABYTE = "String  \"DECIMAL_TERABYTE\""
DISK_DRIVE = "String  \"DISK_DRIVE\""
ELIGIBLE_PARTICIPANT = "String  \"ELIGIBLE_PARTICIPANT\""
ESTABLISHMENT = "String  \"ESTABLISHMENT\""
FEED = "String  \"FEED\""
FLOATING_CLIENT_DEVICE = "String  \"FLOATING_CLIENT_DEVICE\""
FLOATING_USER = "String  \"FLOATING_USER\""
FLOATING_USER_SESSION = "String  \"FLOATING_USER_SESSION\""
FLOATING_USER_SINGLE_INSTALL = "String  \"FLOATING_USER_SINGLE_INSTALL\""
FLOATING_USER_SINGLE_SESSION = "String  \"FLOATING_USER_SINGLE_SESSION\""
FLOATING_USER_SINGLE_SESSION_SINGLE_INSTALL = "String  \"FLOATING_USER_SINGLE_SESSION_SINGLE_INSTALL\""
GENERAL_PURPOSE_GRAPHICS_PROCESSING_UNIT = "String  \"GENERAL_PURPOSE_GRAPHICS_PROCESSING_UNIT\""
HOST_SERVER = "String  \"HOST_SERVER\""
HUNDRED_THOUSAND_SQUARE_METERS = "String  \"HUNDRED_THOUSAND_SQUARE_METERS\""
IDLE_STANDBY_SERVER = "String  \"IDLE_STANDBY_SERVER\""
INSTALL = "String  \"INSTALL\""
INSTALL_WITH_3_AUTHORIZED_USERS = "String  \"INSTALL_WITH_3_AUTHORIZED_USERS\""
INSTALL_WITH_PAGES = "String  \"INSTALL_WITH_PAGES\""
INSTANCE = "String  \"INSTANCE\""
LIMITED_USE_AUTHORIZED_USER = "String  \"LIMITED_USE_AUTHORIZED_USER\""
LIMITED_USE_MANAGED_SERVER = "String  \"LIMITED_USE_MANAGED_SERVER\""
LIMITED_USE_SOCKET = "String  \"LIMITED_USE_SOCKET\""
LIMITED_USE_VIRTUAL_SERVER = "String  \"LIMITED_USE_VIRTUAL_SERVER\""
LINEAR_ASSET = "String  \"LINEAR_ASSET\""
MAILBOX = "String  \"MAILBOX\""
MANAGED_CHASSIS = "String  \"MANAGED_CHASSIS\""
MANAGED_CLIENT_DEVICES = "String  \"MANAGED_CLIENT_DEVICES\""
MANAGED_DEVICES = "String  \"MANAGED_DEVICES\""
MANAGED_SERVER = "String  \"MANAGED_SERVER\""
MANAGED_SWITCH = "String  \"MANAGED_SWITCH\""
MANAGED_VIRTUAL_NETWORK_DEVICE = "String  \"MANAGED_VIRTUAL_NETWORK_DEVICE\""
MANAGED_VIRTUAL_SERVER = "String  \"MANAGED_VIRTUAL_SERVER\""
MILLION_OF_SERVICE_UNIT_PER_HOURS = "String  \"MILLION_OF_SERVICE_UNIT_PER_HOURS\""
MILLION_SPEND_CONVERSION_UNITS = "String  \"MILLION_SPEND_CONVERSION_UNITS\""
MILLION_SQUARE_FEET = "String  \"MILLION_SQUARE_FEET\""
MONTHLY_JOBS = "String  \"MONTHLY_JOBS\""
NETWORK_NODE = "String  \"NETWORK_NODE\""
ONE_M_ORDER_LINES = "String  \"ONE_M_ORDER_LINES\""
PAGE = "String  \"PAGE\""
PER_TOKEN = "String  \"PER_TOKEN\""
POPULATED_SOCKET = "String  \"POPULATED_SOCKET\""
PORT = "String  \"PORT\""
PRINTER = "String  \"PRINTER\""
PROCESSOR = "String  \"PROCESSOR\""
PROCESSOR_DAY = "String  \"PROCESSOR_DAY\""
PROCESSOR_VALUE_UNIT = "String  \"PROCESSOR_VALUE_UNIT\""
RACK = "String  \"RACK\""
REGISTERED_USER = "String  \"REGISTERED_USER\""
RESOURCE_VALUE_UNIT = "String  \"RESOURCE_VALUE_UNIT\""
SERVER_DEVICE = "String  \"SERVER_DEVICE\""
SERVER_GREATER_OR_EQUAL_TO_1000 = "String  \"SERVER_GREATER_OR_EQUAL_TO_1000\""
SERVER_LESS_THAN_1000 = "String  \"SERVER_LESS_THAN_1000\""
SERVER_WITH_ONE_PROCESSOR = "String  \"SERVER_WITH_ONE_PROCESSOR\""
SIMULTANEOUS_SESSION = "String  \"SIMULTANEOUS_SESSION\""
SOCKET = "String  \"SOCKET\""
STG_TIER = "String  \"STG_TIER\""
STORAGE_DEVICE = "String  \"STORAGE_DEVICE\""
STORE = "String  \"STORE\""
SWITCH = "String  \"SWITCH\""
TEN_AUTHORIZED_USER = "String  \"TEN_AUTHORIZED_USER\""
TEN_MONTHLY_JOBS = "String  \"TEN_MONTHLY_JOBS\""
TERABYTE = "String  \"TERABYTE\""
TERMINAL = "String  \"TERMINAL\""
TICKETS = "String  \"TICKETS\""
TIERED_DECIMAL_TERABYTES = "String  \"TIERED_DECIMAL_TERABYTES\""
TIERED_TERABYTES = "String  \"TIERED_TERABYTES\""
TIERED_TERABYTES_LARGE = "String  \"TIERED_TERABYTES_LARGE\""
TIERED_TERABYTES_SMALL = "String  \"TIERED_TERABYTES_SMALL\""
TIVOLI_MANAGEMENT_POINT = "String  \"TIVOLI_MANAGEMENT_POINT\""
TOKEN = "String  \"TOKEN\""
USER = "String  \"USER\""
USER_VALUE_UNIT = "String  \"USER_VALUE_UNIT\""
VIRTUAL_SERVER = "String  \"VIRTUAL_SERVER\""
VU_VALUE_UNIT = "String  \"VU_VALUE_UNIT\""
def ():
    '''returns Metric\n\n
    ()\n
    (final String type, final String subType, final Number value, final Date startTime, final Date endTime)\n
    (final String type, final Number value, final Date timestamp)\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final String type)\n
    '''
def getSubType():
    '''returns String\n\n
    getSubType()\n
    '''
def setSubType():
    '''returns None\n\n
    setSubType(final String subType)\n
    '''
def getValue():
    '''returns Number\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Number value)\n
    '''
def getStartTime():
    '''returns Date\n\n
    getStartTime()\n
    '''
def setStartTime():
    '''returns None\n\n
    setStartTime(final Date startTime)\n
    '''
def getEndTime():
    '''returns Date\n\n
    getEndTime()\n
    '''
def setEndTime():
    '''returns None\n\n
    setEndTime(final Date endTime)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
