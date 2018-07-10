function myFunctionOutput(){
    var e = document.getElementById("blockOutput");
    var str = e.options[e.selectedIndex].value;
    var strArray = str.split(":");
    document.getElementById("outputOrganization").value=strArray[0];
    document.getElementById("outputContact").value=strArray[1];
    document.getElementById("outputNumber").value=strArray[2];
    document.getElementById("outputAdress").value=strArray[3];

}

function myFunctionInput(){
    var e = document.getElementById("blockInput");
    var str = e.options[e.selectedIndex].value;
    var strArray = str.split(":");
    document.getElementById("inputOrganization").value=strArray[0];
    document.getElementById("inputContact").value=strArray[1];
    document.getElementById("inputNumber").value=strArray[2];
    document.getElementById("inputAdress").value=strArray[3];

}

//SELECT2
function formatState (state) {
  if (!state.id) {
    return state.text;
}
var baseUrl = "/user/pages/images/flags";
var $state = $(
    '<span><img src="' + baseUrl + '/' + state.element.value.toLowerCase() + '.png" class="img-flag" /> ' + state.text + '</span>'
    );
return $state;
};

$(document).ready(function() {
    $('.js-example-basic-single').select2({
    width: 'resolve' // need to override the changed default
});
});

//Делает row кликабельным
jQuery(document).ready(function($) {
    $('#orders').on('click','.clickable-row', function () {
        window.location = $(this).data("href");

    });
});

//Notifications

function myNotify(notificationId, link) {
    $.notify({
    // options
    icon: 'glyphicon glyphicon-warning-sign',
    title: 'Новая заявка №'+link,
    message: "",
    url: "/orders/showOrder/"+link+"/",
    target: '_blank'
},{
    // settings
    element: 'body',
    position: null,
    type: "info",
    allow_dismiss: true,
    newest_on_top: true,
    showProgressbar: false,
    placement: {
        from: "bottom",
        align: "right"
    },
    offset: 20,
    spacing: 10,
    z_index: 1031,
    delay: 0,
    timer: 1000,
    url_target: '_blank',
    mouse_over: null,
    animate: {
        enter: 'animated fadeInUp',
        exit: 'animated fadeOutUp'
    },
    onShow: null,
    onShown: null,
    onClose: function (){deleteNotification(notificationId);},
    onClosed: null,
    icon_type: 'class',
    template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
    '<button id="test" type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
    '<span data-notify="icon"></span> ' +
    '<span data-notify="title">{1}</span> ' +
    '<span data-notify="message">{2}</span>' +
    '<div class="progress" data-notify="progressbar">' +
    '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
    '</div>' +
    '<a href="{3}" target="{4}" data-notify="url"></a>' +
    '</div>' 
});
}

//Каждые пять секунд запрашивает есть ли новые заявки
//new ajax
$(document).ready(function(){
    var currentURL = window.location.href;
    if ($('#u_id').val()==1&&!currentURL.includes("showOrder/")&&!currentURL.includes("showTemplate/")) {
        var ids = [];

        $.ajax({
            type: 'GET',
            url: '../get_notifications/',
            dataType: 'json',
            success: function(data){
                for (var i = data.length - 1; i >= 0; i--) {
                    if (!ids.includes(data[i].id)) {
                        myNotify(data[i].id, data[i].order_id)
                        ids.push(data[i].id);
                    }
                }
            }
        });

        window.setInterval(function(){

            $.ajax({
                type: 'GET',
                url: '../get_notifications/',
                dataType: 'json',
                success: function(data){
                    for (var i = data.length - 1; i >= 0; i--) {
                        if (!ids.includes(data[i].id)) {
                            myNotify(data[i].id, data[i].order_id)
                            ids.push(data[i].id);
                        }
                    }
                }
            });
        }, 5000);
    }
});

function deleteNotification(id){

    var info = 'id='+id;
    if (true) {
        $.ajax({
            type: "GET",
            url: "../delete_notification/"+id+"/",
            data: info
        });
    }
}


