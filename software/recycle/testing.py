from twilio.rest import Client

client = Client("AC6e0cc6c973c287570f121a12718e9db5", "b29af806cb1a081efe276158be9d2032")

# message = client.calls.create(
#       from_='+13605357953',
#       to='+2347084375332',
#       twiml="<Response><Say>Adeyemi, please we come to notice that you are at longitude and latitude which is not far from the a recycle bin that is full. Please kindly dispose the plastic bin, thank you.</Say></Response>"
#   )

# print(message.recordings)
# # print(message.Status().RINGING)
# # print(message.Status().BUSY)
# # print(message.Status().CANCELED)
# # print(message.Status().COMPLETED)
# # print(message.Status().FAILED)
# # print(message.Status().NO_ANSWER)
# # print(message.Status().QUEUED)
# # print(message.Status().IN_PROGRESS)
# while message.fetch().status != "no-answer" and message.fetch().status != "completed":
#   ins = message.fetch()
#   print(ins.status)
#   if ins.status == "in-progress":
#     print(ins.to)
validation_request = client.validation_requests.create(
  phone_number="+2347084375332",
  friendly_name="adeyemi"
)
print(validation_request)
                    