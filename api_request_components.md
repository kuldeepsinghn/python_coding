# HTTP Request components
#### HTTP request is called a "resource", whose nature isn't defined further; it can be a document, a photo, or anything else
## 1. Resource URI
- A Uniform Resource Identifier (URI) is a character sequence that identifies a logical (abstract) or physical resource -- usually, but not always, connected to the internet.
- A URI distinguishes one resource from another.
- A Uniform Resource Identifier (URI) is a character sequence that identifies a logical (abstract) or physical resource -- usually, but not always, connected to the internet. A URI distinguishes one resource from another.
- The strings of characters incorporated in a URI serve as identifiers, such as a scheme name and a file path.
- In the URI, the file path may be empty.

### How Uniform Resource Identifiers work
- A URI provides a simple, extensible way to identify internet resources.
- The resource identifiers can also be reused in different contexts.
- URIs can identify different types of resources, including:
- 1.electronic documents
- 2.webpages
- 3.images
- 4.information sources with a consistent purpose


#### every URL is URI but not vice versa

- Uniform Resource Identifier syntax
- The generic form of any URI scheme is

#### [//[user:password@]host[:port]][/]path[?query][#fragment]

- A URI may consist of the following elements:(discuss it latter)
- 
- 1.Scheme
- 2.Authority
- 3.query(optional)
- fragment(optional)

### types of URI
#### 1.URL(Uniform resource Locator)
#### 2.URN(Uniform Resource Names)
#### 1.Uniform Resource Locator (URL)
-  A URL is used to identify and locate webpages
- A URI identifies a resource but does not imply or guarantee access to it.
- but a URL identifies the resources and also specifies how it can be accessed or where it is located
- This is why a URL contains unique components, such as the protocol, domain and/or subdomain, in addition to other URI components.

- A URL is a subset of URIs. This means all URLs are URIs.
- A URL is a location-dependent URI that may or may not be persistent
- This means that if the resource's location changes, the URL also changes to reflect and point to the new location.
- URL examples:

- https://www.techtarget.com/whatis/definition/URI-Uniform-Resource-Identifier

- https://datatracker.ietf.org/doc/html/rfc3986

- https://www.w3.org/Addressing/URL/uri-spec.html

#### 2. URN (Uniform Resource Name)
- Like a URL, a URN identifies a resource. 
-  a URN is location-independent and persistent, meaning that it always identifies the same resource over time.
- A URN continues to persist even when the resource no longer exists or becomes unavailable.
- A URN does not state which protocol should be used to locate and access the resource. Instead, it labels the resource with a persistent, location-independent and unique identifier.
-  it has 3 components
- 1.The label "urn"
- 2.A colon
- 3.A character string as the unique identifier
- URN examples (provided by IETF RFC 2986):

- urn:oasis:names:specification:docbook:dtd:xml:4.1.2
- urn:example:animal:ferret:nose 



### uri vs url
- the "URI" and "URL" are different. 
- A URI is an identifier of a specific resource while a URL is a special type of identifier that identifies a resource and specifies how it can be accessed.
- The analogy of a person's name and address can explain this difference. In this case, the name is the URI because it identifies the person. However, it doesn't explain how the person can be found or where they live. For this, the address or URL is required.
## 2. HEADERS
- The HTTP headers are used to pass additional information between the clients and the server through the request and response header. 
- these are case-sensitive and seperated by colon and in key-value pair
- The end of the header section denoted by an empty field header.

#### There are four kinds of headers context-wise:  
- 1.General Header: it applied on Request and Response headers both but with out affecting the database body.
- 2.Request Header: it contains information about the fetched request by the client.
- 3.Response Header: it contains the location of the source that has been requested by the client.
- 4.Entity Header: it contains the information about the body of the resources like MIME type, Content-length.


#### Headers can also be categorized according to how proxies handle them:  
- Connection
- Keep-Alive
- Proxy-Authenticate
- Proxy-Authorization
- TE
- Trailer
- Transfer-Encoding
- Authentication


#### header Authorization :- It is used to request restricted documents.
#### Proxy-Authenticate :-	It is a response header gives access to a resource file by defining an authorization method. It allows the proxy server to transmit the request further by authenticating it.
#### Proxy-Authorization :-	It is a request type of header. This header contains the credentials to authenticate between the user agent and the user-specified server. 
#### WWW-Authenticate :-	It is a response header that defines the authentication method. It should be used to gain access to a resource.

#### Caching 
- age
- cache control
- clear-site-data
- expires
- pragama
- warnings


### client hints
- accept-CH
- Accept-CH-Lifetime
- Content-DPR	
- DPR
- Device memory
- early data
- save data
- viewport-width
- width
- .......... to be continued(learn latter)

## 3.Authorization


## 4. Body


