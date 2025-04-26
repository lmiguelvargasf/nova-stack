# src/backend/schema.py

import strawberry

from .apps.users.graphql.schema import UserMutation, UserQuery


@strawberry.type
class Query(UserQuery):
    pass


@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
