# src/backend/schema.py

import strawberry

from .apps.users.graphql.mutations import UserMutation
from .apps.users.graphql.queries import UserQuery


@strawberry.type
class Query(UserQuery):
    pass


@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
