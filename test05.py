# คำสั่งรับค่าข้อความ  string ทางแป้นพิมพ์ ใช้ฟังก์ชั่น input()
# ตัวแปร varible คือ ชื่อที่ Dev ตั้วฃงขึ้นมาเอง(ต้องเป็นไปตามกฎการตั้งชื่อ)เอาไว้เก็บข้อมูลที่เกิดขึ้นในโปรแกรม

fullname = input('ป้อนชื่อ : ')
year_born = input('ป้อนปีเกิด พ.ศ.: ')
print('----------------')
print(f'สวัสดีคุณ{fullname}')
print(f'คุณเกิดปี {year_born}ตอนนี้คุณอายุ{2568 - int(year_born)}')
print('---------------------')
#ใช้ ,
print('สวัสดีคุณ',fullname,'คุณเกิดปี พ.ศ.: ',year_born)
print('ตอนนี้คุณอายุ',(2568 - int(year_born)))
print('---------------------')
#ใช้ +
print('สวัสดีคุณ'+fullname+'คุณเกิดปี พ.ศ.: '+year_born)
# ใช้ format
print('สวัสดีคุณ'{}'คุณเกิดปี พ.ศ.: '{}format(fullname,year_born)
print('ตอนนี้คุณอายุ{}'.format(2568 - int(year_born)))
print('---------------------')
