from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def capture_event(request):
    if request.method == "POST":
        # Extract data from POST request and save to the database
        # For simplicity, this assumes data is sent as JSON
        data = json.loads(request.body)
        event = WorkpieceEvent.objects.create(**data)
        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)
