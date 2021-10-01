CRUD for users

Registration user - /auth/users/
                    method: post
                    data: username (required)
                          password (required)
                          is_active (required)
                          last_name
                          first_name
                          is_superuser


Token authentication - /auth/token/login/
                       method: post
                       data: username (required)
                             password (required)
                       response: auth_token


Get users - /api/v1/users/

Get, Put, Patch, Delete - /api/v1/users/{id}/