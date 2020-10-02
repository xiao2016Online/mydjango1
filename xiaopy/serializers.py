from rest_framework import serializers

from xiaopy.models import User


class UserSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=36)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    sex = serializers.BooleanField()

    class Meta:
        # 要指定验证字段
        fields = '__all__'
        # 指定的模型类
        model = User
        # extra_kwargs = {"field_name":{"write_only":True}}

    def create(self, validated_data):
        print('序列化%s' % validated_data)
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
