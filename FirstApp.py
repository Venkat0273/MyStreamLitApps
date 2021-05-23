__author__ = 'Venkatarami Reddy'
import streamlit as st
import numpy as np
import pandas as pd
import cx_Oracle as Oracle


def db_config():
    engine = Oracle.makedsn('localhost', '1521', service_name='orcl')
    con = Oracle.connect(user='scott', password='scott', dsn=engine)
    return con


def first_app():
    connection = db_config()
    cur = connection.cursor()
    st.title('My First App')
    st.header('First App')
    st.subheader('My First App')
    st.button('Click to Submit', key='submit')
    st.checkbox('Check', value=False, key='check')
    st.radio('IDs', options=('ID1', 'ID2', 'ID3'))
    st.text('Employee records from database')
    db_nam = st.sidebar.selectbox('Database Names', ('Venkat', 'SMITH', 'KING'))
    st.write(db_nam)
    query = """SELECT 'EMPLOYEE NAME IS: ' || ENAME || ' AND HE IS EARNING ' || SAL || '$' FROM EMP
                WHERE ENAME = :db_nam"""
    res = cur.execute(query, (db_nam,)).fetchall()
    # st.write(res)
    for rec in res:
        st.write(rec)
    records = st.sidebar.selectbox('Employees', res)
    st.write(records)
    inp = st.text_input('Enter some value')
    st.write('You have entered: ', inp)
    inp_2 = st.text_area('Enter some text here:')
    st.write('You have entered: ', inp_2)
    names = st.sidebar.selectbox('Names', ('Venkat', 'Naga', 'Manishree'))
    st.write('U have selected', names)
    st.write('Data Below')
    st.write(pd.DataFrame({'First': [1, 2, 3],
                           'Second': [2, 3, 4],
                           'Third': [3, 4, 5],
                           }
                          )
             )

    data = pd.read_csv('C:\\Users\\Manishree\\OneDrive\\Desktop\\train.csv', header=0)
    st.write('Data from Desktop')
    st.write(data.loc[1:4, ['id', 'vendor_id']]
             )
    side = st.sidebar.selectbox('Which ID?', data.loc[2:5, 'id'].tolist())
    st.write(side)
    conditional_data = data.loc[data.loc[:, 'id'] == side, ['id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime']]
    data_id, data_vendor_id, data_pick_date, data_drop_date = \
        conditional_data.id.values, conditional_data.vendor_id.values, conditional_data.pickup_datetime.values\
            , conditional_data.dropoff_datetime.values
    st.write(f'The ID You have selected {data_id} \n and it\'s vendor id is {data_vendor_id}\
                and pick up date time is {data_pick_date} and drop date time is {data_drop_date}')

    code = """def func():
    print('Its a function')
            """
    st.code(code, language='python')

    df = pd.DataFrame({'Col1': [1, 2, 3, 4], 'Col2': [2, 3, 4, 5]})
    st.dataframe(df)
    st.table(df)


first_app()