function printOrder(){
    orderId=document.getElementById("order_id");
    outputOrg=document.getElementById("outputOrg");
    outputContact=document.getElementById("outputContact");
    outputNumber=document.getElementById("outputNumber");
    outputAdress=document.getElementById("outputAdress");

    inputOrg=document.getElementById("inputOrg");
    inputContact=document.getElementById("inputContact");
    inputNumber=document.getElementById("inputNumber");
    inputAdress=document.getElementById("inputAdress");

    cargo=document.getElementById("cargo");
    weight=document.getElementById("weight");

    comments=document.getElementById("comments");

    //информация юзера
    user_id=document.getElementById("user_id");

    userLast=document.getElementById("userLast");
    userFirst=document.getElementById("userFirst");
    userFamily=document.getElementById("userFamily");

    phoneNumber=document.getElementById("phoneNumber");
    insideNumber=document.getElementById("insideNumber");

    email=document.getElementById("email");


    myWindow=window.open("");
    myWindow.document.writeln("<!DOCTYPE html><html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"><link rel=\"stylesheet\" type=\"text/css\" href=\"/static/orders/css/style2.css\" media=\"all\"/></head><body onload='window.print()'>");
    myWindow.document.writeln("<h2>Заявка на транспортировку номер "+orderId.innerHTML+"</h2>");
    myWindow.document.writeln("<h3>1.Отправитель:</h3>");
    myWindow.document.writeln("<p class=\"outputContact\">Контактное лицо: <b>"+outputContact.innerHTML+"</b></p>");
    myWindow.document.writeln("<p class=\"outputOrg\">Организация отправтеля: <b>"+outputOrg.innerHTML+"</b></p>");
    myWindow.document.writeln("<p class=\"outputAdress\">Адрес: <b>"+outputAdress.innerHTML+"</b></p>");
    myWindow.document.writeln("<p class=\"outputNumber\">Номер: <b>"+outputNumber.innerHTML+"</b></p>");
    myWindow.document.writeln("<h3>2.Получатель:</h3>");
    myWindow.document.writeln("<p class=\"outputContact\">Контактное лицо: <b>"+inputContact.innerHTML+"</b></p>");
    myWindow.document.writeln("<p class=\"outputOrg\">Организация отправтеля: <b>"+inputOrg.innerHTML+"</b></p>");
    myWindow.document.writeln("<p class=\"outputAdress\">Адрес: <b>"+inputAdress.innerHTML+"</b></p>");
    myWindow.document.writeln("<p class=\"outputNumber\">Номер: <b>"+inputNumber.innerHTML+"</b></p>");
    myWindow.document.writeln("<h3>3.Информация о грузе:</h3>");
    myWindow.document.writeln("<p class=\"cargo\">характер груза: <b>"+cargo.innerHTML+"</b></p>");
    myWindow.document.writeln("<p class=\"weight\">вес: <b>"+weight.innerHTML+"</b></p>");
    myWindow.document.writeln("<h3>4.Коментарии:</h3>");
    myWindow.document.writeln("<p class=\"commentary\"><b>"+comments.innerHTML+"</b></p>");
    myWindow.document.writeln("<h3>5.Заказчик:</h3>");
    myWindow.document.writeln("<p><b>"+userLast.innerHTML + " " + userFirst.innerHTML + " " + userFamily.innerHTML +"</b></p>");
    myWindow.document.writeln("<p>Моб. телефон: <b>"+ phoneNumber.innerHTML + "</b> Внутренний:<b>" + insideNumber.innerHTML +"</b></p>");
    myWindow.document.writeln("<p><b>"+email.innerHTML + "</b></p>");
    myWindow.document.writeln("</body></html>");
    myWindow.document.close();
    myWindow.focus();
    myWindow.onfocus = function(){ setTimeout(function(){ myWindow.close(); } , 500); };
}


