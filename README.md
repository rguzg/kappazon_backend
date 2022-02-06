# Kappazon Backend
Kappazon is the world's newest online marketplace!

This repository is for Kappazon's backend. This backend exposes the following endpoints:

## No Auth Endpoints

### POST /api/token

If provided with a valid username and password, this endpoint will return an **access token** that can be used to authenticate future requests as well as a **refresh token**.

The access token will expire after an hour. To get a new token, call [`/api/token/refresh`](#POST-/api/token/refresh).

The returned tokens have the following claims:
- User's full name
- User's user type
- User's image URL

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
  "username": "john_doe@mail.com",
  "password": "pas$w0rd"
}
```

#### Response

If a valid username and password was provided:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
  "access": "<JWT_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>" 
}
```

If an invalid username or password was provided:
- **HTTP Status Code**: 400 or 401

### POST /api/token/refresh

If provided with a valid refresh token, this endpoint will return an **access token** that can be used to authenticate future requests.

The access token will expire after an hour. To get a new token, call this endpoint again.

The returned token has the following claims:
- User's full name
- User's user type
- User's image URL

#### Request

- **Content-Type**: application/json
- **Request Body**:

```json
{
  "refresh": "Example_Refresh_Token"
}
```

#### Response

If a valid refresh token was provided:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
  "access": "Example_Token"
}
```

If an invalid password was provided:
- **HTTP Status Code**: 400 or 401

### POST /users/create_customer

Creates a new customer user.

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
    "email": "john.doe@email.com",
    "password": "pas$w0rd",
    "first_name": "John",
    "last_name": "Doe", 
    "birthdate": "03/12/2019",
    "gender": "male",
    "image_url": "Example URL"
}
```

#### Response

If the user was created successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "email": "john.doe@email.com",
    "password": "pas$w0rd",
    "first_name": "John",
    "last_name": "Doe", 
    "birthdate": "03/12/2019",
    "gender": "male",
    "image_url": "Example URL"
}
```

If the user wasn't created successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 400
- **Response Body**:
```json
{
  "error": "Error Description",
}
```

## Auth Endpoints

Endpoints that require authentication must send a valid JWT token in the `Authorization` header using the following format:
`Authorization: Bearer <JWT_TOKEN>`. If the token is invalid, or the token doesn't provide sufficient permissions the request will be rejected with an 403 status code.

### GET /user

Returns the current user's information

#### Response

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "first_name": "John",
    "last_name": "Doe", 
    "birthdate": "03/12/2019",
    "email": "john.doe@email.com",
    "gender": "male",
    "user_type": "customer"
}
```

## POST /user

Modifies the current user's information. For changing the password, use /user/change_password.

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
    "first_name": "John",
    "last_name": "Doe", 
    "birthdate": "03/12/2019",
    "gender": "male",
    "image_url": "Example URL"
}
```

#### Response

If the user was modified successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "email": "john.doe@email.com",
    "password": "pas$w0rd",
    "first_name": "John",
    "last_name": "Doe", 
    "birthdate": "03/12/2019",
    "gender": "male",
    "image_url": "Example URL",
    "user_type": "Customer"
}
```

If the user wasn't modified successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 400
- **Response Body**:
```json
{
  "error": "Error Description",
}
```

### GET /cart

Returns the current user's cart information

#### Response

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "total_price": 000, 
    "total_items": 3, 
    "items": [
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        },
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        },
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        }
    ]
}
```

### POST /cart

Adds/Modifies an item on the current user's cart. If the item is already in the cart, the quantity will be updated. If the item is not in the cart, it will be added to the cart.

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
    "product": "product_id",
    "quantity": 5,
}
```

#### Response

If the item was added successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "total_price": 000, 
    "total_items": 3, 
    "items": [
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        },
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        },
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        }
    ]
}
```
If the cart item wasn't added successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 400
- **Response Body**:
```json
{
  "error": "Error Description",
}
```
### DELETE /cart

Deletes an item on the current user's cart. Calling this endpoint has the same effect as calling `POST /cart` with a quantity of 0.

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
    "product": "product_id",
}
```

#### Response

