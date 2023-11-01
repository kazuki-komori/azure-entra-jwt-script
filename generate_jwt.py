from msal import PublicClientApplication
from dotenv import load_dotenv
import os

load_dotenv()

app = PublicClientApplication(
    client_id=os.environ["CLIENT_ID"],
    authority=os.environ["AUTHORITY"],
)

result = app.acquire_token_interactive(scopes=["User.Read"])

if "access_token" in result:
    print(result["access_token"])
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))
