import streamlit as st
import numpy as np
from Interpolate import *
import matplotlib.pyplot as plt
from Perform_Interpolation import *
from Eval_Func import *
import pandas as pd

st.sidebar.title("""**Polynomial Interpolator**""")
st.sidebar.subheader("""*Receive a polynomial function that maps your given inputs to your given outputs*""")

st.sidebar.write("""""")

st.sidebar.write("""*Please separate all values with a space!*""")

st.sidebar.write("""""")
st.sidebar.write("""""")

st.sidebar.write("""""")
st.sidebar.write("""""")

a = st.sidebar.text_input("""Input values:""")

st.sidebar.write("""""")
st.sidebar.write("""""")

b = st.sidebar.text_input("""Output values:""")

x = list(map(int, a.strip().split()))
y = list(map(int, b.strip().split()))


def displayPolynom():
    if len(y) > 0 and len(x) == len(y):
        polynomial = PolyInterpolate(x, y)
        j = range(len(polynomial.find_coefficients()))
        l = range(len(polynomial.find_coefficients()))[1:]

        for i in j:
            a = f"""f(x) = {polynomial.find_coefficients()[0].round(6)}"""
            for i in l:
                if polynomial.find_coefficients()[i] > 0:
                    a += f""" + {polynomial.find_coefficients()[i].round(6)}x^{i}"""
                elif polynomial.find_coefficients()[i] < 0:
                    a += f"""{polynomial.find_coefficients()[i].round(6)}x^{i}"""
                else:
                    continue

        st.container()
        col1, col2, col3, col4 = st.columns(4)
        col1.subheader('Your Function')
        col1.latex(a)

        min = st.sidebar.text_input("""*Enter the starting value for the x-axis*""")
        col1.min

        max = st.sidebar.text_input("""*Enter the ending value for the x-axis*""")
        col1.max

        if min.isdigit():
            min = int(min)

        if max.isdigit():
            max = int(max)

        def eval(n):
            result = 0
            l = len(polynomial.find_coefficients())
            for k in range(n):
                for i in range(l):
                    Sum = polynomial.find_coefficients()[i]
                    term = Sum * ((k) ** i)
                    result += term
            return result

        def eval1(n):
            return eval(n) - eval(n - 1)

        def eval2(minimum=1, maximum=10):
            soltnLst = []
            for i in range(minimum, maximum + 1):
                soltn = eval1(i)
                soltn += 1
                soltnLst.append(soltn)
            return pd.DataFrame(np.array(soltnLst), index=range(minimum, maximum + 1))

        if min:
            st.line_chart(eval2(minimum=min, maximum=min+10))
            st.write("""*Note that the y-values for this chart are somewhat 
            inaccurate due to rounding error.*""")
        elif max:
            st.line_chart(eval2(maximum=max))
            st.write("""*Note that the y-values for this chart are somewhat 
            inaccurate due to rounding error.*""")
        elif min and max:
            st.line_chart(eval2(min, max))
            st.write("""*Note that the y-values for this chart are somewhat 
            inaccurate due to rounding error.*""")
        else:
            st.line_chart(eval2())
            st.write("""*Note that the y-values for this chart are somewhat 
            inaccurate due to rounding error.*""")

    else:
        st.write("""*Your input and output lists are different lengths!*""")


displayPolynom()
