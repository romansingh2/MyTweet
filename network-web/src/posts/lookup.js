import {backendLookup} from '../lookup'

export function apiPostFeed(callback, nextUrl) {
    let endpoint = "/posts/feed"
    
    if (nextUrl !== null && nextUrl !== undefined){
        endpoint = nextUrl.replace("http://localhost:8000/api", "")
    }
    backendLookup("GET", endpoint, callback)
}



export function apiPostCreate(newPost, callback){
    backendLookup("POST", "/posts/create/", callback, {tweet: newPost})
  } //method is post, endpoint is /posts/create, data is tweet


export function apiPostAction(postId, action, callback){
    const data = {id: postId, action: action}
    backendLookup("POST", "/posts/action/", callback, data)
}


export function apiPostDetail(postId, callback){
    backendLookup("GET", `/posts/${postId}/`, callback)
}


export function apiPostList(username, callback, nextUrl) {
    let endpoint = "/posts/"
    if (username) {
        endpoint = `/posts/?username=${username}`
    }
    if (nextUrl !== null && nextUrl !== undefined){
        endpoint = nextUrl.replace("http://localhost:8000/api", "")
    }
    backendLookup("GET", endpoint, callback)
}

