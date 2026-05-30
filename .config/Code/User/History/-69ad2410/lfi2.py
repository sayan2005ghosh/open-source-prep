vault_users = {
    "Admin": {"pin": 1234, "clearance": 5, "status": "active"},
    "Sayan": {"pin": 8888, "clearance": 2, "status": "active"},
    "Guest": {"pin": 0000, "clearance": 1, "status": "blocked"}
} 
def enter_vault():
    username=input("Name:")
    if username=="Sayan":
        print(f"{username}")
        