# Kindle update your API URL
from `https://codechef-api.vercel.app/{handle of user}` to `https://codechef-api.vercel.app/handle/{handle of user}`







# CodeChef REST API

This is a RESTful API built with Node.js that allows users to retrieve data of other CodeChef users using their handle.
The API uses web scraping techniques with fetch, JSDOM, and Express to fetch and parse the required information.
You can use prebuild components of heatmap and rating graph with various themes to add in you project.
Visit [Here](https://codechef-api.vercel.app) for more info

#### If you like it please star it 🥺

## API Reference
https://codechef-api.vercel.app/handle/handle_of_user

#### Get all items

```http
  GET /handle/{your codechef handle}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `handle` | `string` | **Required**. Codechef handle of user|


### Components 

##### Heatmap: 
![image](https://github.com/user-attachments/assets/7477d725-8d20-4385-b146-e13ca1591626)

##### Rating Graph:
![image](https://github.com/user-attachments/assets/d8f809be-eb7f-41c4-8e7f-69ff292699de)



## Authors

- [@deepaksuthar40128](https://www.github.com/deepaksuthar40128)


## Demo

 https://codechef-api.vercel.app/handle/one_deepak


## Installation

Install my-project with npm

```bash
  npm install
  cd codechef-api
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/deepaksuthar40128/Codechef-API
```

Go to the project directory

```bash
  cd codechef-api
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```



