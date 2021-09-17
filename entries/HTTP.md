# HTTP
Also known as Hyper Text Transfer Protocol

# Requests
`GET / HTTP/1.1`
`Host: www.example.com`

This request has two lines.
- Line 1
	- `GET` > the type of request
	- `/`  > the specified directory of the request, in this case the home directory
	- `HTTP/1.1` > which version of HTTP to use
- Line 2
	- `Host: www.example.com` > the website we're making the request to

# Responses
`HTTP/1.1 200 OK`
`Content-Type: text/html`

This response has two lines.

- Line 1
	- `HTTP/1.1` the http version of the response
	- `200` the response code
	- `OK` the human readable interpretation of the response code
- Line 1
	- The format of the data returned


# Common HTTP Status Codes
200 - Everything's good
301 - Moved permanently
403 - Forbidden
404 - Not Found
500 - Internal Server Error