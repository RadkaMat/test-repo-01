import streamlit as st
st.title('Aplikace generování barev')
st.write('Generátor náhodných barev do čtverce 5x5')
obrazek = [[1,1,1,1],[1,0,1,0],[1,1,1,1],[1,0,0,0],[1,1,0,1],]
from matplotlib import pyplot as plt
plt.imshow(obrazek, cmap = 'gray')
plt.colorbar()
