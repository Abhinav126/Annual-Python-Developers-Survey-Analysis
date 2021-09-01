import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Python Developer Survey Analysis')

@st.cache
def load_data():
    return pd.read_csv('Data/2020_sharing_data_outside.csv', low_memory=False)

@st.cache
def load_ques():
    return pd.read_csv('Data/Python Developers Survey questions_outside.csv')

df = load_data()
ques = load_ques()

def show_plot(func,col):
    data = df[col].value_counts()
    st.markdown(ques[ques.shortname == col]['question_title'].iloc[0],unsafe_allow_html=True)
    st.plotly_chart(func(None,data.index,data.values))

def multi_col(func,name):
    names = [i for i in df.columns if i.startswith(name)]
    values = [list(df[i].value_counts())[0] for i in names]
    names = [i.split('.')[-1] for i in names]
    st.markdown(ques[ques.shortname == name]['question_title'].iloc[0],unsafe_allow_html=True)
    st.plotly_chart(func(None, names, values))


def page0():
    st.title('Python Developer Survey Analysis')
    st.image('scaled-python.jpeg')
    st.header('NTCC Project 2021 (Annual Python Developers Survey Analysis)')
    st.image('AMITY.jpg')
    
    st.markdown("""
    **Name**: Abhinav Kumar Pathak\n
    **Batch**: 2019-2022\n
    **Enrollment NO**: A7304819056\n
    **Name of NTCC**: Summer Internship 2021 – 1 (ETSI101)\n
    **Faculty Guide’s Name**: Dr. Shahnaz Fatima
    """)
    st.success('Welcome to Data Analysis')
    st.image('unnamed.jpg')
    st.subheader('Annual Python Developers Survey Analysis ',)
    
    st.write('So here in the project will see that about how many peoples are on the world uses python language in day-to-day life how many peoples like this Python language and how many peoples would prefer to use it in future so by using data analytics collecting data from different sources we will collect the data and see that annually how many peoples are you using Python or any other language they prefer to use. The survey asked participants about which tools and features of the languages they used the most often. 90% of developers use Python’s version control system “at least sometimes”. Code refactoring is used by 89% and autocomplete is used by 88% of developers.')
    
    st.subheader('Why the developer or the people uses Python the most as any other languages ?')
    st.write('1-) Python language is incredibly easy to use and learn for new beginners and newcomers. The python language is one of the most accessible programming languages available because it has simplified syntax and not complicated, which gives more emphasis on natural language. Due to its ease of learning and usage, python codes can be easily written and executed much faster than other programming languages.')
    st.write('2-) Mature and Supportive Python Community : There are plenty of documentation, guides and Video Tutorials for Python language are available that learner and developer of any skill level or ages can use and receive the support required to enhance their knowledge in python programming language.')
    st.write('3-) Support from Renowned Corporate Sponsors : Programming languages grows faster when a corporate sponsor backs it. For example, PHP is backed by Facebook, Java by Oracle and Sun, Visual Basic & C# by Microsoft. Python Programming language is heavily backed by Facebook, Amazon Web Services, and especially Google.')
    st.write('4-) Hundreds of Python Libraries and Frameworks: Due to its corporate sponsorship and big supportive community of python, python has excellent libraries that you can use to select and save your time and effort on the initial cycle of development. There are also lots of cloud media services that offer cross-platform support through library-like tools, which can be extremely beneficial.')
    st.write('There are many frameworks and libraries are available for python language, such as:')
    st.write('matplotib for plotting charts and graphs')
    st.write('SciPy for engineering applications, science, and mathematics')
    st.write('BeautifulSoup for HTML parsing and XML')
    st.write('NumPy for scientific computing')

    st.write('5-) Versatility, Efficiency, Reliability, and Speed : Ask any python developer, and they will wholeheartedly agree that the python language is efficient, reliable, and much faster than most modern languages. Python can be used in nearly any kind of environment, and one will not face any kind of performance loss issue irrespective of the platform one is working.')
    



def page1():
    st.title('Question and plots')
    st.write('See The new world')
    show_plot(px.pie,'is.python.main')
    st.info('80% percent people uses python as there main language')
    multi_col(px.bar,'other.lang')
    st.info('Other Language Java Script and HTML/CSS is used the most')
    show_plot(px.pie,'main.purposes')
    st.info('Most of the people uses python for work and personal use ')
    multi_col(px.pie,'other.purposes')
    multi_col(px.bar,'cloud.platform')
    st.info('AWS cloud platform people uses the most')
    multi_col(px.pie,'run.in.cloud')
    multi_col(px.bar,'develop.for.cloud')
    multi_col(px.pie,'devenv.os')
    multi_col(px.bar,'orm')
    multi_col(px.bar,'database')
    show_plot(px.pie,'ide.main')
    multi_col(px.bar,'ide.editor')
    multi_col(px.bar,'web.frameworks')
    multi_col(px.bar,'data.frameworks')
    multi_col(px.bar,'other.frameworks')

def page2():
    st.header('Country wise number of respondents')
    data = df['country.live'].value_counts()
    st.markdown(ques[ques.shortname == 'country.live']['question_title'].iloc[0],unsafe_allow_html=True)
    st.plotly_chart(px.scatter(None,data.index,data.values,data.index,size=data.values))
    show_plot(px.bar,'age')

def page3():
    st.title('About this Analysis')
    st.markdown ("This project is helping me in an analysis of annually how many people use this in Python language are any other languages which they prefer to use, what they think about the Python language is, how it works, how it is useful, why they prefer to use Python, which other programming language they are using, what are the other platforms, what more things they want to update in Python features and what more they want from Python. The data which we have collected shows us that about 80% from all the countries users Python as their main. The data also shows us that other languages like HTML, JavaScript, CSS is used the most. People also use Python for their personal use, for storing cloud services people mostly uses AWS cloud platform. For web framework and libraries they uses Django most. The data also so us that most of the people uses Python are from United States because we get more response from United States. So this project “Annual Python Developer Survey Analysis” provides us the information about the data which we have collected and provides us useful meaning full information. ")
    st.image('21249.jpg')


def page4():
    st.title('View Data Set')
    st.write(df.head(12300))

pages = {
    'Introduction' : page0,
    'View Data Set' : page4,
    'Survey results' : page1,
    'About responders' : page2,
    'About project' : page3,
    }

page = st.sidebar.radio('Select a page',list(pages.keys()))

pages[page]()
