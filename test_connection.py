from snowflake.snowpark import Session
from snowflake.connector.errors import DatabaseError, OperationalError

if __name__ == "__main__":

    try:
        session = Session.builder.getOrCreate()
        account = session.get_current_account()
        print("Success you're connected to Snowflake account: " + account)
        print("Enjoy the Hands-on Lab!")
    except OperationalError as oe:
        print(oe.msg)
    except DatabaseError as de:
        print(de.msg)