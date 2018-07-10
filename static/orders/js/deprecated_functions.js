$(document).ready(function(){
    var currentURL = window.location.href;
    if ($('#u_id').val()==1&&!currentURL.includes("viewOrder.")) {
        var ids = [];
        $.ajax({
            url:"../../static/orders/php/getNotifications.php",
            type:"POST",
            dataType:"json",
            success:function(results){
                console.log(results)
                            /*notifications=msg;
                            console.log(msg[0]);*/
                            $.each(results['notifications'], function (key, val) {
                                console.log("notification id: "+val.id+", link:"+val.order_id);
                                if (!ids.includes(val.id)) {
                                    myNotify(val.id,val.link);
                                    ids.push(val.id);
                                }
                            });

                        }
                    });
        window.setInterval(function(){

            $.ajax({
                url:"../../static/orders/php/getNotifications.php",
                type:"POST",
                dataType:"json",
                success:function(results){
                            /*notifications=msg;
                            console.log(msg[0]);*/
                            $.each(results['notifications'], function (key, val) {
                                console.log("notification id: "+val.id+", link:"+val.order_id);
                                if (!ids.includes(val.id)) {
                                    myNotify(val.id,val.link);
                                    ids.push(val.id);
                                }
                            });

                        }
                    });
        }, 5000);
    }
});

function deleteNotification(id){

    var info = 'id='+id;
    if (true) {
        $.ajax({
            type: "POST",
            url: "../../static/orders/php/deleteNotification.php",
            data: info
        });
    }
}