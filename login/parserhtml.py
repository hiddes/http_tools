# -- coding:utf8 -- #

from HTMLParser import HTMLParser
import re

form_re = re.compile(r'<form[\s\S]*?</form>')

html = '''
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8">
<title>麦子学院 - 专业IT职业在线教育平台</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="renderer" content="webkit">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="麦子学院，IT职业培训，IT技能培训，IT在线教育，IT在线学习，编程学习，android,ios,php,java,python,html5,cocos2dx">
<meta name="description" content="麦子学院专注IT职业在线教育，提供android开发、ios开发、coocs2d-x、Unity3D、游戏原画、物联网、产品经理、嵌入式、php等一系列线上IT培训服务，推出在线教育智能化学习系统，保证在线学习效果，每年帮助上万名软件开发学习者成功就业。">
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta name="baidu-site-verification" content="TlN38QiORE" />
<link href="/static/css/base.css?84545744114" rel="stylesheet">
<link href="/static/css/microoh-v5.css" rel="stylesheet">
<link href="/static/css/flat-ui.css" rel="stylesheet">
<link href="/static/css/animate.css" rel="stylesheet">
<link href="/static/css/develop.css" rel="stylesheet">
<link href="/static/css/toolbar.css" rel="stylesheet">
<link rel="shortcut icon" type="image/x-icon" href="/static/images/favicon.ico" />

    <link rel="stylesheet" type="text/css" href="/static/css/style.css?36514874">
    <link rel="stylesheet" type="text/css" href="/static/css/jquery.bxslider.css">


<script src="/static/js/jquery-1.11.1.min.js"></script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?e3879546912fd4b2d6e909e064d49262";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<!-- PHPStat Start -->
<script language="JavaScript" id="phpstat_js_id_10001292">
var _trackData = _trackData || [];
(function() {
var phpstat_js = document.createElement('script'); phpstat_js.type = 'text/javascript';
phpstat_js.charset = 'utf-8'; phpstat_js.id = 'phpstat_async_js_id_10001292'; phpstat_js.async = true;
phpstat_js.src = '//y1.yeefx.cn/count/10001292/10001292.js';
var phpstat_cjs = document.getElementsByTagName('script')[0]; phpstat_cjs.parentNode.insertBefore(phpstat_js, phpstat_cjs);
})();
</script>
<!--/PHPStat End -->
<!--[if lt IE 9]>
<script src="/static/js/html5shiv.min.js"></script>
<script src="/static/js/respond.min.js"></script>
<![endif]-->
</head>

<body>
<div class="microoh-main">

    <header class="navbar navbar-default navbar-fixed-top" data-spy="affix" data-offset-top="64">

          <div class="container">
              <div class="navbar-header">
                  <a class="navbar-brand" href="/" title="麦子学院"><img src="/static/images/logo.png" alt="麦子学院logo"><img src="/static/images/logo-font.png" alt="麦子学院"></a>
              </div>
              <div class="collapse navbar-collapse" id="microoh-navbar-collapse">
                  <ul class="nav navbar-nav navbar-left">
                      <li class="zy_menu_D "><a href="/course/">企业直通班</a>
                          <i class="zy_menu_div2_arr"></i>
                          <div class="zy_menu_div2">

                          </div>

                      </li>

                      <li><a href="/group/">麦子圈</a></li>
                      <li><a href="/common/apppage/"><img src="/static/images/zy_phone1.png" style="vertical-align: middle; height: 22px; margin-top: -4px; margin-right: 5px;">移动APP</a></li>

                  </ul>
              <textarea id="zy_menu_div2_txt">

                      <a href="/course/android-px/"><img src="/uploads/course/2015/09/Android应用开发_mini.png">Android应用开发</a>

                      <a href="/course/ios-px/"><img src="/uploads/course/2015/09/iOS_wVXQhJF.png">iOS应用开发</a>

                      <a href="/course/qrsqd-px/"><img src="/uploads/course/2015/09/qrsqd_mini.png">嵌入式驱动开发</a>

                      <a href="/course/cocos2d-x-px/"><img src="/uploads/course/2015/09/Cocos2d-x手游开发_mini.png">Cocos2d-x手游开发</a>

                      <a href="/course/web-px/"><img src="/uploads/course/2015/09/Web前端开发_mini.png">Web前端开发</a>

                      <a href="/course/pm-px/"><img src="/uploads/course/2015/09/产品经理_mini.png">产品经理</a>

                      <a href="/course/python-px/"><img src="/uploads/course/2015/09/Python-Web开发_mini.png">Python Web开发</a>

                      <a href="/course/qrs-px/"><img src="/uploads/course/2015/09/嵌入式应用开发_mini.png">嵌入式应用开发</a>

                      <a href="/course/iot-px/"><img src="/uploads/course/2015/09/物联网开发_mini.png">物联网开发</a>

                      <a href="/course/androidjg-px/"><img src="/uploads/course/2015/09/Android架构设计_mini.png">Android架构设计</a>

                      <a href="/course/wp-px/"><img src="/uploads/course/2015/09/WP应用开发_mini.png">WP应用开发</a>

                      <a href="/course/yuanhua-px/"><img src="/uploads/course/2015/09/游戏原画设计_mini.png">游戏原画设计</a>

                      <a href="/course/php-px/"><img src="/uploads/course/2015/09/PHP-Web开发_mini.png">PHP Web开发</a>

                      <a href="/course/java-px/"><img src="/uploads/course/2015/09/Java-Web开发_mini.png">Java Web开发</a>

                      <a href="/course/cocos2d-px/"><img src="/uploads/course/2015/09/Cocos2d手游开发_mini.png">Cocos2d手游开发</a>

                      <a href="/course/ux-px/"><img src="/uploads/course/2015/09/rjjhsj_mini.png">软件交互设计</a>

                      <a href="/course/te-px/"><img src="/uploads/course/2015/09/test_mini.png">软件测试</a>

                      <a href="/course/cg-px/"><img src="/uploads/course/2015/09/jsjdhzz_mini.png">计算机动画制作</a>

                      <a href="/course/drupal-px/"><img src="/uploads/course/2015/09/drupal_mini.png">drupal开发</a>

                      <a href="/course/u3d-px/"><img src="/uploads/course/2015/10/Unity3D游戏开发.png">Unity3D游戏开发</a>

                      <a href="/course/ui-px/"><img src="/uploads/course/2015/11/UI.png">UI设计</a>

              </textarea>
                  <form class="navbar-form navbar-left" role="search" onsubmit="return false">
                      <div class="form-group" >
                          <i class="v5-icon v5-icon-search"></i>
                          <input type="text" class="form-control" style=" width: 362px;" id="search" placeholder="搜索你感兴趣的课程">
                      </div>
                      <div class="search-dp" id="hotkeyword">
                          <!--推荐关键词-->
                          <div class="hotkeyword">
                              <h4>推荐搜索关键词</h4>
                              <ul class="cf">
                                  <li>加载中……</li>
                              </ul>
                          </div>
                      </div>
                  </form>
              <ul class="nav navbar-nav navbar-left zy_bav" style="margin-left: 4px;">

                      <li><a href="/common/apppage/"><img src="/static/images/zy_phone1.png" style="vertical-align: middle; height: 22px; margin-top: -4px; margin-right: 5px;">移动APP</a></li>

              </ul>
                  <div class="v5-topbar-login">

                      <div class="v5-topbar-login-off">
                          <a onclick="login_popup()" class="visible-md visible-lg">登录</a>
                          <a href="/user/mobile/login/" class="visible-xs visible-sm">登录</a>
                      </div>

                  </div>
                  <div class="navbar-search-btn visible-xs visible-sm">
                    <a href="/common/mobile/search/" class="sch"></a>
                  </div>
              </div>
              <div class="search-dp" id="keyword-group">
                <!--搜索结果-->
                <div class="keyword-group scroll-pane">
                    <dl class="">
                        <dt>职业课程</dt>
                        <dd class="careercourses cf"></dd>
                    </dl>
                    <dl class="">
                        <dt>课程</dt>
                        <dd class="courses cf"></dd>
                    </dl>
                </div>
            </div>
          </div>
      </header>
  <div class="wap_top textC">
  	<a href="/" class="colorff" style="color: #ffffff;">麦子学院</a>
      <div class="wap_top_tou">

          <a href="/user/mobile/login/" style="font-size: 16px;border-radius: inherit; overflow: inherit; width: 100px; text-align: left; color: #ffffff; margin-top: 7px;">登录</a>

      </div>
      <a href="/common/mobile/search/" class="wap_top_a"><img style="width: 18px;" src="/group/static/iphone/images/wap_u8.png"></a>
  </div>




<div class="zy_banner">
    <div class="zy_banner_img">
        <div></div>
        <i></i>
        <div style="display: none;"><img src="/uploads/ad/2016/01/新年banner_backimage.png"><img src="/uploads/ad/2016/01/官网banner_backimage.png"><img src="/uploads/ad/2015/09/在线学习_backimage.jpg"></div>
    </div>
	<div class="container">
    	<div class="zy_bannerL">
        	<ul class="bxslider">


                     <li ><a big="/uploads/ad/2016/01/新年banner_backimage.png" href="http://www.maiziedu.com/group/article/12642/" title="新年大促" target="_blank" style="cursor:pointer;"> <img alt="新年大促" src="/uploads/ad/2016/01/新年banner.png"></a></li>

                     <li ><a big="/uploads/ad/2016/01/官网banner_backimage.png" href="http://www.maiziedu.com/group/article/12637/" title="么么贷" target="_blank" style="cursor:pointer;"> <img alt="么么贷" src="/uploads/ad/2016/01/官网banner.png"></a></li>

                     <li ><a big="/uploads/ad/2015/09/在线学习_backimage.jpg" href="http://www.maiziedu.com/common/study" title="在麦子学院如何在线学习" target="_blank" style="cursor:pointer;"> <img alt="在麦子学院如何在线学习" src="/uploads/ad/2015/09/在线学习.jpg"></a></li>


            </ul>
        </div>
        <div class="zy_bannerR font12 ">
        	<div class="zy_bannerR_tit">
            	<p class="textC marginB20"><img src="/static/images/qyztb.png"></p>
                <div class="zy_bannerR_titD">
                	<a href="/course/"><img src="/static/images/qyztb_icon1.png"><p>费用<br>无压力</p></a><a href="/course/"><img src="/static/images/qyztb_icon2.png"><p>零基础<br>教学</p></a><a href="/course/"><img src="/static/images/qyztb_icon3.png"><p>智能在线<br>学习</p></a><a href="/course/"><img src="/static/images/qyztb_icon4.png"><p>名师小班<br>指导</p></a><a href="/course/"><img src="/static/images/qyztb_icon5.png"><p>名师评测<br>考核</p></a><a href="/course/"><img src="/static/images/qyztb_icon6.png"><p>全国就业<br>服务</p></a>
                    <p class="textC ">
                        <a class="a1" onclick="openVideo()">如何学习？<img src="/static/images/gogo.png" class="t3out"></a>
                        <a class="a2" href="/common/lps/demo/" target="_blank">在线学习<br>超前体验</a>
                    </p>
                </div>
            </div>
            <a href="/course/" class="zy_bannerR_go textC fontCW">加入直通班<img src="/static/images/qyztb_arrow.png" class="t3out"></a>
        </div>
    </div>
</div>

<div class="zy_bg_w font12">
	<div class="container">
    	<!--企业直通班-->
        <div class="zy_index_box">
        	<p class="zy_index_box_tit color99 font14"><a href="/course/" class="font22 s1 color33">企业直通班</a><span class="s2">智能化学习体验，名师小班指导，入学签订保就业协议</span><a href="/course/" class="zy_amore2">查看更多直通班课程 ></a><a class="zy_amore" href="/course/">更多 ></a></p>
            <ul class="zy_slClass">

                    <li>
                        <div class="zhi_img"><img alt="Web前端开发" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/Web前端开发_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">Web前端开发</p>
                            <p>28课程</p>
                            <p>193天学习时长</p>
                            <p class="color99">14041人正在学习</p>
                        </div>
                        <a title="Web前端开发" href="/course/web-px/"></a>
                    </li>

                    <li>
                        <div class="zhi_img"><img alt="嵌入式驱动开发" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/qrsqd_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">嵌入式驱动开发</p>
                            <p>38课程</p>
                            <p>284天学习时长</p>
                            <p class="color99">7672人正在学习</p>
                        </div>
                        <a title="嵌入式驱动开发" href="/course/qrsqd-px/"></a>
                    </li>

                    <li>
                        <div class="zhi_img"><img alt="计算机动画制作" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/jsjdhzz_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">计算机动画制作</p>
                            <p>3课程</p>
                            <p>28天学习时长</p>
                            <p class="color99">1047人正在学习</p>
                        </div>
                        <a title="计算机动画制作" href="/course/cg-px/"></a>
                    </li>

                    <li>
                        <div class="zhi_img"><img alt="Android架构设计" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/Android架构设计_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">Android架构设计</p>
                            <p>22课程</p>
                            <p>154天学习时长</p>
                            <p class="color99">4839人正在学习</p>
                        </div>
                        <a title="Android架构设计" href="/course/androidjg-px/"></a>
                    </li>

                    <li>
                        <div class="zhi_img"><img alt="软件交互设计" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/rjjhsj_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">软件交互设计</p>
                            <p>1课程</p>
                            <p>7天学习时长</p>
                            <p class="color99">2342人正在学习</p>
                        </div>
                        <a title="软件交互设计" href="/course/ux-px/"></a>
                    </li>

                    <li>
                        <div class="zhi_img"><img alt="嵌入式应用开发" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/嵌入式应用开发_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">嵌入式应用开发</p>
                            <p>35课程</p>
                            <p>244天学习时长</p>
                            <p class="color99">5568人正在学习</p>
                        </div>
                        <a title="嵌入式应用开发" href="/course/qrs-px/"></a>
                    </li>

                    <li>
                        <div class="zhi_img"><img alt="PHP Web开发" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/PHP-Web开发_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">PHP Web开发</p>
                            <p>32课程</p>
                            <p>224天学习时长</p>
                            <p class="color99">9533人正在学习</p>
                        </div>
                        <a title="PHP Web开发" href="/course/php-px/"></a>
                    </li>

                    <li>
                        <div class="zhi_img"><img alt="WP应用开发" class="lazy" src="/static/images/default2.png" data-original="/uploads/course/2015/09/WP应用开发_large.png"></div>
                        <div class="zhi_font color66">
                            <p class="color00 font16 p1">WP应用开发</p>
                            <p>39课程</p>
                            <p>273天学习时长</p>
                            <p class="color99">2376人正在学习</p>
                        </div>
                        <a title="WP应用开发" href="/course/wp-px/"></a>
                    </li>

            </ul>
        </div>
        <!--免费公开课-->
        <div class="zy_index_box">
        	<p class="zy_index_box_tit color99 font14"><a href="/course/list/" class="font22 s1 color33" target="_blank">免费公开课</a><span class="s2">注册用户即可全免费学习</span><a href="/course/list/" class="zy_amore2" target="_blank">查看更多公开课 ></a><a class="zy_amore" href="/course/list/" target="_blank">更多 ></a></p>
            <ul class="zy_course_list">

                    <li><a title="Unity3d之3D坦克大战实战" href="/course/u3d/659-9767" target="_blank">
                        <p><img alt="Unity3d之3D坦克大战实战" src="/static/images/default2.png" data-original="/uploads/course/2016/01/坦克大战.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">Unity3d之3D坦克大战实战</p>
                            <p class="color99">1573人正在学习</p>
                        </div>
                    </a></li>

                    <li><a title="HBase基础" href="/course/others/620-8940" target="_blank">
                        <p><img alt="HBase基础" src="/static/images/default2.png" data-original="/uploads/course/2015/11/HBase-基础课程.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">HBase基础</p>
                            <p class="color99">3898人正在学习</p>
                        </div>
                    </a></li>

                    <li><a title="Python 爬虫基础" href="/course/python/645-9570" target="_blank">
                        <p><img alt="Python 爬虫基础" src="/static/images/default2.png" data-original="/uploads/course/2015/12/Python_爬虫基础.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">Python 爬虫基础</p>
                            <p class="color99">7998人正在学习</p>
                        </div>
                    </a></li>

                    <li><a title="ecshop独立网店二次开发" href="/course/php/660-9796" target="_blank">
                        <p><img alt="ecshop独立网店二次开发" src="/static/images/default2.png" data-original="/uploads/course/2016/01/ecshop独立网店二次开发.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">ecshop独立网店二次开发</p>
                            <p class="color99">2095人正在学习</p>
                        </div>
                    </a></li>

                    <li><a title="Unity基础游戏特效" href="/course/u3d/655-9673" target="_blank">
                        <p><img alt="Unity基础游戏特效" src="/static/images/default2.png" data-original="/uploads/course/2016/01/Unity.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">Unity基础游戏特效</p>
                            <p class="color99">699人正在学习</p>
                        </div>
                    </a></li>

                    <li><a title="Unity3D常用网络框架与实战解析" href="/course/u3d/654-9618" target="_blank">
                        <p><img alt="Unity3D常用网络框架与实战解析" src="/static/images/default2.png" data-original="/uploads/course/2016/01/Unity3D常用网络框架与实战解析.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">Unity3D常用网络框架与实战解析</p>
                            <p class="color99">1003人正在学习</p>
                        </div>
                    </a></li>

                    <li><a title="ARPG游戏实战" href="/course/u3d/653-9594" target="_blank">
                        <p><img alt="ARPG游戏实战" src="/static/images/default2.png" data-original="/uploads/course/2015/12/ARPG游戏实战.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">ARPG游戏实战</p>
                            <p class="color99">2705人正在学习</p>
                        </div>
                    </a></li>

                    <li><a title="laravel实战" href="/course/php/649-9503" target="_blank">
                        <p><img alt="laravel实战" src="/static/images/default2.png" data-original="/uploads/course/2015/12/laravel实战.jpg" class="lazy" style="display: inline;"></p>
                        <div class="">
                            <p class="font14">laravel实战</p>
                            <p class="color99">6971人正在学习</p>
                        </div>
                    </a></li>

            </ul>
        </div>

        <div class="zy_index_box marginB20 zy_hotsBox" style="display:table; padding-top: 10px;">
        	<div class="zy_hots font20 color33">热门标签</div>
            <div class="zy_hotsR">

                    <a href="/course/list/?catagory=Scrapy" target="_blank">Scrapy</a>

                    <a href="/course/list/?catagory=Hibernate" target="_blank">Hibernate</a>

                    <a href="/course/list/?catagory=MongoDB" target="_blank">MongoDB</a>

                    <a href="/course/list/?catagory=Mysql" target="_blank">Mysql</a>

                    <a href="/course/list/?catagory=Nginx" target="_blank">Nginx</a>

                    <a href="/course/list/?catagory=Linux" target="_blank">Linux</a>

                    <a href="/course/list/?catagory=iOS" target="_blank">iOS</a>

            </div>
        </div>

    </div>
</div>






























































<div class="zy_bg_w font12 marginB50">
	<div class="container">
    	<!--名师风采-->
        <div class="zy_index_box">
        	<p class="zy_index_box_tit color99 font14"><a href="/course/teachers/" class="s1 font22 color33" target="_blank">名师风采</a><span class="s2">汇聚行业大牛</span><a href="/course/teachers/" target="_blank">查看更多老师 ></a></p>
            <ul class="zy_ming_div">

                    <li><a title="Sundy" href="/group/common/dynmsg/5/" target="_blank">
                        <div class="marginB10 t3out"><img alt="android开发工程师 sundy" class="lazy" src="/static/images/default2.png" data-original="/uploads/avatar/2015/09/c4380892-632d-11e5-a7f5-00163e02100b_big.jpg"></div>
                        <p class="color33 font18 textC marginB10">Sundy</p>
                        <p class="color99 pb">麦子学院首席讲师，国内知名的软件开发架构师。擅长领域包括移动互联网开发，嵌入式以及大数据，人工智能...... 丰富的海外工作经验及管理经验。</p>
                        </a>
                    </li>

                    <li><a title="高焕堂" href="/group/common/dynmsg/2021/" target="_blank">
                        <div class="marginB10 t3out"><img alt=" android开发工程师 高焕堂" class="lazy" src="/static/images/default2.png" data-original="/uploads/avatar/2015/07/高焕堂.jpg_JtkNJ8I.jpg"></div>
                        <p class="color33 font18 textC marginB10">高焕堂</p>
                        <p class="color99 pb">现任亚太地区Android技术大会主席，台湾Android领域框架开发联盟总架构师。华语世界第一位安卓书籍作者。</p>
                        </a>
                    </li>

                    <li><a title="柯博文" href="/group/common/dynmsg/1481/" target="_blank">
                        <div class="marginB10 t3out"><img alt=" ios开发工程师 柯博文" class="lazy" src="/static/images/default2.png" data-original="/uploads/avatar/2014/12/柯博文.jpg"></div>
                        <p class="color33 font18 textC marginB10">柯博文</p>
                        <p class="color99 pb">美国硅谷LoopTek CTO，台北录克软件CEO。专注于Apple iPhone手机应用软件开发，游戏大富翁的开发者。</p>
                        </a>
                    </li>

                    <li><a title=" 王北南" href="/group/common/dynmsg/3263/" target="_blank">
                        <div class="marginB10 t3out"><img alt=" 驱动开发工程师 王北南" class="lazy" src="/static/images/default2.png" data-original="/uploads/avatar/2015/08/王北南-220.jpg"></div>
                        <p class="color33 font18 textC marginB10"> 王北南</p>
                        <p class="color99 pb">美国Syracuse大学助教 8年J2EE软件开发经验 4年大数据应用架构师经验。曾任国内多家公司技术总监、架构师Tech Lead。
</p>
                        </a>
                    </li>

                    <li><a title="丁群" href="/group/common/dynmsg/1484/" target="_blank">
                        <div class="marginB10 t3out"><img alt=" ios开发工程师 丁群" class="lazy" src="/static/images/default2.png" data-original="/uploads/avatar/2014/12/丁群.jpg"></div>
                        <p class="color33 font18 textC marginB10">丁群</p>
                        <p class="color99 pb">前索尼高级工程师，现任百度音乐高级工程师。游戏&lt;人人都能弹吉他&gt;的开发者。8年的iOS手机软件开发经验，10年软件开发经验。</p>
                        </a>
                    </li>

            </ul>
        </div>
    </div>
</div>


  <div class="v5-footer" style=" background: #f5f5f5;">
    <div class="container">
        <div class="v5-footer-links cf visible-md visible-lg">
          <dl class="f-link">
            <dt>友情链接</dt>
            <dd>
              <ul>

              <li class="cf">

                  <a target="_blank" href="http://ke.qq.com/" title="null">腾讯课堂</a>
                   <span></span>

                  <a target="_blank" href="http://www.langsin.com/" title="null">浪曦IT视频</a>
                   <span></span>

                  <a target="_blank" href="http://www.swiftv.cn/" title="SwiftV课堂">SwiftV课堂</a>
                   <span></span>

                  <a target="_blank" href="http://www.java1234.com/" title="null">java1234</a>
                   <span></span>

                  <a target="_blank" href="http://www.youmi.cn/" title="优米网">优米网</a>
                   <span></span>

                  <a target="_blank" href="http://html5cn.org/" title="HTML5中国">HTML5中国</a>
                   <span></span>

                  <a target="_blank" href="http://open.itcast.cn/" title="公开课">公开课</a>
                   <span></span>

                  <a target="_blank" href="http://www.php186.com/" title="web">web</a>
                   <span></span>

                  <a target="_blank" href="http://www.centoscn.com/" title="CentOS中文站">CentOS中文站</a>
                   <span></span>

                  <a target="_blank" href="http://www.jc88.net/" title="教程巴巴">教程巴巴</a>
                   <span></span>

                  <a target="_blank" href="http://www.thinkcss.com/" title="CSS">CSS</a>
                   <span></span>

                  <a target="_blank" href="http://www.jq-school.com/" title="jquery学堂">jquery学堂</a>
                   <span></span>

                  <a target="_blank" href="http://www.5icool.org/" title="网页特效代码">网页特效代码</a>
                   <span></span>

                  <a target="_blank" href="http://bbs.51testing.com/forum.php" title="51Testing测试论坛">51Testing测试论坛</a>
                   <span></span>

                  <a target="_blank" href="http://www.rapidbbs.cn/" title="锐普PPT论坛">锐普PPT论坛</a>
                   <span></span>

                  <a target="_blank" href="http://www.yanj.cn/" title="PPT素材">PPT素材</a>
                   <span></span>

                  <a target="_blank" href="http://www.zzyjs.com/" title="在职研究生">在职研究生</a>
                   <span></span>

                  <a target="_blank" href="http://www.lampbrother.net/" title="兄弟连IT教育">兄弟连IT教育</a>
                   <span></span>

                  <a target="_blank" href="http://www.ittribalwo.com/" title="IT部落窝">IT部落窝</a>
                   <span></span>

                  <a target="_blank" href="http://c.biancheng.net/" title="C语言">C语言</a>
                   <span></span>

                  <a target="_blank" href="http://www.ixueyi.com/" title="兴趣爱好网">兴趣爱好网</a>
                   <span></span>

                  <a target="_blank" href="http://www.yiibai.com/" title="易百教程">易百教程</a>
                   <span></span>

                  <a target="_blank" href="http://www.siludao.com/" title="答案网"> 答案网</a>
                   <span></span>

                  <a target="_blank" href="http://bbs.it-home.org/" title="程序员之家  ">程序员之家  </a>
                   <span></span>

                  <a target="_blank" href="http://www.kokojia.com/" title="视频教程">视频教程</a>
                   <span></span>

                  <a target="_blank" href="http://www.icoolxue.com/" title="爱酷学习网">爱酷学习网</a>
                   <span></span>

                  <a target="_blank" href="http://www.ablesky.com/" title="能力天空">能力天空</a>
                   <span></span>

                  <a target="_blank" href="http://www.idcs.cn/" title="服务器租用">服务器租用</a>
                   <span></span>

                  <a target="_blank" href="http://www.rr-sc.com/" title="人人素材">人人素材</a>
                   <span></span>

                  <a target="_blank" href="http://www.neitui.me/" title="内部推荐">内部推荐</a>
                   <span></span>

                  <a target="_blank" href="http://www.ushendu.com/" title="u盘启动盘制作工具">u盘启动盘制作工具</a>
                   <span></span>

                  <a target="_blank" href="http://www.xuexiniu.com/" title="Rhino（犀牛）培训">Rhino（犀牛）培训</a>
                   <span></span>

                  <a target="_blank" href="http://www.elsyy.com/" title="在线学习平台">在线学习平台</a>
                   <span></span>

                  <a target="_blank" href="http://www.500d.me/" title="简历模板">简历模板</a>
                   <span></span>

                  <a target="_blank" href="http://www.hao123.com/" title="hao123">hao123</a>
                   <span></span>

                  <a target="_blank" href="http://www.howzhi.com/" title="好知">好知</a>


              </li>

              </ul>
            </dd>
          </dl>
          <dl class="follow">
            <dd>
              <ul>
                <li><a href="http://weibo.com/microoh"><p><img src="/static/images/weibo_code.png"></p><p>关注麦子学院<br>新浪微博</p></a></li>
                <li style="margin-left: 50px;"><p><img src="/static/images/weichat_code.png"></p><p>关注麦子学院<br>官方微信</p></li>
              </ul>
            </dd>
          </dl>
          <dl class="webmap">
            <dt>网站导航</dt>
            <dd>
              <ul>
                <li><a href="/common/about">关于我们</a></li>
                  <li><a href="/course/">企业直通班</a></li>
                <li><a href="/common/join">加入我们</a></li>
                  <li><a href="/group/">麦子圈</a></li>
                <li><a href="/common/contact">联系我们</a></li>
                  <li><a href="/common/apppage/">下载APP</a></li>
                  <li><a href="/group/common/feedback/publish/">意见反馈</a></li>
              </ul>
            </dd>
          </dl>
        </div>


    </div>
  </div>

<div class="v5-footer">
    <div class="container">
        <div class="v5-footer-bottom">
            <p>© 2012-2015 <a href="http://www.maiziedu.com">www.maiziedu.com</a></p>
            <p>蜀ICP备13014270号-4 Version 4.0.6 release20150115.1</p>
        </div>
    </div>
  </div>

<div class="modal fade" id="VideoDemo" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-content zy_VideoDemo" style="width: 800px;">
        <a class="close"></a>
        <div style="height: 400px;">
            <video id="microohvideo" class="video-js vjs-default-skin vjs-big-play-centered"
                               autoplay="autoplay" controls="controls" preload="none" width="100%" height="100%"
                               poster="">
                <source src="" type='video/mp4'/>
            </video>
        </div>

    </div>
</div>

<div class="wap_right_meg">
    <a class="wap53"><img src="/static/images/wap_53_meg.png"></a>
    <a href="tel:400-862-8862"><img src="/static/images/wap_iphone_meg.png"></a>
</div>



</div>

<div class="toolbar">
    <a href="javascript:;" class="toolbar-item toolbar-item-weixin"><span class="toolbar-layer"></span></a>
    <a href="javascript:;" class="toolbar-item toolbar-item-weibo"><span class="toolbar-layer"></span></a>
    <a href="/group/common/feedback/publish/" class="toolbar-item toolbar-item-fankui"><span>意见反馈</span></a>
    <a class="toolbar-item toolbar-item-gotop"><span>返回顶部</span></a>
</div>
<div class="lixianB" >
    <p><input type="text" placeholder="请输入您的电话号码" id="telInput" class="intxt"></p>
    <p><input type="button" value="免费通话咨询" id="callBtn" class="inbtn"></p>
    <div><img src="/static/images/kuang.png"></div>
</div>




<!--弹出层区块-->
<!--登录-->
<div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-sm">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h4 class="modal-title" id="loginModalLabel" style="font-size: 18px;">

                        登录

                </h4>
            </div>
            <div class="modal-body">
                <section class="box-login v5-input-txt" id="box-login">
                    <form id="login_form" action="/user/login/" method="post" autocomplete="off">

                        <ul>
                            <li class="form-group"><input class="form-control" id="id_account_l" maxlength="50" name="account_l" placeholder="请输入邮箱账号/手机号" type="text" /></li>
                            <li class="form-group"><input class="form-control" id="id_password_l" name="password_l" placeholder="请输入密码" type="password" /></li>

                        </ul>
                    </form>
                    <p class="good-tips"><a href="#" data-toggle="modal" data-target="#forgetpswModal" id="btnForgetpsw" class="fr">忘记密码？</a>还没有账号？<a  phptag="phptag_register" href="" data-toggle="modal" data-target="#registerModal" id="btnRegister">立即注册</a></p>
                    <div>
                        <button id="login_btn" type="button" class="btn btn-micv5 btn-block" onclick="login_form_submit('login-form-tips')">登录</button>
                    </div>
                    <div id="login-form-tips" class="tips-error bg-danger">错误提示</div>

                    <div class="threeLogin"><span>其他方式登录</span><a class="nqq" href="/user/connect/?partner=qq"></a><a class="nwx" href="/user/connect/?partner=wechat"></a><!--<a class="nwb"></a>--></div>

                </section>
            </div>
        </div>
    </div>
</div>
<!--找回密码-->
<div class="modal fade" id="forgetpswModal" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-sm">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" data-toggle="modal" data-target="#loginModal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h4 class="modal-title" id="forgetpswModalLabel" style="font-size: 18px;">找回密码</h4>
            </div>
            <div class="modal-body">
                <section class="box-forgetpsw v5-input-txt" id="box-forgetpsw">
                    <form id="find_password_form" action="/user/password/find/" method="post" autocomplete="off">

                        <ul>
                            <li class="form-group"><input class="form-control" id="id_account" maxlength="50" name="account" placeholder="请输入注册邮箱账号或手机号码" type="text" /></li>
                            <li class="form-group"><input autocomplete="off" class="form-control form-control-captcha fl" id="id_captcha_f_1" name="captcha_f_1" placeholder="请输入验证码" type="text" /> <input class="form-control form-control-captcha fl" id="id_captcha_f_0" name="captcha_f_0" placeholder="请输入验证码" type="hidden" value="4e424c9122b3d95ebcc197796b23b0788d916fc4" /> &nbsp;<img src="/captcha/image/4e424c9122b3d95ebcc197796b23b0788d916fc4/" alt="captcha" class="captcha" /><span class="v5-yzm fr"><a id='findpassword-captcha-refresh' class="captcha-refresh" href="#">换一张</a></span></li>
                            <li class="form-group">&nbsp;</li>
                        </ul>
                        <div>
                            <button id="findpassword_btn" type="button" class="btn btn-micv5 btn-block" onclick="find_password_form_submit()">提交</button>
                        </div>
                        <div id="findpassword-tips" class="tips-error bg-danger">错误提示</div>
                    </form>
                </section>
            </div>
        </div>
    </div>
</div>

<!-- 忘记密码，手机验证码输入界面 -->
<div class="modal fade" id="forgetpswMobileModal" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-sm">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h4 class="modal-title" id="forgetpswMobileModalLabel" style="font-size: 18px;">手机验证</h4>
            </div>
            <div class="modal-body">
                <section class="box-forgetpsw v5-input-txt" id="box-forgetpsw-mobile-code">
                    <form id="mobile_code_password_form" action="/user/password/find/mobile/" method="post" autocomplete="off">

                        <ul>
                            <li class="form-group" id="mobile_code_password_form_message">手机短信验证码已发送，请查收！</li>
                            <li class="form-group"><input id="id_mobile_f" name="mobile_f" type="hidden" /></li>
                            <li class="form-group"><input class="form-control" id="id_mobile_code_f" name="mobile_code_f" placeholder="请输入短信验证码" type="text" /></li>
                        </ul>
                        <div>
                            <button id="mobile_code_password_btn" type="button" class="btn btn-micv5 btn-block" onclick="mobile_code_password_form_submit()">下一步</button>
                        </div>
                        <div id="mobile_code_password-tips" class="tips-error bg-danger">错误提示</div>
                    </form>
                </section>
            </div>
        </div>
    </div>
</div>

<!--注册-->
<div class="modal fade" id="registerModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
                <h4 class="modal-title" id="registerModalLabel" style="font-size: 18px;">

                注册
                </h4>
            </div>
            <div class="modal-body">
                <section class="box-register v5-input-txt" id="box-register">
                    <ul class="register-tabs" role="tablist">
                        <li class="active"><a href="#register-email" role="tab" data-toggle="tab" onclick="change_form('email_register_form')">邮箱注册</a></li>
                        <li><a href="#register-mobile" role="tab" data-toggle="tab" onclick="change_form('mobile_register_form')">手机注册</a></li>
                    </ul>
                    <div class="tab-content">
                        <div class="tab-pane active" id="register-email">
                            <form id="email_register_form" action="/user/register/email/" method="post" autocomplete="off">

                                <div class="form-group cf_g"><input class="form-control" id="id_email" maxlength="30" name="email" placeholder="请输入邮箱账号" type="text" /></div>
                                <div class="form-group cf_g"><input class="form-control" id="id_password" maxlength="50" name="password" placeholder="请输入密码" type="password" /></div>
                                <div class="form-group cf cf_g"><input autocomplete="off" class="form-control form-control-captcha fl" id="id_captcha_1" name="captcha_1" placeholder="请输入验证码" type="text" /> <input class="form-control form-control-captcha fl" id="id_captcha_0" name="captcha_0" placeholder="请输入验证码" type="hidden" value="546eab0d964f0dc170d19c31b62236bd70dee335" /> &nbsp;<img src="/captcha/image/546eab0d964f0dc170d19c31b62236bd70dee335/" alt="captcha" class="captcha" /><span class="v5-yzm fr"><a id='email-captcha-refresh' class="captcha-refresh" href="#">换一张</a></span></div>

                            </form>
                        </div>
                        <div class="tab-pane" id="register-mobile">
                            <form id="mobile_register_form" action="/user/register/mobile/" method="post" autocomplete="off">

                                <div class="form-group cf"><input autocomplete="off" class="form-control form-control-captcha fl" id="id_captcha_m_1" name="captcha_m_1" placeholder="请输入验证码" type="text" /> <input class="form-control form-control-captcha fl" id="id_captcha_m_0" name="captcha_m_0" placeholder="请输入验证码" type="hidden" value="dfab72cb10efbdc52f268a494a22eb4601632ae2" /> &nbsp;<img src="/captcha/image/dfab72cb10efbdc52f268a494a22eb4601632ae2/" alt="captcha" class="captcha" /><span class="v5-yzm fr"><a id='mobile-captcha-refresh' class="captcha-refresh" href="#">换一张</a></span></div>
                                <div class="form-group cf"><input class="form-control form-control-phone fl" id="id_mobile" maxlength="11" name="mobile" placeholder="请输入手机号" type="text" /><span class="send-code fr"><button id="send_sms_btn" type="button" class="btn btn-micv5 btn-send" onclick="send_sms_code('mobile_register_form','register-tips')">发送验证码</button></span></div>
                                <div class="form-group"><input class="form-control" id="id_mobile_code" name="mobile_code" placeholder="请输入短信验证码" type="text" /></div>
                                <div class="form-group"><input class="form-control" id="id_password_m" maxlength="50" name="password_m" placeholder="请输入密码" type="password" /></div>

                            </form>
                        </div>
                    </div>
                    <p class="good-tips">已经有账号？<a href="#" data-toggle="modal" data-target="#loginModal" id="btnLogin">立即登录</a></p>
                    <div>
                        <button id="register_btn"  phptag="phptag_register_login" type="button" class="btn btn-micv5 btn-block" onclick="register_form_submit()">注册并登录</button>
                    </div>
                    <div id="register-tips" class="tips-error bg-danger">错误提示</div>
                </section>
            </div>
        </div>
    </div>
</div>
<!--zhouyi:7-30-->
<!--邮件验证-->
<div class="modal fade" id="emailValidate" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-content zy_email">
        <a class="close"></a>
        <p class="i"><img src="/static/images/zy_send.png"></p>
        <p id="emailValidateEE">我们向您的邮箱<span>548748451@qq.com</span>发送了一封验证邮件</p>
        <p>为保证您账号的安全和方便您参加我们的活动，邮箱完成验证才能继续学习哦</p>
        <p class="a"><a target="_blank">去邮箱验证</a></p>
        <p class="sendE2" style="display: none;">没收到，您可以查看您的垃圾邮件和被过滤邮件，也可以再次发送验证邮件（<span class="c5c">60s</span>）</p>
        <p class="sendE">没收到，您可以查看您的垃圾邮件和被过滤邮件，也可以<a class="c5c">再次发送验证邮件</a></p>
        <p class="zy_success t5o upmove"><img src="/static/images/zy_right.png"><span>验证邮件发送成功</span></p>
    </div>
</div>





<ul class="zy_foot_div">
    <li><a href="/course/" class="a1 "><p class="p"></p><p>课程中心</p></a></li>
    <li><a href="/group/ask/" class="a2"><p class="p"></p><p>麦子圈</p></a></li>
    <li><a href="/common/apppage/" class="a3 "><p class="p"></p><p>APP</p></a></li>
</ul>
<div style="width: 100%; height: 64px;" class="zy_foot_divDD"></div>

<script src="/static/js/jquery-migrate-1.2.1.min.js"></script>
<script src="/static/js/jquery.featureCarousel.min.js"></script>
<script src="/static/js/jquery.carouFredSel.js"></script>
<script src="/static/js/bootstrap.min.js"></script>
<script src="/static/js/jquery.placeholder.js"></script>
<script src="/static/js/jquery.mousewheel.js"></script>
<script src="/static/js/jquery.jscrollpane.min.js"></script>
<script src="/static/js/mz-jPages.min.js"></script>
<script src="/static/js/Swiper.js"></script>
<script src="/static/js/microoh-v5.js"></script>
<script src="/static/js/ie10-viewport-bug-workaround.js"></script>
<script src="/static/js/flat-ui.min.js"></script>
<script src="/static/js/application.js"></script>
<script src="/static/js/mz-common.js"></script>
<!-- GoogleAnalytics代码 -->


<script src="/static/js/jquery.bxslider.js"></script>
<script src="/static/js/jquery.lazyload.js"></script>
<link rel="stylesheet" href="/static/css/videojs/video-js.css">
<script src="/static/js/videojs/video.js"></script>
<script>
    videojs.options.flash.swf = "/static/js/videojs/video-js.swf"
</script>
<script>
function openVideo(){
    $('#VideoDemo').modal('show');
    $("#microohvideo").children().attr("src","http://ocsource.maiziedu.com/lps_intro.mp4")
}
$(function(){
    $(".zy_banner").css("backgroundImage","url("+$(".bxslider li").eq(0).children("a").attr("big")+")");

	$('.bxslider').bxSlider({
		mode: 'horizontal',
		auto:true,
		hideControlOnEnd:true,
        onSlideAfter:function(slideElement, oldIndex, newIndex){
            $(".zy_banner").css("backgroundImage","url("+slideElement.children("a").attr("big")+")");
        }
	});
	$('.bxslider2').bxSlider({
		pager:false,
		auto:false,
		slideWidth: 275,
		minSlides: 1,
		maxSlides: 4,
		moveSlides: 1,
		slideMargin: 10,
		pause:6000,
		onSlideAfter:function(slideElement, oldIndex, newIndex){
			$('html,body').animate({scrollTop: ($(window).scrollTop()-0.1)+'px'}, 400);

		}
	});

	$("img.lazy").lazyload({ threshold :100,placeholder : "/static/images/default.png",failure_limit:20,skip_invisible : false });

    //video
    var player = videojs("microohvideo", {
        controls: true,
        playbackRates: [1, 1.25, 1.5, 2]
    });

    player.pause();
    $(".zy_VideoDemo .close").unbind().click(function(){
        player.pause();
        $('#VideoDemo').modal('hide');
    });
    $('#VideoDemo').on('hide.bs.modal', function () {
        player.pause();
    });
})
</script>







<script>
$(function(){






})

    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o),
                m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-61416428-1', 'auto');
    ga('require', 'displayfeatures');
    ga('send', 'pageview');








</script>

<div style="position: fixed;top: 300px;right: 0px;">
 <script type='text/javascript' src='http://tb.53kf.com/kf.php?arg=10114760&style=1'></script>
</div>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-51873363-14']);
 _gaq.push(['_trackPageview']);
(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();

</script>  <!-- END SITE FOOTER -->

</body>
</html>


'''


class HTMLForms(HTMLParser):
    """
    test
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.fields = dict()
        self.submit = dict()
        self.fields['name'] = []

    def handle_starttag(self, tag, attrs):
        if tag == 'form':
            for key, value in attrs:
                if key == 'action':
                    self.fields['action'] = value
                elif key == 'method':
                    self.fields['method'] = value
        elif tag == 'input':
            for key, value in attrs:
                if key == 'type':
                    self.submit['type'] = value
                elif key == 'onclick':
                    self.submit['onclick'] = value
        else:
            for key, value in attrs:
                if key == 'name':
                    self.fields['name'].append(value)

    # def handle_data(self, data):
    #     if self.form:
    #         self.data += data
    #     if self.data and not self.form:
    #         self.forms.append(self.data)
    #         self.data = ''


def get_html_form(html):
    return [i for i in re.findall(form_re, html)]

if __name__ == '__main__':
    # hp = HTMLForms()
    # hp.feed(html)
    # hp.close()
    forms = get_html_form(html)
    hp = HTMLForms()
    hp.feed(forms[1])
    hp.close()
    print hp.fields