def tupper(user_input) :
    return  user_input.upper()

def totitle(user_input) :
    return  user_input.title()

def save_to_file(user_input,A,B) :
    with open("/Users/mdharmal/Desktop/output2.txt",'w') as ff :
        ff.write(user_input + " " + A + " " + B )
def read_the_file() :
    with open ("/Users/mdharmal/Desktop/output2.txt", 'r') as ff:
        data = ff.readline()
        print("data writtern in file is : " , data)


def main() :
    user_input = input("Enter your name : ")
    A = totitle(user_input)
    B = tupper(user_input)
    print("Titled input : ",A)
    print ("upper input : ", B)
    save_to_file(user_input,A,B)
    print("Done writing to the file. ..")
    read_the_file()


if __name__ == "__main__" :
    main()