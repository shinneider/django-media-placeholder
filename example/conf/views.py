from django.shortcuts import render_to_response
# from .models import SampleModel


def home(request):
    # sample = SampleModel.objects.first()
    return render_to_response('home.html')  # , {'sample': sample})
