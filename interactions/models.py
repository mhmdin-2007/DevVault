from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from posts.models import Post 

class Notification(models.Model):
    '''
    Notification model to display users activity on their content.
    '''
    class Category(models.TextChoices):
        POST = 'POST', 'New Post'
        LIKE = 'LIKE', 'Liked your Post'
        COMMENT = 'COMMENT', 'Commented on your Post'
        ANSWER = 'ANSWER', 'Answered your question'
        FOLLOW = 'FOLLOW', 'Follow You'
        BOOKMARK = 'BOOKMARK', 'Bookmarked your post'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
    )

    message = models.CharField(max_length=255)
    activity = models.CharField(max_length=20, choices=Category.choices)
    link = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        indexes = [
            models.Index(fields=['user', 'is_read']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"user: {self.user.username} - {self.message[:30]}"

    def mark_as_read(self):
        """Mark this notification as read."""
        if not self.is_read:
            self.is_read = True
            self.save()

class Like(models.Model):
    '''
    Like any content (post, answer, etc.).
    Uses FenericForeignKey for flexible relationshiops.
    '''
    #feilds
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes',
        related_query_name='like'
    )
    #generic relation fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'content_type', 'object_id']
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]

    def __str__(self):
        return f"{self.user.username} liked {self.content_type} (ID: {self.object_id})"
    
class Comment(models.Model):
    '''
    Comment on any content.
    Uses GenericForeignKey for flexible relationships.
    '''
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    
    #Generic relation fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name='Parent Comment'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
            models.Index(fields=['parent']),
        ]

    def __str__(self):
        return f"{self.user.username} commented on {self.content_type} (ID: {self.object_id})"
    
    @property
    def is_reply(self):
        '''Check if this comment is a reply to another commment.'''
        return self.parent is not None
    
    @property
    def replies_count(self):
        '''Count of direct replies to this commnet.'''
        return self.replies.count()

class Vote(models.Model):
    '''
    Vote on any content.
    Uses GenericForeignKey for flexible relationships.
    '''
    class VoteType(models.IntegerChoices):
        DOWNVOTE = -1, 'Downvote'
        UPVOTE = 1, 'Upvote'

    #fields
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    vote_type = models.IntegerField(choices=VoteType.choices)
    #Generic relation fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['user', 'content_type', 'object_id']
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]

    def __str__(self):
        return f"{self.user.username} {self.get_vote_type_display()} on {self.content_type} (ID: {self.object_id})"
    
class Bookmark(models.Model):
    """
    Bookmark any content that you might like and save it for latar.
    And uses genericForeignKey for flexible relationships.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookmarks'
    )

    #generic relation fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'content_type', 'object_id']
        ordering = ['-created_at']
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]

    def __str__(self):
        return f"{self.user.username} bookmarked {self.content_type} (ID: {self.object_id})"
    
   
class Follow(models.Model):
    '''
    Follow model for user-to-user relationships.
    A user can follow another user.
    '''
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='Following'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    class Meta:
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'

        # هر کاربر نمیتونه دوبار یه نفر رو فالو کنه
        unique_together = ['follower', 'following']
        
        # این قسمت رو باید توی views چک کنیم  که کاربر نمیتونه خودش رو هم فالو کنه
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(follower=models.F('following')),
                name='cannot_follow_self'
            )
        ]

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
    

class Answer(models.Model):
    '''
    Answer model for posts.
    Each answer belongs to a post and a user.
    Only one answer per post can be accepted.
    '''

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Post'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Author'
    )
    content = models.TextField(verbose_name='Content')
    is_accepted = models.BooleanField(
        default=False,
        verbose_name='Is Accepted'
    )
    solution_file = models.FileField(
        upload_to='solutions/',
        blank=True,
        null=True,
        verbose_name='AnswerFile'
    )
    solution_note = models.TextField(
        blank=True,
        verbose_name='AdditionalInformations'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

        constraints = [
            models.UniqueConstraint(
                fields=['post'],
                condition=models.Q(is_accepted=True),
                name='unique_accepted_answer'
            )
        ]
    
    def save(self, *args, **kwargs):
        '''
            Override save to handle accepted answer logic.
        '''
        if self.is_accepted:
            Answer.objects.filter(post=self.post).exclude(id=self.id).update(is_accepted=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Answer by {self.author.username} on {self.post.title[:30]}"
    

class Activity(models.Model):
    '''
    Model to track user activities for the feed.
    '''
    class ActivityType(models.TextChoices):
        POST = 'POST', 'New Post'
        LIKE = 'LIKE', 'Liked a Post'
        COMMENT = 'COMMENT', 'Commented on a Post'
        FOLLOW = 'FOLLOW', 'Follow a User'
        ANSWER = 'ANSWER', 'Answered a Question'

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='activities'
    )
    activity_type = models.CharField(
        max_length=20,
        choices=ActivityType.choices
    )
    content_object = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='targeted_activities'
    )
    description = models.CharField(max_length=225, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} - {self.created_at}"