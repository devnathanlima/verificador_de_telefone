import phonenumbers
from phonenumbers import geocoder, timezone, carrier

phone = input("Digite o telefone no formato +551140028922: ")
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
print(geocoder.country_name_for_number(phone_number, 'pt'))
print(timezone.time_zones_for_number(phone_number))
print(carrier.name_for_number(phone_number, 'pt'))
