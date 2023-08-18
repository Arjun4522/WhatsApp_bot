import pywhatkit as kit
import time

message = input("Enter the message you want to send: ")


recipient_numbers = []


num_recipients = int(input("Enter the number of recipients: "))

for i in range(num_recipients):
    country_code = input(f"Enter the country code for recipient {i+1}: ")
    number = input(f"Enter the phone number for recipient {i+1} (without country code): ")
    recipient_numbers.append({"country_code": country_code, "number": number})

for recipient in recipient_numbers:
    full_number = f"+{recipient['country_code']}{recipient['number']}"
    kit.sendwhatmsg_instantly(full_number, message)
    print(f"Message sent to {full_number}")

    time.sleep(20)

print("All messages sent.")
