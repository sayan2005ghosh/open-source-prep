vault_users = {
    "Admin": {"pin": 1234, "clearance": 5, "status": "active"},
    "Sayan": {"pin": 8888, "clearance": 2, "status": "active"},
    "Guest": {"pin": 0000, "clearance": 1, "status": "blocked"}
}

def enter_vault():
    username = input("Enter Name: ")

    # STEP 1: Check if the name exists in our dictionary
    if username in vault_users:
        
        # STEP 2: Ask for PIN and convert to INT to match the dictionary type
        user_pin = int(input(f"Enter PIN for {username}: "))
        
        # STEP 3: Check if the PIN is correct for THIS specific user
        if user_pin == vault_users[username]["pin"]:
            
            # STEP 4: Check if they are blocked
            if vault_users[username]["status"] == "active":
                
                # STEP 5: Check clearance level
                clearance = vault_users[username]["clearance"]
                
                if clearance >= 3:
                    print(f"✅ Access Granted. Welcome {username}. Clearance: {clearance}")
                else:
                    # STEP 6: The "Secret Code" fallback for low clearance
                    print("⚠️ Clearance too low.")
                    secret = input("Enter Secret Access Code: ")
                    if secret == "OpenSesame":
                        print(f"✅ Access Granted via Secret Code. Welcome {username}.")
                    else:
                        print("❌ Denied: Invalid Secret Code.")
            else:
                print(f"❌ Denied: User '{username}' is currently blocked.")
        else:
            print("❌ Denied: Incorrect PIN.")
    else:
        print("❌ Denied: Username not found in system.")

# Run the system
enter_vault()