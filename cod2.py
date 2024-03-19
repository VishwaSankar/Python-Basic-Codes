st=str("This is an example for the programming journey in python")
st1="AMAZING123"
st2="H\tE\tL\tL\tO"
print(st.endswith("python"))
print(st2.expandtabs(2))
print(st.index("an"))
if(st1.isalnum()):
    print("The string is alphanumeric")
else:
    print("It is not alphanumeric")

title="the amazing spiderman"
tit=title.split(" ")
print(tit)
x="###".join(tit)
print(x)
st4="Hulk"
print(st4.center(20,"*"))
print(st4.ljust(20,"0"))

