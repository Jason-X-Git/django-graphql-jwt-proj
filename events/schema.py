import graphene
from graphene_django.types import DjangoObjectType
from .models import Event
import json
from django.db.models import Q

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = '__all__'


class Query(graphene.ObjectType):
    events = graphene.List(EventType,
                           search=graphene.String(),
                           first=graphene.Int(),
                           skip=graphene.Int(),
                           last=graphene.Int(),
                           )

    def resolve_events(self, info, search=None,
                       first=None, skip=None, last=None,
                       **kwargs):

        qs = Event.objects.all()

        if search:
            filter = (
                Q(url__icontains=search) |
                Q(name__icontains=search)
            )
            qs = qs.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        if last:
            qs = qs[::-1][:last]

        return qs


class CreateEventMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        url = graphene.String()

    name = graphene.String()
    url = graphene.String()
    created = graphene.DateTime()
    id = graphene.Int()

    def mutate(root, info, name, url=None):
        obj = Event.objects.create(
            name=name,
            url=url
        )
        return CreateEventMutation(
            id=obj.id,
            created=obj.created,
            name=obj.name,
            url=obj.url,
            )


class Mutation(graphene.ObjectType):
    create_event = CreateEventMutation.Field()
