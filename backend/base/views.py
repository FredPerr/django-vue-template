# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from base.serializers import UserSerializer
from base.models import User

@csrf_exempt
def user_view(request, id=0):
    method = request.method
    serializer = None
    parser = JSONParser()

    def validate_and_save_serializer(serializer):
        if serializer.is_valid():
            serializer.save()
            return True
        return False

    if method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif method == 'POST':
        users_data = parser.parse(request)
        serializer = UserSerializer(data=users_data)
        success = validate_and_save_serializer(serializer)
        return JsonResponse("Added successfully!" if success else "Failed to save the request!", safe=False)

    elif method == 'PUT':
        users_data = parser.parse(request)
        user = None
        try:
            user = User.objects.get(id=users_data['id'])
        except User.DoesNotExist:
            return JsonResponse("The targeted user does not exist!", safe=False)
        except KeyError:
            return JsonResponse("You must enter the key of the user to update!", safe=False)
        serializer = UserSerializer(user, data=users_data)
        success = validate_and_save_serializer(serializer)
        return JsonResponse("Updated successfully!" if success else "Failed to save the request!", safe=False)
    elif method == 'DELETE':
        user = User.objects.get(id=id)
        feedback = user.delete()
        return JsonResponse("Removed successfully!" if feedback[0] > 0 else "No item was removed!", safe=False) # TODO check if the return type is correct
    return JsonResponse("Request type not supported!", safe=False)