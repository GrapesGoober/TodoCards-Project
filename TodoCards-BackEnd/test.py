import user
import decks
import mysql.connector

result = user.hash_password("ajarn123")
print(len(result))
print(result)
print(user.is_password_correct(result, "ajarn123"))

#ajarn ajarn123 6a195e4ec0e9de6a5d35562e4f920e72a57d4b9750ba00964756d2e9ff3290123ad74d0b75edf4f77d1c2ebe3d6c10c7

#bob bob123 4cbeba55bcfada7cf0142c53c101d9ac770abb26d02235b6f71a77d6d7f86bb10ac1e543dd8cbafcf8952c2d40528297

#cindy cindy123 42e97aa817224cb8b2d50562f2fb2933bef91495f6166b1e7f33701765db0cac598fd8abd828b5a92ae56a8d17f5eb3b

#dean dean123 782b68900f3f74ac2d5eeccf5791ea19f0ff5f9d21309be379b24a6767836f1cafedcaa379ab923f8ce28dfe441b87f8

#fay fay123 1429511ebd6b934780d07ae90f6715c018f97ace7001302dac2488e8a74ce8f311f1212d3c3154943757be6e80897a09

#------------------------------------------------
#check access
#def check_deck_view_access(mydb, deck_id, username):
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TodoCards"
)
checkview = decks.check_deck_view_access(mydb, 4, "dean")
print(checkview)

mydb.close()