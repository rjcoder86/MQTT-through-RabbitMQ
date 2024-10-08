# MQTT-through-RabbitMQ

## Overview

This project involves generating status messages using RabbitMQ with MQTT, consuming these messages to store them in MongoDB, and exposing an API with FastAPI to retrieve message counts within a given time range.


## Setup Instructions

### Prerequisites

- Python 3.6+
- RabbitMQ
- MongoDB

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/rjcoder86/MQTT-through-RabbitMQ.git
2. **Create a Virtual Environment**

    ```sh
    python3 -m venv env
    source env/bin/activate
3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
4. **Set Up Mongodb**

- Download and install MongoDB from MongoDB official site.
- Start MongoDB server

5. **Set Up RabbitMQ**

- Install RabbitMQ:

    #### On Windows
    Download the RabbitMQ installer from the official RabbitMQ website and follow the instructions.

    - Start RabbitMQ:

    #### On Windows
    Run the RabbitMQ Server from the Start Menu or using the command prompt:

    
    rabbitmq-server.bat


#### File Structure
```
    MQTT-through-RabbitMQ/
    ├── images 
    │   ├── swagger_output1.png
    │   └── swagger_output12.png 
    ├── main.py            
    ├── consumer.py        
    ├── app.py             
    ├── mongo_connector.py  
    ├── requirements.txt  
    └── README.md
```

**Run the Project**

 - Start Rabbitmq message generator
  ```sh
    py main.py
```

 - Start Consumer server
  ```sh
    py consumer.py
```
 - Start FastAPI Application
  ```sh
    py app.py
```

**Component Details**

`main.py`

Generates status messages with values from 0 to 6 every second and publishes them to a RabbitMQ queue using MQTT.

`consumer.py`

Consumes messages from the RabbitMQ queue, processes them, and stores them in MongoDB.

`app.py`

Provides a FastAPI endpoint to retrieve the count of status messages stored in MongoDB within a specified time range.

`mongo_connector.py`

Contains a MongoDB connector class that handles data insertion and retrieval operations.



**FastAPI endpoints**

- GET /get: Retrieves count of status messages for a given time range.

Parameters:

- start_time (string or list): Start time in "HH:MM:SS
" format or list [YYYY, MM, DD, HH, MM, SS].
- end_time (string or list): End time in "HH:MM:SS
" format or list [YYYY, MM, DD, HH, MM, SS].

- sample output

![Sample Image](images/swagger_output2.png)

![Sample Image](images/swagger_output1.png)
