import psycopg2
import os

# Load environment variables from Lambda
DB_HOST = os.getenv("DB_HOST")  # RDS Endpoint
DB_USER = os.getenv("DB_USER")  # RDS Username
DB_PASSWORD = os.getenv("DB_PASSWORD")  # RDS Password
DB_NAME = os.getenv("DB_NAME")  # RDS Database Name
DB_PORT = int(os.getenv("DB_PORT", 5432))  # Default PostgreSQL Port

def lambda_handler(event, context):
    try:
        # Connect to PostgreSQL RDS
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            port=DB_PORT
        )
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW();")  # Test query
            result = cursor.fetchone()
        
        return {
            "statusCode": 200,
            "body": f"Connected Successfully! Current Time: {result[0]}"
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
