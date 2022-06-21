"""MySQL Connection Errors

Nearly all of these raise OperationalError. COMMANDS_OUT_OF_SYNC
raises ProgrammingError.

"""

if __name__ == "__main__":
    """
    Usage: python CR.py [/path/to/mysql/errmsg.h ...] >> CR.py
    """
    import fileinput
    import re

    data = {}
    error_last = None
    for line in fileinput.input():
        line = re.sub(r"/\*.*?\*/", "", line)
        m = re.match(r"^\s*#define\s+CR_([A-Z0-9_]+)\s+(\d+)(\s.*|$)", line)
        if m:
            name = m.group(1)
            value = int(m.group(2))
            if name == "ERROR_LAST":
                if error_last is None or error_last < value:
                    error_last = value
                continue
            if value not in data:
                data[value] = set()
            data[value].add(name)
    for value, names in sorted(data.items()):
        for name in sorted(names):
            print("{} = {}".format(name, value))
    if error_last is not None:
        print("ERROR_LAST = %s" % error_last)


ERROR_FIRST = 2000
MIN_ERROR = 2000
UNKNOWN_ERROR = 2000
SOCKET_CREATE_ERROR = 2001
CONNECTION_ERROR = 2002
CONN_HOST_ERROR = 2003
IPSOCK_ERROR = 2004
UNKNOWN_HOST = 2005
SERVER_GONE_ERROR = 2006
VERSION_ERROR = 2007
OUT_OF_MEMORY = 2008
WRONG_HOST_INFO = 2009
LOCALHOST_CONNECTION = 2010
TCP_CONNECTION = 2011
SERVER_HANDSHAKE_ERR = 2012
SERVER_LOST = 2013
COMMANDS_OUT_OF_SYNC = 2014
NAMEDPIPE_CONNECTION = 2015
NAMEDPIPEWAIT_ERROR = 2016
NAMEDPIPEOPEN_ERROR = 2017
NAMEDPIPESETSTATE_ERROR = 2018
CANT_READ_CHARSET = 2019
NET_PACKET_TOO_LARGE = 2020
EMBEDDED_CONNECTION = 2021
PROBE_SLAVE_STATUS = 2022
PROBE_SLAVE_HOSTS = 2023
PROBE_SLAVE_CONNECT = 2024
PROBE_MASTER_CONNECT = 2025
SSL_CONNECTION_ERROR = 2026
MALFORMED_PACKET = 2027
WRONG_LICENSE = 2028
NULL_POINTER = 2029
NO_PREPARE_STMT = 2030
PARAMS_NOT_BOUND = 2031
DATA_TRUNCATED = 2032
NO_PARAMETERS_EXISTS = 2033
INVALID_PARAMETER_NO = 2034
INVALID_BUFFER_USE = 2035
UNSUPPORTED_PARAM_TYPE = 2036
SHARED_MEMORY_CONNECTION = 2037
SHARED_MEMORY_CONNECT_REQUEST_ERROR = 2038
SHARED_MEMORY_CONNECT_ANSWER_ERROR = 2039
SHARED_MEMORY_CONNECT_FILE_MAP_ERROR = 2040
SHARED_MEMORY_CONNECT_MAP_ERROR = 2041
SHARED_MEMORY_FILE_MAP_ERROR = 2042
SHARED_MEMORY_MAP_ERROR = 2043
SHARED_MEMORY_EVENT_ERROR = 2044
SHARED_MEMORY_CONNECT_ABANDONED_ERROR = 2045
SHARED_MEMORY_CONNECT_SET_ERROR = 2046
CONN_UNKNOW_PROTOCOL = 2047
INVALID_CONN_HANDLE = 2048
UNUSED_1 = 2049
FETCH_CANCELED = 2050
NO_DATA = 2051
NO_STMT_METADATA = 2052
NO_RESULT_SET = 2053
NOT_IMPLEMENTED = 2054
SERVER_LOST_EXTENDED = 2055
STMT_CLOSED = 2056
NEW_STMT_METADATA = 2057
ALREADY_CONNECTED = 2058
AUTH_PLUGIN_CANNOT_LOAD = 2059
DUPLICATE_CONNECTION_ATTR = 2060
AUTH_PLUGIN_ERR = 2061
INSECURE_API_ERR = 2062
FILE_NAME_TOO_LONG = 2063
SSL_FIPS_MODE_ERR = 2064
MAX_ERROR = 2999
ERROR_LAST = 2064
