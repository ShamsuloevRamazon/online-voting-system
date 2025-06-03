from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def vote(request):
    candidate_id = request.data.get('candidate_id')
    user_id = hash(request.META.get('REMOTE_ADDR'))  # Анонимный хеш
    Vote.objects.create(candidate_id=candidate_id, user_id=user_id)
    return Response({"status": "Vote recorded"})