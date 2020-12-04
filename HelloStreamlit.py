import streamlit as st
import pandas as pd
import numpy as np


st.title('My first App')

st.write('データフレーム')
st.write(

    pd.DataFrame({
        '1st columns': [1, 2, 3,4],
        '2nd columns': [10, 20, 30, 40]
    })
)#ページ上でクリックとかするとそーとできる

"""
# My first App
## マジックコマンド
こんな感じでマジックコマンドを使用できる。MarkDown対応
"""
if st.checkbox('Show DataFrame'):
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    st.line_chart(chart_df)

# 詳しくはドキュメント参照
