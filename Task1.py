import pandas as pd

def fun(url):
    c = pd.read_csv(url)
    print(c)

try:
    url = input("Enter URL - ")
    fun(url)
except FileNotFoundError:
    print("The entered URL is not correct")

