(this["webpackJsonpnetwork-web"]=this["webpackJsonpnetwork-web"]||[]).push([[0],{14:function(e,t,n){},15:function(e,t,n){},17:function(e,t,n){"use strict";n.r(t);var s=n(1),c=n.n(s),a=n(6),o=n.n(a),r=(n(14),n.p+"static/media/logo.6ce24c58.svg");n(15);function i(e,t,n,s){var c;s&&(c=JSON.stringify(s));var a=new XMLHttpRequest,o="http://localhost:8000/api".concat(t);a.responseType="json";var r=function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),s=0;s<n.length;s++){var c=n[s].trim();if(c.substring(0,e.length+1)===e+"="){t=decodeURIComponent(c.substring(e.length+1));break}}return t}("csrftoken");a.open(e,o),a.setRequestHeader("Content-Type","application/json"),r&&(a.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest"),a.setRequestHeader("X-Requested-With","XMLHttpRequest"),a.setRequestHeader("X-CSRFToken",r)),a.onload=function(){n(a.response,a.status)},a.onerror=function(e){console.log(e),n({message:"The request was an error"},400)},a.send(c)}var l=n(0);function u(e){var t=e.post,n=e.action,s=e.didPerformAction,c=t.likes?t.likes:0,a=e.className?e.className:"btn btn-primary btn-sm",o=n.display?n.display:"Action",r=function(e,t){console.log("the response is "+e," the status is "+t),200!==t&&201!==t||!s||s(e,t)},u="like"===n.type?"".concat(c," ").concat(o):o;return Object(l.jsx)("button",{className:a,onClick:function(e){e.preventDefault(),function(e,t,n){i("POST","/posts/action/",n,{id:e,action:t})}(t.id,n.type,r)},children:u})}var d=n(8),j=n(2);function b(e){var t=e.post;return t.parent?Object(l.jsx)("div",{className:"row",children:Object(l.jsxs)("div",{className:"col-11 mx-auto p-3 border rounded",children:[Object(l.jsx)("p",{className:"mb-0 text-muted small",children:"Retweet"}),Object(l.jsx)(p,{hideActions:!0,className:" ",post:t.parent})]})}):null}function p(e){var t=e.post,n=e.didRetweet,a=e.hideActions,o=Object(s.useState)(e.post?e.post:null),r=Object(j.a)(o,2),i=r[0],p=r[1],m=e.className?e.className:"col-10 mx-auto col-md-6",f=window.location.pathname.match(Object(d.a)(/([0-9]+)/,{postid:1})),O=f?f.groups.postid:-1,h="".concat(t.id)==="".concat(O),v=function(e,t){200===t?p(e):201===t&&n&&n(e)};return Object(l.jsxs)("div",{className:m,children:[Object(l.jsxs)("div",{children:[Object(l.jsxs)("p",{children:[t.id," - ",t.tweet]}),Object(l.jsx)(b,{post:t})]}),Object(l.jsxs)("div",{className:"btn btn-group",children:[i&&!0!==a&&Object(l.jsxs)(c.a.Fragment,{children:[Object(l.jsx)(u,{post:i,didPerformAction:v,action:{type:"like",display:"Likes"}}),Object(l.jsx)(u,{post:i,didPerformAction:v,action:{type:"unlike",display:"Unlike"}}),Object(l.jsx)(u,{post:i,didPerformAction:v,action:{type:"retweet",display:"Retweet"}})]}),!0===h?null:Object(l.jsx)("button",{className:"btn btn-outline-primary btn-sm",onClick:function(e){e.preventDefault(),window.location.href="/".concat(t.id)},children:"View"})]})]})}var m=n(3);function f(e){var t=Object(s.useState)([]),n=Object(j.a)(t,2),c=n[0],a=n[1],o=Object(s.useState)([]),r=Object(j.a)(o,2),u=r[0],d=r[1],b=Object(s.useState)(!1),f=Object(j.a)(b,2),O=f[0],h=f[1];Object(s.useEffect)((function(){var t=Object(m.a)(e.newPosts).concat(c);t.length!==u.length&&d(t)}),[e.newPosts,u,c]),Object(s.useEffect)((function(){if(!1===O){!function(e,t){var n="/posts/";e&&(n="/posts/?username=".concat(e)),i("GET",n,t)}(e.username,(function(e,t){200===t?(a(e),h(!0)):alert("There was an error")}))}}),[c,O,h,e.username]);var v=function(e){var t=Object(m.a)(c);t.unshift(e),a(t);var n=Object(m.a)(u);n.unshift(u),d(n)};return u.map((function(e,t){return Object(l.jsx)(p,{post:e,didRetweet:v,className:"my-5 py-5 border bg-white text-dark"},"".concat(t,"-{item.id}"))}))}var O=n(9);function h(e){var t=c.a.createRef(),n=e.didPost,s=function(e,t){201===t?n(e):(console.log(e),alert("An error occured please try again"))};return Object(l.jsx)("div",{className:e.className,children:Object(l.jsxs)("form",{onSubmit:function(e){e.preventDefault();var n=t.current.value;i("POST","/posts/create/",s,{tweet:n}),t.current.value=" "},children:[Object(l.jsx)("textarea",{ref:t,required:!0,className:"form-control",name:"post"}),Object(l.jsx)("button",{type:"submit",className:"btn btn-primary my-3",children:"Post"})]})})}function v(e){var t=Object(s.useState)([]),n=Object(j.a)(t,2),c=n[0],a=n[1],o="false"!==e.canPost;return Object(l.jsxs)("div",{className:e.className,children:[!0===o&&Object(l.jsx)(h,{didPost:function(e){var t=Object(m.a)(c);t.unshift(e),a(t)},className:"col-12 mb-3"}),Object(l.jsx)(f,Object(O.a)({newPosts:c},e))]})}function x(e){var t=e.postId;console.log(e);var n=Object(s.useState)(!1),c=Object(j.a)(n,2),a=c[0],o=c[1],r=Object(s.useState)(null),u=Object(j.a)(r,2),d=u[0],b=u[1],m=function(e,t){200===t?b(e):(console.log(e),alert("There was an error finding your post."))};return Object(s.useEffect)((function(){!1===a&&(console.log(t),function(e,t){i("GET","/posts/".concat(e,"/"),t)}(t,m),o(!0))}),[t,a,o]),null===d?null:Object(l.jsx)(p,{post:d,className:e.className})}var g=function(){return Object(l.jsx)("div",{className:"App",children:Object(l.jsxs)("header",{className:"App-header",children:[Object(l.jsx)("img",{src:r,className:"App-logo",alt:"logo"}),Object(l.jsxs)("p",{children:["Edit ",Object(l.jsx)("code",{children:"src/App.js"})," and save to reload."]}),Object(l.jsx)("div",{children:Object(l.jsx)(v,{})}),Object(l.jsx)("a",{className:"App-link",href:"https://reactjs.org",target:"_blank",rel:"noopener noreferrer",children:"Learn React"})]})})},w=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,18)).then((function(t){var n=t.getCLS,s=t.getFID,c=t.getFCP,a=t.getLCP,o=t.getTTFB;n(e),s(e),c(e),a(e),o(e)}))},N=document.getElementById("root");N&&o.a.render(Object(l.jsx)(g,{}),N);var y=c.a.createElement,k=document.getElementById("network");k&&o.a.render(y(v,k.dataset),k),document.querySelectorAll(".project4-detail").forEach((function(e){o.a.render(y(x,e.dataset),e)})),w()}},[[17,1,2]]]);
//# sourceMappingURL=main.4ad29ba8.chunk.js.map