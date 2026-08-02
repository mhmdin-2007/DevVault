from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Post, Activity, Like, Comment, Follow, Answer

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
        #like is on a Post
        if instance.content_type.model == "post":
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