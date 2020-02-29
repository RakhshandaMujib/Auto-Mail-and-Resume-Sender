import smtplib
from email.message import EmailMessage 

#**********Some gloabal data**********
EMAIL_ADDRESS = 'youremailid@gmail.com' 
EMAIL_PASSWORD = 'yourpwd'
name_email = dict()

def get_recipients():
	"""
	Creates a dictionary of recipients called 'name_email' with the keys as 
	the name of the recipient and the values as their e-mail ID. 
	"""
	num =  int(input('How many companies do you want to send the mail to?'))
	print("Enter the name of the companies and their e-mail IDs separated by ','")
	for company in range(num):
		name, e_id = input().split(',')
		name_email[name.strip()] = e_id.strip()	

def create_msg(company):
	"""
	Creates a message object ready to send to the recipients.
	Argument:
		company - A dictionary item, with the name and e-mail ID of the
				  recepient.
	Returns:
		msg - The message object to be sent. 
	"""
	msg = EmailMessage() #Creating an EmailMessage object.

	#Create the message:
	msg['Subject'] = 'Application for the position of a Data Analyst Intern.'
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = name_email[company]
	msg.set_content(f"Hello!\n\nI am Rakhshanda Mujib and I am writing this "\
		   "mail to you to apply for the position of a Data Analyst Intern at" \
		   f"{company} as a part of my Summer Internship Program (21 May"\
		   " 2020 to 16 July 2020). \n\nWarm regards\nRakhshanda\n"
		   "+91 9007392826\n\nEnclosure: Resume")


	#Attach the file:
	with open('your resume along with the path and extention', 'rb') as resume:
		resume_data = resume.read()
		resume_name = resume.name
	msg.add_attachment(resume_data, maintype = 'application',
					   subtype = 'octet-stream', filename = resume_name)
	
	#Return the message object:
	return msg

def main():
	"""
	Driver function:
	- Gets the details of recipients.
	- Connects to the e-mail server.
	- Sends e-mails to the recipients. 

	"""
	
	#Get details of the recipients:
	get_recipients()
	
	#Using the context manager to connect to our mail server, here Gmail.
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo() #Identifies itself with the mail server being used.
		smtp.starttls() #Encrypting the traffic. 
		smtp.ehlo() #Re-identifies as an encrypted connection.
		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #Login with the credentials.

		for company in name_email:
			msg = create_msg(company) #Get the message.
			print(f'\nSending e-mail to {company}...') 
			smtp.send_message(msg) #Send message.
			print(f'E-mail to {company} sent successfully!') #Success message.


if __name__ == '__main__':
	main()