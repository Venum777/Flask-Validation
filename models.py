class User:
    """User."""

    def __init__(
        self,
        login: str,
        password: str,
        first_name: str
    ) -> None:
        self.login = login
        self.password = password
        self.first_name = first_name
    
    @staticmethod
    def create(
        login: str,
        password: str,
        password2: str,
        first_name: str,
        users: list['User']
    ) -> 'User':
        user: User = User(
            login=login,
            password=password,
            first_name=first_name
        )
        print(users)
        if len(password) < 4:
            raise ValueError(
                "Password is too short"
            )
        if password != password2:
            raise ValueError(
                "Password confirm is not correct"
            )
        user.login_valid(users=users)
        return user
    
    def login_valid(self, users: list['User']) -> bool:
        if users == []:
            return True
        for user in users:
            if user.login == self.login:
                raise ValueError(
                    "Login is not unique"
                ) 
        return True