import React  from 'react'

import {apiPostAction} from './lookup' 



export function ActionBtn(props) {
    const {post, action, didPerformAction} = props
    const likes = post.likes ? post.likes : 0
    
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    
    const handleActionBackendEvent = (response, status) =>{
      console.log(response, status)
      if ((status === 200 || status === 201) && didPerformAction){ //if status is 200 or 201 and didperformaction exists, pass on response and status to didperformaction
      
        didPerformAction(response, status)
        
      }     
    }
    const handleClick = (event) => {
      event.preventDefault()
      apiPostAction(post.id, action.type, handleActionBackendEvent)
    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return <button className={className} onClick={handleClick}>{display}</button>
  }