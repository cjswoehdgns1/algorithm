b=input()
a={
'c=': 'č',
'c-':'ć',
'dz=': 'dž',
'd-': 'đ',
'lj':'lj',
'nj':'nj',
's=':'š',
'z=':'ž',
}
for i in a:
    if( b.find(i) != -1):
        b = b.replace(i, "|")
print(list(b).__len__())
