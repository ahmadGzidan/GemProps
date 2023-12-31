from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.serializers  import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    token = request.auth

    if token:
        
        token.delete()
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'No token provided.'}, status=status.HTTP_400_BAD_REQUEST)