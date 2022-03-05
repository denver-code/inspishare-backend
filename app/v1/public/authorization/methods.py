from fastapi import (
    HTTPException,
    Header
)

import jwt


async def login_required(authorization=Header("Authorization")):
    try:
        session = authorization
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")

#
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         try:
#             if request.headers.get("Authentication"):
#                 jwt_data = jwt.decode(request.headers.get("Authentication").replace("Bearer ", ""), SECRET,
#                                       algorithms=["HS256"])
#                 if int(datetime.datetime.now().timestamp()) > jwt_data['expires_in']:
#                     return jsonify({
#                         "status": 401,
#                         "message": "Unauthorized"
#                     }), 401
#                 return f(*args, **kwargs)
#             else:
#                 return jsonify({
#                     "status": 401,
#                     "message": "Unauthorized"
#                 }), 401
#         except:
#             return make_response(jsonify({
#                 "status": 400,
#                 "message": "JWT token is invalid"
#             }), 400)
#
#     return wrap
