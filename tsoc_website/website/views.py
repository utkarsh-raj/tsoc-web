from django.shortcuts import render, redirect
from website.models import Participant
from django.http import JsonResponse

# Create your views here.

def registration(request):
    if request.method == "POST":
        name = request.POST["name"]
        branch = request.POST["branch"]
        batch = request.POST["batch"]
        comments = request.POST["comments"]

        participant = Participant(name = name, branch = branch, batch = batch, comments = comments)

        participant.save()

        return render(request, "acknowledge.html")
    else:
        return render(request, "registration.html")

def administrator(request):
    participants = Participant.objects.all()
    print(participants)

    print("============ ============")

    count = 0

    for participant in participants:
        count += 1
        print(participant.name, "-", participant.branch, "-", participant.batch, "-", participant.comments)

    print("Total participants registered are", count)

    print("============ ============")
        
    return JsonResponse({
        "message": "If you can read the message, I admire your curiosity. You are welcome to join TSoC Devs and also this is Json Response, if you are feeling adventurous."
    })