import React, {useState}  from 'react'

import {ActionBtn} from './buttons'


import {
  UserDisplay,
  UserPicture
} from '../profiles'



export function ParentPost(props){
    const {post} = props
    return post.parent ? <Post isRetweet retweeter={props.retweeter} hideActions className={' '} post={post.parent} /> : null
  }

  export function Post(props) {
      const {post, didRetweet, hideActions, isRetweet, retweeter} = props
      const [actionPost, setActionPost] = useState(props.post ? props.post : null)
      let className = props.className ? props.className : 'col-10 mx-auto col-md-6'
      className = isRetweet === true ? `${className} p-2 border rounded` : className
      const path = window.location.pathname
      const match = path.match(/(?<postid>\d+)/ )
      const urlPostId = match ? match.groups.postid : -1 //if match than its match.groups.postid, otherwise its
      const isDetail = `${post.id}` === `${urlPostId}`
      const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `/${post.id}`
      }

      const handlePerformAction = (newActionPost, status) => {
        if (status === 200){
          setActionPost(newActionPost)
        } else if (status === 201) {
          if (didRetweet){
            didRetweet(newActionPost)
          }
        }
      }
      return <div className={className}>
        {isRetweet === true &&<div className='mb-2'>
        <span className='small text-muted'>Retweet via <UserDisplay user={retweeter} /></span>
        </div>}
        <div className='d-flex'>
          <div className=''>
            <UserPicture user={post.user} />


          </div>
          <div className='col-11'>
              <div>
                <p>
                <UserDisplay includeFullName user={post.user} />
                
                </p>
                <p> {post.tweet}</p>
                <ParentPost post={post} retweeter={post.user}/>
              </div>   
           <div className='btn btn-group px-0'>
           {(actionPost && hideActions !== true) && <React.Fragment> 
              <ActionBtn post={actionPost} didPerformAction = {handlePerformAction} action={{type: "like", display:"Likes"}}/>
              <ActionBtn post={actionPost} didPerformAction = {handlePerformAction} action={{type: "unlike", display:"Unlike"}}/>
              <ActionBtn post={actionPost} didPerformAction = {handlePerformAction} action={{type: "retweet", display:"Retweet"}}/>
             </React.Fragment>
            }
              {isDetail === true ? null : <button className = "btn btn-outline-primary btn-sm" onClick ={handleLink}>View</button>}
            </div>
            </div>
         
        </div>  
        </div>    
  }