# ########################### AUTH #############################################################################
# from django.contrib.auth import authenticate, login
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .decorators import admin_required, worker_required, client_required
# from .serializers import LoginSerializer

# class LoginAPIView(APIView):
#     @method_decorator(csrf_exempt)
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
#         if user is not None:
#             login(request, user)
#             token, created = Token.objects.get_or_create(user=user)
#             if user.is_staff:  # Si el usuario es un administrador
#                 return Response({'id': user.id,
#                                  'usuario': user.username,
#                                  'admin': True,
#                                  'token': token.key,
#                                  }, status=status.HTTP_200_OK)
#             elif user.is_superuser:  # Si el usuario es un trabajador
#                 return Response({'id': user.id,
#                                  'usuario': user.username,
#                                  'trabajador': True,
#                                  'token': token.key,
#                                  }, status=status.HTTP_200_OK)
#             else:  # Si el usuario es un cliente
#                 return Response({'id': user.id,
#                                  'usuario': user.username,
#                                  'cliente': True,
#                                  'token': token.key,
#                                  }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

#     @method_decorator(admin_required)
#     def admin_view(self, request):
#         return Response({'message': 'Bienvenido, administrador!'})

#     @method_decorator(worker_required)
#     def worker_view(self, request):
#         return Response({'message': 'Bienvenido, trabajador!'})

#     @method_decorator(client_required)
#     def client_view(self, request):
#         return Response({'message': 'Bienvenido, cliente!'})



# class UserLogout(APIView):
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         logout(request)
#         return Response('Logout successfully')

# ########################### USER #############################################################################
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.role = 'client'  # Asignamos el rol "cliente" al nuevo usuario
#             user.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})

# ########################### SERVICES #########################################################################
# ########################### .... #############################################################################



