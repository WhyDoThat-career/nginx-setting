SECRET_KEY = 'whydothat_secretkey'

db = load_key(key_file='./keys/aws_sql_key.json')
database = "crawl_job"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{database}?charset=utf8mb4"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
