import streamlit as st
import pickle


model = pickle.load(open('random_forest_model.pkl','rb'))

def mlr_prediction(age, meno, size, grade,nodes, pgr, er, hormon, rfstime):
    a = str(age)
    b = float(meno)
    c = float(size)
    d = float(grade)
    e = float(nodes)
    f = float(pgr)
    g = float(er)
    h = float(hormon)
    i = float(rfstime)

    prediction = model.predict([[a,b,c,d,e,f,g,h,i]])
    #print(prediction)
    #return abs(prediction)

    # Conver prediction to status
    if prediction[0] == 0:
         return "Being alive without recurrence"
    else:
         return "Recurrence or death"

def main():
     #web title
     st.title('Breast Cancer Recurrence Predictor')
     st.markdown('Predict the likelihood of recurrence or death based of patient information and tumor characteristics.')

     #Define the fron end elements of the web page like the font and background color, the padding and the text
     html_temp = """

     """
     
     #This line allows us to display the front end aspects we gave defined in the above code
     st.markdown(html_temp, unsafe_allow_html = True)

     #The following code creates text boxes in which the user can include the data requered to make the predictions
     st.header('Patient information')
     age = st.text_input('Age')
     meno = st.text_input('Menopausal status (0=premenopausal, 1=postmenopausal)')
     st.header('Tumor information')
     size = st.text_input('Tumor size (Range 3-120)')
     grade = st.text_input('Tumor grade (Range 1-3)')
     nodes = st.text_input('Number of positive nodes (Range 1-51)')
     pgr = st.text_input('Progesterone receptors measured in fmol/l (Range 0-2380)')
     er = st.text_input('Estrogen receptors measured in fmol/l (Range 0-1144)')
     hormon = st.text_input('Hormonal therapy given(0= no therapy, 1=receiving therapy)')
     rfstime = st.text_input('Recurrence-free survival time in days (Range 1-2659)')
     result = ""

     #The code below ensures theat when the 'Predict bottun is click the mlr_prediction fuction defined above is called
     if st.button("Predict"):
          result = mlr_prediction(age, meno, size, grade,nodes, pgr, er, hormon, rfstime)
     st.success("The status is: {}".format(result))

if __name__=='__main__':
     main()
