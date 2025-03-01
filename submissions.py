from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase credentials from .env file
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_deals_submitted():
    try:
        response = supabase.table("deals_submitted").select("*").execute()
        if response.data:
            return response.data
        else:
            print("No data found in deals_submitted table.")
            return []
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

if __name__ == "__main__":
    deals = fetch_deals_submitted()
    print(deals)
