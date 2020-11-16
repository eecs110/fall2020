from apis import sendgrid



# Your task:
# 1. Send an email to a friend
# 2. Send an email that has an (appropriate) image
#    to a friend. Example:
#    <img src="https://i.pinimg.com/236x/73/49/d8/7349d83b8e7ba1dc97e7e33304c8a7c8--persian-cats-for-sale-teacup-persian-cats.jpg" />
# CAVEAT: 
#    I have a dashboard that allows me to see every email that's
#    getting sent. These are not anonymous. Sarah can see all of the messages.
#    Just wanting to make sure that you know this.

# help(sendgrid)
is_successful = sendgrid.send_mail(
    'vanwars@northwestern.edu',
    'vanwars@northwestern.edu', # if you want to send to multiple ppl, use a list.
    'Testing',
    'Here is an image: <img src="https://i.pinimg.com/236x/73/49/d8/7349d83b8e7ba1dc97e7e33304c8a7c8--persian-cats-for-sale-teacup-persian-cats.jpg" />'
)
print('success:', is_successful)