"""
orders-api configuration.

NOTE (demo): this file intentionally contains a hardcoded credential so that
CloudBees Unify's automatic security scanning flags a finding in the
component's Security tab. Do NOT hardcode secrets in real code — load them
from a secrets manager or environment variables.
"""

DB_HOST = "db.internal.example.com"
DB_PORT = 5432
DB_NAME = "orders"
DB_USER = "orders_service"

# Hardcoded password — intentional demo finding.
DB_PASSWORD = "P@ssw0rd123!"
AWS_ACCESS_KEY_ID = "AKIA5Q7W8E9R1T2Y3U4I";
AWS_SECRET_ACCESS_KEY = "aB3c+D4eF5gH6iJ7kL8mN9oP0qR1sT2uV3wX4yZ5";

def database_url():
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
