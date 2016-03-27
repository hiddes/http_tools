#coding:utf8
import urllib
str = 'pt_clientip=0d49b269618f9d80f; pt_serverip=b7e10abf20e2f4c6e; pgv_pvid=60765423488; pgv_info=ssid=s28963139001; ptisp=ctc; RK=xRvPndadly; ptcz=948290f035d2f047c3af52b222e52baaa8deb14259911e35df69dbf342363c6b6e; pt2gguin=o227512532699; uin=o223275125699; skey=@RkffQpStP; p_uin=o2275125699; p_skey=rjBl*yxEhXqWJR2scC3OhPYeKK5WkuzZIAVFCxnJ2xo_; pt4_token=KAcnY6pcxc5e-Y2mdCujEQ__; hasShowWeiyun2275125699=1; Loading=Yes; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=7; qzspeedup=sdch; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; qzmusicplayer=qzone_player_837386694_1446713835840; rv2=80497EE11B6895B30D32712D24AC3B451223E3884531F98BE2A2; property20=93828EFE94EBE701E315523CE810A1F51CB2802E7AE4507A0709A7CEAA5E74860D82CEE2E11FF9E7C4; randomSeed=3523231'

def cookie_to_dict(str):
    cookie_dict = {}
    li = str.split(';')
    for i in li:
        num = i.find('=')
        try:
            cookie_dict[i[:num]] = i[num+1:]
        except Exception as e:
            print e
    return cookie_dict


if __name__ =='__main__':
    cookie = cookie_to_dict(str)
    print cookie
