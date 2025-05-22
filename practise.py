import streamlit as st
import pandas as pd

st.write("### 你好，世界！")

"可以直接展示字符串"

a = 888 * 4
a


[11,22,33]

{"c":"hhh","b":"888"}

st.title("这是一个练习网站💧")


t1,t2,t3=st.tabs(["哈哈","很爱很爱你","djawhkd"])

with t1:


    st.image("微信图片_20240607174558.jpg",width=500)

    df = pd.DataFrame({"学号":["01","02"],"姓名":["傻逼","夏良宇"]
    })

    st.dataframe(df)
    st.divider()
    st.table(df)

    name = st.text_input("请输入名字：")
    if name:
        st.write(f"### 你好,{name}")

    st.text_input("请输入密码：",type="password")

    paragraph = st.text_area("说100个哈")


with t2:
    st.number_input("输入年龄：", value=1, min_value=0,max_value=100, step=1)

    check = st.checkbox("同意以上条款")
    if check:
        st.write("谢谢")

    anle = st.button("对了")
    if anle:
        st.write("## 草泥马")

    gender = st.radio("你的性别",["男","女","未知"], index=None)

    if gender:
        st.write(f"你的性别是{gender}")

    contact = st.selectbox("你喜欢什么",["苹果","香蕉","其他"])

    st.write(f"好的，{contact}")

    fruits = st.multiselect("你喜欢什么",["苹果","香蕉","其他"])

    for fruit  in fruits:
        st.write(f"{fruit}")

    with st.expander("身高信息"):
        nima = st.slider("你的身高是多少厘米", value=70, min_value=100, max_value=200,step=1)

        st.write(f"## {nima}")


with t3:
    ok = st.file_uploader("上传文件", type=["png","jpg","jpeg","py"])
    if ok:
        st.write(f"你上传的文件是{ok.name}")
        st.write(f"文件内容{ok.read()}")





