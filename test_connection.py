# from snowflake.snowpark import Session
# from snowflake.connector.errors import DatabaseError, OperationalError

# if __name__ == "__main__":

#     try:
#         session = Session.builder.getOrCreate()
#         account = session.get_current_account()
#         print("Success you're connected to Snowflake account: " + account)
#         print("Enjoy the Hands-on Lab!")
#     except OperationalError as oe:
#         print(oe.msg)
#     except DatabaseError as de:
#         print(de.msg)

import toml
import os
from snowflake.snowpark import Session
from snowflake.connector.errors import DatabaseError, OperationalError

def get_snowsql_config(config_path='~/.snowflake/connections.toml'):
    # Resolve the full path
    full_path = os.path.expanduser(config_path)

    # Check if the configuration file exists
    if not os.path.exists(full_path):
        raise FileNotFoundError("Snowflake config file not found at the specified location.")

    # Load the TOML configuration file
    with open(full_path, 'r') as config_file:
        config = toml.load(config_file)

    # Choose the default connection or a specific one if needed
    default_connection_name = os.getenv('SNOWFLAKE_DEFAULT_CONNECTION_NAME', 'default')
    if default_connection_name not in config:
        raise ValueError(f"Connection named {default_connection_name} not found in the config file.")

    # Extract settings from the selected connection
    snowsql_config = config[default_connection_name]
    return snowsql_config

if __name__ == "__main__":
    try:
        # Load SnowSQL Config and adjust the role
        snowpark_config = get_snowsql_config()
        snowpark_config['role'] = 'ACCOUNTADMIN'  # Update role to ACCOUNTADMIN

        # Create a Snowflake session using the modified config
        session = Session.builder.configs(snowpark_config).create()

        # Retrieve and print the current account to confirm connection
        account = session.get_current_account()
        print("Success, you're connected to Snowflake account: " + account)
        print("Enjoy the Hands-on Lab!")
    except OperationalError as oe:
        print("Operational Error:", oe.msg)
    except DatabaseError as de:
        print("Database Error:", de.msg)
    except Exception as e:
        print("An unexpected error occurred:", str(e))