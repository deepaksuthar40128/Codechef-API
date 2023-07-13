
# CodeChef REST API

This is a RESTful API built with Node.js that allows users to retrieve data of other CodeChef users using their handle.
The API uses web scraping techniques with Axios, JSDOM, and Express to fetch and parse the required information.

## API Reference
https://codechef-api.vercel.app/handle_of_user
#### Get all items

```http
  GET /handle
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `handle` | `string` | **Required**. Codechef handle of user|


## Authors

- [@deepaksuthar40128](https://www.github.com/deepaksuthar40128)


## Demo

 https://codechef-api.vercel.app/one_deepak


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


## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express

