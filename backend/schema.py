import graphene
import graphql_jwt
import events.schema
import users.schema

# Query for getting the data from the server.


class Query(
    events.schema.Query,
    users.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    events.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
