from django.shortcuts import render, redirect
import time

# Create your views here.
def root(request):
    return redirect('/time_display')

def index(request):
    context = {
        "date": time.strftime("%Y-%m-%d"),
        "time": time.strftime("%H:%M %p")
    }
    return render(request,'index.html', context)