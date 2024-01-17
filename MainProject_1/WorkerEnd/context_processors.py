from .models import worker_db

def worker_profile_exists(request):
    profile_exists = False

    if 'wr_username' in request.session:
        try:
            # Check if the worker profile exists for the logged-in user
            worker_profile = worker_db.objects.get(username=request.session['wr_username'])
            profile_exists = True
        except worker_db.DoesNotExist:
            pass

    return {'profile_exists': profile_exists}