
console.log("Okey")
//Let's write it again de text below
function getContent(fragmentId, callback){

    let x = 10;

    const m = () =>
    {
        let k = 10;
        while (k > 0)
        {
            k--;
            return k;
        } 
    }

    var pages = {
      home: "This is the Home page. Welcome to my site. <img src=\"https://hatrabbits.com/wp-content/uploads/2017/01/random-word-1.jpg\" width=\"300\" height=\"500\"/>",
      about: `This page will describe what my site is about <br><div id="bigNumber">${x}</div>`,
      contact: "Contact me on this page if you have any questions"
    };
  
    callback(pages[fragmentId]);
  }
  
  
  
  function loadContent(){
  
    var contentDiv = document.getElementById("app"),
        fragmentId = location.hash.substr(1);
  
    getContent(fragmentId, function (content) {
      contentDiv.innerHTML = content;
    });
  
  }
/* Not working for now animation test
  let id = null;
function myMove() {
  let elem = document.getElementById("home");
  let pos = 0;
  clearInterval(id);
  id = setInterval(frame, 10);
  function frame() {
    if (pos == 350) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.top = pos + 'px';
      elem.style.left = pos + 'px';
    }
  }
}
*/

  
  if(!location.hash) {
    location.hash = "#home";
  }
  
  loadContent();
  
  window.addEventListener("hashchange", loadContent)

  //Word after de full auto-execution of de script
  console.log("After de Full Execution Code") 


/*class Bot
{
    constructor()
    {
        console.log("Dat is de bot");
    }
}*/
/*
const triple = (x, y) =>
{
    return x*3 + y*3;
}

function getContent(fragmentId, callback){

    document.write('Hello, World!')
    document.write('Hello, World!')
    console.log("Hi");

    var pages = {
      home: "This is the Home page. Welcome to my site.",
      about: "This page will describe what my site is about",
      contact: "Contact me on this page if you have any questions"
    };
  
    callback(pages[fragmentId]);
  }
  
  
  
  function loadContent(){

    document.write('Hello, World!')
    document.write('Hello, World!')
  
    var contentDiv = document.getElementById("app"),
        fragmentId = location.hash.substr(1);
  
    getContent(fragmentId, function (content) {
      contentDiv.innerHTML = content;
    });
  
  }
  
    console.log("Hello world");
    document.write('Hello, World!');

  if(!location.hash) {
    location.hash = "#home";
  }
  
  loadContent();
  
  window.addEventListener("hashchange", loadContent)
  */