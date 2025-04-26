import strawberry
from graphql.error import GraphQLError
from piccolo.apps.user.tables import BaseUser

from .types import UserType


@strawberry.type
class UserQuery:
    @strawberry.field
    async def user(self, id: int) -> UserType:
        user = await BaseUser.objects().get(BaseUser.id == id)
        if user is None:
            raise GraphQLError(f"User with id {id} not found")
        return UserType.from_model(user)
