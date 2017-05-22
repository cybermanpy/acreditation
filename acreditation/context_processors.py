from django.contrib.auth.models import User

# getUser = User.objects.get(username=user)

getUser = 'Anonymous'

def getUsername(request):
    return {'getUser': getUser}