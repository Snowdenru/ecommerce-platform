from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model, authenticate
from apps.accounts.serializer import UserCreateSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        token = Token.objects.create(user=user)
        # send_verification_email.delay(user.id)


class UserLoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        return UserSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": UserSerializer(user).data})
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


from rest_framework.decorators import api_view
from rest_framework import status
from .tasks import add
from django.core.mail import send_mail




@api_view(["GET"])
def run_add_task(request):

    try:
        a = int(10)
        b = int(12)
        # send_mail('Тестируем отправку пиьсма',
        #   'Тело письма',
        #   'subachevdenis@yandex.ru',
        # ['subachevdenis@yandex.ru'], fail_silently=False
        # )

    except Exception as e:
        return Response(
            {"error": f"Параметры должы быть числами{str(e)}"}, status=status.HTTP_404_NOT_FOUND
        )

    task = add.delay(a, b)
    return Response(
        {
            "task_id": task.id,
            "satus": "Задача успешно поставлена в очередь",
            "params": {"a": a, "b": b},
        }, status=status.HTTP_202_ACCEPTED
    )
