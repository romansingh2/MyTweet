import React from 'react'
import {apiPostCreate} from './lookup'


export function PostCreate(props){
  const textAreaRef = React.createRef()
  const {didPost} = props
    const handleBackendUpdate = (response, status) =>{
      if (status === 201){
        didPost(response)
      } else {
        console.log(response)
        alert("An error occured please try again")
      }
    }

    const handleSubmit = (event) => {
      event.preventDefault()
      const newVal = textAreaRef.current.value
      // backend api request
      apiPostCreate(newVal, handleBackendUpdate)
      textAreaRef.current.value = ' '
    }
    return <div className={props.className}>
          <form onSubmit={handleSubmit}>
            <textarea ref={textAreaRef} required={true} className='form-control' name='post'>

            </textarea>
            <button type='submit' className='btn btn-primary my-3'>Post</button>
        </form>
  </div>
}