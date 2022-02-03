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
- User's current cart

#### Request

- **Content-Type**: application/json
- **Request Body**:
```json
{
  "email": "john_doe@mail.com",
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
- **HTTP Status Code**: 403

### POST /api/token/refresh

If provided with a valid refresh token, this endpoint will return an **access token** that can be used to authenticate future requests.

The access token will expire after an hour. To get a new token, call this endpoint again.

The returned token has the following claims:
- User's full name
- User's user type
- User's current cart

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
- **HTTP Status Code**: 403

## Auth Endpoints

Endpoints that require authentication must send a valid JWT token in the `Authorization` header using the following format:
`Authorization: Bearer <JWT_TOKEN>`. If the token is invalid, or the token doesn't provide sufficient permissions the request will be rejected with an 403 status code.