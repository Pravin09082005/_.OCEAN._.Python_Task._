




class UserLogin:
    def __init__(self):
        self.users = {
            "Madhu@SMVEC": "Madhu@123",    #admin
            "pravinstd@smvec": "Pravin@2005"   #normal user
        }



    def login(self):
        uid = input("Enter UID: ")
        password = input("Enter Password: ")
        
        
        if uid in self.users and self.users[uid] == password:
            print(f"Login successful..!!! 🙋 Welcome... {uid}.")
        
            if uid == "Madhu@SMVEC":
                admin = Admin()
                admin.enter_mou_details()
            else:
                print("Your user login is not still opened.")  
        else:
            print("Invalid UID or Password. Access Denied.")

class Admin:
    def __init__(self):
        self.mou_details = {}



    def enter_mou_details(self):
        endYear = input("Enter the end year of the MOU: ")
        dateOfSigning = input("Enter the date of Signing the MOU (DD/MM/YYYY): ")
        purpose = input("Enter the purpose of the MOU: ")
        departments = input("Enter the departments involved in the MOU (comma separated): ")
        
        
        
        self.mou_details["Year"] = endYear
        self.mou_details["Date"] = dateOfSigning
        self.mou_details["Purpose"] = purpose
        self.mou_details["Departments"] = [dept.strip() for dept in departments.split(",")]
        
        
        print("\nMOU Details Entered:")
        print(f"Year: {self.mou_details['Year']}")
        print(f"Date: {self.mou_details['Date']}")
        print(f"Purpose: {self.mou_details['Purpose']}")
        print(f"Departments: {', '.join(self.mou_details['Departments'])}")
        
        # (just a string message)
        self.attach_mou_file()

    def attach_mou_file(self):
        # just a part where the file can be attached when developed into the application
        print("\nAttach the required MOU file")






if __name__ == "__main__":

    user_login = UserLogin()
    user_login.login()
