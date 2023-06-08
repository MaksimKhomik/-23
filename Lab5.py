from num2words  import num2words
name = input("Як вас звати? ")
print("Привіт, " + name + "! Ця програма переведе введене вами число в словесне представлення.")
phone_num = input("Будь ласка, введіть номер телефону: ")
print("Ви ввели номер", phone_num)
num = int(input("Введіть число, яке потрібно перевести в словесне представлення: "))
num_word = num2words(num, lang='uk')
print("Число", num, "у словесному вигляді:", num_word)
