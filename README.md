# **Vehicle Tracking System**  

## **Overview**  
The **Vehicle Tracking System** is a web-based application that enables **real-time vehicle tracking**, **user role management (admin, driver, etc.)**, and **journey duration prediction** using machine learning. It has both frontend and backend components.  

## **Features**  
✅ **User Roles & Authentication** (Admin, Driver, etc.)  
✅ **Real-time Vehicle Tracking**  
✅ **Journey Duration Prediction** (using ML)  
✅ **Django Admin Panel** for managing users & vehicles  
✅ **Sqlite Database Integration**  

## **Technologies Used**  
### **Backend**  
- Django **5.1.7**  
- Sqlite3
- Scikit-Learn (for ML)  
- Pandas & NumPy (Data Processing)  

### **Frontend**  
- Django Templates  
- Crispy Forms (Bootstrap-based UI)  

## **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/CeliaIneza/transport_scheduling.git
cd transport_scheduling
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv venv 
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```



### **4️⃣ Apply Migrations**  
```bash
python manage.py migrate
```

### **5️⃣ Create a Superuser**  
```bash
python manage.py createsuperuser
```

### **6️⃣ Run the Server**  
```bash
python manage.py runserver
```
Now open **http://127.0.0.1:8000/** in your browser!   

## **Machine Learning Model**  
- Predicts **journey duration** based on past data.  
- Uses **Scikit-Learn** and **Joblib** for model training and deployment.  

## **Project Dependencies**  
```
asgiref==3.8.1
crispy-bootstrap4==2024.10
Django==5.1.7
django-crispy-forms==2.3
joblib==1.4.2
mysqlclient==2.2.7
numpy==2.2.4
pandas==2.2.3
python-dateutil==2.9.0.post0
pytz==2025.1
scikit-learn==1.6.1
scipy==1.15.2
six==1.17.0
sqlparse==0.5.3
threadpoolctl==3.6.0
tzdata==2025.1
```
