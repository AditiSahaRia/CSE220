class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            print(idx+1, end='. ')
            profit = self.calcProfit(array[idx])
        #TO DO
        if idx < len(array):
            self.print(array, idx+1)

    def calcProfit(self,investment):
        #TO DO
        if investment == 25000:
            print(f'Investment: {investment}; Profit: 0.0')
        elif investment <= 100000:
            val = ((investment-25000)/100)+((investment-25000)/100)+((investment-25000)/100)+((investment-25000)/100)+(((investment-25000)/100)/2)
            print(f'Investment: {investment}; Profit: {val}')
        else:
            val1 =((investment-100000)/100)+((investment-100000)/100)+((investment-100000)/100)+((investment-100000)/100)+((investment-100000)/100)+((investment-100000)/100)+((investment-100000)/100)+((investment-100000)/100)
            val2 = (75000+75000+75000+75000+(75000/2))/100
            print(f'Investment: {investment}; Profit: {val1+val2}')



#Tester
array=[25000,100000,250000,350000]

f = FinalQ()
f.print(array,0)
#--------------------