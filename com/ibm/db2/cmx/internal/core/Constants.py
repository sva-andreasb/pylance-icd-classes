REPLY_TIMEOUT = "int  Integer.parseInt(DataProperties.getProperty(\"pdq.cmx.readTimeout\")) * 1000"
SOCKET_CONNECT_TIMEOUT = "int  Integer.parseInt(DataProperties.getProperty(\"pdq.cmx.connectTimeout\")) * 1000"
PROCESSOR_NAME = "String  \"CMXCoreProcessor\""
PROCESSOR_VERSION = "int  1"
CONNECT_TO_PROCESSOR_REQUEST = "String  \"1\""
ERROR = "String  \"2\""
CONNECT_TO_PROCESSOR_REPLY = "String  \"3\""
STATEMENT_PULL_DATA_JCC_STATEMENT_STATS = "int  2000"
STATEMENT_PULL_DATA_JCC_STATEMENT_STATS_RESET = "int  2001"
CONNECTION_PULL_DATA_JCC_GATEWAY_INFO = "int  3000"
CONNECTION_PULL_DATA_JCC_CLIENTINFO_AND_REGISTERS = "int  3002"
CONNECTION_PULL_DATA_JCC_MONITOR_INFO = "int  3003"
CONNECTION_PULL_DATA_JCC_UNIT_OF_WORK_INFO = "int  3004"
DATASOURCE_PULL_DATA_JCC_PROPERTIES_MAP = "int  4000"
DATASOURCE_PULL_DATA_JCC_APPL_PROPERTIES_MAP = "int  4001"
DRIVER_PULL_DATA_JCC_PROPERTIES_MAP = "int  5000"
DRIVER_PULL_DATA_JCC_TRANSPORT_POOL_STATS = "int  5001"
