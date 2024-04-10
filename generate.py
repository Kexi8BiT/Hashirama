import random
import string
import hashlib

# Исходный пароль
letters = string.ascii_lowercase
password = ''.join(random.choice(letters) for i in range(10))

hashed_passwd = ""
hash_list = ["sha1", "sha256", "sha512", "sha3_256", "sha3_384", "sha3_512"] # Список использующихся хэш-функций
lst = ['!', '@', '#', '$', '%', '&', '*', '—', '', '+', '=', ';', ':', '?']
# Генерация "соли" для дальнейшего хэширования
s = string.ascii_lowercase+string.digits
sault = ''.join(random.sample(s, 9))
password = password + sault # Добавление соли к изначальному паролю

# Функция хэширования
def hashirama(password):
    global hashed_passwd
    index = random.randrange(len(hash_list))
    h = hashlib.new(hash_list[index])
    h.update(bytes(password, 'utf-8'))
    hashed_passwd = h.hexdigest() + sault # Солим хэшированный пароль

# Выполнение хеширования, количество итераций равно длине списка с хэш-функциями
for i in range(len(hash_list)):
    in_hashing = hashed_passwd[:random.randint(10,40)]
    hashirama(password=hashed_passwd)

def generate_password():
    return f"{chr(random.randint(65,90))}{hashed_passwd[:random.randint(10,13)]}{random.choice(lst)}"