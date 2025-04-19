Word_number=input("Enter a worded number: ")
Word_number+=" Stop"
Word_number=Word_number.title()
Word_number=Word_number.replace("And","")
Word_number=Word_number.replace("-"," ")
Word_number=Word_number.replace(",","")
Word_number=Word_number.replace(".","")


number_dictionary={"Zero":0,"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Eleven":11,"Twelve":12,"Thirteen":13,"Fourteen":14,"Fifteen":15,"Sixteen":16,"Seventeen":17,"Eighteen":18,"Nineteen":19,"Twenty":20,"Thirty":30,"Forty":40,"Fifty":50,"Sixty":60,"Seventy":70,"Eighty":80,"Ninety":90}                
Words_To_Numbers={"Hundred":"0"*2,"Thousand":"0"*3,"Million":"0"*6,"Billion":"0"*9,"Trillion":"0"*12,"Quadrillion":"0"*15,"Quintillion":"0"*18,"Sextillion":"0"*21,"Septillion":"0"*24,"Octillion":"0"*27,"Nonillion":"0"*30,"Decillion":"0"*33}


Word_List=Word_number.split()


Numbers=[]


n=""
sp=0
for i in range(len(Word_List)):
    if Word_List[i]!="Hundred" and Word_List[i] not in number_dictionary:
        if Word_List[i]=="Stop" and Word_List[i-1]=="Hundred":
            n+=str(number_dictionary[Word_List[i-2]])+"0"*2
            Numbers.append(int(n))
        elif Word_List[i-1]=="Hundred":
            n+=str(number_dictionary[Word_List[i-2]])+"0"*2
            n+=Words_To_Numbers[Word_List[i]]
            Numbers.append(int(n))
        else:
            try:
                TL=Word_List[sp:i]
                if "Hundred" in TL:
                    TL.remove("Hundred")
                c=0
                for k in TL:
                    if "ty" in k:
                        c+=1
                    if number_dictionary[k]>=10 and number_dictionary[k]<=19:
                        c+=1
                if c==0 and len(TL)!=1:
                    TL.insert(1,"Zero")
                if c==0 and len(TL)==1:
                    TL.insert(0,"Zero")
                for j in range(len(TL)):
                    try:
                        if "ty" in TL[j]:
                            n+=str(number_dictionary[TL[j]]+number_dictionary[TL[j+1]])
                            break
                        
                        else:
                            n+=str(number_dictionary[TL[j]])
                    except:
                        n+=str(number_dictionary[TL[j]])
                if Word_List[i]!="Stop":
                    n+=Words_To_Numbers[Word_List[i]]
                Numbers.append(int(n))
            except:
                pass
        n=""
        sp=i+1
        
print(sum(Numbers))
