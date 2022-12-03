from sqlalchemy import create_engine, inspect

from secrets import get_aws_secret


def engine_bigquery():
    engine = create_engine(
        "googlebigquery:///?DataSetId=MyDataSetId&ProjectId=MyProjectId&InitiateOAuth=GETANDREFRESH"
        "&OAuthSettingsLocation=/PATH/TO/OAuthSettings.txt")
    return engine


def engine_postgres(server: object = "localhost", schema: object = "", database: object = "", echo: object = True) -> object:
    engine = create_engine(f"postgresql://postgres:{get_aws_secret('postgres_paul_mac')}@{server}:5432/{database}",
                           echo=echo)
    return engine


def test_engine():
    engine = engine_postgres(echo=False)
    engine.connect()
    insp = inspect(engine)
    sc_list = insp.get_schema_names()
    tbl_list = insp.get_table_names()
    print(f'Engine connected to: {engine}')
    print(f"Current user: {engine.execute('SELECT current_user').fetchone()[0]}")
    print(f"Schema name: {engine.execute('select current_schema()').fetchall()[0]}")
    print(f"Database name: {engine.execute('select current_database()').fetchall()[0]}")
    print(f'Tables: {tbl_list}')
    print(f'Schemas: {sc_list}')
