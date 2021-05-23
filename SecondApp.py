__author__ = 'Venkatarami Reddy'

import streamlit as st
import pandas as pd


def second_app():
  st.title('Second Application')
  st.header('Names Information')
  st.subheader('Family Names')
  df = pd.DataFrame({'Family Names': ['Venkat', 'Nageshwaramma', 'Krishna', 'Manishree']})
  st.write('Family Members are', df)
  
  
if __name__ == '__main__':
  second_app()
