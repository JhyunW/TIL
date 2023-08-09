e_arr = ['b''b''c''a']
result = 0
e_result = [''.join(e_arr)]
print(e_result)
print(e_result[0][::-1])
if e_result == e_result[::-1]:
    result += 1

print(result)