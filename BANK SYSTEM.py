print('_'*80)
print('\t','+'*5,'welcome to DIGNITY INTERNATIONAL BANK','+'*5)
print('_'*80)
activity = input('\t\tAre you here to check your account balance ?(yes/no) : ').lower()
print('_'*80)
if activity == 'yes':
    print("\t\tAlright,please supply the following details; ")
else :
    quit()

    

NAME= input('please,enter your fullname : ').upper()
GENDER=input('please,select your gender (male/female) : ').lower()
MARITALSTATUS= input('Marital status (single/married) : ').lower()
PASSWORD = input ('input your password : ').upper()

BANKRECORD ={'AYOOLA FAITH':'$230,000',
              'TONY STARK':'$450,000',
              'BASHEER HAADI':'$900,895,000',
              'PETER PARKER':'$143,000',
              'STEVE ROGGERS':'$320,000',
              'ANTONY JOSHUA':'$560,000',
              'ROMAN REIGNS' : '$349,000',
              'WWILLIAM BRANHAM':'$450,000',
              'FOLARIN ALIYAT':'$456,000',
              'SOLADOYE KOREDE':'$414,450',
              'AWOLADE PEACE':'$469,900',
             'IGE MICHEAL':'$678,000',
              'ADEYEMO FOLASAYO':'$786,900'}

if NAME in BANKRECORD :
    if GENDER == 'male':
        print('_'*80)
        print('Mr',NAME,'your account balance is : ',BANKRECORD.get(NAME))
        print('_'*80)
    elif GENDER == 'female' and MARITALSTATUS=='married':
        print('_'*80)
        print('Mrs',NAME,'your account balance is : ',BANKRECORD.get(NAME))
        print('_'*80)
    elif GENDER == 'female' and MARITALSTATUS=='single':
        print('_'*80)
        print('Miss',NAME,'your account balance is : ',BANKRECORD.get(NAME))
        print('_'*80)
else :
    print('sorry,it seems like you are not our customer')


