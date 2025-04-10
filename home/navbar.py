from .models import Profile

def NavbarFunction(request):
    if request.user.is_authenticated:
        User_Profile = Profile.objects.get(name = request.user.id)
        return {
            "Category" : User_Profile.user_category,
        }
    return {
        "Category" : "Employee",
    } 