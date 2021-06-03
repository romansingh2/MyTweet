import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {ProfileBadgeComponent} from './profiles'
import {FeedComponent, PostsComponent, PostDetailComponent} from './posts'
import reportWebVitals from './reportWebVitals';


const appEl = document.getElementById('root')
if (appEl) {
  ReactDOM.render(<App />, appEl);
}
const e = React.createElement
const postsEl = document.getElementById("network")
if (postsEl) {
  ReactDOM.render(e(PostsComponent, postsEl.dataset), postsEl);
}

const postFeedEl = document.getElementById("network-feed")
if (postFeedEl) {
    ReactDOM.render(
        e(FeedComponent, postFeedEl.dataset), postFeedEl);
}

const PostDetailElements = document.querySelectorAll(".network-detail")

PostDetailElements.forEach(container => {
  ReactDOM.render(e(PostDetailComponent, container.dataset), container);
})

const userProfileBadgeElements = document.querySelectorAll(".network-profile-badge")

userProfileBadgeElements.forEach(container => {
  ReactDOM.render(e(ProfileBadgeComponent, container.dataset), container);
})


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

