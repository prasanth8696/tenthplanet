def check_imei(imei):
        
        if len(imei) != 15 :
            return False
        
        try :
            digits = list(map(int,imei))
            doubled_digits = [  value * 2 if index % 2 != 0 else value  for index,value in enumerate(digits)]
            sum_value = sum([ sum([ int(digit) for digit in str(value) ]) if value > 9 else value for value in doubled_digits])
            
            if sum_value % 10 == 0 :
                return True
            else :
                return False 
            
            
        except ValueError :
            return False
