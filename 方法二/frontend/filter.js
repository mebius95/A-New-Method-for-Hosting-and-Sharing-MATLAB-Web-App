
// 获取点击项的value
function onClickHander(id){
    var thing = document.getElementById(id);
    var thingvalue=thing.getAttribute("value");
    // div不存在value值，无法通过js直接获取，需要使用getAttribute
    console.log("selected"+thingvalue);
    return thingvalue
}

// '#######   +++ notice +++     #######'

// IE下,event对象有srcElement属性,但是没有target属性;
// Firefox下,event对象有target属性,但是没有srcElement属性.但他们的作用是相当的，即：
// firefox 下的 event.target = IE 下的 event.srcElement
// 解决方法:使用obj = event.srcElement ? event.srcElement : event.target;
// 或：var evtTarget = event.target || event.srcElement;

// 绑定button（id="submit"）进行div监听显示
function Get_srcElement(a){
    var srcElement="";
    srcElement = event.srcElement.getAttribute("value") || event.target.getAttribute("value");
    document.getElementById(a).value = srcElement
}


$(function(){
    // 绑定button（id="submit2"）进行img显示
    $('#submit2').click(function(){
        $("#fd").attr('src',"幅度响应.jpg");
        $("#xw").attr('src',"相位响应.jpg");
        $("#dwcj").attr('src',"单位冲激响应.jpg");
        $("#fd1").attr('src',"幅度响应.jpg");
        $("#xw1").attr('src',"相位响应.jpg");
        $("#dwcj1").attr('src',"单位冲激响应.jpg");})
})




// 下拉框选择
$(function(){
$('.ui.selection.dropdown').dropdown();});


