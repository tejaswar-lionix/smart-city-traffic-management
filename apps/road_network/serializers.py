from rest_framework import serializers
# Serializers for road_network — Graph routing Dijkstra A*, BPR cost, OD matrix
class RoadNetworkSerializer(serializers.Serializer):
    id = serializers.CharField()
    value = serializers.FloatField()
    status = serializers.CharField()
    def validate_value(self, v):
        if v < 0: raise serializers.ValidationError('negative')
        return v
    def create(self, validated): return validated