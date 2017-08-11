import json

    def retrieve_posts():
        #Let's imagine that I made a SELECT from some db somewhere
        return [
            { "id": 1, "title": "Easy introduction to Redux", "publish_date": "2017-08-01" },
            { "id": 2, "title": "Serverless", "publish_date": "2017-08-11" },
        ]
    
    def posts(event, context):
        posts = retrieve_posts()

    body = {
        "message": "Nice job! Your function executed successfully!",
        "data": posts
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response