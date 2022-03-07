import re
from rest_framework import serializers
from flightApp.models import Flight,Passenger,Reservation
import re

# Naming way is not fixed, has all the data(dictionary)
# Second priority
def isFlightNumberValid(data):
    # Logic
    print(data)


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields='__all__'
        validators = [isFlightNumberValid,]

    # First priority to run for a perticular field, automatically runs, Fixed naming way validate_fieldName
    def validate_flightNumber(self,flightNumber):
        if(re.match("^[a-z,A-Z,0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Invalid Flight Number. Make sure it is alphanumeric")
        return flightNumber

    # Generic validations will run after all the perticular validations are complete, Last Priority
    def validate(self, data):
        print(data)
        # Logic
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'
