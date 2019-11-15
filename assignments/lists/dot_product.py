#Write a Python program that calculates the dot product of two given vectors
def vector(size):
    vector = []
    for elements in range (size):
        vector_element = input("Element no " +str(elements+1)+": " )
        vector.append(vector_element) 
    return vector

def dot_product(vector1,vector2):
    dot_product = 0
    for elements in range (len(vector1)):
        dot_product += float(vector1[elements]) * float(vector2[elements])
    return dot_product


def main():
    vector_size = int(input("Input vector size: "))
    vector1 = vector(vector_size)
    vector2 = vector(vector_size)
    print (dot_product (vector1,vector2))

main()



