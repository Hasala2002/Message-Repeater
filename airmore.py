from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from pyairmore.services.device import DeviceService

ip=IPv4Address("192.168.1.5")
session=AirmoreSession(ip)

# print(session.is_server_running)
was_accepted = session.request_authorization()
# print(was_accepted)
service = MessagingService(session)
# for i in range(10):
# phnum= str(input('Enter the phone number you want to sent to:\n'))
# msg= str(input('Enter your message:\n'))
# itr= int(input('How many times:\n'))
# for i in range(itr):
#     service.send_message(phnum, msg)

service = DeviceService(session)
details = service.fetch_device_details()
# print(details.power)
# print(details.is_root)
print(details.brand)
print(details.device_name)

