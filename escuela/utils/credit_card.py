from datetime import datetime
class credit_card():

    def __init__(self, credit_card_number, expiry):
        self.credit_card_number = credit_card_number
        self.expiry = expiry

    def credit_card_validator(self):
        #Siguiendo el algoritmo de luhn para verificar las tarjetas
        if str(self.credit_card_number).isalnum:
            return False

        # Invirtiendo la targeta para 
        reversed_credit_card = str(self.credit_card_number)[::-1]
        # validacion de tarjeta
        numero_final = 0

        #Primer paso
        for i in range(1,len(reversed_credit_card), 2):
            if int(reversed_credit_card[i])*2 > 9:
                modulo = (int(reversed_credit_card[i])*2)%10
                numero_final = numero_final + 1 + modulo
            else:
                numero_final = numero_final + int(reversed_credit_card[i])*2

        for i in range(0,len(reversed_credit_card),2):
            numero_final = numero_final + int(reversed_credit_card[i])

        if(numero_final%10 == 0):
            return True
        
        return False
    
    def expiry_validator(self):
        
        try:
            date = datetime.strptime(str(self.expiry), "%Y-%m-%d").date()
            if date >= datetime.now().date():
                return True
        except:
            return False
        return False
    
    def cc_type_validator(self):
        match int(str(self.credit_card_number)[0]):
            
            case 2:
                #Evaluando para mastercard caso: 2221 y 2720
                if str(self.credit_card_number)[0:4] in ["2221","2720"]:
                    if len(str(self.credit_card_number)) == 16:
                        return True
            case 3:
                 #Evaluando para american express
                 if str(self.credit_card_number)[0:2] in ["34","37"]:
                    if len(str(self.credit_card_number)) == 15:
                        return True

            case 4:
                #Evaluando para visa
                if(len(str(self.credit_card_number)) == 16):
                    return True
            
            case 5:
                #Evaluando para mastercard caso: 51 y 55
                if str(self.credit_card_number)[0:2] in ["51","55"]:
                    if len(str(self.credit_card_number)) == 16:
                        return True
            case _:
                return False

    def final_evaluation(self):
        if self.credit_card_validator() and self.expiry_validator() and self.cc_type_validator():
            return True
        return False








