from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from volunteering_module.models import VolunteerMotivator, CertificateForVolunteer


class BaseVolunteerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = VolunteerMotivator
        fields = '__all__'
        abstarct = True


class VolunteerSerializer(BaseVolunteerSerializer):

    class Meta:
        model = VolunteerMotivator
        fields = ('id', 'title', 'description', 'start', 'end', 'user', )


class VolunteerDetailSerializer(BaseVolunteerSerializer):

    class Meta:
        model = VolunteerMotivator
        fields = '__all__'


class BaseCertificateSerializer(serializers.ModelSerializer):
    volunteer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CertificateForVolunteer
        fields = '__all__'
        abstract = True


class VolunteerCertificateSerializer(BaseCertificateSerializer):
    class Meta:
        model = CertificateForVolunteer
        fields = ('id', 'title', 'volunteer')


class VolunteerCertificateDetailSerializer(BaseCertificateSerializer):
    created = serializers.DateTimeField(read_only = True)
    updated = serializers.DateTimeField(read_only = True)
    user_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = CertificateForVolunteer
        fields = ('id', 'volunteer_id', 'title', 'number', 'file', 'created', 'updated', 'user_id')
        validators = [
            UniqueTogetherValidator(
                queryset = CertificateForVolunteer.objects.all(),
                fields = ('volunteer_id', 'user_id')
            )
        ]
