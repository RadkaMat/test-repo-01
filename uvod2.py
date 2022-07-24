import streamlit as st
st.title('Aplikace generování barev')
st.write('Generátor náhodných barev do čtverce 5x5')
def create_image2(color_pic):    
    from numpy import random
    from matplotlib import pyplot as plt
    color_pic = random.random((5,5))
    img = plt.imshow(color_pic)
    img.set_cmap('inferno')
    plt.title('inferno')
    plt.axis('off')
    plt.savefig("test.png")
    obrazek4 = [[]]
