# Common HTTP Status codes

## What is a HTTP status code?
- HTTP status codes are part of the status-line of a HTTP response.
- it is 3-digit integer codes indicate the result of the servers attempt to satisfy the request.

- The first digit of the status-code is used to categorize the response:
- 1xx: Informal
- 2xx: Success, the request has been understood and accepted
- 3xx: Redirection, further action needs to be taken
- 4xx: Client error, there was a problem with the request
- 5xx: Server error, the request has been accepted, but the processing failed due to a server error


### Commonly used HTTP status codes 
### HTTP 200 OK 
- it means the request has succeeded
- it is often used as the default status code to indicate that everything worked as expected.

### HTTP 201 Created
- the request has succeeded and a new resource has been created.
- it used after  a resource has been created by a POST or PUT request (see REST: Creating resources). 
- The Location header field can be used to return the URI(s) of the newly created resource.
- Note that the resource must be created before 201 is returned.

### HTTP 202 Accepted 
- The request has been accepted, but the processing has not been completed. 


### HTTP 204 No Content 
- The request succeeded, but there is no content to send for this request.
- When sending 204 the response body must be empty. Updated meta-information can be passed in response headers.

### HTTP 304 Not Modified
- This status code is used for caching purposes when a client issued a conditional GET request.
- 304 is returned with an empty response body to indicate that the resource has not been modified
- In case the resource has been modified, the resource should be returned with a status code 200 (OK).

### HTTP 307 Temporary Redirect
- The URI of the target resource has been temporary changed and current URI is given in the response Location header.
- Temporary Redirect indicates that the client should use the original request URI for future requests.

### HTTP 308 Permanent Redirect
- Like 307 this status code is used when the target resource URI has been changed.
- 308 indicates that the URI change is permanent and clients should use the updated URI for future requests.


### HTTP 400 Bad Request
- The request has been received, but the server is unable to process it due to malformed request syntax
- The client should not repeat the request without modification. 
### HTTP 401 Unauthorized
- The request lacks credentials and cannot be authenticated. Note that this status code is badly named, it is used to indicate missing authentication not missing authorization.

### HTTP 403 Forbidden
- The client is authenticated, but does not have the permission to use the given request method on the requested resource.
- It is also viable to respond with HTTP 404 (Not Found) in these situations if the server wants to hide the resource.
- The client should not repeat the request (without changing credentials).
- If the client is not authenticated at all, HTTP 401 should be returned instead.

### HTTP 404 Not Found
- The server has not found the requested URI and is therefore unable to process the request.

### HTTP 405 Method Not Allowed
- The server does not allow the requested HTTP method for the given URI.
- eg:- he request specifies the PUT method for a resource that only supports GET and POST. The response must include an Allow header containing a list of valid request methods for the requested resource

### HTTP 409 Conflict
- the request could not be completed due to a conflict with the current state of the resource
- This code must only be used in situations where the user might be able to resolve the conflict and reissue the request.

### HTTP 500 Internal Server Error
The server has encountered a situation it is unable to handle. This is the standard status code for unexpected error on the server during the request processing

