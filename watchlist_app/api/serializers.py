from rest_framework import serializers
from watchlist_app.models import Movie

# Task done using ModelSerializer

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        
        # To display all fields
        fields = "__all__" 

        # To display some fields
        #fields = ['id','name','description']

        # To exclude some specific fields
        # exclude = ["id"]


    
    # Field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name too short")
        else:
            return value

    # Object Level Validation
    def validate(self, data):
        
        # Comparing that name should not be same as description
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description must not be same")
        else:
            return data





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
        

    
