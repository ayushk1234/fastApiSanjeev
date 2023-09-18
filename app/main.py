from random import randrange

from fastapi import FastAPI,Response,status,HTTPException
import uvicorn
from fastapi.params import  Body
from pydantic import  BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    # id : Optional['int']

my_post = [{
    "title" : "first post",
    "content" : "firsy content",
    "id" :1
},
    {
"title": "second post",
    "content" : "second content",
    "id" :2
    }]

@app.get("/")
async def root():
    return {"message": "hi"}

@app.get("/newPage/{name}")
async def info(name):
    return {"message": name}

def find_post(id):
    # pass
    for p in my_post :
        if p['id'] ==id:
            return p


def find_index_post(id):
    for i,p in enumerate(my_post):
        print("i ,p ",i,p)
        if p['id']==id:
            return i



@app.get("/newPage/{name}/{age}")
async def info(name:str,age:int):
    # print
    return {"name" : name,"age":age}

@app.get("/getPost")
async def info():
    # print(name,age)
    return {"data":my_post}

@app.post("/createposts",status_code=status.HTTP_201_CREATED)
async def create_posts(new_post: Post):
    new_post = new_post.dict()
    new_post['id'] =randrange(0,100000)
    my_post.append(new_post)
    # return {"name" : new_post['title'] }
    return {"data" : new_post}

@app.get("/getPost/{id}")
async  def get_single_post(id:int):
    # print(new_post.title)
    # print(type(new_post))
    result = find_post(int(id))
    if not result:
        # response.status_code =status.HTTP_404_NOT_FOUND;
        # return {"message" : f'post with {id} not found'}
        # return
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with {id} not found')

    else :
        return {"data":result}



@app.delete("/deletePost/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deletePost(id :int):
    index = find_index_post(id)
    if index == None:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'no {id} with record found'))

    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/post/{id}")
async def updatePost(id : int,post:Post):
    record = find_index_post(id)
    # record =find_post(int(id))
    if record == None:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no {id} with record found'))

    post = post.dict()
    post['id'] = id
    my_post[record] = post
    # record['title'] = post.title
    # record['content']=post.content

    return {"message" : post}


if __name__ == "__main__":
   uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)