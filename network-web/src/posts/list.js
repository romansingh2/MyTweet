import React, {useEffect, useState}  from 'react'

import {apiPostList} from './lookup'

import {Post} from './detail'

export function PostsList(props) {
    const [PostsInit, setPostsInit] = useState([])
    const [posts, setPosts] = useState([])
    const [nextUrl, setNextUrl] = useState(null)
    const [PostsDidSet, setPostsDidSet] = useState(false)
    useEffect(()=>{
      const final = [...props.newPosts].concat(PostsInit)
      if (final.length !== posts.length) {
        setPosts(final)
      }
    }, [props.newPosts, posts, PostsInit])
    useEffect(() => {
      if (PostsDidSet === false){
        const handlePostListLookup = (response, status) => {
          if (status === 200){
            setNextUrl(response.next)
            setPostsInit(response.results)
            setPostsDidSet(true)
          } else {
            alert("There was an error")
          }
        }
        apiPostList(props.username, handlePostListLookup)
      }
    }, [PostsInit, PostsDidSet, setPostsDidSet, props.username])


    const handleDidRetweet = (newPost) => {
      const updatePostsInit = [...PostsInit]
      updatePostsInit.unshift(newPost)
      setPostsInit(updatePostsInit)
      const updateFinalPosts = [...posts]
      updateFinalPosts.unshift(posts)
      setPosts(updateFinalPosts)
    } 

    const handleLoadNext = (event) => {
      event.preventDefault()
      if (nextUrl !== null) {
        const handleLoadNextResponse = (response, status) =>{
          if (status === 200){
            setNextUrl(response.next)
            const newPosts = [...posts].concat(response.results)
            setPostsInit(newPosts)
            setPosts(newPosts)
          } else {
            alert("There was an error")
          }
        }
        apiPostList(props.username,handleLoadNextResponse, nextUrl)
      }
    }
    return <React.Fragment>{posts.map((item, index)=>{
      return <Post  
        post={item} 
        didRetweet={handleDidRetweet}
        className='my-5 py-5 border bg-white text-dark' 
        key={`${index}-{item.id}`} />
    })}
    { nextUrl !== null && <button onClick={handleLoadNext}className='btn btn-outline-primary'>Load Next </button>}
    </React.Fragment>
  }
