#character in string has index number
        #01234567890123
infoA = 'Hello I Sad Na Hee 55555'
    # 43240987654321 ติดลบ -
print(infoA[6])
print(infoA[-9])

#เข้าถึงตัวอักษรหลายๆ ตัวใน string เราจะใช้วิธี slicing ด้วย index number
# na hee
print(infoA[12:18])
print(infoA[-12:-6])

# o sau 20
print(infoA[4:12])

#String Method
print(infoA.upper()) #ทำให้ String เป็นตัวพิมม์ใหญ่
print(infoA.lower()) #ทำให้ string เป็นตัวพิมม์เล็ก
print(infoA.capitalize()) #ทำให้หน้าประโยคเป็นพิมใหญ่
print(infoA.title()) #ทำให้ตัวหน้าเป็นพิมใหญ่
print(infoA.count("Hee")) #นับ string
print(infoA.isdigit()) #method is เอาไว้พิสูจน์บางใดบางอย่าง
print(infoA.isupper()) #พิสูจน์ ว่าพิมม์ใหญ่หมดมั้ย
infoB = infoA.replace("Hee","Mee") #ใช้เเทน string ที่อยากเเทนที่
print(infoB)
print(infoB.replace('Hello','Yeeeeee'))

#String Function 
print(len(infoA)) #ใช้นับตัวอักษรทั้งหมด ใน info ที่ต้องการให้เเสดง

print("Hee","Mee",35,end=" ")
print("Hee"+"Mee"+str(35))
print("Hee",35,sep="")
print("04",'09',"2003",sep="/") #sep สามารถนำมาเเบ่งหรือใส่อะไรก็ได้ระหว่าง ","
print("04",'กันยายน',"2003",sep="-")
