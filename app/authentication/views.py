from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()


class RegistrationUserApi(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        print(data)
        user = User(username=request.data.get('username'))
        user.set_password(request.data.get('password'))
        user.save()
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response(token)