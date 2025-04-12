from authlib.integrations.flask_client import OAuth
import os

oauth = OAuth()
class OauthConfig:
    google = oauth.register(
        name="google",
        client_id= os.environ["google_oauth_id"],
        client_secret=os.environ["google_oauth_client_secret"],
        access_token_url="https://oauth2.googleapis.com/token",
        access_token_params=None,
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        authorize_params={"scope": "openid email profile"},
        jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
        client_kwargs={"scope": "openid email profile"},
    )