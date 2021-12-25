from kavenegar import *
import datetime

# time now
time_now = datetime.datetime.now()

# time now just(month and day)
time = time_now.month , time_now.strftime("%d")

# date birth
date_birth = datetime.datetime(1991,10,5)

# date birth just(month and day)
birth = date_birth.month , date_birth.strftime("%d")

if time == birth:
  api = KavenegarAPI('55334B43664F5579436E35724264695A356579466257634470724835543670615779704771334B307970343D')
  params = { 
    'sender' : '1000596446', 
    # mobile number
    'receptor': '**********', 
    'message' :'happy birthday'  
}
  response = api.sms_send(params)

else:
    print('Your birthday is not now')
