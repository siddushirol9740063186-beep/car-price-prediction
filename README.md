🚗 Car Price Prediction

📌 Project Overview  
This project uses Machine Learning to predict the resale price of used cars. Users can input car details and get an estimated price instantly through a simple web interface built with Streamlit.

---

📊 Dataset  
The model is trained on the CarDekho dataset, which includes features like:  
- Year of purchase  
- Present price  
- Kilometers driven  
- Fuel type  
- Seller type  
- Transmission  
- Number of owners  

---

⚙️ Technologies Used  
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

🚀 Features  
- Predict car price instantly  
- Clean and user-friendly interface  
- Fast and accurate predictions  
- Real-time web app using Streamlit  

---

📂 Project Structure  
car-price-prediction/  
│── app.py                  (Streamlit application)  
│── model.pkl               (Trained ML model)  
│── car_data.csv            (Dataset)  
│── car_price_model.py      (Model training code)  
│── requirements.txt        (Dependencies)  

---

▶️ How to Run Locally   

1. Install dependencies  
pip install -r requirements.txt  

2. Train the model (creates model.pkl)  
python car_price_model.py  

3. Run the Streamlit app  
streamlit run app.py  

---

🌐 Deployment (Streamlit Cloud)  

1. Push all files to GitHub  
2. Go to https://streamlit.io/cloud  
3. Click "New App"  
4. Select your repository  
5. Choose app.py  
6. Click Deploy  

---

📈 Output  
The application predicts the estimated resale price of a car based on user inputs.

---

👨‍💻 Developed By  
Siddu Shirol  

---

📌 Future Improvements  
- Improve model accuracy  
- Add more features (brand, fuel efficiency, etc.)  
- Enhance UI design  
- Deploy with custom domain  

---

⭐ Acknowledgment  
Dataset provided by CarDekho  
