from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review 
# Task done using ModelSerializer


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        
        # To display all fields
        fields = "__all__"

        # To display some fields
        #fields = ['id','name','description']

        # To exclude some specific fields
        # exclude = ["id"]


    # getting the length of name 
    # def get_len_of_names(self, object):
    #     return len(object.title)
    
    # Field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Title too shorttoo short")
    #     else:
    #         return value

    # Object Level Validation
    # def validate(self, data):
        
    #     # Comparing that name should not be same as description
    #     if data['title'] == data['storyline']:
    #         raise serializers.ValidationError("Title and Storline must not be same")
    #     else:
    #         return data

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    # It displays only string related fields
    # watchlist =  serializers.StringRelatedField(many=True)

    # It displayes only primary key related fields
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # It displays url at the place of id
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='stream-details'
    # )
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"



# Task done using serializers.Serializer

# def desc_length(values):
#     if len(values) < 5:
#         raise serializers.ValidationError("Too short description")  # Field level Validation using validator


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[desc_length])
#     active = serializers.BooleanField(default=True)

#     def create(self, validate_data):
#         return Movie.objects.create(**validate_data)

#     def update(self,instance, validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.description = validate_data.get('description', instance.description)
#         instance.active = validate_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # Field level validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name too short")
#         else:
#             return value

#     # Object Level Validation
#     def validate(self, data):
        
#         # Comparing that name should not be same as description
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description must not be same")
#         else:
#             return data
        

    
