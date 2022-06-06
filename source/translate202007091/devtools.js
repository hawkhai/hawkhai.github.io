chrome.runtime.connect({name:"devtools"}).onMessage.addListener(function(e){e&&console.log(e)});
