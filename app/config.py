from dotenv import load_dotenv
import os
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


Secret_Key = os.getenv("SECRET_KEY")