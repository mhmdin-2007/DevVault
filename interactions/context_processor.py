from .models import Notification

def notification_count(request):
    '''add unread notification count to all template.'''
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(
            is_read=False
        ).count()
    else:
        unread_count = 0
    
    return {
        'unread_count': unread_count
    }