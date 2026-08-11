from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Post, Activity, Bookmark, Like, Comment, Follow, Answer, Notification

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        content_object = instance.content_object
        if content_object and hasattr(content_object, 'author'):
            if instance.user != content_object.author:
                Notification.objects.create(
                    user=content_object.author,
                    message=f"{instance.user.username} liked your post: {content_object.title[:30]}",
                    activity=Notification.Category.LIKE,
                    link=f"/post/{content_object.slug}/",
                )

@receiver(post_save, sender=Bookmark)
def create_bookmark_notification(sender, instance, created, **kwargs):
    if created:
        content_object = instance.content_object
        if content_object and hasattr(content_object, 'author'):
            if  content_object.author != instance.user:
                Notification.objects.create(
                    user=content_object.author,
                    message=f"{instance.user.username} bookmarked your post: {content_object.title[:30]}",
                    activity=Notification.Category.BOOKMARK,
                    link=f"/post/{content_object.slug}/"
                )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender,instance, created, **kwargs):
    if created:
        content_object = instance.content_object
        if content_object and hasattr(content_object, 'author'):
            if instance.user != content_object.author:
                Notification.objects.create(
                    user=content_object.author,
                    message=f"{instance.user.username} commented on your post: {content_object.title[:30]}",
                    activity=Notification.Category.COMMENT,
                    link=f"/post/{content_object.slug}/",
                )

@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        if instance.following != instance.follower:
            Notification.objects.create(
                user=instance.following,
                message=f"{instance.user.username} started following you!",
                activity=Notification.Category.FOLLOW,
                link=f"/accounts/profile/{instance.follower.username}/"
            )

@receiver(post_save, sender=Answer)
def create_answer_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if instance.author != post.author:
            Notification.objects.create(
                user=post.author,
                message=f"{instance.author.username} answered your question: {post.title[:30]}",
                activity=Notification.Category.ANSWER,
                link=f"/post/{post.slug}/"
            )

@receiver(post_save, sender=Post)
def create_post_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=instance.author,
            activity_type=Activity.ActivityType.POST,
            content_object=ContentType.objects.get_for_model(instance),
            object_id=instance.id,
            description=f"created a new post: {instance.title[:30]}"
        )

@receiver(post_save, sender=Like)
def create_like_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=instance.user,
            activity_type=Activity.ActivityType.LIKE,
            content_object=instance.content_type,
            object_id= instance.object_id,
            description=f"liked a post"
        )

@receiver(post_save, sender=Comment)
def create_comment_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=instance.user,
            activity_type=Activity.ActivityType.COMMENT,
            content_object=instance.content_type,
            object_id=instance.object_id,
            description=f"commented: {instance.content[:30]}..."
        )

@receiver(post_save, sender=Follow)
def create_follow_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=instance.follower,
            activity_type=Activity.ActivityType.FOLLOW,
            target_user=instance.following,
            description=f"followed {instance.following.username}"
        )

@receiver(post_save, sender=Answer)
def create_answer_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=instance.author,
            activity_type=Activity.ActivityType.ANSWER,
            content_object=ContentType.objects.get_for_model(instance),
            object_id=instance.id,
            description=f"answered a question: {instance.post.title[:30]}"
        )

