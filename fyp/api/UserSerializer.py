
from rest_framework.response import Response
from rest_framework import serializers
from api.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('rating', 'phone', 'about', 'address')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name',
                  'last_name', 'password', 'patient_status', 'doctor_status', 'admin_status', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)

        instance.patient_status = validated_data.get(
            'patient_status', instance.patient_status)
        instance.doctor_status = validated_data.get(
            'doctor_status', instance.doctor_status)

        instance.admin_status = validated_data.get(
            'admin_status', instance.admin_status)

        instance.save()

        profile.phone = profile_data.get('phone', profile.phone)
        profile.about = profile_data.get('about', profile.about)
        profile.rating = profile_data.get('rating', profile.rating)
        profile.address = profile_data.get('address', profile.address)
        profile.save()

        return instance

    def delete(self, instance):
        instance.delete()
        return instance

    def get_user_by_id(self, username):
        user = User.objects.get(username=username)
        return user

    def logout(self, request):
        request.user.logout()
        return Response(status=status.HTTP_200_OK)
