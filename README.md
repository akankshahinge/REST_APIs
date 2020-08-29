# REST APIs
This repo consists of basics related to REST APIs

### What is API?
An API is a program that takes in some data and gives back some other data, usually after processing it.
### Example
Twitter search accepts data, process it and sends data back.
### API consists of three parts
1. User: the person who makes a request
2. Client: the computer that sends the request to the server
3. Server: the computer that responds to the request
### How APIs works?
Imagine a waiter in a restaurant.  You, the customer, are sitting at the table with a menu of choices to order from, and the kitchen is the provider who will fulfill your order.

You need a link to communicate your order to the kitchen and then to deliver your food back to your table. It can’t be the chef because she’s cooking in the kitchen. You need something to connect the customer who’s ordering food and the chef who prepares it.  That’s where the waiter — or the API —  enters the picture.

The waiter takes your order, delivers it to the kitchen, telling the kitchen what to do. It then delivers the response, in this case, the food, back to you.
### There are four types of actions an API can take:

1. GET: requests data from a server — can be status or specifics (like last_name)
2. POST: sends changes from the client to the server; think of this as adding information to the server, like making a new entry
3. PUT: revises or adds to existing information
4. DELETE: deletes existing information

Difference between UPDATE and PUT is that, UPDATE will update existing resources and PUT will first check for resources and if there is no resource then it will create a resource and if there is a resource then it will update it.
