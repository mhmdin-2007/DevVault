from django.contrib import admin
from .models import Answer, Vote, Bookmark, Follow, Comment

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'is_accepted', 'created_at']
    list_filter = ['is_accepted', 'created_at']
    search_fields = ['content', 'author__username', 'post__title']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'target','content_type', 'object_id', 'vote_type', 'created_at']
    list_filter = ['vote_type', 'created_at']
    search_fields = ['user__username']
    readonly_fields = ['created_at', 'updated_at']

    @admin.display(description='Target')
    def target(self, obj):
        if obj.content_object is None:
            return '-'

        return str(obj.content_object)

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'target','content_type', 'object_id', 'created_at']
    search_fields = ['user__username']
    readonly_fields = ['created_at']

    @admin.display(description='Target')
    def target(self, obj):
        if obj.content_object is None:
            return '-'

        return str(obj.content_object)

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following', 'created_at']
    search_fields = ['follower__username', 'following__username']
    readonly_fields = ['created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'short_content', 'target', 'content', 'content_type', 'parent','created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'content']
    readonly_fields = ['created_at', 'updated_at']

    @admin.display(description='Target')
    def target(self, obj):
        if obj.content_object is None:
            return '-'

        return str(obj.content_object)

    @admin.display(description='Comment')
    def short_content(self, obj):
        return obj.content[:50]
