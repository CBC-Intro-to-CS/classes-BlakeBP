class User:
    def __init__(self, friend_last_name, friend_first_name,):


        self.first_name = "Blake"
        self.last_name = "Pelley"
        self.friend_last_name = "Province"
        self.friend_first_name = "Gunner"

        
    def describe_user(self):
        print(f"Your name is {self.first_name} {self.last_name}, and your friend's name is {self.friend_first_name} {self.friend_last_name}.")
        print(f"Hello {self.first_name}!,Hello{self.friend_first_name}!")

