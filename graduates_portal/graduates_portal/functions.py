from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# def send_email(user,hash,template,subject):
# 	htmly = get_template(template)
# 	d = Context({ 
#         'username': str(user.username),
#         'name' : str(user.first_name),
#         'hash' : hash
#         })
#     html_content = htmly.render(d)
#     return requests.post(
#         "https://api.mailgun.net/v3/portal.tggroup.kz/messages",
#         auth=("api", "key-abaa952d6eb9e3680d396982d31486e7"),
#         data={"from": "Upgrade Land <no-reply@upgrade-land.kz>",
#               "to": user.email,
#               "subject": subject,
#               "html": html_content
#               })

# def send_confirm_message(user,hash):
#     send_email(user,hash,"invite.html","Активация аккаунта в Upgrade Land")

# def send_reset_message(user,hash):
#     send_email(user,hash,"restore.html","Восстановление пароля в Upgrade Land")

def send_email():
	message = Mail(
		from_email='Graduates Portal <no-reply@portal-graduates.kz',
		to_emails=user.email,
		subject='Доброго времени суток! Прошу пройти по ссылке для потдверждения.',
		html_content='<strong>and easy to do anywhere, even with Python</strong>')
	try:
		sg = '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'
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(e.message)
		send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)

def send_confirm_message(user,hash):
    send_email(user,hash,"invite.html","Активация аккаунта в Upgrade Land")

def send_reset_message(user,hash):
    send_email(user,hash,"restore.html","Восстановление пароля в Upgrade Land")
