
var request = new XMLHttpRequest();
var url = "http://192.168.122.100:20265/centerportal/resource/getWebSiteResources"
request.open('GET',url,true)
request.send()

request.change = function(){
    if(request.readyState == 4 && request.status == 200){
        var json = JSON.parse(request.responseText);
        runapi.alert(json)
    }

}


