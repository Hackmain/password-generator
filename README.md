# password-generator
simple password generator code in python


import random: هذا يستورد مكتبة random، والتي تحتوي على وظائف لإنشاء أرقام عشوائية.
import string: هذا يستورد مكتبة string، والتي تحتوي على سلاسل محددة مسبقًا من الأحرف والأرقام والرموز.
def generate_password(length): تعريف دالة جديدة تُسمى generate_password تأخذ مُدخل واحد يُسمى length يُحدد طول كلمة السر.
characters = string.ascii_letters + string.digits + string.punctuation: يُنشئ سلسلة من الأحرف تحتوي على حروف كبيرة وصغيرة وأرقام ورموز.
password = ''.join(random.choice(characters) for i in range(length)): يُنشئ كلمة سر عشوائية بطول length، باستخدام دوران loop لاختيار حرف عشوائي من السلسلة characters.
return password: تعيد كلمة السر التي تم إنشاؤها.
print(generate_password(12)): يطبع كلمة سر بطول 12 حرفًا.
هذا الكود يضمن أن كلمة السر ستكون قوية بمزجها بين الحروف الكبيرة والصغيرة والأرقام والرموز.



