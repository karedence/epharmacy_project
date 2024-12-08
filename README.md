Project: Interactive E-Pharmacy Management System

The system aims at overcoming the challenges faced by patients in obtaining prescribed medications and helps pharmacies manage their inventory more efficiently. 
With the rise of e-commerce and digital health services, the system integrates cloud technology, machine learning, and real-time analytics to create a seamless experience
for both patients and pharmacists.

1.Overview
System Purpose	Addresses challenges in obtaining prescribed medications and managing pharmacy inventory efficiently.
Core Technologies	Combines cloud computing, machine learning, big data analysis, and responsive web technologies.
Target Users	Patients seeking medications and pharmacists managing inventory.
Main Deliverables	A dual-portal system with real-time updates, inventory management, and analytical dashboards.

Component	Description
Frontend	- Patient Portal: Built with HTML5, CSS3, and AJAX for a dynamic, interactive experience.
	- Pharmacy Portal: Uses HTML5 for structure, CSS3 for design, and AJAX for smooth user interactions.
Backend	- Developed using Django, a Python-based framework, handling all logic, database interactions, and authentication.
Database	- Utilizes Amazon RDS for a scalable and secure database solution, supporting efficient data management and access.
Real-Time Streaming	- Implemented Apache Kafka for real-time inventory updates and live monitoring of demand changes.
Data Analysis	- Powered by Hadoop for processing large datasets, providing insights into drug demand, stock levels, and trends.

2. System objectives:
2.1 Main Objective: To enables patients to search for and locate required medications efficiently while empowering pharmacies to manage inventory and
     predict demand trends effectively through machine learning and cloud.

Specific Objectives	Description
Patient Portal	- To provide secure login for patients.
	- To allow searching and locating prescribed medications in registered pharmacies.
	- To display availability, pricing, and pharmacy details.
Pharmacy Portal	-To enable pharmacies to register and manage inventory

3.Technical Implementation
Aspect	Details
Backend	Developed with Django for secure and modular backend architecture.
Frontend	Interactive and responsive interfaces built with AJAX, HTML5, and CSS3.
Database Management	Utilizes Amazon RDS for scalable, reliable, and high-availability relational data storage.
Real-Time Streaming	Apache Kafka manages live data updates for inventory and demand tracking.
Big Data Analysis	Hadoop analyzes extensive pharmacy and patient data to uncover patterns and forecast trends.
Analytics and Reporting	Dashboards using machine learning models provide visual insights into pharmacy performance.

4. How the project executed
4.1 Set Up the Project Environment
4.1.1 Installed Tools and Frameworks:
Python: 
Alread installed on the computer

Django project and MySQL client libraries:
Used the following commands
 django-admin startproject epharmacy
cd epharmacy
python manage.py startapp accounts
python manage.py startapp pharmacy
python manage.py startapp dashboard
pip install django mysqlclien

Hadoop Install and configuration for MapReduce functionality
Followed this link: https://www.youtube.com/watch?v=kUX6dCbdU3Q&t=1265s

Apache Kafka
Followed this link: https://www.youtube.com/watch?v=gE0sWA2kTfk&t=11s

Creating the Mysql database into Amazon WS RDS and connect it with Django
Followed this link: https://www.youtube.com/watch?v=HGOrsBzQrq0

4.1.2 Project structure
 
 epharmacy/
    epharmacy/
        settings.py
        urls.py
        wsgi.py
    accounts/
        models.py
        views.py
        urls.py
        forms.py
    pharmacy/
        models.py
        views.py
        urls.py
        forms.py
    dashboard/
        views.py
        urls.py
        hadoop_integration.py
        kafka_integration.py
    templates/
        base.html
        accounts/
            login.html
            signup.html
        pharmacy/
            medicine_list.html
            medicine_form.html
        dashboard/
            analytics.html
        Hadoop/
               mapper.py
               reducer.py
        Kafka/
            scriptrs/
    static/
        css/
        js/
5. Challenges and Solutions
Challenge	Description	Solution
Data Synchronization	Ensuring real-time inventory updates across multiple pharmacies.	Implemented Apache Kafka and WebSocket protocols for instant syncing.
Scalability	Handling surges in traffic during public health crises.	Leveraged elastic scaling and cloud load balancing solutions.
User Interface	Designing an intuitive platform for users with varying technical expertise.	Used AJAX for dynamic updates and responsive design principles.
Demand Forecasting	Predicting shortages or overstock based on fluctuating demand.	Implemented machine learning models (regression, LSTM) for accurate forecasting.
6. Future Out looks
Based on the current technological advancement and data analytics, the following have to be considered to improve the system:
-Uploading medical diagnostic reports and extract them using optical character recognition (OCR),
-Allowing the patients to order medicines online,
-Integration of tele-medicine in the E-pharmacy system,
-Allow patients to consult certified doctors via video or chat’
-Enable doctors to prescribe medications directly, which are automatically linked to the E-pharmacy system for easy procurements.

