print("************************************************************")
print("**********  type start with your desired action.  **********")
print("commands :\n --a - paste contect stright into CL without open")
print("************************************************************")
ans = input("Enter txt path ")
sd = "\\"

if ans[-3::] == "--b":
    text = input("Enter html code :\n")
    html = text
    newhtml = html.replace("//","\//").replace("\"",sd+"\"",)
    print("content:\n\n\n\n")
    print(newhtml)

elif ans[-3::] == "--a":
    path = input("Enter path of the file:")
    with open(path, "r+") as file:
        html = file.read()
        newhtml = html.replace("//","\//").replace("\"",sd+"\"",)
    with open(path[0:-4]+"_new.txt","w") as file1:
        file1.write(newhtml)



