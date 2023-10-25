
import os
from supabase import create_client, Client


# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# FIXME: to be handled as environment virables

url = "https://augbubllerfwdiqvpdfx.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF1Z2J1YmxsZXJmd2RpcXZwZGZ4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5ODA1NTIyNCwiZXhwIjoyMDEzNjMxMjI0fQ.F0dJnaiXNxOo9oN4zLeXzKQPthImaDNemO7x0cJJHIg"


supabase: Client = create_client(url, key)


def addAttendee(name: str, location: int = 0):
    data = supabase.table('attendees').insert(
        {"name": name, "location": location}).execute()

    print("Successfully added: ", data)
