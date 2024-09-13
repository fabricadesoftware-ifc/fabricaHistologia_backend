from core.posts.models import Posts, Point
from rest_framework import serializers

class PointRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields: list[str] = [
            "id",
             "label_title",
             "description",
             "position",
             "color",
             "posts",
             "analyzed_structures",
             "analyzed_functions",
        ] 

class PointWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields: list[str] = [
             "label_title",
             "description",
             "position",
             "color",
             "posts",
             "analyzed_structures",
             "analyzed_functions",
             
        ] 

class PostsRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields: list[str] = [
            "id",
            "date_analysis",
            "post_date",
            "species",
            "type_cut",
            "increase",
            "coloring",
            "image",
            "autor_user",
            "organ",
            "type_post",
        ]
    

class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields: list[str] = [
            "species",
            "image",
            "autor_user",
            "organ",
            "type_post"
        ]
      

class PostsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields: list[str] = [
            "date_analysis",
            "post_date",
            "species",
            "type_cut",
            "increase",
            "coloring",
            "image",
            "autor_user",
            "organ",
            "type_post"
        ]
        