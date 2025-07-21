from rest_framework import serializers
from .models import WheelSpecification

class WheelSpecificationSerializer(serializers.ModelSerializer):
    fields = serializers.DictField(write_only=True, required=False)

    class Meta:
        model = WheelSpecification
        exclude = ['id']

    def to_internal_value(self, data):
        data = data.copy()
        fields_data = data.pop('fields', None)
        if not fields_data or not isinstance(fields_data, dict):
            raise serializers.ValidationError({
                'fields': ['This field is required and must be a valid object.']
            })
        merged = {**data, **fields_data}
        return super().to_internal_value(merged)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        field_keys = [
            'treadDiameterNew', 'lastShopIssueSize', 'condemningDia', 'wheelGauge',
            'variationSameAxle', 'variationSameBogie', 'variationSameCoach',
            'wheelProfile', 'intermediateWWP', 'bearingSeatDiameter',
            'rollerBearingOuterDia', 'rollerBearingBoreDia', 'rollerBearingWidth',
            'axleBoxHousingBoreDia', 'wheelDiscWidth'
        ]
        rep['fields'] = {key: rep.pop(key) for key in field_keys}
        return rep
