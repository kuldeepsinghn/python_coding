# API - Application Programming Interface

## what is an API?
- it is mechanism that enables two software components to communicate with each other.
- it provides set of definations and protocols
- it provides the limited data to client 
- it not provides client to get the personal data from server
- API architecture is usually explained in terms of client and server
- The application sending the request is called the client
- the application sending the response is called the server

- There are four different ways that APIs can work depending on when and why they were created. 
## 1.SOAP APIs 
- Simple Object Access Protocol. Client and server exchange messages using XML 
- This is a less flexible API that was more popular in the past.

## 2.RPC APIs
- These APIs are called Remote Procedure Calls. The client completes a function (or procedure) on the server, and the server sends the output back to the client. 

## 3 Websocket APIs
- Websocket API is another modern web API development that uses JSON objects to pass data
-  A WebSocket API supports two-way communication between client apps and the server. 
- The server can send callback messages to connected clients, making it more efficient than REST API.


## 4.REST APIs
- REST stands for Representational State Transfer. 
- These are the most popular and flexible APIs found on the web today 
- The client sends requests to the server as data.
- The server uses this client input to start internal functions and returns output data back 
- The main feature of REST API is statelessness
- statelessness means  that servers do not save client data between requests
- Client requests to the server are similar to URLs you type in your browser to visit a website.

## What is web API?
- it  is an application processing interface between a web server and web browser
- All web services are APIs but not all APIs are web services.
- rest api is a special type of api that uses the standard architectural style


## what are API integration?
- it is a software components that automatically update data b/w client and server.

## benefits of rest APIs
- 4 main benefits
- 1.Integration - it is integrated new applications with existing software systems.
  - it increases development spped because each fucntionality doesn't have written from scratch.
  - it can be used to leverage the code 
  - 
## HTTP Request and Response 

- HTTP - Hpyer Text Transfer Protocol
- so baiscally protocol set of rules so how the communications should happen it w il define 



- let's assume there is a client and server
-       client  --------->    server
-            request

-       client <-----------  server
-               response

- so it happens for the how using HTTP it is called request response cycle 

- the communication happen using request and response

## request in rest:
- to make valid request , the client need to include 4 things
- 1. URL(Uniform Resource Locator)
- 2. method
- 3. List of Header
- 4. Body


### 1. URL:
- it is a easy way to communicate with server
- it tells server what or which things client wants to interact, called resources


### 2. Method:
- it tells the server what kind of action the client wants server to take.
- there are 4 method which are used commonly in APIs are:
- 1.Get --- asks the server to reterive the server
- 2.Post --- asks the server to create a new resource
- 3.Put -- asks server to edit or update an existing resources
- 4.Delete -- asks  server to delete a resource 


### 3.Headers
- headere provide meta_info about request.

### 4. Body :
- the request body contains the data the clients wants to send the server/


- eg:- URL -- http://website.com
-  Method -- POst
-  Header -- user-agent
-  Body -- data 


### response in rest 
- the server response with the status code 
- status code - verify each and every action you will an status code
- status code 3 digit numbers

- eg:- status code -- 200(ok)
-      Headers -- content-type:text
-      Body -- data


### data formats:
- a well designed format is dictated by what makes the info the easiest for the intended audience to understand
- the most common formats found  APIs are
- 1.JSON
- 2.XML

- Json - it is very simple format that has two peices -- 'key'and 'value'
- ex: {"name":"api"}

- XML - it provides some building blocks
- the main block is called node
- it always start from root node inside that we have child nodes.

- ex :- opening tag --><name>api</name> <-- closing tag



### how data formats in HTTP:
- using header we can inform server what info we are sending and what we are expecting in return



- content:type: when the clients send the content-type it says what format the data is.
- accept : the accept header tells server what data it is able to accept



-   client ----------------------->   server
-       accept:"application/json"

-   client <------------------------ server
-         content-type:"application/json"



