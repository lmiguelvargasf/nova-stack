import strawberry


@strawberry.input
class UserInput:
    username: str
    first_name: str
    last_name: str
    email: str
