# src/backend/schema.py

import strawberry

from .apps.users.graphql.schema import UserQuery


@strawberry.type
class Query(UserQuery):
    pass


# @strawberry.type
# class Mutation:
#     pass

schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation
)
