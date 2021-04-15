
def haveProjectPermission(request, project):
    user = request.user
    return user in project.users_assigned.all()

def haveTaskPermission(request, task):
    user = request.user
    return user in task.users_assigned.all()
