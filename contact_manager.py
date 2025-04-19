import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("⚠️ Contact already exists!")
        return
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts(contacts)
    print("✅ Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\n📭 No contacts found.")
        return
    print("\n📒 Contact List:")
    for name, details in contacts.items():
        print(f"{name} - 📞 {details['Phone']} | 📧 {details['Email']} | 📍 {details['Address']}")

def search_contact(contacts):
    query = input("🔎 Search by name or phone: ").strip().lower()
    found = False
    for name, details in contacts.items():
        if query in name.lower() or query in details["Phone"]:
            print(f"\n✔️ Found: {name} | {details['Phone']} | {details['Email']} | {details['Address']}")
            found = True
            break
    if not found:
        print("❌ No matching contact found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("❌ Contact not found!")
        return
    print("Enter new details (leave blank to keep current value):")
    phone = input(f"New Phone [{contacts[name]['Phone']}]: ").strip()
    email = input(f"New Email [{contacts[name]['Email']}]: ").strip()
    address = input(f"New Address [{contacts[name]['Address']}]: ").strip()

    if phone:
        contacts[name]["Phone"] = phone
    if email:
        contacts[name]["Email"] = email
    if address:
        contacts[name]["Address"] = address

    save_contacts(contacts)
    print("✅ Contact updated successfully!")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n======= CONTACT BOOK MENU =======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("=================================")

        choice = input("Choose an option (1–6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("👋 Exiting Contact Book. Stay connected!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
