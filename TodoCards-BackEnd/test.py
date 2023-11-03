import user

result = user.hash_password("password1234")
print(result)
print(user.is_password_correct(result, "password1234"))