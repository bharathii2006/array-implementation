MAX_SIZE=5
stack=[]
top=-1
def push(book_title):
    global top
    if top>=MAX_SIZE-1:
        print("Stackoverflow!cannot push more books:")
    else:
        top+=1
        stack.append(book_title)
        print(f"book{book_title}pushed into the stack")

def pop():
    global top
    if top==-1:
        print(f"stack underflow!cannot pop any book")
    else:
        removed_book=stack.pop()
        print(f"book popped from {removed_book} the stack")
        top-=1

def peek():
    if top==-1:
        print("stack in empty.No book to peak")
    else:
        print(f"top book on the stack:{stack[top]}")


def display():
    if top==-1:
        print("stack is empty")
    else:
        print("books in stack (top to bottom):")
        for i in range(top,-1,-1):
            print(f"{i+1}.{stack[i]}")


push("harrypotter")
push("ponniyin selvan")
push("mahabharatam")
push("the hobbert")
push("we met again stangers")
display()
peek()
pop()
pop()
display()
peek()

              
