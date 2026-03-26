from pathlib import Path

fp = Path('chapter27_english.html')
text = fp.read_text(encoding='utf-8')

# Replace imageUrls block
start = text.find('imageUrls: [')
if start == -1:
    raise ValueError('imageUrls block not found')
end = text.find('],', start)
if end == -1:
    raise ValueError('end of imageUrls block not found')
end = end + 2

new_urls = [
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489956/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_1_n6g5se.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489962/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_2_heiukr.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489957/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_4_dbm8uq.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489956/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_5_jn4ugx.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489956/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_6_phzqth.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489960/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_7_ttpgvw.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489961/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_8_wgauyz.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489958/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_9_jlcmf6.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489961/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_10_qekd80.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489961/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_12_znjtir.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489963/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_13_y6ztls.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489963/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_14_ivvhf4.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489965/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_15_uysx7k.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489964/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_16_alwzyp.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489966/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_17_ec3mlv.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489966/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_18_ub7umx.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489968/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_19_d3gmex.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489970/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_20_yxfw8p.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489969/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_21_i8gjti.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489968/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_22_xb6m9c.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489968/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_23_heodp4.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489957/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_24_tuvwfx.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489958/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_25_bhcb8q.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489960/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_26_qloi9m.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489959/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_27_qjgmuo.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489964/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_28_xmqzbq.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489962/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_30_pejmdq.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489965/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_31_rjvm47.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489965/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_32_dzqr5t.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489966/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_33_n92sht.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489966/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_34_o6q5cw.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489967/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_35_jyfll3.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489968/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_36_xwsayx.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489969/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_37_obnpzq.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489972/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_38_cxksqk.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489970/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_39_jqwpyp.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489972/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_40_jfenrv.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489970/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_42_jxbhv4.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489973/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_43_sv1cs7.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489974/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_44_gexyor.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489972/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_45_esfqsw.png",
"https://res.cloudinary.com/dbulxrm7b/image/upload/v1774489972/%E9%B9%AB%E5%B7%A2%E5%A4%96%E4%BC%A027_46_cmomdg.png"]

new_block = 'imageUrls: [\n' + '\n'.join('            '+u for u in new_urls) + '\n        ],'
text = text[:start] + new_block + text[end:]

# talkContent already set to empty string above by manual edit.

fp.write_text(text, encoding='utf-8')
print('done')
