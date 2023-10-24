from django.shortcuts import render

def view_data(request):
    events = WorkpieceEvent.objects.all()
    return render(request, 'data_view.html', {'events': events})
