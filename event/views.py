from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, Tech, PostScreen, PostRes
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import EventSerializer, TechSerializer


def homeView(request):
    events = Event.objects.all().order_by('event_date')
    return render(request, "home.html", {"events": events})


def postView(request, event_id):
    detail_post = get_object_or_404(Event, pk=event_id)
    tech_post = Tech.objects.filter(event__id=event_id)
    post_screen = PostScreen.objects.filter(event__id=event_id)
    post_res = PostRes.objects.filter(event__id=event_id)
    post_screens_id = []
    post_screens_modal = []
    for p_s in range(len(post_screen)):
        post_screens_id.append("#" + str(p_s))
        post_screens_modal.append(str(p_s))
    return render(request, "post.html", {"post": detail_post, "tech": tech_post,
                                         "screens": zip(post_screen, post_screens_id, post_screens_modal),
                                         "res": post_res})


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-event_date')
    serializer_class = EventSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class TechViewSet(viewsets.ModelViewSet):
    queryset = Tech.objects.all().order_by('-event')
    serializer_class = TechSerializer
    permission_classes = [permissions.IsAuthenticated]
