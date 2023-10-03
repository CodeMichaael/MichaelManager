from .models import ConnectionManager
from .serializers import ConnectionManagerSerializer
import uuid
from colorama import Fore
import platform
import requests

api_url = 'http://127.0.0.1:8000/connections'

computer_name = platform.node()
random_uuid = uuid.uuid4()

def main():
    validate = ConnectionManager.objects.filter(to_computer_id=computer_name)
    if validate:
        print(f"{Fore.CYAN}MichaelManager {Fore.BLUE}Connected and waiting for request.")
        while True:
            response = requests.get(api_url)
            headers = response.headers

            if headers["cmd"] != "connection-request":
                pass
            else:
                serializer = UserConnectionSerializer(data=headers)
                if serializer.is_valid():
                    serializer.save()
                    connectionid = serializer.validated_data["connection_id"]
                    task = serializer.validated_data["request"]
                    user_id = serializer.validated_data["user_id"]
                    manager = ConnectionManager.objects.get(to_computer_id=computer_name)
                    connid = manager.connection_id
                    user = manager.user_id
                    
                    if connectionid == connid and user_id == user:
                        try:
                            from .tasks import task
                            task()
                        except ImportError or NameError:
                            pass

    else:
        uuid = random_uuid()
        instance = ConnectionManager(connection_id=uuid, to_computer_id=computer_name)
        instance.save()
        print(f"{Fore.CYAN}MichaelManager {Fore.BLUE}Not connected. Use /connect {uuid} to our discord bot to connect.")
        main()

if __name__ == '__main__':
    main()
                


                
