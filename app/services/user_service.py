import json

def get_user_service():
    file = open("services.json")
    services = json.load(file)
    file.close()
    print(services)
    return services

