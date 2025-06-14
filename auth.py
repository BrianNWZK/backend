from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def register_user(email: str, password: str):
    return supabase.auth.sign_up({"email": email, "password": password})

def login_user(email: str, password: str):
    return supabase.auth.sign_in_with_password({"email": email, "password": password})
