class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num
        # self.isvalid=Luhn.check(self.card_num)
    
    def valid(self):
        card_num="".join(self.card_num.split())
        if str(card_num).isdigit() and len(str(card_num))>1:
            card_num=[int(d) for d in str(card_num)]
            odd_digits=card_num[-1::-2]
            even_digits=card_num[-2::-2]
            total_sum=sum(odd_digits) 

            for i in even_digits:
                if i*2<=9:
                    total_sum+=i*2
                else:
                    total_sum+=i*2-9
            return total_sum%10==0
        return False
