import re
from pathlib import Path

urls = [
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292406/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_42_yznrzu.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292386/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_44_jxaf6l.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292385/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_46_phinmj.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292379/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_45_pggjqw.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292344/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_40_hlxzth.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292328/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_41_dvykby.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292316/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_38_tdyai5.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292313/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_39_twsjzr.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292310/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_37_uphwv1.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292301/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_18_way50c.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292257/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_28_zedqcc.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292251/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_34_bktbap.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292244/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_36_mxmsfy.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292244/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_35_lyped7.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292237/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_33_ikhvgg.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292226/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_13_izqlax.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292177/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_12_qypqkg.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292167/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_32_pssawm.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292165/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_16_vflgq8.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292163/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_14_ryhoqm.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292157/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_15_wyzwap.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292135/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_30_foxznr.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292131/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_17_yel4ax.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292131/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_31_n8hxqk.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292117/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_9_epzcxt.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292104/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_11_ycimtd.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292060/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_6_pqkvhh.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292058/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_7_svzegd.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292048/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_27_wqlbhy.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292047/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_8_imzgmu.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292029/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_26_wdohgy.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292028/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_10_rquwum.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292024/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_22_i2e7wr.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292021/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_5_mtadfn.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292013/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_25_fk7yrv.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292005/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_24_i5u57d.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779292001/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_3_fnqt3q.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779291988/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_4_zunwis.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779291970/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_1_jyg1sr.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779291967/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_2_nsrddc.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779291965/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_21_ybg4zj.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779291964/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_20_ddgxoj.png",
    "https://res.cloudinary.com/dbulxrm7b/image/upload/v1779291957/%E6%96%97%E7%89%8C%E5%A4%96%E4%BC%A028_19_q8ikbt.png"
]

pattern = re.compile(r'_([0-9]+)(?:_[^_/]+)?\.png$')


def sort_key(url):
    match = pattern.search(url)
    if match:
        return int(match.group(1))
    return float('inf')

sorted_urls = sorted(urls, key=sort_key)

for url in sorted_urls:
    print(url)

html_file = Path(__file__).with_name('chapter28_english.html')
if html_file.exists():
    marker_start = 'imageUrls: ['
    marker_end = '        ],'
    html = html_file.read_text(encoding='utf-8')
    start = html.find(marker_start)
    if start != -1:
        end = html.find(marker_end, start)
        if end != -1:
            end += len(marker_end)
            before = html[:start]
            after = html[end:]
            urls_block = '        ' + marker_start + '\n'
            for url in sorted_urls:
                urls_block += f'          "{url}",\n'
            urls_block += '        ],'
            html_file.write_text(before + urls_block + after, encoding='utf-8')
            print('\nUpdated chapter28_english.html with sorted URLs.')
