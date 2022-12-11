import os
import traceback
from sendgrid import SendGridAPIClient
from dotenv import load_dotenv

load_dotenv()


class SendgridTeammatesManage:
    def __init__(self) -> None:
        self.sg = self.authorize_client()

    def main(self) -> None:
        self.get_teammates()
        self.get_scopes()
        # self.add_teammate()

    def authorize_client(self) -> SendGridAPIClient:
        sg = SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

        print(os.environ.get("SENDGRID_API_KEY"))
        print(sg)

        return sg

    def get_teammates(self):
        response = self.sg.client.teammates.get()

        print(response.status_code)
        print(response.body)
        print(response.headers)

        return response

    def get_scopes(self):
        response = self.sg.client.scopes.get()

        print(response.status_code)
        print(response.body)
        print(response.headers)

        return response

    def add_teammate(self):
        email = "example@exemple.com"
        scopes = ["user.profile.read", "user.profile.update"]
        is_admin = False

        data = {"email": email, "scopes": scopes, "is_admin": is_admin}

        print(data)

        try:
            response = self.sg.client.teammates.post(request_body=data)

            print(response.status_code)
            print(response.body)
            print(response.headers)

            return response
        except Exception:
            print(traceback.format_exc())


if __name__ == "__main__":
    sendgrid_teammates_manage = SendgridTeammatesManage()
    sendgrid_teammates_manage.main()
