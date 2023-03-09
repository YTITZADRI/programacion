# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
 
cuerpo = input("Entrada: ")
message = input("Que mensaje quieres enviarle?: ")
cantidad = int(input("Cuantas veces quieres enviarlo?: "))





correos = ["baques.romeu.eric@institutvalles.cat","portana.gelabert.jan@institutvalles.cat","soler.pacheco.arnau@institutvalles.cat","zamora.gomez.david@institutvalles.cat"]


# send the message via the server.
i = 0
while i < len(correos):

	msg = MIMEMultipart()

	password = "Adria2007!"
	msg['From'] = "cabrera.luque.adria@institutvalles.cat"
	msg['Subject'] = cuerpo
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
 
#create server
	server = smtplib.SMTP('smtp.gmail.com: 587')
 
	server.starttls()
 
# Login Credentials for sending the mail
	server.login(msg['From'], password)
 
 
	a = 0
	msg['To'] = correos[i]
	print(correos[i])
	while a < cantidad:
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		print("successfully sent email to %s:" % (msg['To']))
		a += 1
	server.quit()
	i += 1


 
