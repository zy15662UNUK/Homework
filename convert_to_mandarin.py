
def convert_to_mandarin(us_num):
 trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si','5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
 int_us_num = int(us_num)
 ten_digi = int_us_num // 10
 one_digi = int_us_num % 10
 if ten_digi == 0:
     one_digi_pro = trans[str(one_digi)]
     return one_digi_pro
 elif one_digi == 0:
     if ten_digi == 1:
         return 'shi'
     else:
         ten_digi_pro = trans[str(ten_digi)]
         return ten_digi_pro + ' '+ 'shi'
     
 else:
     if ten_digi == 1:
         one_digi_pro = trans[str(one_digi)]
         return 'shi'+ ' '+ one_digi_pro
     else:
         ten_digi_pro = trans[str(ten_digi)]
         one_digi_pro = trans[str(one_digi)]
         return ten_digi_pro + ' '+ 'shi'+' '+one_digi_pro
         
     
    
     
