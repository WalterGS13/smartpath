if('serviceWorker' in navigator)
{
    navigator.serviceWorker.register('/sw.js').then(reg =>{console.log("registration successful");
    }).catch(error=>{console.error(error);});
}