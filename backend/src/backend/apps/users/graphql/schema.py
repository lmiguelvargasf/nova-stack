import strawberry
from graphql.error import GraphQLError
from piccolo.apps.user.tables import BaseUser

from .types import UserType


@strawberry.type
class UserQuery:
    @strawberry.field
    async def user(self, id: strawberry.ID) -> UserType:
        user_id = int(id)
        user = await BaseUser.objects().get(BaseUser.id == user_id)
        if user is None:
            raise GraphQLError(f"User with id {user_id} not found")
        return UserType.from_model(user)


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(
        self,
        username: str,
        first_name: str,
        last_name: str,
    ) -> UserType:
        existing_user = await BaseUser.objects().get(BaseUser.username == username)
        if existing_user:
            raise GraphQLError(f"User with username '{username}' already exists.")

        user = BaseUser(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        await user.save()

        return UserType.from_model(user)
