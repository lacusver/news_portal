from rest_framework import serializers
from .models import News, Comments, Likes

class CommentSerializer(serializers.ModelSerializer):
    news_title = serializers.ReadOnlyField(source='news.title')
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comments
        fields = ('news','news_title','content', 'user')


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
        model = Likes
        fields = "__all__"

    def create(self, validated_data):
        like, _ = Likes.objects.update_or_create(
            user=validated_data.get('user'),
            news=validated_data.get('news'),
            defaults={'liked':validated_data.get('liked')}
        )
        return like


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_name = serializers.ReadOnlyField(source='author.username')
    likes = serializers.IntegerField(read_only=True)
    comments = serializers.IntegerField(read_only=True)
    newscomment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = News
        fields = "__all__"