If the item was deleted successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "total_price": 000, 
    "total_items": 2, 
    "items": [
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        },
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "price": 100,
            "quantity": 1
        },
    ]
}
```
If the cart item wasn't added successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 400
- **Response Body**:
```json
{
  "error": "Error Description",
}
```
### GET /purchases

Gets a paginated list of purchases made by the current user.

#### Request

- **Query Parameters**:
    - page: Current page of the list. Default is 1.
    - limit: Number of items per page. Default is 10.
    - offset: Number of items to skip. Default is 0.

#### Response

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "count": 1,
    "next": "Example URL",
    "previous": "Example URL",
    "results": [   
        {
            "purchase_date": "03/12/2019", 
            "state": "pending" || "completed", 
            "product_total": 100,
            "shipping_total": 50,
            "items": [
                {
                    "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
                    "name": "Example Item",
                    "price": 100,
                    "quantity": 1
                },
                {
                    "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
                    "name": "Example Item",
                    "price": 100,
                    "quantity": 1
                },
            ]
        }
    ]
}
```

### POST /purchases

Creates a purchase using the current user's cart.

#### Response

If the purchase was successful:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
  "purchase_date": "03/12/2019", 
  "state": "pending" || "completed", 
  "product_total": 100,
  "shipping_total": 50,
  "items": [
      {
          "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
          "name": "Example Item",
          "price": 100,
          "quantity": 1
      },
      {
          "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
          "name": "Example Item",
          "price": 100,
          "quantity": 1
      },
  ]
}
```

If the purchase wasn't successful:

- **Content-Type**: application/json
- **HTTP Status Code**: 400
- **Response Body**:
```json
{
  "error": "Error Description",
}
```

### GET /products

Gets a paginated list of existing products.

#### Request

- **Query Parameters**:
    - page: Current page of the list. Default is 1.
    - limit: Number of items per page. Default is 10.
    - offset: Number of items to skip. Default is 0.
    - show_nostock: If set to true, will include products that are out of stock. Default is false.
    - show_archived: If set to true, will include products that are archived. Default is false.

#### Response

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "count": 1,
    "next": "Example URL",
    "previous": "Example URL",
    "results": [   
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "description": "Description",
            "price": 100,
            "inventory": 1,
            "image_url": "Example URL",
            "archived": false,
            "last_modified_date": "03/12/2019",
            "last_modified_by": "Example User"
        },
        {
            "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
            "name": "Example Item",
            "description": "Description",
            "price": 100,
            "inventory": 1,
            "image_url": "Example URL",
            "archived": true,
            "last_modified_date": "03/12/2019",
            "last_modified_by": "Example User"
        },
    ]
}
```

### GET /products/{product_id}

Gets details of an existing product.

#### Response

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
    "name": "Example Item",
    "description": "Description",
    "price": 100,
    "inventory": 1,
    "image_url": "Example URL",
    "archived": true,
    "last_modified_date": "03/12/2019",
    "last_modified_by": "Example User"
}

```

### POST /products

Creates or modifies a product. If the product already exists, the given fields in the request body will be updated. If no product id is provided, a new product will be created. 

This endpoint can only be used by admin users.

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
    "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
    "name": "Example Item",
    "description": "Description",
    "price": 100,
    "inventory": 1,
    "image_url": "Example URL",
    "archived": true,
}

```

#### Response

If the product was added successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
    "name": "Example Item",
    "description": "Description",
    "price": 100,
    "inventory": 1,
    "image_url": "Example URL",
    "archived": true,
    "last_modified_date": "03/12/2019",
    "last_modified_by": "Example User"
}
```

If the item wasn't added:

- **Content-Type**: application/json
- **HTTP Status Code**: 400
- **Response Body**:
```json
{
  "error": "Error Description",
}
```

### DELETE /products

Archives a product. This endpoint can only be used by admin users.

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
    "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
}

```

#### Response

If the product was archived successfully:

- **Content-Type**: application/json
- **HTTP Status Code**: 200
- **Response Body**:
```json
{
    "id": "5e9f8f8f-f9d3-4f2b-b8f8-f8f8f8f8f8f8",
    "name": "Example Item",
    "description": "Description",
    "price": 100,
    "inventory": 1,
    "image_url": "Example URL",
    "archived": true,
    "last_modified_date": "03/12/2019",
    "last_modified_by": "Example User"
}
```

If the item wasn't archived:

- **Content-Type**: application/json
- **HTTP Status Code**: 400
- **Response Body**:
```json
{
    "error": "Error Description",
}
```