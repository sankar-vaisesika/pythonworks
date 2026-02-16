#admin control using decorator

def admin_only(func):

    def wrapper(user_role):

        if user_role.lower()!="admin":

            return "Access Denied"
        
        return func(user_role)
    
    return wrapper


@admin_only
def view_dashboard(user_role):

    return "Welcome to admin dashboard"

print(view_dashboard("Admin"))
print(view_dashboard("user"))
