import strawberry
from graphql.error import GraphQLError
from piccolo.apps.user.tables import BaseUser

from .inputs import UserInput
from .types import UserType


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, user_input: UserInput) -> UserType:
        existing_user = await BaseUser.objects().get(
            BaseUser.username == user_input.username
        )
        if existing_user:
            raise GraphQLError(
                f"User with username '{user_input.username}' already exists."
            )

        user = BaseUser(
            username=user_input.username,
            first_name=user_input.first_name,
            last_name=user_input.last_name,
            email=user_input.email,
        )
        await user.save()

        return UserType.from_model(user)
